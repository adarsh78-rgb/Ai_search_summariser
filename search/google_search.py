from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def google_search(query, num_results=5):
    search = GoogleSearch({
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num_results
    })
    results = search.get_dict()
    links = []

    for res in results.get("organic_results", []):
        if 'link' in res:
            links.append(res['link'])
    return links


# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# def google_search(query, num_results=5):
#     query = urllib.parse.quote_plus(query)
#     url = f"https://www.google.com/search?q={query}"

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#     }

#     response = requests.get(url, headers=headers)
#     if response.status_code != 200:
#         print("Failed to retrieve search results.")
#         return []

#     soup = BeautifulSoup(response.text, "html.parser")
#     search_results = []

#     for g in soup.find_all('div', class_='tF2Cxc'):
#         link_tag = g.find('a')
#         if link_tag and link_tag['href']:
#             search_results.append(link_tag['href'])
#             if len(search_results) >= num_results:
#                 break

#     return search_results
