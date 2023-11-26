# Define the functions
def query_sum(arr, L, R):
    return sum(arr[i] for i in range(L + 1) if arr[i] > arr[R])

def process_queries(arr, queries):
    result = []
    for L, R in queries:
        result.append(query_sum(arr, L, R))
    return result

# First test case
A1 = [6, 7, 2, 5]
queries1 = [(2, 2), (3, 1)]
result1 = process_queries(A1, queries1)
print(result1)  # Output: [13, 0]

# Second test case
A2 = [1, 2, 3, 4]
queries2 = [(3, 1), (2, 0)]
result2 = process_queries(A2, queries2)
print(result2)  # Output: [7, 5]
