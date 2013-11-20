# Name: Zach Linton
# Evergreen Login: linzac03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###
a = 1
b = 2
c = 3

def multi(x,y,z):
    prod = x*y*z
    return prod
# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"
n = multi(a,b,c)
print n
# ... write your code and comments here (and remove this line)


###
### Problem 4
###
a = {"a":1}
b = {"b":2}
c = {"c":3}
ls = []

def append_func(a,x,y,z):
    a.append(x)
    a.append(y)
    a.append(z)
    return a

n = append_func(ls,a,b,c)

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"
print n
# ... write your code and comments here (and remove this line)


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"
for d in ls:
    print d
# ... write your code and comments here (and remove this line)

###
### Problem 6
###
ls = {"a" : 1, "b" : 2}
ls2 = {"d" : 4, "e" : 5}
combi = dict(ls.items() + ls2.items())
# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"
print combi
# ... write your code and comments here (and remove this line)

###
### Problem 7
###
a = [
    {"State" : "WA", "Bird" : "American Goldfinch", "Nickname" : "The Evergreen State"},
    {"State" : "OR", "Bird" : "Western Meadowlark", "Nickname" : "Beaver State"},
    {"State" : "CA", "Bird" : "California Quail", "Nickname" : "The Golden State"}
    ]

newdict = {}
for row in a:
    newdict[row["State"]] = row["Nickname"]

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"
print newdict
# ... write your code and comments here (and remove this line)

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
