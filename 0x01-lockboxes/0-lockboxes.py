def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)


return all(unlocked)


# Test cases
print(canUnlockAll([[1], [2], [3], []])) #  True 
print(canUnlockAll([[1, 3], [3, 0, 1], [2], [0]])) #  True
print(canUnlockAll([[1, 2, 3], [0], [4], []])) #  False
