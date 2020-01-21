def backtrack(ans, s, arr, pos, N):
    letter_map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    if len(s) == N:
        ans.append(s)
        return
    
    letter_arr = letter_map[arr[pos]]
    for i in range(len(letter_arr)):
        backtrack(ans, s+letter_arr[i], arr, pos+1, N)

def letterCombinations(digits: str) -> [str]:
    ans = []
    N = len(digits)
    arr = list(digits)
    backtrack(ans, "", arr, 0, N)
    return ans

print(letterCombinations("234"))
