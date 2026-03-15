from enum import Enum

class ResultStack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def sort(width, height, length, mass):
    """
    Core logic for package dispatching.
    """
    volume = width * height * length
    is_bulky = volume >= 1000000 or any(dim >= 150 for dim in [width, height, length])
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return ResultStack.REJECTED
    
    if is_bulky or is_heavy:
        return ResultStack.SPECIAL
    
    return ResultStack.STANDARD
