#Submit a Form With MechanicalSoup

import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
#get the headless browser object for the given url
login_page = browser.get(url)
#this helps me get the html code of the website
login_html = login_page.soup

# 2
#out of the list of form tag objects take the 0th index object
form = login_html.select("form")[0]
#out of the list of inputs of form object we take the 0th and 1st objects.
#now put the values for both as the inputs you are giving
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
#now submit the input form object and the url of the page
profiles_page = browser.submit(form, login_page.url)
#Now that you have the profiles_page variable set, it’s time to programmatically obtain the URL for each link on the /profiles page.
links = profiles_page.soup.select("a")

for link in links:
    address = link["href"]
    text = link.text
    print(f"{text}: {address}")

base_url = "http://olympus.realpython.org"
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")