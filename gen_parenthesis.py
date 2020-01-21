def backtrack(ans, s, left, right, N):
    if len(s) == 2*N:
        ans.append(s)
    if left < N:
        backtrack(ans, s+'(', left+1, right, N)
    if right < left:
        backtrack(ans, s+')', left, right+1, N)

    return ans
def generateParenthesis(N):
    ans = []
    backtrack(ans, '', 0, 0, N)
    return ans
    

ans = generateParenthesis(3)
print(ans)
