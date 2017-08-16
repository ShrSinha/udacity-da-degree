import time,urllib,requests
from bs4 import BeautifulSoup

def wikipedia_crawl(initial_url,target_url="https://en.wikipedia.org/wiki/Philosophy",max_steps=25):
    """ Follow the first URL from one page to next and see if the crawl ends up at 
    target page within specified steps.
    
    The URL should not be a citation etc. It should be part of page's content.
    The initial page is assumed to be different from target page.

    initial_url -- string. 
    target_url -- string.
    max_steps -- int.
    """

    def find_first_url(url):
        # Function to find the page's first url, ignoring help and citations.
        link = None
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        content = soup.find(id="mw-content-text").find(class_="mw-parser-output")

        for element in content.find_all("p", recursive=False):
            if element.find("a", recursive=False):
                link = element.find("a", recursive=False).get('href')
                break

        if not link:
            return

        first_url = urllib.parse.urljoin('https://en.wikipedia.org/', link)

        return first_url

    def continue_crawl(search_history, target_url, max_steps):
        # Function to evaluate if crawl should continue.
        if search_history[-1] == target_url:
            print("Search has found the target page.")
            return False
        elif len(search_history) > max_steps:
            print("Search has exceeded upper limit without reaching target page.")
            return False
        elif search_history[-1] in search_history[:-1]:
            print("Search has entered a loop without reaching target page.")
            return False
        else:
            return True

    search_history = [initial_url]

    while continue_crawl(search_history, target_url, max_steps):
        # Function to implement crawl.
        # Function waits for 2 seconds before sending the next web page request.
        first_url = find_first_url(search_history[-1])

        if not first_url:
            print("Search has arrived at a web page with no links and is aborted.")
            break

        search_history.append(first_url)

        time.sleep(2) 



wikipedia_crawl("https://en.wikipedia.org/wiki/Special:Random")        