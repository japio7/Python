import random

def randomMatrix(col, row, min, max):
    for j in range(row):
        line = ""
        for i in range(col):
            line += str(random.randint(min, max)) + "\t"
        print(line)
        
randomMatrix(5,10,1,50)
