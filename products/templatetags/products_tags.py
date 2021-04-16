from django import template

register = template.Library()


# Split Filter Tag found at:
# https://roytuts.com/creating-custom-template-tags-and-filter-in-django/
@register.filter(name='split')
def split(str, delimiter):
    return str.split(delimiter)


@register.filter
def to_ampersand(value):
    return value.replace("_N_", " & ").replace("_", " ")


@register.simple_tag
def current_query_url(key, value, urlencode=None):
    # Isolate the page number in the format ?page=1
    url = "?{}={}".format(key, value)
    if urlencode:
        queries = urlencode.split("&")
        # Isolate queries from page number
        filtered_queries = filter(lambda q: q.split("=")[0] != key, queries)
        # Join queries using the ampersand
        encoded_queries = "&".join(filtered_queries)
        # Reattach the queries to the page number
        url = "{}&{}".format(url, encoded_queries)
    return url


@register.filter
def can_review(user, reviews):
    reviews = reviews
    user = user
    reviewers = reviews.values_list('user', flat=True)
    if (user in reviewers):
        can_review = False
    else:
        can_review = True
    return can_review
