# Python web crawler

from urllib.request import urlopen
html = urlopen("http://www.wikipedia.org")
print(html.read())