from models import Author, Quotes, Tag
from connect import connect
import json
from datetime import datetime


def convert_born_date(date_str):
    return datetime.strptime(date_str, "%B %d, %Y")


with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)

for author_data in authors_data:
    born_date_str = author_data.pop('born_date')
    author_data['born_date'] = convert_born_date(born_date_str)
    author = Author(**author_data)
    author.save()

with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)

for quote_data in quotes_data:
    tags = quote_data.pop('tags', [])  
    quote_data['tags'] = [{'name': tag} for tag in tags]  # Konwersja tagów na format oczekiwany przez model
    author_name = quote_data.pop('author')
    author = Author.objects(fullname=author_name).first()
    if author:
        quote_data['author'] = author   # Utworzenie referencji do autora
        quote = Quotes(**quote_data)
        quote.save()                    # Zapisanie cytatu z referencją do autora
    else:
        print(f"The author '{author_name}' does not exist.")