# Staff-Software-Engineer-Developer-Experience

This repository contains the package sorting function for Smarter Technology’s robotic automation line. The goal is to accurately dispatch packages to specific stacks based on their physical dimensions (volume) and mass.

## Logic Overview

The dispatcher evaluates every package against two primary criteria to determine its handling requirements:

1.  **Bulky**: A package is considered bulky if its volume is ≥ 1,000,000 cm³ OR if any single dimension (width, height, or length) is ≥ 150 cm.
2.  **Heavy**: A package is considered heavy if its mass is ≥ 20 kg.

### Dispatch Criteria

| Stack | Description |
| :--- | :--- |
| **STANDARD** | Packages that are neither bulky nor heavy. |
| **SPECIAL** | Packages that are either heavy or bulky (but not both). |
| **REJECTED** | Packages that are both heavy and bulky. |

---

## Technical Implementation

### Type Safety with Enums
To avoid "magic strings" and potential typos in downstream systems, this implementation utilizes Python's built-in `Enum` module. The `sort()` function returns a member of the `ResultStack` class, ensuring that the robotic arm's logic only ever operates on validated states.

### Project Structure
```text
├── main.py              # Logic and Enum definitions
│── tests/
│  |── test_sort.py     # Comprehensive unit tests
└── README.md            # Technical documentation
