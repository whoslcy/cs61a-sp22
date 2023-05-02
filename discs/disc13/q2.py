import re
def match_url(text):
    """
    >>> match_url("https://cs61a.org/resources/#regular-expressions")
    True
    >>> match_url("https://pythontutor.com/composingprograms.html")
    True
    >>> match_url("https://pythontutor.com/should/not.match.this")
    False
    >>> match_url("https://link.com/nor.this/")
    False
    >>> match_url("http://insecure.net")
    True
    >>> match_url("htp://domain.org")
    False
    """
    scheme = r'^(https?://)?'
    domain = r'[a-zA-Z0-9\.-]+'
    path = r'(/\w+.\w+)*'
    anchor = r'(/#[\w-]*)?$'
    full_string = scheme + domain + path + anchor
    return bool(re.match(full_string, text))