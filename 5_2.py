a = int(input())
b = int(input())
c = int(input())

if a <= b and a <= c:
    minv = a
elif b <= a and b <= c:
    minv = b
else:
    minv = c

print(minv)