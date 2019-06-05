import re


def domain_name(url):
    return re.search('^http(s)?://(www\.)?(?P<domain>[\w\-_]*).*', url).group('domain')


print(domain_name('http://github.com/carbonfive/raygun'))
