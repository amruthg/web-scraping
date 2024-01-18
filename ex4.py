import mechanicalsoup
browser = mechanicalsoup.Browser()  #imports a headless web browser object

url = "http://olympus.realpython.org/login"
page = browser.get(url) #page is a Response object that stores the response from requesting the URL from the browser

print(page) #returns status code 200 meaning successful request transmission
#404 and 500 are for errors

print(type(page))       #response object
print(type(page.soup))  #type= beautiful soup object
print(page.soup)        #gives me the html code of the file


