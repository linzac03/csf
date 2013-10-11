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
triangular = triangular + n#n was not included in the scope of i
print "Triangular number", n, "via loop:",triangular
print "Triangular number", n, "via formula:", (n * (n + 1) / 2)        

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
fact = 1
for i in range(1,n+1): ##oh
    fact = i * fact
print fact
print 1*2*3*4*5*6*7*8*9*10

# ... write your code and comments here (and remove this line)

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"


#for n in range(0,numlines+1):
 #   for i in range(0,numlines+1):
  #      #i = fac * n 
   # n = numlines - n
    #print i
    #print n
numlines = 10
fac = 1
for n in range(numlines):
    #n = numlines - n
           
    for i in range (numlines - n):
        fac = i * fac
    print fac ##HELP <('^'>)
    #print i
    #print n

# ... write your code and comments here (and remove this line)

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"
p = 0
for n in range (1,10):
    x = 1.0 / n
    #print x
    #for x in range (2):
        #if x <= 1:
    p = p + x
print p

# ... write your code and comments here (and remove this line)

###
### Collaboration
###

# lessea24, kevin

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
