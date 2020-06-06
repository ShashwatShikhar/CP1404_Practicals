import wikipedia

def search_wikipedia():
    search = input("Search: ")
    while search != "":
        print(wikipedia.summary(search))
        page = wikipedia.page(search)
        print("Page Title:", page.title)
        print("Page URL:", page.url)
        print("Page Content:", page.content)
        print("Page Image:", page.images[0])
        print("Page Link:", page.links[0])
        search = input("Search: ")
    print("Thank you ")

search_wikipedia()