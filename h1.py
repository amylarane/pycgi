
class H1:
    text = ""
    
    def __init__(self):
        pass

    def set_text(self, text):
        self.text = text
        return self

    def __str__(self):
        return "<h1>" + self.text + "</h1>"

