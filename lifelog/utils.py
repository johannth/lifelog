from datetime import datetime

import dateutil.parser


def to_unix_timestamp(dt):
    timestamp = (dt - datetime(1970, 1, 1)).total_seconds()
    return timestamp


def from_unix_timestamp(timestamp):
    if timestamp:
        return datetime.utcfromtimestamp(float(timestamp))
    else:
        return None


def to_iso_8601(dt):
    return dt.isoformat()


def from_iso_8601(isoformat):
    if isoformat:
        return dateutil.parser.parse(isoformat)
    else:
        return None
