#!/usr/bin/env python3

"""Download HTML page using standard library."""


from urllib import request


def download_html(url):
    """Download html from url."""
    response = request.urlopen
    response = request.urlopen(url)
    html_text = response.read().decode('UTF-8')
    return html_text


def save_html(url):
    """Save html from url.

    :param: url address
    """
    html = download_html(url)
    name = url.rpartition('/')[-1]
    with open(f'{name}.html', 'w') as fo:
        fo.write(html)


if __name__ == "__main__":
    save_html('https://github.com')
