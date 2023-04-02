def convertToInt(n: list, number: int = 0):return convertToInt(n[1:], number*10+n[0]) if n else number
for i in range(int(input())): print(convertToInt(list(range(1,i+2))+list(range(i,0,-1))))