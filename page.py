class Page:
    head = []
    body = []

    def __init__(self):
        pass

    def http_header(self):
        return "Content-Type: text/html\n\n<!DOCTYPE html>\n"

    def set_title(self, text):
        self.head += [self.make_title(text)]
        return self

    def add(self, html):
        self.body += [html]
        return self

    def __str__(self):
        html = self.http_header()

        html += "<head>\n"
        for tag in self.head:
            html += str(tag) + "\n"
        html += "</head>\n"

        html += "<body>\n"
        for tag in self.body:
            html += str(tag) + "\n"
        html += "</body>\n"

        return html

    def make_title(self, text):
        return "<title>" + text + "</title>"
