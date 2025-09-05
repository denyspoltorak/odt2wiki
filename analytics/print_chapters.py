from plugins import Analytics


# Print chapter (file or web page) names
class PrintChapters(Analytics):
    def _process_chapter(self, section):
        print("  " * section.header.outline_level + section.header.to_string())
        return True
    

export = PrintChapters