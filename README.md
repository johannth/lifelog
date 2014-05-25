Lifelog
=======

Capture life as an immutable stream of events by aggregating data from different sources (third-party APIs and manual input) and expose data as an personal API of your life's events.

+ An event is a dictionary of properties, keys and values.
+ Each event has at least the following properties:
    + id
    + stream
    + timestamp: "2014-03-14T03:06:28+0000"

Design Statement
----------------

+ Easy to input manual data if no automatic source is available.
+ Easy to add automatic data sources, either with callbacks or periodic updates.
+ Capture all relevant data from automatic sources even if it doesn't get used for metrics immediately.
+ No duplicate events.
+ Easy to transform values from events into actionable metrics to display on a dashboard.

Proposed streams
----------------

/
/wrote
/read
/read/articles
/read/books
/watched
/played
/played/games
/time
/time/work
/time/sleep
/health
/health/weight
/health/heartbeat
/food/meals
/food/wines
/photos
/location

Version 0.1
-----------

+ API hosted on Heroku using the scheduler add-on to query the third party api-s
+ Use fouth.org to easily access with API data such as the paper API.
+ Sends events to keen.io.
+ Stores backup of events as files on Dropbox as json using the following example folder structure:

```
pocket_read_articles
├── 2014-05-23.json
├── 2014-05-24.json
└── 2014-05-25.json
``

Inspiration
-----------

api.naveem.com

Installation
============

This project depends on:

+ [fouth](https://foauth.org/) for accessing third party data.
+ [keen.io](https://keen.io) for data storage and analytics core.
+ redis for caching.

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create an .env:

```
SECRET_KEY=...

FOUTH_USERNAME=...
FOUTH_PASSWORD=...

REDIS_URL=...

KEEN_PROJECT_ID=...
KEEN_WRITE_KEY=...
KEEN_READ_KEY=...
``




