"""
This script demonstrates how to use multithreading to fetch web content concurrently.
It uses the requests library to fetch HTML and BeautifulSoup to parse and extract the page title.
"""
import threading
import time
import requests
from bs4 import BeautifulSoup

URLS = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
]

def fetch_content(url):
    print(f"Fetching content from {url}")
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    print(f"Content fetched from {url}, title: {soup.title.string if soup.title else 'No Title'}")

threads=[]

for url in URLS:
    thread = threading.Thread(target=fetch_content, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

