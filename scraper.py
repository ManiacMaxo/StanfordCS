from argparse import ArgumentParser
from pprint import pprint
from typing import Tuple
from urllib.parse import urljoin
from urllib.request import urlopen

from bs4 import BeautifulSoup, Tag

parser = ArgumentParser()
parser.add_argument("url", help="URL to the edstem.org assignment board")


def get_absolute_url(url: str, relative_url: str):
    if relative_url.startswith("http"):
        return relative_url

    return urljoin(url, relative_url)


def get_content(url: str) -> Tuple[BeautifulSoup, str]:
    resp = urlopen(url)

    if resp.status != 200:
        raise Exception(f"Failed to get content from URL: {resp.status} {resp.reason}")

    data = resp.read().decode("utf-8")

    return BeautifulSoup(data, "html.parser"), resp.url


def get_assignments(content: BeautifulSoup, url: str):
    announcements = content.find("div", {"class": "announcement-col-inner"})

    if not isinstance(announcements, Tag):
        raise Exception("Failed to find announcements")

    assignments = {}

    for announcement in announcements.find_all("div", {"class": "announcement"}):
        title = announcement.find("div", {"class": "newsfeedTitle"}).text
        paragraphs = announcement.find_all("p")

        description = "\n".join([p.text.strip() for p in paragraphs])

        links = set(
            get_absolute_url(url, a["href"])
            for p in paragraphs
            for a in p.find_all("a", href=True)
        )

        assignments[title] = {
            "content": description,
            "links": list(links),
        }

    return assignments


def main():
    args = parser.parse_args()
    content, url = get_content(args.url)

    pprint(get_assignments(content, url))


if __name__ == "__main__":
    main()
