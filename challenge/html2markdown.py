import re
def html2markdown(html):
    '''Take in html text as input and return markdown'''
    md = re.sub(r"<em>(.+?)</em>", r"*\1*", html)
    md = re.sub(r"(\s+)", " ", md)
    md = re.sub(r"<p>(.+?)</p>", r"\1\n\n", md).rstrip()
    md = re.sub(r"<a href=\"(.+?)\">(.+?)</a>", r"[\2](\1)", md)
    return md