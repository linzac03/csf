# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
import hw2_test

print "Problem 1 solution follows:"

x = 0
y = 0
while (y <= hw2_test.n):
    x = x + y
    y = y + 1
print x 

# ... write your code and comments here (and remove this line)


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"


for x in range(2,11): ##Use 11 to include 10
    print (1.0 / x)
      





###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(0,n+1):
    triangular = triangular + i 
#v
print "Triangular number", n, "via loop:",triangular
print "Triangular number", n, "via formula:", (n * (n + 1) / 2)        
#v --> had triangular = triangular + n while n was not included in the scope of i

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
fact = 1
k = 1*2*3*4*5*6*7*8*9*10
for i in range(1,n+1): ##oh
    fact = i * fact
print "The product of all the integers up to %s via loop: %s and via multiplication: %s." % (str(n), str(fact), str(k))
 


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"
#for n in range(0,numlines+1):
#    for i in range(0,numlines+1):
#        i = fac * n 
#    n = numlines - n
#    print i
#    print n
    

numlines = 10
fact = 1   
p = numlines
for n in range(1,numlines):
    fact = fact * (n + 1)
print fact   
for i in range(1,numlines+1):
    fact = fact / (i + 1)
    print fact
##HELP <('^'>)
    #print i
    #print n


###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"
p = 0
y = 10
for n in range (1,y-1):
    x = 1.0 / n
    p = p + x
print "e = "+str(p)

##i don't know what i did or why i changed the ranged to (1,y-1)

###
### Collaboration
###

# lessea24, kevin, hannah

###
### Reflection
###
#https://wiki.python.org/moin/ForLoop
#http://stackoverflow.com/questions/17157275/walking-through-nested-for-statements
#http://codeacademy.com (Python, Strings & Console Output)
#http://www.greenteapress.com/thinkpython/thinkpython.pdf
#ICPUP, 3.2
#
#This assignment was hard, I'm not sure how long this took.
#I worked on it in lab and all this morning.
#I don't know if it was the concussion I had or if I've just been slacking.
#After reading chapters 7 and 10 I felt I was capable enough for most everything,
#except problems 5 and 6. Nesting the for loops is something that I can't figure
#out on my own, I guess I just don't understand exactly how an inner for statements behaves inside an outer for statement.
#

