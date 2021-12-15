#https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def is_leap(year):
    if year % 4 ==0:
        if year % 100 == 0 and year % 400 !=0:
            return False
        return True
    return False

year = int(input())
print(is_leap(year))