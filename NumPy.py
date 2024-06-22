import numpy as np  
#ndarrays, or NumPy arrays are the central data structure  
#similar to Python lists except are more efficient due to fixed size/data type 

#1D 
array_1D = np.array([1,2,3,4,5])   

#2D 
array_2D = np.array([[True, False, True], [False,True,False]])  
 
#Arrays w/ specific functions
zero_2D = np.zeros((4,4),dtype=int)   
ones_1D = np.ones((4), dtype=str) 
identity = np.eye(3,dtype=int) 

A = np.array([[2,3,4,5],
              [4,3,4,5],
              [2,3,4,5]]) 
B = np.array([[5,4,3,2],
              [5,4,3,2],
              [5,4,3,2], 
              [5,4,3,2]]) 

C = np.array([[2,3,5],[4,5,1],[4,2,3]])

#Matrix operations  

#Multiplication
arrayD = np.dot(A,B)
print(arrayD)
 
#Transpose 
print(A.T)

#Determinant
print(np.linalg.det(C)) 

#Inverse 
print(np.linalg.inv(C)) 

#Random Sampling 

#Uniformly distributed between 0 and 1
random_arr = np.random.random((3,3))  

#Integers between 1,14 
random_int = np.random.randint(1, 15, size=(5, 3))

#Normal dist where Mean = 15, SD = 5
normal_sam = np.random.normal(15,5, size = (5,3)) 

#Permutation 
permuted = np.random.permutation(A)

print(permuted)