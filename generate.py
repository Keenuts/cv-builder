#!/usr/bin/env python3
from jinja2 import Template, Environment, BaseLoader, FileSystemLoader
import json
import datetime
import os

template_file = None
content_file = None
content = None

INFO_FILEPATH    = "info.json"
TEMPLATE_PREVIEW = "preview-template.html"
TEMPLATE_PRINT   = "print-template.html"
TEMPLATE_TEXT    = "text-template.html"

OUTPUT_PREVIEW = "build/preview.html"
OUTPUT_PRINT   = "build/print.html"
OUTPUT_TEXT   = "build/cv.md"

def LoadInfo(path):
    try:
        with open(path) as f:
            raw = f.read()
            info = json.loads(raw)
    except (FileNotFoundError, PermissionError) as e:
        print("An error occured:", e)
        return None
    except json.JSONDecodeError as e:
        print("Error in the JSON file:", e)

        lines = raw.split("\n")
        for i in range(max(e.lineno - 3, 0), e.lineno + 4):
            if i >= len(lines):
                break

            if i == e.lineno:
                print("\t>%d|\t%s" % (i, lines[i]))
            else:
                print("\t %d|\t%s" % (i, lines[i]))
        return None

    return info

def CreateFromTemplate(template, info, dest):
    env = Environment(loader=FileSystemLoader(os.getcwd()))
    template = env.get_template(template)
    result = template.render(info=info)

    try:
        dirname = os.path.dirname(dest)
        os.makedirs(dirname, exist_ok=True)

        out = open(dest, "w")
        out.write(result)
        out.close()
    except (FileNotFoundError, PermissionError) as e:
        print("Cannot write output file:", e)


info = LoadInfo(INFO_FILEPATH)
if info == None:
    exit(1)

CreateFromTemplate(TEMPLATE_PREVIEW, info, OUTPUT_PREVIEW)
CreateFromTemplate(TEMPLATE_PRINT, info, OUTPUT_PRINT)
CreateFromTemplate(TEMPLATE_TEXT, info, OUTPUT_TEXT)
print("done at ", datetime.datetime.now().strftime('%H:%M:%S'))
