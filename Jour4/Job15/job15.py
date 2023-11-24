numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
rounded = [0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while i < 9:
    if numbers[i] - (numbers[i] // 1) < 0.5:
        rounded[i] = numbers[i] // 1
    else:
        rounded[i] = numbers[i] // 1 + 1
    i += 1

sorted = [0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while i < 9:
    j = i + 1
    while j < 9:
        if rounded[i] > rounded[j]:
            temp = rounded[i]
            rounded[i] = rounded[j]
            rounded[j] = temp
        j += 1
    i += 1

print(rounded)