#Take input
n = int(input("Enter the number of rows:"))
print(" mirrored half Pyramid pattern of stars(*)")
#outer loop to handle number of rows
for i in range(n):
#inner loop to handle number of columns
    for j in range(i+1):
        print("*",end="")