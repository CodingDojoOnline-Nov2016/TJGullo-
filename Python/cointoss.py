'''You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.

Sample output should be like the following:

          Starting the program...

Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
........
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far

Ending the program, thank you!'''

#import random
#random_num = random.random()

#x = .23945593
#y = .798839238
#x_rounded = round(x)
# x_rounded will be rounded down to 0
#y_rounded = round(y)
# y_rounded will be rounded up to 1

import random


flips = 0
headcount = 0
tailcount = 0
while flips < 5001:
    random_num = random.randint(0,1)
    flips += 1
    if random_num == 0:
        headcount += 1
        print "Attempt #{}: Throwing a coin... It was heads! So far {} heads and {} tails!".format(flips, headcount, tailcount)
    else:
        tailcount += 1
        print "Attempt #{}: Throwing a coin... It was tails! So far {} heads and {} tails!".format(flips, headcount, tailcount)
