# Inline variable
Sometimes a variable is not so expressive like its value, so the
its usage can be replaced with its assignment.
This operation simplify additional refactoring techniques.

**example**
```python
base_price = anOrder.basePrice
return (base_price > 1000)
```

```python
return (anOrder.basePrice > 1000)
```


## How to inline variable
 * Check out if the right assign member has side effects
 * Check out if the assignment is unique
   * if is not unique than is possible to substitute each
   variable reference until another value is provided.
   And repeat this process for the new value.
 * Substitute each variable reference using a test each time
 * Delete the variable