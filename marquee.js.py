"""

# Marquee.js

A microframework for creating unambitious web applications.

## What is Marquee.js

What _isn't_ marquee.js?

First of all, Marquee.js is not a JS thing. It's a python thing.

Marquee.js is a library for very quickly turning
a markdown file into a webpage, paying as little attention as possible
to things like 'features' or 'advanced functionality' or 'working'.

## What language is Marquee.js written in?

Python.

## How do I install it?

I'm not sure. Maybe pip install markdown and then just copy marquee.js.py
into any folder? I'm not yer' mama.

## How do I use it?

    >>> python3 marquee.js.py drone_ver.md drone_ver_template.html > index.html

"""

import markdown
import argparse
from string import Template

parser = argparse.ArgumentParser()
parser.add_argument("markdown", help="markdown")
parser.add_argument("template", help="template")
args = parser.parse_args()

with open(args.markdown, 'r') as f:
    html = markdown.markdown(f.read(), extensions=['markdown.extensions.tables'])

with open(args.template, 'r') as f:
    form = Template(f.read())

print(form.substitute({'html':html}))
