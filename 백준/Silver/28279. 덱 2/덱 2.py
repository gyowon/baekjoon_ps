import sys
from collections import deque
N=int(sys.stdin.readline())
dq=deque([])
for i in range(N):
    ins=list(map(int,sys.stdin.readline().split()))
    if ins[0]==1:
        dq.appendleft(ins[1])
    elif ins[0]==2:
        dq.append(ins[1])
    elif ins[0]==3:
        if len(dq)>0:
            print(dq.popleft())
        else:
            print(-1)
    elif ins[0]==4:
        if len(dq)>0:
            print(dq.pop())
        else:
            print(-1)
    elif ins[0]==5:
        print(len(dq))
    elif ins[0]==6:
        if len(dq)>0:
            print(0)
        else:
            print(1)
    elif ins[0]==7:
        if len(dq)>0:
            print(dq[0])
        else:
            print(-1)
    elif ins[0]==8:
        if len(dq)>0:
            print(dq[-1])
        else:
            print(-1)