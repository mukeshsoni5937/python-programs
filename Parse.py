import re
from urllib.request import urlopen
def parse_webpage(url):
    try:
        # Open the URL and read its HTML content
        with urlopen(url) as response:
            html_content = response.read().decode('utf-8') 
        
        # Find all the links using regular expressions
        links = re.findall(r'href=["\'](.*?)["\']', html_content)
        
        # Print out all the links found
        for link in links:
            print(link)
    except Exception as e:
        print("Failed to retrieve webpage:", e)

url = 'https://en.wikipedia.org/wiki/Wiki'
parse_webpage(url)

