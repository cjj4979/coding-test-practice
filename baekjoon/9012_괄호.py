import sys

num = int(sys.stdin.readline())
parens = [list(sys.stdin.readline().strip()) for _ in range(num)]
for i in range(num):
    stack = []
    for j in range(len(parens[i])):
        if parens[i][j] == ')':
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
        else:
            stack.append(parens[i][j])
        if j == len(parens[i]) - 1:
            if stack:
                print("NO")
            else:
                print("YES")

'''
(())
starts with ) -> invalid
) + ) -> invalid
( + ( -> append
( + ) -> pop


1.  if current = )
        if stack empty then no
        else pop
    else
        append current

'''