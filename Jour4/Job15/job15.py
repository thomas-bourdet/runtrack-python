def round_number(n):
    if n - int(n) < 0.5:
        return int(n)
    else:
        return int(n) + 1

def sort_list(lst):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            j += 1
        i += 1
    return lst

numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
rounded = []
i = 0
while i < len(numbers):
    rounded.append(round_number(numbers[i]))
    i += 1

sorted = sort_list(rounded)

print(sorted)