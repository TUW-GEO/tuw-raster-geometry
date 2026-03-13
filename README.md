# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/TUW-GEO/tuw-raster-geometry/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                           |    Stmts |     Miss |   Cover |   Missing |
|----------------------------------------------- | -------: | -------: | ------: | --------: |
| src/tuw\_raster\_geometry/\_\_init\_\_.py      |        5 |        1 |     80% |        11 |
| src/tuw\_raster\_geometry/common\_types.py     |        3 |        0 |    100% |           |
| src/tuw\_raster\_geometry/optional\_modules.py |       30 |       14 |     53% |3, 6, 11, 20-26, 33-37, 44-48 |
| src/tuw\_raster\_geometry/pixel.py             |       33 |        0 |    100% |           |
| src/tuw\_raster\_geometry/projected.py         |        9 |        2 |     78% |    12, 15 |
| src/tuw\_raster\_geometry/tile\_operations.py  |       13 |        0 |    100% |           |
| **TOTAL**                                      |   **93** |   **17** | **82%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/TUW-GEO/tuw-raster-geometry/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/TUW-GEO/tuw-raster-geometry/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/TUW-GEO/tuw-raster-geometry/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/TUW-GEO/tuw-raster-geometry/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FTUW-GEO%2Ftuw-raster-geometry%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/TUW-GEO/tuw-raster-geometry/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.