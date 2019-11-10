# Replace temp with query
Used when a variable is initialized than readed for the rest of the code.
The variable can be declared immutable. 

![Schema](./image.png)
 
Shortly: duplicate expression, 
More shortly: < Very Short version >

## How to replace with query
**example**
```python
base_price = qty * price
if base_price > 1000:
    return base_price * 0.95
else:
    return base_price * 0.98
```

 * Check that the function is deterministic
   ```python
   base_price = qty * price  # it is
   if base_price > 1000:
       return base_price * 0.95
   else:
       return base_price * 0.98
   ```
 
 * Extract the variable assignment in a function
   * If there are side effects separate query from modifier
   ```python
   def base_price_fn(qty:int, price:float):   
       return qty * price
   
   base_price = qty * price
   if base_price > 1000:
       return base_price * 0.95
   else:
       return base_price * 0.98
   ```
   
 * Replace variable expression with function call
   ```python
   def base_price_fn(qty:int, price:float):
       return qty * price
   
   base_price = base_price_fn(qty, price)
   if base_price > 1000:
       return base_price * 0.95
   else:
       return base_price * 0.98
   ```
 
 * Use inline variable to remove temporary variable
   ```python
   def base_price_fn(qty:int, price:float):
       return qty * price
   
   if base_price_fn(qty, price) > 1000:
       return base_price_fn(qty, price) * 0.95
   else:
       return base_price_fn(qty, price) * 0.98
   ```
