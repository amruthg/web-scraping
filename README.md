# web-scraping

Collecting data from websites using an automated process is known as web scraping.

In most of the cases you are not allowed to scrape from websites  because:

  >personal data;
  >too much data makes too many requests resulting in server crash.

to download the beautiful soup library for specific html parsing use the below code
```
$ python -m pip install beautifulsoup4
```
#we can replace all these lines using the .replace file if we want to.

#and if you want to get only specific type of text from the file.Then, you first get the bottlesoup object and then do
#then use the .findall() on it to get the required text.

#but sometimes you want to find the data based on the tags.
#for example all the list of images in the the html file. then, use .find_all("img") to get all the instances of image tags

#there is a difference between the findall and finsd_all tags. the first one is used to find all the substrings in a string
#wheras the 2nd one fins all the opening tags with the given argument name.
#the 2nd one is used for tag objects
