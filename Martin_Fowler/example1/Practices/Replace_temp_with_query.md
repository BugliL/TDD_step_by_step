# Replace temp with query
Used when a variable is initialized than read for the rest of the code

**example**
```python
base_price = qty * price
if base_price > 1000
    return base_price * 0.95
else:
    return base_price * 0.98
```

```python
def base_price()
    return qty * price

if base_price() > 1000
    return base_price() * 0.95
else:
    return base_price() * 0.98
```

## How to replace with query
 * Check that the function is deterministic
 * If possible declare that variable constant
 * Extract the variable assignment in a function
   * If there are side effects separate query from modifier
 * Use inline variable to remove temporary variable
