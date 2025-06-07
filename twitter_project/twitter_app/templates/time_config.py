from django import template
from django.utils import timezone
from django.utils.timesince import timesince
import re

register = template.Library()

@register.filter
def configured_time(value):
    """
    Twitter-like time: '5m', '2h', '3d', or 'May 20' if older than 7 days.
    """
    if not value:
        return ""
    now = timezone.now()
    diff = now - value
    days = diff.days
    if days < 0:
        return ""
    if days == 0:
        time_str = timesince(value)
        match = re.match(r"(\d+)\s+(\w+)", time_str)
        if not match:
            return time_str
        num, unit = match.groups()
        unit = unit.lower()
        if unit.startswith("minute"):
            return f"{num}m"
        elif unit.startswith("hour"):
            return f"{num}h"
        else:
            return "now"
    elif days < 7:
        return f"{days}d"
    else:
        return value.strftime("%b %-d") if hasattr(value, 'strftime') else value.strftime("%b %d")