"Matching images from the ODT to local files"

from PIL import Image, UnidentifiedImageError
from zipfile import ZipFile
from collections import defaultdict
import os
import math


PICTURES_FOLDER = "Pictures/"


def _assert(_):
    assert False
    
def _calc_stat_for_channel(histogram, channel_index, numpixels):
    offset = channel_index * 256
    return sum([histogram[offset + i] * i for i in range(256)]) / numpixels

def _calc_stats(image):
    assert len(image.getbands()) == 4
    numpixels = image.width * image.height
    histogram = image.histogram()
    return _Stats(  _calc_stat_for_channel(histogram, 0, numpixels), 
                    _calc_stat_for_channel(histogram, 1, numpixels), 
                    _calc_stat_for_channel(histogram, 2, numpixels))

def _load_image(source):
    with Image.open(source) as image:
        image.load()
    if len(image.getbands()) == 1:
        image = image.convert("RGBA")
    assert len(image.getbands()) == 4
    return image

class _Stats:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        
    def eq_strict(self, other):
        return self._eq(other, 0.0001)
    
    def eq_loose(self, other):
        return self._eq(other, 0.15)
    
    def eq_double(self, other):
        return self._eq(other, 0.3)
    
    def _eq(self, other, abs_tolerance):
        return math.isclose(self.r, other.r, rel_tol=0, abs_tol=abs_tolerance) \
            and math.isclose(self.g, other.g, rel_tol=0, abs_tol=abs_tolerance) \
            and math.isclose(self.b, other.b, rel_tol=0, abs_tol=abs_tolerance)
    
    def __repr__(self):
        return f"R:{self.r}, G{self.g}, B{self.b}"


class _FileRecord:
    def __init__(self, filename, stats):
        self.filename = filename
        self.stats = stats
    
    def __repr__(self):
        return self.filename + ": " + repr(self.stats)


def match_images(archive: ZipFile, image_folder: str):
    # Calculate statistics for each image in the local images directory
    has_ambiguous = False
    aspect_ratios = defaultdict(list)
    print("Processing local images...")
    for path, _, files in os.walk(image_folder, onerror=_assert):
        for f in files:
            try:
                # Open the image
                filename = os.path.join(path, f)
                # Load the image
                img = _load_image(filename)
                aspect = int(img.width / img.height * 100)
                stats = _calc_stats(img)
                # Make sure there are no similar images
                for a in range(aspect - 2, aspect + 3):
                    for r in aspect_ratios[a]:
                        if r.stats.eq_double(stats):
                            has_ambiguous = True
                            print(f"Similar images:")
                            print(f"{a}: {r}")
                            print(f"{aspect}: {_FileRecord(filename, stats)}")
                            print()
                # Register the image
                aspect_ratios[aspect].append(_FileRecord(filename, stats))
            except UnidentifiedImageError:
                pass
    assert not has_ambiguous
    print("Local images were processed sucessfully")
    # Match images from the ODT to the local images
    matched = {}
    unmatched = set()
    infos = archive.infolist()
    perfect_matches = 0
    loose_matches = 0
    print("Processing images in the ODT...")
    for i in infos:
        if i.filename.startswith(PICTURES_FOLDER):
            assert i.filename not in matched
            assert i.filename not in unmatched
            # Open the image
            with archive.open(i) as img_file:
                img = _load_image(img_file)
            aspect = int(img.width / img.height * 100)
            stats = _calc_stats(img)
            # Find a strictly matching local image
            found = None
            for r in aspect_ratios[aspect]:
                if r.stats.eq_strict(stats):
                    assert not found
                    found = r.filename
                    perfect_matches += 1
            # Looser match for resized images
            if not found:
                for a in range(aspect - 1, aspect + 2):
                    for r in aspect_ratios[a]:
                        if r.stats.eq_loose(stats):
                            if found:
                                has_ambiguous = True
                                print(f"Ambiguous match from {i.filename} to: {r.filename} and {found}")
                            found = r.filename
                            loose_matches += 1
            if not found:
                print("Unmatched:", i.filename, aspect, stats)
                for a in range(aspect - 1, aspect + 2):
                    print("->", a)
                    for r in aspect_ratios[a]:
                        print(r)
                print()
            # Write down results
            if found:
                matched[i.filename] = found
            else:
                unmatched.add(i.filename)
    assert not has_ambiguous
    print(f"ODT images were processed sucessfully. Matched: {len(matched)}, unmatched: {len(unmatched)}")
    return matched, unmatched
