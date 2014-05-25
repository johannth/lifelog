#!/usr/bin/env python

from datetime import timedelta

from lifelog.app import create_app
from lifelog.sources.pocket import get_read_articles_stream
from lifelog.extensions import cache, analytics_store
from lifelog.utils import from_iso_8601, to_iso_8601

POCKET_CACHE_KEY = "pocket:read:last_updated"


def feed_latest_pocket_data_to_analytics_store(cache, analytics_store):
    since = from_iso_8601(cache.get(POCKET_CACHE_KEY))

    print("Fetching pocket data since {}".format(since))

    article_stream = get_read_articles_stream(since)

    print("Saving stream to analytics store")
    save_article_stream_to_analytics_store(article_stream, cache, analytics_store)


def save_article_stream_to_analytics_store(article_stream, cache, analytics_store):
    for i, article_event in enumerate(article_stream):
        print(u"Processing article event {} - {}:{} {}".format(
            i,
            article_event["item_id"],
            article_event.get("resolved_title", "No Title"),
            article_event["time_updated"]
        ))

        analytics_store.add_event("pocket_read_articles", article_event,
            timestamp=from_iso_8601(article_event["timestamp"]))

        # We store the time_updated so if anything crashes we can continue from
        # that point and don't get duplicates. The extra five seconds are so that
        # we don't get the last item again.
        last_updated = from_iso_8601(article_event["time_updated"]) + timedelta(seconds=5)
        cache.set(POCKET_CACHE_KEY, to_iso_8601(last_updated))


if __name__ == '__main__':
    create_app()
    feed_latest_pocket_data_to_analytics_store(cache, analytics_store)
