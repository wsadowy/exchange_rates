Exchange Rates
========

The following is a Django application, whose purpose is to obtain the information on current exchange rates (compared to Euro)
from https://www.ecb.europa.eu RSS feed and serve them through REST API.
The application uses `Scrapy` for crawling the web page and `Django Rest Framework` for API responses.


## Installation

Clone the repository

```bash
$ git clone https://github.com/wsadowy/main_repo
```
Export the export DJANGO_SETTINGS_MODULE variable
```bash
$ export DJANGO_SETTINGS_MODULE=exchange_rates.settings
```

It is best to use `virtualenv` to install the app.

```bash
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

```

## Usage


Navigate to the `exchange_rates` directory and run

```bash
$ ./manage.py crawl
```
to scrape the RSS feed, and then

```bash
$ ./manage.py runserver
```
to run the development server locally.

Test the installation by navigating to

```
localhost:8000/currencies
```
in your browser.

You should see the API response with exchange rates from the RSS feed.


## To do

* Cron job running the crawl command once a day after the RSS feed has been refreshed.
* Complete unit tests.


