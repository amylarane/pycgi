from page import Page
from h1 import H1

def make_page():
    return Page()

def make_header():
    return H1()

def render(page):
    print(page)
