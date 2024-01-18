# regexes are patterns used to find strings

import re

re.findall("ab*c","ab")
# we are searchinf for arg1 in arg2

# b* means it includes all instances of 0 to any number of b's

re.findall("ab*c", "abcd")      #abc
re.findall("ab*c", "acc")       #ac
re.findall("ab*c", "abcac")     #abc
re.findall("ab*c", "abdc")      #returns an empty list

# this pattern matching is case sensitive
# but if you want to ignore the case

re.findall("ab*c", "ABC", re.IGNORECASE)

# the dot character in "a.c" is used to signify all characters starting 
# with 'a' and ending with 'c' and seperated by a single character in the entire given string

re.findall("a.c", "abc")        #abc
re.findall("a.c", "abbc")       #
re.findall("a.c", "ac")         #
re.findall("a.c", "acc")        #acc

# 'a.*c' is used when we want to find all substrings in a given string that start with 'a', end with 'c' and have
#any number if charcaters repeating any number of times

re.findall("a.*c", "abc")       #abc
re.findall("a.*c", "abbc")      #abbc
re.findall("a.*c", "ac")        #ac
re.findall("a.*c", "abbddc")    #abbddc
re.findall("a.*c", "abbccddc")  #takes the last c => abbccddc

#findall function return all the occurences of the subsrings where as match returns a MATCH object of only the first and 
# inclusive match and leaves the rest.

match_results = re.search("ab*c", "ABC", re.IGNORECASE)#this returns the index of the content
match_results.group()#this returns the content
print(match_results.group())

#Python’s regular expressions are greedy
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)






