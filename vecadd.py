
print("this is a little differnt from the main one ")

vec1=[1,2,3,4]
vec2=[5,6,7,8]

for i in range (0,len(vec1)):
	output=output+vec1[i]*vec2[i]
	
print(output)




#to show parallelism
import numpy as np

vec1=np.array([1,2,3,4])
vec2=np.array([5,6,7,8])

vec3=np.dot(vec1,vec2)

print(vec3)

#adding this new line to test that modifying it does not modify the parallel one .
print("After modifying\n")
