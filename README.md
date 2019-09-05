
# py-scrape-sportsbookreview

[![License](https://img.shields.io/github/license/likecarter/py-scrape-sportsbookreview)](https://dtmtheodds.com)

[py-scrape-sportsbookreview](https://github.com/LikeCarter/py-scrape-sportsbookreview//) is an implementation of [Scrapy](https://github.com/scrapy/scrapy) that pulls historical betting odds from [SBR](https://www.sportsbookreview.com/). 

## Prerequisites

- Python 2.7 or Python 3.5+
- Works on Linux, Windows, Mac OSX, BSD

## Installing

In order to run the scraper, ensure that you have (Git)[https://git-scm.com/] and [Python](https://www.python.org/) installed.

Install scrapy:

```bash
pip install scrapy
```

Clone a copy of the repo:

```bash
git clone https://github.com/LikeCarter/py-scrape-sportsbookreview/
```

Change to the py-scrape-sportsbookreview directory:

```bash
cd py-scrape-sportsbookreview
```

## Usage

```bash
scrapy crawl dtmto
```

### Running Tests

```bash
scrapy check
```

### Debugging

```bash
scrapy parse --spider=myspider -c parse_item -d 2 -v <item_url>
```

## Thanks

**py-scrape-sportsbookreview** © 2019+, Carter Sprigings. Released under the [MIT] License.<br>
Authored and maintained by Carter Sprigings with help from contributors ([list][contributors]).

> [dtmtheodds.com](http://dtmtheodds.com) &nbsp;&middot;&nbsp;
> GitHub [@likecarter](https://github.com/likecarter)

[MIT]: http://mit-license.org/
[contributors]: http://github.com/likecarter/py-scrape-sportsbookreview/contributors
