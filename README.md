# data-collection-disaster-news-classification

This is a Python script that uses the [snscrape](https://github.com/JustAnotherArchivist/snscrape) library to scrape tweets from Twitter based on specific keywords and dates. The script outputs the scraped tweets to a CSV file for further analysis.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
pip install -r requirements.txt
```

## Usage
You can change these parameters to customize the scraper according to your needs
```python
import snscrape.modules.twitter as sntwitter
import pandas as pd

# change keywords
keywords = []

# customize your scraping queries e.g.
query = "(from:elonmusk) " + " OR ".join(keywords)

# limit the no. of tweets to scrap off twitter e.g.
limit = 50

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/susanhsrestha/data-collection-disaster-news-classification/blob/main/LICENSE)
