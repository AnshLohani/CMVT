import random
import matplotlib.pyplot as plt 


####
# n ---> no. of pens 
# x ---> no. of times to run 
####

def random_num():
    a = random.randrange(-1,2,2)
    return a



def plot_CMVT(n,x):

    templist = list()


    tempdict = dict()
#    for l in range(-x,x+1):
#        tempdict[l] = 0


    for j in range(x):
        z=0
        for i in range(n):
            x = random_num()
            z=z+x
        templist.append(z)

    templist.sort()


    for i in templist:
        tempdict[i] = templist.count(i)
        
    
    xaxis = list()
    xaxis = tempdict.keys()

    yaxis = list()
    yaxis = tempdict.values()
    bin=1
    plt.bar(xaxis,yaxis,bin)
    plt.xlabel('X - Axis')
    plt.ylabel('Y - Axis')


n= int(input("Enter the number of pens: "))
x= int(input("Enter the number of times the ball is thrown: "))
plot_CMVT(n,x)
