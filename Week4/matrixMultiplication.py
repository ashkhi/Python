import random

mat1XDim = abs(int(input("Please enter matrix1 # rows : ")))
mat1YDim = abs(int(input("Please enter matrix1 # colmns : ")))

mat2XDim = abs(int(input("Please enter matrix2 # rows : ")))
mat2YDim = abs(int(input("Please enter matrix2 # colmns : ")))

if(mat1YDim != mat2XDim):
    print("The multiplication can not be performed, dim mismatch")
else:
    mat1 = []
    mat2 = []

    for i in range(mat1XDim):
        r1 = []
                
        for j in range(mat1YDim):
            r1.append(random.randint(1, 10))
                    
        mat1.append(r1)

    for i in range(mat2XDim):
        r2 = []
        
        for j in range(mat2YDim):
            r2.append(random.randint(1, 10))
        
        mat2.append(r2)

    print("\nGiven matrix 1 : ")
    for i in range(mat1XDim):
        print(mat1[i])

    print("\nGiven matrix 2 : ")
    for i in range(mat2XDim):
        print(mat2[i])

    res = []
    print("\nMultiplication : ")

    vect1 = []
    vect2 = []

    for i in range(mat1XDim):
        r = []
        vect1 = mat1[i]

        for j in range(mat2YDim):
            dotProduct = 0

            vect2 = []
            for k in range(mat2XDim):
                vect2.append(mat2[k][j])
            
            for l in range(len(vect1)):
                dotProduct += (vect1[l] * vect2[l])
            
            r.append(dotProduct)
        
        res.append(r)

    for i in range(mat1XDim):
        print(res[i])