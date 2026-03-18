n = int(input())
x = input()

palin = []
final_palin = []
result = x[0]  # assume first character is the longest palindrome initially

for center in range(n):

    # =====================
    # ODD LENGTH PALINDROME
    # =====================
    palin = []
    final_palin = []
    palin.append(x[center])         # middle character
    median_left = center - 1        # one step left of center
    median_right = center + 1       # one step right of center

    while median_left >= 0 and median_right <= n - 1:
        if x[median_left] == x[median_right]:
            palin.append(x[median_left])
            palin.append(x[median_right])
            median_left -= 1
            median_right += 1
        else:
            break                   # stop expanding if mismatch

    # rebuild palindrome from palin list
    middle = palin[0]
    pairs = palin[1:]
    left = []
    right = []
    for i in range(0, len(pairs), 2):
        left.append(pairs[i])
        right.append(pairs[i+1])
    left.reverse()
    final_palin = left + [middle] + right
    candidate = "".join(final_palin)

    # update result if longer or lexicographically smaller
    if len(candidate) > len(result) or \
       (len(candidate) == len(result) and candidate < result):
        result = candidate

    # =====================
    # EVEN LENGTH PALINDROME
    # =====================
    palin = []
    final_palin = []
    median_left = center            # left center
    median_right = center + 1      # right center

    if median_right <= n - 1:      # make sure right is within bounds
        while median_left >= 0 and median_right <= n - 1:
            if x[median_left] == x[median_right]:
                palin.append(x[median_left])
                palin.append(x[median_right])
                median_left -= 1
                median_right += 1
            else:
                break              # stop expanding if mismatch

        # rebuild palindrome from palin list
        for k in range(len(palin)-1, 0, -2):
            final_palin.append(palin[k])
        for l in range(0, len(palin), 2):
            final_palin.append(palin[l])
        candidate = "".join(final_palin)

        # update result if longer or lexicographically smaller
        if len(candidate) > len(result) or \
           (len(candidate) == len(result) and candidate < result):
            result = candidate

print(len(result))
print(result)