import math


a=int(input('enter a : '))
b=int(input('enter b : '))
c=int(input('enter c : '))
root1=(-b+ math.sqrt(b**2-4*a*c))/(2*a)
root2=(-b- math.sqrt(b**2-4*a*c))/(2*a)
print('root are:',root1,root2)
# ok i done it
# with this snippet:        
a=int(input('enter a number: '))
if a>0:
    print('positive')
else:
    print('negative')
# What is the difference between the two snippets?
a=15
b=25
c=1
root1=(-b+ math.sqrt(b**2-4*a*c))/(2*a)
root2=(-b- math.sqrt(b**2-4*a*c))/(2*a)
print('root are:',root1,root2)
# ok i done it
# with this snippet:

# A. The first snippet calculates the roots of a quadratic equation, while the second snippet checks if a number is positive or negative.git