#Interact With Websites in Real Time

#Sometimes we want to be able to fetch real-time data from a website that offers continually updated information.

#we can automate this process using the .get() method of the MechanicalSoup Browser object.

#The first thing we need to do is determine which element on the page contains the result of the die roll.

# mech_soup.py

# mech_soup.py
import mechanicalsoup
import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(4):
    #make the headless browser for the given url
    page = browser.get("http://olympus.realpython.org/dice")
    #the tag holds the first css id selector named result
    tag = page.soup.select("#result")[0]
    #we take the text lying between the 2 id tags of result
    result = tag.text
    #we are printing the result
    print(f"The result of your dice roll is: {result}")

    #we are executing this if condition because we dont want to wait for another 10 secs after the last ietration
    if i < 3:
        #we wait for 10 secinds before entering the next iteration
        time.sleep(2)

