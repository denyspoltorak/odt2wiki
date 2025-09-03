import document

class MetapatternsCustomization(document.Customization):
    @staticmethod
    def needs_split(section):
        return True

customization = MetapatternsCustomization()