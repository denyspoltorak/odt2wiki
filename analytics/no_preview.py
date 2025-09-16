from plugins import Analytics
from document import Image


# Find duplicate chapters (file names)
class HasDuplicateChapters(Analytics):
    def __init__(self):
        self._no_images = []
        self._multiple_images = []
    
    def _process_chapter(self, section):
        name = section.header.to_string()
        num_images = 0
        for c in section.content:
            if isinstance(c, Image):
                num_images += 1
        if not num_images:
            self._no_images.append(name)
        elif num_images > 1:
            self._multiple_images.append(name)
        return True
    
    def _finalize(self):
        print()
        print("Chapters with no preview images:")
        for c in self._no_images:
            print(c)
        print()
        print("Chapters with multiple preview images:")
        for c in self._multiple_images:
            print(c)
        print()
    

export = HasDuplicateChapters