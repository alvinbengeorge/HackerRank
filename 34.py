# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A, B = map(int, input().split()), map(int, input().split())
print(*product(A, B))
