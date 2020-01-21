def trap(height: [int]) -> int:
    i = j = 0
    length = len(height)
    sum_rain = 0
    rain = 0
    rain_stack = []
    while i < length-1:
        j += 1

        print("j:", j)
        if j == length:
            i += 1
            j = i
            rain = 0
            continue

        if height[i] <= height[j]:
            rain_stack.append(rain)
            print("statck:", i, j, height[i], height[j], rain)
            i = j
            rain = 0
        else:
            print("sum:", i, j, height[i], height[j], rain)
            rain += height[i] - height[j]
            print(rain)
    print(rain_stack)
    return sum(rain_stack)

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,3]))
