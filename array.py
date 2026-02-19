arr = list()
n = int(input("Size: "))
if n < 0:
    print("Error: negative size")
print("Enter elements:")
i = 0
while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1
print("Array:")
i = 0
while (i < n):
    print(arr[i], end = " ")
    i += 1
print("")
