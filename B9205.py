from collections import deque

T=int(input())

for t in range(T):
    answer=""
    N=int(input()) #편의점의 개수
    field=[[0 for _ in range(2)] for _ in range(N)]
    x1, y1=map(int, input().split())
    for n in range(N):
        field[i][0]=int(input())
        field[i][1]=int(input())
    x2, y2=map(int, input().split())

    visit=[[0 for _ in range(2)] for _ in range(N+2)]
    queue=deque()
    while queue:

    print(answer)