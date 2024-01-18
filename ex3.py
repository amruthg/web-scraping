#Extract Text From HTML With Regular Expressions

#we know that python is a greedy language but .*? is a non greedy quantifier

from bs4 import BeautifulSoup
from urllib.request import urlopen

#the first 3 steps are from ex1
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
#this step creates a beautiful soup object and the first argument is the variable with the decoded html response
#and the 2nd argument is the inbuilt python parser that we are using
#here we have created a beautiful soup object and assigned it to the variable soup.
soup = BeautifulSoup(html, "html.parser")
#this line gives me the content left after removing all html tags and code syntaxes
print(soup.get_text())
#we can notice extra lines being left in between. These are nothing but the '\n' characters in between



#if you want the type og tag from the variable holding a tag object
#then use the .name 

image1, image2 = soup.find_all("img")
print(image1.name)

#You can access the HTML attributes of the Tag object by putting their names between square brackets, just 
#as if the attributes were keys in a dictionary.

image1["src"]    #gives the src attribute 
image2["src"]    #gives the src attribute  

#Certain tags in HTML documents can be accessed by properties of the Tag object.
print(soup.title)      #gives the title of the html file

#Beautiful Soup automatically cleans up the tags for you

#You can also retrieve just the string between the title tags with the .string property of the Tag object:
print(soup.title.string)

#One of the features of Beautiful Soup is the ability to search for specific kinds of tags whose attributes match certain values.
soup.find_all("img", src="/static/dionysus.jpg")


