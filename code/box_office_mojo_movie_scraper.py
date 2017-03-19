import requests
from bs4 import BeautifulSoup
from pprint import pprint

def clean_html(soup):
    """Get rid of all bold, italic, underline and link tags"""
    invalid_tags = ['b', 'i', 'u', 'nobr', 'font']
    for tag in invalid_tags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()
    return soup


def extract_basic_movie_info(page):
    try:
        center = page.findAll('center')
        if len(center) == 0:
            pass
        table = center[0].findAll('table')[0]
        rows = table.findAll('tr')
        for table_row in rows:
            contents = [td.renderContents() for td in table_row.findAll('td')]
            contents = [item.split(":") for item in contents]
            data = {item[0]: item[1] for item in contents}
            pprint(data)
    except():
        print "Something went wrong parsing a movie's page"
        raise


def get_movie_summary_by_id(movie_id):
    url_start = 'http://www.boxofficemojo.com/movies/?page=summary&id='
    url_end = '.htm'

    raw_page = requests.get(url_start + movie_id + url_end)
    page = BeautifulSoup(raw_page.content, 'html.parser')
    page = clean_html(page)

    extract_basic_movie_info(page)


get_movie_summary_by_id('legendary2016')
