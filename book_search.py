
# book_search.py
# Library Management System - Book Search Module

books = [
    {"id": 1, "title": "Python Programming", "author": "John Smith", "year": 2022},
    {"id": 2, "title": "Data Structures and Algorithms", "author": "Robert Lafore", "year": 2019},
    {"id": 3, "title": "Artificial Intelligence", "author": "Stuart Russell", "year": 2021},
    {"id": 4, "title": "Database Management Systems", "author": "Raghu Ramakrishnan", "year": 2018},
    {"id": 5, "title": "Computer Networks", "author": "Andrew Tanenbaum", "year": 2020},
]


def search_books(keyword):
    """Search for books by title or author."""
    keyword = keyword.strip().lower()

    if not keyword:
        return []

    results = []

    for book in books:
        if (keyword in book["title"].lower()
                or keyword in book["author"].lower()):
            results.append(book)

    return results


def display_books(book_list):
    """Display the matching books."""
    if not book_list:
        print("No books found.")
        return

    print("\nBooks found:")
    print("-" * 65)
    print(f"{'ID':<5}{'Title':<38}{'Author':<20}{'Year'}")
    print("-" * 65)

    for book in book_list:
        print(
            f"{book['id']:<5}"
            f"{book['title']:<38}"
            f"{book['author']:<20}"
            f"{book['year']}"
        )


def main():
    """Run the interactive book search."""
    print("===================================")
    print("     LMS - BOOK SEARCH MODULE")
    print("===================================")

    while True:
        keyword = input(
            "\nEnter book title or author (or 'exit' to quit): "
        ).strip()

        if keyword.lower() == "exit":
            print("Exiting Book Search. Thank you!")
            break

        results = search_books(keyword)
        display_books(results)


if __name__ == "__main__":
    main()
