import matplotlib.pyplot as plt 
x = list(range(0,10)) 
y = list(range(-10,0)) 
# plt.plot(x,y) 
# plt.show() 

a = [0,-34,-4,3,8,9] 
b = [5,3,2,5,4,3] 
plt.plot(a,b)  
#First two set min-max X axis and next two set min-max Y axis
plt.axis([-15,15,-20,20])   
#Setting increments at bottom and top 
#plt.xtics(#tuple of all current ticks(),#tuple of new change())
#Labeling 
plt.title("First Plot") 
plt.xlabel("Array A") 
plt.ylabel("Array B")
plt.show()