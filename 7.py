#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

from itertools import product

inp = input().split()
k, m, li = int(inp[0]), int(inp[1]), []

li = (list(map(int, input().split()))[1:] for _ in range(k))
results = map(lambda x: sum(i**2 for i in x)%m, product(*li))
    
print(max(results))
