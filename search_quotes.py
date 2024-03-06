from models import Quotes, Author, Tag
from connect import connect


def search_quotes():
    while True:
        command = input("Enter the command (tag:<tag> / tags:<tag,tag> / name:<author's fullname> / exit): \n")
        if command.startswith("name:"):
            author_name = command.split(":")[1].strip()
            author = Author.objects(fullname=author_name).first()
            if author:
                quotes = Quotes.objects(author=author)  
                if quotes:
                    for quote in quotes:
                        print(f"Quote: {quote.quote}\n")
                else:
                    print("No quote for the author.")
            else:
                print("No author with the given name.")

        elif command.startswith("tag:"):
            tag = command.split(":")[1].strip()
            quotes = Quotes.objects(tags__name=tag)
            if quotes:
                for quote in quotes:
                    print(f"Quote: {quote.quote}\n")
            else:
                print(f"No quotes for tag: {tag}.")

        elif command.startswith("tags:"):
            tags = command.split(":")[1].strip().split(",")
            quotes = Quotes.objects(tags__name__in=tags)
            if quotes:
                for quote in quotes:
                    print(f"Quote: {quote.quote}\n")
            else:
                print(f"No quotes for tags: {', '.join(tags)}.")
        
        elif command == "exit":
            break
        else:
            print("Invalid command.")

search_quotes()

