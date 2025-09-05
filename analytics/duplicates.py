from plugins import Analytics


# Find duplicate chapters (file names)
class HasDuplicateChapters(Analytics):
    def __init__(self):
        self._duplicate = None
        self._visited_names = set()
    
    def _process_chapter(self, section):
        if self._duplicate:
            return False
        name = section.header.to_string()
        if name in self._visited_names:
            self._duplicate = name
            return False
        else:
            self._visited_names.add(name)
            return True
    
    def _finalize(self):
        return self._duplicate
    

export = HasDuplicateChapters