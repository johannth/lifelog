import pytest

from lifelog.sources import pocket


@pytest.fixture
def raw_article():
    return {
        u'authors': {u'9109759': {u'author_id': u'9109759',
                           u'item_id': u'605584922',
                           u'name': u'Matt Gemmell',
                           u'url': u'http://mattgemmell.com/about'}},
        u'excerpt': u'Cut the bezel and you\u2019ve got a machine that is essentially the size of the 11\u201d Air, just a wee bit taller, but closer to the 13\u201d when it comes to productivity.  I enjoyed the article, and I\u2019d love that machine too.',
        u'favorite': u'0',
        u'given_title': u'Continue reading \u2192',
        u'given_url': u'http://mattgemmell.com/small-screen-productivity/',
        u'has_image': u'1',
        u'has_video': u'0',
        u'image': {u'height': u'360',
                   u'item_id': u'605584922',
                   u'src': u'https://farm8.staticflickr.com/7207/14031265236_230015a1f2_z.jpg',
                   u'width': u'640'},
        u'images': {u'1': {u'caption': u'',
                           u'credit': u'',
                           u'height': u'360',
                           u'image_id': u'1',
                           u'item_id': u'605584922',
                           u'src': u'https://farm8.staticflickr.com/7207/14031265236_230015a1f2_z.jpg',
                           u'width': u'640'}},
        u'is_article': u'1',
        u'is_index': u'0',
        u'item_id': u'605584922',
        u'resolved_id': u'605584922',
        u'resolved_title': u'Small screen productivity',
        u'resolved_url': u'http://mattgemmell.com/small-screen-productivity/',
        u'sort_id': 22,
        u'status': u'1',
        u'time_added': '1400330205',
        u'time_favorited': '0',
        u'time_read': '1400393776',
        u'time_updated': '1400393778',
        u'word_count': u'1943'
    }


def test_cleanup_article_data_transforms_timestamps(raw_article):
    event = pocket.article_to_event(raw_article)

    assert event["time_added"] == "2014-05-17T12:36:45"


def test_cleanup_article_data_replaces_empty_timestamps_with_nones(raw_article):
    event = pocket.article_to_event(raw_article)

    assert event["time_favorited"] is None


def test_cleanup_article_data_uses_bools(raw_article):
    event = pocket.article_to_event(raw_article)

    assert event["is_article"]
    assert event["favorite"] is False


def test_cleanup_article_converts_word_count_to_int(raw_article):
    event = pocket.article_to_event(raw_article)

    assert event["word_count"] == 1943


def test_article_event_has_authors_as_an_array(raw_article):
    event = pocket.article_to_event(raw_article)

    assert event["authors"] == [{u'author_id': u'9109759',
                           u'item_id': u'605584922',
                           u'name': u'Matt Gemmell',
                           u'url': u'http://mattgemmell.com/about'}]
