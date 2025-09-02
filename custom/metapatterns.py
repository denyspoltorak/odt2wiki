import document

class MetapatternsCustomization(document.Customization):
    @staticmethod
    def needs_split(doc):
        return True

customization = MetapatternsCustomization()