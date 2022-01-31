from fractions import Fraction

#ordinary differential equation in the form: dy/dx = x + 1/2y
diffeq = lambda x,y: (x-y)/2

#Table
table = dict()
table['c1']= []
table['c2']= [1/2,1/2]
table['c3']= [1/2,0,1/2]
table['c4']=[1,0,0,1]

def printTable(order):
    #Include code to print the table
    if order == 2:
        print('c1' + '|' + '""')
        print(str(table['c2'][0]) + '|' + str(table['c2'][1]))
    elif order == 3:
        print('c1' + '|' + '""')
        print(str(table['c2'][0]) + '|' + str(table['c2'][1]))
        print(str(table['c3'][0]) + '|' + str(table['c3'][1]) + ' '+ str(table['c3'][2]))
    else:
        print('c1' + '|' + '""')
        print(str(table['c2'][0]) + '|' + str(table['c2'][1]))
        print(str(table['c3'][0]) + '|' + str(table['c3'][1]) + ' '+ str(table['c3'][2]))
        print(str(table['c4'][0]) + '|' + str(table['c4'][1]) + ' '+ str(table['c4'][2])+ ' '+ str(table['c4'][3]))
        


def rk4(x0,y0,dx,x,order):

    s = int((x-x0)/dx)

    if order == 0 or order ==1 or order > 4:
        print ("The minimum order needs to be 2, 3 or 4")
    elif order == 2:
        #call the printtable with order argument
        printTable(order)
        for i in range(1,s+1):
            k1 = diffeq(x0,y0) * dx
            k2 = diffeq(x0 + table['c2'][0] * dx,y0 + k1 * table['c2'][1]) * dx
            x0+=dx
        y_new = y0 + (1.0/6.0) * (k1 + k2)
    elif order == 3:
        #call the printtable with order argument
        printTable(order)
        for i in range(1,s+1):
            k1 = diffeq(x0,y0) * dx
            k2 = diffeq(x0 + table['c2'][0] * dx,y0 + k1 * table['c2'][1]) * dx
            k3 = diffeq(x0 + table['c3'][0] * dx,y0 +(k1 * table['c3'][1])+ (k2 * table['c3'][2])) * dx
            x0+=dx
        y_new = y0 + (1.0/6.0) * (k1 + 2*k2 + k3)
    else:
        #call the printtable with order argument
        printTable(order)
        for i in range(1,s+1):
            k1 = diffeq(x0,y0) * dx
            k2 = diffeq(x0 + table['c2'][0] * dx,y0 + k1 * table['c2'][1]) * dx
            k3 = diffeq(x0 + table['c3'][0] * dx,y0 +(k1 * table['c3'][1])+ (k2 * table['c3'][2])) * dx
            k4 = diffeq(x0 + table['c4'][0] * dx,y0 + (k1 * table['c4'][1])+ (k2 * table['c4'][2]))  * dx
            x0+=dx
        y_new = y0 + (1.0/6.0) * (k1 + 2*k2 + 2*k3 + k4)
    return y_new


#user inputs
x0 = float(input("Please enter the starting point of x you would like to compute for:"))
y0 = float(input("Please enter the starting point of y you would like to compute for:"))
dt = float(input("Please enter the step-size, or Δx value you would like to use:"))
x = float(input("Please enter the final x value you would like to use the Runge-Kutta Method to approximate:"))
print("The value of the function at the x-value you gave is", rk4(x0,y0,dt,x))