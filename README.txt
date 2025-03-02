# Number to Text Malay
This project provides a utility class `nombor_melayu` to convert numeric values into Malay text representation with currency denomination (Ringgit Malaysia).

## Features
- Converts integer and floating numbers into Malay text.
- Supports currency format with sen representation.
- Handles numbers up to trillion.

## Usage
```python
from nombor_melayu import nombor_melayu

value = 1234.56
text = nombor_melayu.number_to_text(value)
print(text)
