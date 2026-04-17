class Matrix:
    
    def __init__(self, rows, cols):
        #Create a matrix with given rows and cols, filled with 0.
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]
    
    def set(self, i, j, value):
        #Set value at row i, column j.
        self.data[i][j] = value
    
    def get(self, i, j):
        #Get value at row i, column j.
        return self.data[i][j]
    
    def add(self, other):
        #Add two matrices of same size.
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result
    
    def multiply(self, other):
        #Multiply two matrices.
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                result.data[i][j] = total
        return result
    
    def display(self):
        for row in self.data:
            print(row)

if __name__ == "__main__":
    print("Matrix Demo:")
    A = Matrix(2, 3)
    A.set(0, 0, 1); A.set(0, 1, 2); A.set(0, 2, 3)
    A.set(1, 0, 4); A.set(1, 1, 5); A.set(1, 2, 6)
    print("Matrix A:")
    A.display()
    
    B = Matrix(3, 2)
    B.set(0, 0, 7); B.set(0, 1, 8)
    B.set(1, 0, 9); B.set(1, 1, 10)
    B.set(2, 0, 11); B.set(2, 1, 12)
    print("Matrix B:")
    B.display()
    
    C = A.multiply(B)
    print("A * B:")
    C.display()