# Reverse a string without using a built-in reverse function.
name = "devnox solutions"
length = len(name)
result = ""
for i in range(length,0,-1):
    result += name[i-1]
print(result) 

