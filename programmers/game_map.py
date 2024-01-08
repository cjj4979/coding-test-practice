from collections import deque
def solution(maps):
    answer = -1
    q = deque()
    q.append((0, 0, 1))
    visited = set()
    
    while q:
        c = q.popleft()
        if (c[0], c[1]) in visited or maps[c[0]][c[1]] == 0:
            continue
        visited.add((c[0], c[1]))
        if c[0] == len(maps)-1 and c[1] == len(maps[0])-1:
            answer = c[2]
            break
        if c[0] > 0:
            q.append((c[0]-1, c[1], c[2]+1))
        if c[1] > 0:
            q.append((c[0], c[1]-1, c[2]+1))
        if c[0] < len(maps)-1:
            q.append((c[0]+1, c[1], c[2]+1))
        if c[1] < len(maps[0])-1:
            q.append((c[0], c[1]+1, c[2]+1))
    return answer