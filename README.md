This repo is a fork of [pyswagger](https://github.com/pyopenapi/pyswagger), for my own need.

**appswag** is exactly what **pyswagger** is (same code, same apis). But **appswag** is a package (which does'nt interfer with pyswagger), and will contain some minor changes ... just for me/us.

**New version 0.10.0**, for py3.7 to py3.12 !

[Available on pypi](https://pypi.org/project/appswag/#history)


All pytests works: `285 passed, 4 skipped, 11 warnings in 11.24s`

    py -m pytest .\appswag\tests

And it's buildable

    py .\setup.py bdist

[![Upload Python Package](https://github.com/manatlan/appswag/actions/workflows/python-publish.yml/badge.svg)](https://github.com/manatlan/appswag/actions/workflows/python-publish.yml)

[![Test](https://github.com/manatlan/appswag/actions/workflows/python-package.yml/badge.svg)](https://github.com/manatlan/appswag/actions/workflows/python-package.yml)
