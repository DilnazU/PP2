a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a == c) or (b == d) or (a - c == b - d) or (a - c == -(b - d)):
    print("YES")
else:
    print("NO")