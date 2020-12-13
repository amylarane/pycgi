#!/usr/bin/python3
from pycgi import *

header = make_header().set_text("Hello World!")
page = make_page().set_title("Hi :)").add(header)

render(page)

