#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

cube = lambda x: x**3 

def fibonacci(n):
    li = [0,1]
    for i in range(2, n):
        li.append((li[i-2]+li[i-1]))
        
    return li[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))