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

#Practical Examples: Deriving Patterns from Data 

#Lets create a large dataset with a mean of 50 and standard deviation of 15 
data = np.random.normal(50,15, size = (5,10))  
mean = np.mean(data) 
sd = np.std(data) 
min = np.min(data)
max = np.max(data) 

print(f"Mean: {mean}\nStandard Deviation: {sd}\nMin Val: {min}\nMax Val: {max}") 

#Patterns: Identifying samples within one standard deviation of the mean 
test = np.sum((data>(mean-sd))&(data<(mean+sd))) 
percentage_within_one_std = (test / len(data))

print(f"Percentage of samples within one standard deviation from the mean: {percentage_within_one_std}%") 

#Summary 

#NumPy arrays are efficient for numerical operations 
#Vectorization allows us to perform operations on the entire array without explicit loops
#Linear algebra operations (matrix multiplication, transposition, and inversion) are supported with NumPy 
# and help to identify patterns within data which is useful for ML  
#Random sampling for generating datasets and simulations


