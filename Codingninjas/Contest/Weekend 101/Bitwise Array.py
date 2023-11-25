def is_possible_array(n, x, y):
    for i in range(n):
        if (y >> i) & 1 and not ((x >> i) & 1):
            return False

    return True

# Take user input
t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())

    # Check if it's possible
    result = is_possible_array(n, x, y)
    print(1 if result == True else 0)