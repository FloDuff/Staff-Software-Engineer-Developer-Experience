# Staff Software Engineer - Package Sorter

## Overview
A Python package sorting function for Smarter Technology's robotic automation line. Dispatches packages to specific stacks (STANDARD, SPECIAL, REJECTED) based on physical dimensions and mass.

## Project Structure
- `main.py` - Core sorting logic with `sort()` function and `ResultStack` enum
- `test.py` - Unit tests (6 tests, all passing)
- `README.md` - Logic documentation

## Sorting Logic
- **STANDARD**: Package is neither bulky nor heavy
- **SPECIAL**: Package is either bulky or heavy (but not both)
- **REJECTED**: Package is both bulky and heavy

### Definitions
- **Bulky**: Volume >= 1,000,000 cm³ OR any single dimension >= 150 cm
- **Heavy**: Mass >= 20 kg

## Running Tests
```bash
python3 test.py -v
```

## Workflow
- **Start application**: Runs `python3 test.py -v` (console output)

## Language & Runtime
- Python 3.12 (via NixOS stable-25_05)
- No external dependencies required
