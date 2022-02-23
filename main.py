import requests
from bs4 import BeautifulSoup

URL = "https://www.audible.com/search?keywords=book&node=18573211011"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_books = soup.find_all(name="h3", class_="bc-heading bc-color-link bc-pub-break-word bc-size-medium")

book_titles = [book.getText() for book in all_books]
books = book_titles[::-1]

with open("books.txt", mode="w") as file:
    for book in books:
        file.write(f"{book}\n")


