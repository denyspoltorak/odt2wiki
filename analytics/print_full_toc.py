from plugins import Analytics


# Print the detailed table of contents
class PrintFullToc(Analytics):
    def _process_chapter(self, section):
        self._print_section(section)
        return True
    
    def _process_subsection(self, section):
        self._print_section(section)
        return True
    
    def _print_section(self, section):
        print("  " * section.header.outline_level + section.header.to_string())
    

export = PrintFullToc