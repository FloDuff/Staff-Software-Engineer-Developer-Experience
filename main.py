from enum import Enum

class ResultStack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def sort(width, height, length, mass):
    """
    Evaluates package dimensions and mass to determine dispatch stack.
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
    print("--- Smarter Technology Dispatcher ---")
    # Quick visual check for the reviewer
    sample = sort(200, 200, 200, 50)
    print(f"Test Case [200x200x200, 50kg]: {sample.value}")
    print("Run 'python -m unittest discover tests' for full validation.")
