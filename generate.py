#!/usr/bin/env python3
from jinja2 import Template, Environment, BaseLoader, FileSystemLoader
import json
import datetime
import os

template_file = None
content_file = None
content = None

INFO_FILEPATH            = "info.json"
COVER_BLOCKS_DIR         = "cover-letter"

TEMPLATE_CV_PREVIEW      = "templates/cv-preview.html"
TEMPLATE_CV_PRINT        = "templates/cv-print.html"
TEMPLATE_CV_TEXT         = "templates/cv-text.html"

TEMPLATE_COVER_PREVIEW   = "templates/cover-preview.html"
TEMPLATE_COVER_PRINT   = "templates/cover-print.html"
TEMPLATE_COVER_TEXT   = "templates/cover-text.html"

OUTPUT_CV_PREVIEW    = "build/cv-preview.html"
OUTPUT_CV_PRINT      = "build/cv-print.html"
OUTPUT_CV_TEXT       = "build/cv-text.md"

OUTPUT_COVER_PREVIEW = "build/cover-preview.html"
OUTPUT_COVER_PRINT = "build/cover-print.html"
OUTPUT_COVER_TEXT = "build/cover-text.txt"

COVER_BLOCK_INTRO = "introduction.md"
COVER_BLOCK_EXPERIENCE = "experience.md"
COVER_BLOCK_CONCL = "conclusion.md"

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

    info['cwd'] = os.getcwd()
    return info

def LoadBlock(blockpath):
    try:
        with open(blockpath) as f:
            raw = f.read()
    except (FileNotFoundError, PermissionError) as e:
        return False, ""
    return True, raw

def CoverLoadBlocks(path, info):
    blocks = {}

    companyFile = info['company'].lower().replace(' ', '-') + ".md"
    if not os.path.isfile(os.path.join(path, companyFile)):
        companyFile = 'company-generic.md'

    to_load = [
        ("intro", COVER_BLOCK_INTRO),
        ("company", companyFile),
        ("experience", COVER_BLOCK_EXPERIENCE),
        ("conclusion", COVER_BLOCK_CONCL),
    ]

    for tl in to_load:
        res, content = LoadBlock(os.path.join(path, tl[1]))
        if not res:
            print("Could not load the block %s. Aborting now." % tl[1])
        blocks[tl[0]] = content

    return blocks

def CreateFromTemplate(template, info, dest):
    env = Environment(loader=FileSystemLoader(os.getcwd()))

    try:
        template = env.get_template(template)
    except Exception:
        print("Unable to laod the template %s. Aborting now." % template)
        exit(1)
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

CreateFromTemplate(TEMPLATE_CV_PREVIEW, info, OUTPUT_CV_PREVIEW)
CreateFromTemplate(TEMPLATE_CV_PRINT,   info, OUTPUT_CV_PRINT)
CreateFromTemplate(TEMPLATE_CV_TEXT,    info, OUTPUT_CV_TEXT)

blocks = CoverLoadBlocks(COVER_BLOCKS_DIR, info)

info['blocks'] = {}
for k in blocks:
    info['blocks'][k] = blocks[k]

CreateFromTemplate(TEMPLATE_COVER_PREVIEW, info, OUTPUT_COVER_PREVIEW)
CreateFromTemplate(TEMPLATE_COVER_PRINT, info, OUTPUT_COVER_PRINT)
CreateFromTemplate(TEMPLATE_COVER_TEXT, info, OUTPUT_COVER_TEXT)

print("done at ", datetime.datetime.now().strftime('%H:%M:%S'))
