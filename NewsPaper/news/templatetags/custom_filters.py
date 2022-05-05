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


@register.filter(name="pagination_start")
def pagination_start(value, num_pages):
    return max(1, value - 2 if value == num_pages else value - 1)


@register.filter(name="pagination_end")
def pagination_end(value, num_pages):
    return min(num_pages, value + 2 if value == 1 else value + 1)


@register.simple_tag(takes_context=True)
def filtered_posts(context, posts):
    return context["filter"].qs if context.get("search_enabled", False) else posts
