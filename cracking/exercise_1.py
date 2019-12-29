# 1.1
def isUnique(str):
    checker = []
    for i in range(256):
        checker.append(False)

    for i in range(len(str)):
        j = ord(str[i])
        if checker[j] == True:
            return False
        checker[j] = True

    return True

print("test", isUnique("test"))
print("abcd", isUnique("abcd"))

def isUniqueBit(str):
    checker = 0
    for i in range(len(str)):
        j = ord(str[i])
        if checker & (1<<j):
            return False
        checker |= 1 << j

    return True

print("bit test", isUniqueBit("test"))
print("bit abcd", isUniqueBit("abcd"))

# 1.2
def reverse(str):
    str = list(str)
    start = 0
    end = len(str)-1
    while start < end:
        tmp = str[end]
        str[end] = str[start]
        str[start] = tmp
        start = start + 1
        end = end - 1
    return ''.join(str)

print("bittest", reverse("bittest"))
print("bitabcd", reverse("bitabcd"))

# 1.3
def permutation(s, t):
    s = sorted(list(s))
    t = sorted(list(t))
    if s == t:
        return True
    else:
        return False
print("bittest, bittest: ", permutation("bittest", "bittest"))
print("bittest, bittess: ", permutation("bittest", "bittess"))

def permutation2(s, t):
    if len(s) != len(t):
        return False

    checker = []
    for i in range(256):
        checker.append(0)

    for i in range(len(s)):
        j = ord(s[i])
        checker[j] += 1
    for i in range(len(t)):
        j = ord(t[i])
        checker[j] -= 1
        if checker[j] < 0:
            return False

    return True
print("god, dog: ", permutation2("god", "dog"))
print("god, dogg: ", permutation2("god", "dogg"))

# 1.5
def compressBad(s):
    rst = ""
    last = s[0]
    count = 1
    for i in range(1, len(s)):
        if last == s[i]:
            count += 1
        else:
            rst += last + str(count) + ""
            last = s[i]
            count = 1
    rst += last + str(count) + ""
    return rst

print("aabccccaa:", compressBad("aabccccaa"))

# 1.7
def setZeros(matrix):
    m = len(matrix)
    n = len(matrix[0])

    rows = cols = []
    for i in range(m): rows.append(0)
    for j in range(n): cols.append(0)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = 1
                cols[j] = 1

    for i in range(m):
        for j in range(n):
            if rows[i] == 1:
                matrix[i][j] = 0
            if cols[j] == 1:
                matrix[i][j] = 0

    return matrix

matrix = [
    [1,1,1,1],
    [1,0,1,1],
    [1,1,1,1],
]
print(setZeros(matrix))

# 1.8
def isRotation(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return -1
    s1 = s1 + s1
    return s1.find(s2)
s1 = "waterbottle"
s2 = "erbottlewat"
print("find: ", isRotation(s1, s2))
