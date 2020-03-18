try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found.")


def ImportanceChecker(query, stoplevel=10, pauselevel=1):
    """
    Checks 'importance' by analyzing google search results for a person/topic and
    finding if they have a wikipedia page among the top results. Number of search
    results required is automatically set to 10.
    """

    #urlgenerator runs relatively slowly to prevent google from blocking user IP
    urlgenerator = search(query, stop=stoplevel, pause=pauselevel)
    for _ in range(stoplevel):
        url = next(urlgenerator)
        if 'wikipedia' in url:
            return True
    return False


def main():
    print("Who do you want to be searched? ", end="")

    query = input()

    important = ImportanceChecker(query)

    if (important):
        print(f"{query} is important!")
    else:
        print(f"{query} isn't that important.")

if __name__ == "__main__":
    main()