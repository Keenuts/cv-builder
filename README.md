# CV-Builder & Cover letter generator

I needed a CV, and coulnd't use InDesign anymore.
I also Needed something that could run all my computers, regardless of the OS.
Last but not least, I did NOT wanted to use LaTex.

This tool is provided as is, maybe I'll fix new issues, maybe not, dunno yet.

## Features

* generate a CV using JSON file
* also generates a MarkDown output for 'copy-paste your CV' fields
* can generate a cover-letter with generic & specific blocks
* also generates a .txt cover-letter for mails or copy-paste fields

## Requirements

This tool needs jinja2

## Project architecture

```
    .
    |-- templates/
    |-- cover-letter/
    |-- info.json
    |-- style.css
    `-- generate.py
```
    
### info.json

Contains all the informations needed to generate your CV.

### templates/

This folder contains all the templates.
Most of the time, you'd like to update the **cv-base.html** or **cover-base.html**

### cover-letter/

This folder contains the basic blocks to compose a cover letter.
By design, intro, experience and conclusion blocks are generic.
But you **may** want to add some specific content for your cover letter.

Example:

* I want to write a cover-letter for **SECRET COMPANY**
* Change the **info.json** 'company' field to **'SECRET COMPANY'**
* Create a file **secret-company.md** in cover-letter/

If no specific block can be found, fallback block is company-generic.md.


## How to use it ?

- modify **info.json** to add your informations
- Run **generate.py**, it will create a **build** folder.

```
    .
    |--build/
       |
       |-- cv-preview.html
       |-- cv-print.html
       |-- cv-text.md
       |-- cover-preview.html
       |-- cover-print.html
       `-- cover-text.txt
```

- open **cv-preview.html** in your browser to preview your CV.
- use **cv-print.html** to print/save the PDF

you can also:

- modify **templates/cv-base.html** to change the look of the CV.
- modify **templates/cover-base.html** to change the look of the cover-letter.
- modify **cover-letter/*.md** to change the content of your cover letter.
