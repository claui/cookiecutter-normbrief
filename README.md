# cookiecutter-normbrief

[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for a [Normbrief](https://www.deutschepost.de/de/b/briefvorlagen/normbrief-din-5008-vorlage.html), a letter that conforms to the German national standard [DIN 5008](https://en.wikipedia.org/wiki/DIN_5008).

## Project status

This is **alpha-quality software**. The letter scaffolded by this template is **nowhere near conforming** to DIN 5008 yet. I hope we’ll get there, though.

## Project goals

This project produces a letter template. It aims for the following goals:

- **Few moving parts**: To use the letter template, you currently need to have Linux, a text editor, [Pandoc](https://pandoc.org/) and a browser installed.

- **SCM-friendly**: the letter uses text-based markup so you can check it into Git if you like.

- Plays well with [VS Code](https://code.visualstudio.com/): The Markdown preview built into Visual Studio Code displays an OK-ish approximation of the letter as you type.

## Non-goals

Non-goals of this project include [WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG), ease of use for non-nerds, and more.

## Using cookiecutter-normbrief

### Basic usage

To run the template generator, make sure you have a working
Cookiecutter installation. Then run:

```
cookiecutter gh:claui/cookiecutter-normbrief
```

### Alternative usage

If you use `cookiecutter-normbrief` often, you can add to your
`.cookiecutterrc` an `abbreviations` section like so:

```
abbreviations:
    normbrief: https://github.com/claui/cookiecutter-normbrief.git
```

Then, to generate a project, run:

```
cookiecutter normbrief
```

## See also

- https://en.wikipedia.org/wiki/DIN_5008
- https://www.deutschepost.de/de/b/briefvorlagen/normbrief-din-5008-vorlage.html
- https://github.com/mac-and-i/Normbrief-mit-Markdown

## License

Copyright (c) 2022 Claudia Pellegrino <clau@tiqua.de>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).

### Additional license files

This project may include additional license files other than the
Apache License. Those are just there for the template user’s
convenience so they can choose a license for their own content.
Those licenses may not apply to this project. The only license
that applies to this project is the Apache License.
