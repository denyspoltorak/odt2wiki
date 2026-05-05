from plugins import Analytics
from document import Image


# Find images with no alt descriptions
class ImagesWithNoAltDescriptions(Analytics):
    def __init__(self):
        self._no_alts = set()
        self._customization = None
    
    def __call__(self, section):
        for c in section.content:
            if isinstance(c, Image):
                image_name = c.data.short_name
                if image_name:
                    try:
                        self._customization.get_image_alt_text(image_name)
                    except AssertionError:
                        self._no_alts.add(image_name)
        return True
    
    def _set_customization(self, customization):
        assert customization
        assert self._customization is None
        self._customization = customization
    
    def _finalize(self):
        print()
        print("Images with no alt description:")
        for c in self._no_alts:
            print(c)
        print()


export = ImagesWithNoAltDescriptions