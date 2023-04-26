#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    keys = [0]  # keys already possessed
    i = 0       # index of the box being checked

    # check if all boxes can be unlocked
    while i < len(keys):
        for key in boxes[i]:
            if key not in keys and key < len(boxes):
                keys.append(key)
        i += 1

    return len(keys) == len(boxes)

