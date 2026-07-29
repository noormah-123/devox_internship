import numpy as np

# Create arrays
a = np.array([3, 1, 4, 1, 5])      # 1D array (a list of numbers)
b = np.arange(10)                 # [0, 1, 2, ..., 9]
c = np.arange(1, 13).reshape(3,4) # numbers 1..12 reshaped into 3 rows x 4 cols

print("a:", a)
print("b:", b)
print("c:\n", c)

# Indexing & slicing 
# 1D indexing
print("a[0] =", a[0])      # first element
print("a[-1] =", a[-1])    # last element
print("a[1:4] =", a[1:4])  # slice: elements at positions 1,2,3
print("a[::2] =", a[::2])  # every 2nd element

# 2D indexing uses [row, column]
print("c[0,0] =", c[0,0])      # top-left
print("c[2,3] =", c[2,3])      # bottom-right
print("first row:", c[0, :])   # row 0, all columns
print("last column:", c[:, -1])# all rows, last column
print("middle block:\n", c[1:3, 1:3])  # rows 1..2 and cols 1..2

# Boolean masks (select/replace)
mask = c % 2 == 0               # True where c is even
print("mask (even?):\n", mask)
print("even numbers in c:", c[mask])   # select only evens

c2 = c.copy()                   # important: makes a real copy
c2[c2 < 6] = 0                  # replace all values < 6 with 0
print("c with values < 6 set to 0:\n", c2)

# ---------- 4) Basic stats ----------
print("c sum:", c.sum())
print("c min/max:", c.min(), c.max())
print("c mean:", c.mean())

# axis=0 => per column, axis=1 => per row
print("column sums:", c.sum(axis=0))
print("row means:", c.mean(axis=1))