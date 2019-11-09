# Inline variable
Consist in replacing a variable with his expression.
It's used when a variable is not so expressive like its value, so the its usage can be replaced with its assignment.

Inverse of [Extract variable](../Extract%20variable)
Shortly: replace, delete
More shortly: Let ide do it for you

![Schema](./image.png)
 

## How to inline variable
on simplify additional refactoring techniques.

**example**
```python
    def get_base_price(anOrder: OrderObject):
        base_price = anOrder.basePrice
        return (base_price > 1000)
```

 * Check out if the right assign member has side effects and if is unique
   ```python
       def get_base_price(anOrder: OrderObject):
           # No side effects
           base_price = anOrder.basePrice
           return (base_price > 1000)
   ``` 
      
 * Substitute each variable reference using a test each time until is no more referenced
   ```python
       def get_base_price(anOrder: OrderObject):
           base_price = anOrder.basePrice
           return (anOrder.basePrice > 1000)
   ```
 
 * Remove the variable
   ```python
       def get_base_price(anOrder: OrderObject):           
           return (anOrder.basePrice > 1000)
   ``` 
