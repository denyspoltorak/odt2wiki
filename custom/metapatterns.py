import document

class MetapatternsCustomization(document.Customization):
    @staticmethod
    def needs_split(section):
        # Split a chapter if it contains subchapters
        num_summaries = 0
        for c in section.children:
            for gc in c.children:
                if gc.header.to_string() == "Summary":
                    num_summaries += 1
        if num_summaries > 1:
            return True
        # Split select long chapters
        if section.header.to_string() in ("The heart of software architecture", "Appendix E. Evolutions."):
            return True
        # Otherwise use default rules
        return False

customization = MetapatternsCustomization()