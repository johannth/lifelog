import os

from lifelog.cache import Cache
from lifelog.analytics import AnalyticsStore

cache = Cache()
analytics_store = AnalyticsStore(
    project_id=os.environ["KEEN_PROJECT_ID"],
    write_key=os.environ["KEEN_WRITE_KEY"],
    read_key=os.environ["KEEN_READ_KEY"]
)


def init_extensions(app):
    cache.init_app(app)