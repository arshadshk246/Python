def leaders(arr):
    lead = set()
    for i in range(len(arr) - 1):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                flag = j
            else:
                continue
        lead.add(arr[flag])
    return lead


arr = [13, 87, 45]
leaders(arr)
