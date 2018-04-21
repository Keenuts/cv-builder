# CV-Builder

I needed a CV, and coulnd't use InDesign anymore.
I also Needed something that could run all my computers, regardless of the OS.
Last but not least, I did NOT wanted to use LaTex.

This tool is provided as is, maybe I'll fix new issues, maybe not, dunno yet.

## Requirements

This tool needs jinja2

## How to use it ?

- modify **info.json** to add your informations
- modify **cv-template.html** to change the look of the CV
- Run **generate.py**, it will create a **build** folder.

```
    .
    |--build/
       |
       |-- preview.html
       `-- print.html
```

- open **preview.html** in your browser to preview your CV.
- use **print.html** to print/save the PDF
