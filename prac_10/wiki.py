import wikipedia

search_term = input("Enter a search term: ")
while search_term != "":
    print(wikipedia.search(search_term))
    search_term = input("Enter a search term: ")
