import re

def is_valid_url(url):
    youtube_url_regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
    return re.match(youtube_url_regex, url) is not None
