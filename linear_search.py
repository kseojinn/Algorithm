def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1

# Input data.
data = []
target = 
result = linear_search(data, target)
print(result)