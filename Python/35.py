# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import  permutations

arr, r = input().split()
for i in sorted(permutations(arr, int(r))):
    print(*i, sep="")