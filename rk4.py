import math 
import matplotlib.pyplot as plt

#ordinary differential equation
diffeq = lambda x,y: -1/(x-5.51)**2
#analytical function
f = lambda x: 1/(x-5.51)

#Since there may be errors with allowing the user to input starting conditions and step sizes, 
#there will be a section of the code dedicated to using pure provided values for the RK4 algorithm.

xi = 0
xf = 10
h = 1
s = math.ceil((xf-xi)/h)
x = 0
y = 2
print(x)
print(math.e)
type(x)

x_plt = []
y_pred = []
y_an = []

for i in range(1,s+1):
  k1 = diffeq(x,y)
  k2 = diffeq(x + h/2, y + k1 * h/2)
  k3 = diffeq(x + h/2, y + k2 * h/2)
  k4 = diffeq(x + h, y + k3 *h)
  y += (1.0/6.0) * (k1 + 2*k2 + 2*k3 + k4) * h
  x_plt.append(x)
  y_pred.append(y) 
  y_an.append(f(x))
  x += h

print(x_plt)
print(y_pred)
f_lambda = f(x)
print(f_lambda)
plt.plot(x_plt,y_pred, 'bo', x_plt, y_an, 'r+')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(["Code", 'Analytic'])
