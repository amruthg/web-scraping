from urllib.request import urlopen

# urlib is a livrary that contains tools to handle with urls

# the above file is responsible for opening a url in the program

url = "http://olympus.realpython.org/profiles/aphrodite"
# instantiating a url variable

# now opening the url which returns a http response
page = urlopen(url)

#now if for getting the htm cotent from the page

html_bytes= page.read()#this returns a group of bytes
html = html_bytes.decode("utf-8")#this decodes the bytes to strings

# to see the html contents of the page
# print(html)

# EXTRACTING TEXT FROM HTML USING STRING METHODS

title_index =  html.find("<title>")
#the find function returns -1 if result is not found

start_index = title_index + len("<title>")

end_index = html.find("</title>")

title = html[start_index:end_index]

print(title)









