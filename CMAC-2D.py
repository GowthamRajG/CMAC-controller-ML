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
test=train+0.001

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
s=np.zeros(6282)
#training the data
count=np.zeros(3140)
while error_threshold>-0.0001:

        for i in range (1,len(train)):
        
            # for i,j in enumerate(x_values):
        
        
        
               if i<len(train):
        
              #      if j==train[i]:
                        m=2*i
                        n=2*i+1
                        o=2*i+2
                        before = weight_vector[(m)]*0.8
                        current = weight_vector[n]
                        after = weight_vector[o]*0.2
                        
                        y_yield=before+current+after
                        print ('y_yield=',y_yield)
                    
            #for i in y:
                        y_error=y[m]-y_yield
                        print ('y_value[',i,']=',y[i])
                        y_error_corrected=(y_error/3)
                        print ('y_error_corrected=',y_error_corrected)
                        weight_vector[m]=(y_error_corrected)+(weight_vector[m])
                        weight_vector[n]=y_error_corrected+(weight_vector[n])
                        weight_vector[o]=(y_error_corrected)+(weight_vector[o])
                        print (weight_vector)
                        count[i]=i+1
                        s[i]=y_error
                        # plt.plot(s[i], weight_vector[i])                
                        plt.plot(count[i],s[i])  
                        plt.autoscale(enable=True, axis='both', tight=None)
        plt.show()				
        error_threshold=y_error	

        print (error_threshold)

print (weight_vector)
	
# testing the data

#for k in range (1,len(test)):

#    y_output=weight_vector[2*k]
#print (y_output)
print(len(weight_vector))
# weight_vector=np.delete(weight_vector,0)
# weight_vector=np.delete(weight_vector,6280)		
print(len(weight_vector))
print(len(x))
y_output=np.zeros(3140)
test_error1=np.zeros(3140)
test_error2=np.zeros(6282)
for k in range (1,len(test)):

    y_output[k]=weight_vector[2*k]
    test_error1[k]=test[k]-y_output[k]
    test_error2[2*k]=test[k]-y_output[k]

print (len(y_output))
	
plt.plot(test, y_output)
	
plt.show()
# plt.plot(test_error1, y_output)
# plt.show()
# plt.plot(test_error2, weight_vector)
# plt.show()
	
