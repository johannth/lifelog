import redis


class Cache(object):

    def __init__(self, redis=None):
        self.redis = redis

    def init_app(self, app):
        self.redis = redis.from_url(app.config["REDIS_URL"])

    def get(self, key):
        return self.redis.get(key)

    def set(self, key, blob, expiry=None):
        self.redis.set(key, blob, ex=expiry)

    def get_many(self, keys):
        return self.redis.mget(keys)

    def exists(self, key):
        return self.redis.exists(key)

    def flush(self):
        self.redis.flushdb()
