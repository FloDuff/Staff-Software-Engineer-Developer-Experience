from enum import Enum

class ResultStack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def sort(width, height, length, mass):
    """
    Categorizes a package for Smarter Technology's robotic arm.
    
    Returns a ResultStack Enum member instead of a string for type safety.
    """
    
    # Check for bulkiness (Volume >= 1,000,000 or any side >= 150cm)
    volume = width * height * length
    is_bulky = volume >= 1000000 or any(dim >= 150 for dim in [width, height, length])
    
    # Check for weight (Mass >= 20kg)
    is_heavy = mass >= 20
    
    # 1. Both criteria met -> REJECTED
    if is_bulky and is_heavy:
        return ResultStack.REJECTED
    
    # 2. Only one criterion met -> SPECIAL
    if is_bulky or is_heavy:
        return ResultStack.SPECIAL
    
    # 3. Neither met -> STANDARD
    return ResultStack.STANDARD

# --- Demonstration of usage ---
if __name__ == "__main__":
    package_type = sort(200, 200, 200, 50)
    
    # The safety benefit: you compare against the Enum, not a string
    if package_type == ResultStack.REJECTED:
        print(f"Action: Alerting floor supervisor. Status: {package_type.value}")
    
    # Quick Test Suite
    assert sort(10, 10, 10, 5) == ResultStack.STANDARD
    assert sort(150, 10, 10, 5) == ResultStack.SPECIAL
    assert sort(10, 10, 10, 25) == ResultStack.SPECIAL
    assert sort(200, 200, 200, 50) == ResultStack.REJECTED
    
    print("All logic tests passed successfully.")
