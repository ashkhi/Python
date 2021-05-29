import random

mat1XDim = abs(int(input("Please enter matrix1 # rows : ")))
mat1YDim = abs(int(input("Please enter matrix1 # colmns : ")))

mat2XDim = abs(int(input("Please enter matrix2 # rows : ")))
mat2YDim = abs(int(input("Please enter matrix2 # colmns : ")))

if(mat1XDim != mat2XDim or mat1YDim != mat2YDim):
    print("The addition can not be performed, dim mismatch")
else:
    mat1 = []
    mat2 = []

    for i in range(mat1XDim):
        r1 = []
        r2 = []
        
        for j in range(mat1YDim):
            r1.append(random.randint(1, 10))
            r2.append(random.randint(1, 10))
        
        mat1.append(r1)
        mat2.append(r2)

    print("Given matrices : ")
    for i in range(mat1XDim):
        print(mat1[i], end="\t\t")
        print(mat2[i])

    res = []
    print("Addition : ")
    for i in range(mat1XDim):
        r = []
        
        for j in range(mat1YDim):
            r.append(mat1[i][j] + mat2[i][j])

        res.append(r)

    for i in range(mat1XDim):
        print(res[i])