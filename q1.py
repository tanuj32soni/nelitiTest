from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
import re


def word_frequencies(base_url):
    """
    Downloads the content from the given URL and returns a dict {word -> frequency}
    giving the count of each word on the page. Ignores HTML tags in the response.
    :param url: Full URL of HTML page
    :return: dict {word -> frequency}
    """
    html = urlopen(base_url)
    bs_obj = BeautifulSoup(html.read(), features="html.parser");
    count = Counter()
    words=0
    # remove script and css
    for script in bsObj(["script", "style"]):
        script.clear()

    text = bsObj.get_text()
    text = re.sub(r'[\t\r\n]', '', text)

    count.update(text.split(" "))
    print(count)
    return count