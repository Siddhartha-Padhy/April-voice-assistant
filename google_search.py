from config import *
import webbrowser

"""
Function to open the web browser with the query searched in it.
srch_data: Query
* If srch_data is the name of a website present in BOOKMARKS then web browser will directly open with the website.
"""
def g_search():
    heading = "Web Search"
    desc = []
    found = False
    config.speak("Enter query")
    srch_data = config.listen()
    if srch_data == None:
        print("Query Please")
        g_search()
    else:
        desc.append("Query: "+srch_data)
        srch_data = srch_data.replace(" ","+")
        for website, url in BOOKMARKS.items():
            if website == srch_data:
                found = True
                webbrowser.open(url)

        if found==False:
            url = 'https://www.google.co.in/search?q=' + srch_data
            webbrowser.open(url)

    return (heading, desc)
