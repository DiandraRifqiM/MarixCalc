import numpy as np



def crtMatrix(prompt="Enter matrix"):
    loopVal = True
    Data = []
    print("Create a matrix!\n")
    while loopVal:
        try:
            cols = int(input("Input number of coloumns: "))
            rows = int(input("Input number for rows: "))
        except ValueError:
            print("Please enter valid input!")
            return
        
        totalElm = rows*cols
        usrNum = (input(f"Enter {totalElm} number to create matrix: "))
        
        try:
            values = list(map(int, usrNum.split()))
            if len(values) != totalElm:
                print(f"You must input {totalElm} numbers!")
                return
        except ValueError:
            print("Please enter valid input!")
            return
        
        usrMatrix = np.array(values).reshape([rows, cols])
        return usrMatrix

def print_matrix(matrix, label="Result"):
    print(f"\n{label}:")
    print(matrix)

def matAdd():
    A = crtMatrix("Matrix A")
    B = crtMatrix("Matrix B")
    if A.shape != B.shape:
        print("Matrix must have the same shape!")
        return
    print_matrix(A + B)

def matSub():
    A = crtMatrix("Matrix A")
    B = crtMatrix("Matrix B")
    if A.shape != B.shape:
        print("Matrix must have the same shape!")
        return
    print_matrix(A - B)

def matMult():
    A = crtMatrix("Matrix A")         
    B = crtMatrix("Matrix B")         
    if A.shape[1] != B.shape[0]:
        print("Matrix A's columns must match Matrix B's rows")
        return
    print_matrix(A.dot(B))

def matDet():
    A = crtMatrix("Matrix A")
    if A.shape[0] != A.shape[1]:
        print("Matrix must be square to compute!")
        return 
    print_matrix(np.round(np.linalg.det(A)))

def matInv():
    A = crtMatrix("Matrix A")
    if A.shape[0] != A.shape[1]:
        print("Marix must be square to inverted!")
        return
    try:
        print_matrix(np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("Error: Matrix is singular and cannot be inverted.")

def matTrans():
    A = crtMatrix("Matrix A")
    print_matrix(np.transpose(A))
    
def main():
    
    loopVal = True
    while loopVal:
        print("Matrix Calculator\n")        
        print("\n Choose Method \n1. Addition \n2. Substraction \n3. Multiplication \n4. Determinand Matrix \n5. Inverse Matrix \n6. Transpose Matrix \n")
        
        try:
            mode = int(input("Choose method by number: "))
        except ValueError:
            print("Choose by their number not name!")
            continue
        
        match mode:
            case 1 :
                matAdd()
                break
            case 2:
                matSub()
                break
            case 3:
                matMult()
                break
            case 4:
                matDet()
                break
            case 5:
                matInv()
                break
            case 6:
                matTrans()
                break
            case default:
                print("\nChoose number available!")
                continue
            
        
        isDone = input("Are you done (y/n)? ")
        if isDone.lower() == "y":
            loopVal = False
            
            
        
if __name__ == "__main__":
    main()
    
    
    