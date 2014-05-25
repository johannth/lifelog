import functools

from lifelog.foauth import foauth
from lifelog.utils import to_unix_timestamp, from_unix_timestamp, to_iso_8601

POCKET_API_URL = 'getpocket.com/v3'

pocket_post = functools.partial(foauth,
                                base_api_url=POCKET_API_URL,
                                method='POST')


def get_articles(state='all', since=None, content_type='article', sort='oldest'):
    data = {
        'state': state,
        'detailType': 'complete',
        'contentType': content_type,
        'sort': sort
    }

    if since:
        data['since'] = str(int(to_unix_timestamp(since)))

    response = pocket_post('get', data=data)
    response_data = response.json()

    if response_data['list']:
        all_articles = response_data['list'].itervalues()
        valid_articles = (a for a in all_articles if a['status'] != '2')
        sorted_articles = sorted(valid_articles, key=lambda a: a['sort_id'])
        return sorted_articles
    else:
        return []


def get_read_articles_stream(since):
    articles = (a for a in get_articles(state="archive", since=since) if a["time_read"])
    return (article_to_event(a) for a in articles)


def article_to_event(article):
    article_event = article.copy()
    for key in ("time_added", "time_favorited", "time_read", "time_updated"):
        article_event[key] = convert_timestamp_to_isoformat(article[key])

    if article_event["time_read"]:
        article_event["timestamp"] = article_event["time_read"]
    else:
        article_event["timestamp"] = article_event["time_updated"]

    for key in ("authors", "images", "videos", "tags"):
        if key in article:
            article_event[key] = article[key].values()

    for key in ("is_article", "is_index", "favorite", "has_image", "has_video"):
        article_event[key] = article[key] == '1'

    if 'word_count' in article:
        article_event['word_count'] = int(article.get('word_count', 0))

    return article_event


def convert_timestamp_to_isoformat(timestamp):
    if timestamp == '0':
        return None
    else:
        return to_iso_8601(from_unix_timestamp(timestamp))
