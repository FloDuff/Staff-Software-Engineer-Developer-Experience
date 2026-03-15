from enum import Enum
import time

class ResultStack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def sort(width, height, length, mass):
    """
    Determines the dispatch stack for a package based on dimensions and mass.
    """
    volume = width * height * length
    is_bulky = volume >= 1000000 or any(dim >= 150 for dim in [width, height, length])
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return ResultStack.REJECTED
    
    if is_bulky or is_heavy:
        return ResultStack.SPECIAL
    
    return ResultStack.STANDARD

if __name__ == "__main__":
    # Internal validation output for the reviewer
    test_cases = [
        (10, 10, 10, 5),      # STANDARD
        (200, 200, 200, 50),  # REJECTED
        (150, 10, 10, 5),     # SPECIAL
    ]
    
    print("--- Smarter Technology Robotic Arm Online ---")
    for w, h, l, m in test_cases:
        print(f"Input: {w}x{h}x{l}, {m}kg -> Result: {sort(w, h, l, m).value}")
    
    print("\nLogic is active. System standing by...")
    
    # This loop prevents Replit Deployments from "crashing" 
    # because it keeps the program running.
    while True:
        time.sleep(3600)
