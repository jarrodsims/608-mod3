# built-in-min-max-jarrodsims.py
"""Program that determines the maximum and minimum of three numbers"""

def maximum(value1, value2, value3):
    """Return the maximum of three values"""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print('Maximum value equal to', maximum(12,27,36))
print('Maximum value equal to', min(15,9,27))
print('Jarrod Sims')