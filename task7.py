'''
For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal
to zero.
Try to use the cascade if-elif-else for it.
'''

def positive_negative_num(number):
    if number == 0:
        print(0)
    elif number > 0:
        print (1)
    else:
        print(-1)

positive_negative_num(5)