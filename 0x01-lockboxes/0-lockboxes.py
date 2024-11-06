#!/usr/bin/python3
"""
Function to determine if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """Determines if all boxes can be opened starting from the first box.
    
    Args:
        boxes (list of lists): Each box contains keys to other boxes.
        
    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    # Start with the first box unlocked
    unlocked = {0}
    # Stack of boxes to check (start with the first box)
    stack = [0]

    # Process boxes until there are no more keys to use
    while stack:
        current_box = stack.pop()  # Take the last box added to the stack
        
        for key in boxes[current_box]:
            # If the key unlocks a new box, mark it as unlocked and add it to the stack
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                stack.append(key)

    # All boxes are unlocked if we have `n` boxes in the `unlocked` set
    return len(unlocked) == len(boxes)

