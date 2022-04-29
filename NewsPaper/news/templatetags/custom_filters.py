import re

from django import template

register = template.Library()

BAD_WORDS = ["хуй", "пизда"]


@register.filter(name="censor")
def censor(value):
    for bad_word in BAD_WORDS:
        for match in re.finditer(bad_word, value):
            value = value[: match.start()] + "*" * len(bad_word) + value[match.end() :]
    return value
