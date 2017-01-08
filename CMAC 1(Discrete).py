#plotting a curve

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Plotting

x = np.arange(0, 6.28, 0.001)
y = np.sin(x)
#plt.plot(x, y)
#plt.show()
#y_values=np.loadtxt('yvalues.txt')
#x_values=[1,2,3,4,5]

print (x)
print (y)
	
#Splitting the data points

train = np.arange(0,6.28,0.002)
#train=x
#test = np.arange(2,5,2)
test=x

#print (train)
#print (test)
wv=[0]
weight_vector=x*0
print (weight_vector)
weight_vector=np.append([0],weight_vector)
weight_vector=np.append(weight_vector,[0])
#weight_vector=weight_vector.append(0)


# weight_vector=np.lib.pad(weight_vector, (1,1), 'constant', constant_values=(0, 0))

#weight vector(w) = 3

before=current=after=None
l = len(weight_vector)

error_threshold = 0.2

#training the data
count=100
while count>0:

        for i in range (1,len(train)):
        
            # for i,j in enumerate(x_values):
        
        
        
               if i<len(train):
        
              #      if j==train[i]:
                        m=2*i
                        n=2*i+1
                        o=2*i+2
                        before = weight_vector[(m)]
                        current = weight_vector[n]
                        after = weight_vector[o]
                        
                        y_yield=before+current+after
                        print ('y_yield=',y_yield)
                    
            #for i in y:
                        y_error=y_values[m]-y_yield
                        print ('y_value[',i,']=',y_values[i])
                        y_error_corrected=(y_error/3)
                        print ('y_error_corrected=',y_error_corrected)
                        weight_vector[m]=y_error_corrected
                        weight_vector[n]=y_error_corrected
                        weight_vector[o]=y_error_corrected
                        print (weight_vector)
                        count=count-1
error_threshold=y_error	

print (weight_vector)
	
# testing the data

for k in range (1,len(test)):

    y_output=weight_vector[2*k]
    print (y_output)
	
    plt.plot(test[k], y_output)
	
plt.show()
	
