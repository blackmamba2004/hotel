from datetime import datetime
from calendar import timegm

def convert_to_timestamp(datetime: datetime) -> int:
    return timegm(datetime.utctimetuple())
