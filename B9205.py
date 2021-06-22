from collections import deque

T=int(input())

for t in range(T):
    N=int(input()) #편의점의 개수
    field=[[0 for _ in range(N)] for _ in range(N)]
    x1, y1=map(int, input().split())
    x2, y2=map(int, input().split())
