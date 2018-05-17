#(Largest rows and columns) Write a program that randomly fills in 0s and 1s into
#a matrix, prints the matrix, and finds the rows and columns with the most
#1s.
import random

item = []
column = 0
row = 0
count_row = 0
col = 0
count_col = 0
countr = 0
countl = 0

for i in range(0,4):
    item.append([])
    for j in range(0,4):
        item[i].append(random.randint(0,1))

print(item)
for i in range(0,4):
    for j in range(0,4):
        if item[i][j]==1:
            countr += 1
        if item[j][i]==1:
            countl += 1
    if countr>count_row:
        count_row = countr
        row = i
    if countl>count_col:
        count_l = count_col
        column = i
    countr = 0
    countl = 0

print("The largest row index: ",row+1)
print("The largest column index:",column+1)