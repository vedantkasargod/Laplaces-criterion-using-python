def laplaces(matrix):
    a=[]           #Initialized an empty list
    for row in matrix:
        averages=sum(row)/len(row)
        a.append(averages)
    return a

matrix_table = [
    [3, 5, 2],
    [1, 8, 4],
    [6, 3, 7]
]
answer=laplaces(matrix_table)
print(answer)