#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import math

ab = int(input())
bc = int(input())

print(str(round(math.degrees(math.atan(ab/bc))))+chr(176))