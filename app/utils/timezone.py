from config.settings import settings
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def utc_to_local(utc_dt) -> datetime:
    return utc_dt.replace(tzinfo=ZoneInfo('UTC')).astimezone(tz=ZoneInfo(settings.timezone))