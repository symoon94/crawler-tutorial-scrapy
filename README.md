# crawler-tutorial

This short programs are crawlers scraping a [quote site](http://quotes.toscrape.com/) and a site of the [CoreTech](http://coretech21c.co.kr/) company.


## Installation

To install Scrapy using [conda](https://www.accordbox.com/blog/scrapy-tutorial-4-how-install-scrapy-windows//), run:

    $ conda install -c conda-forge scrapy

Alternatively, if you’re already familiar with installation of Python packages, you can install Scrapy and its dependencies from PyPI with:

    $ pip install Scrapy


## Usage

To scrape the site and store the data:

    $ cd scrapy
    $ scrapy crawl quote -o quote.json

or

    $ cd coretech
    $ scrapy crawl coretech -o coretech.json

To see the json files on the localhost page, run:

    $ python -m http.server 8000


## Author

Sooyoung Moon / [@symoon94](https://www.facebook.com/msy0128) 