# Consolidate conditional expression 
Consist in changing a bunch of if conditions that call the same function or execute the same 
code with just one if condition.

![Schema](./image.png)
 

## How to Consolidate conditional expression
Merge conditions with logic operators in couple until there's only one, than check if is 
[Extract function]("../Extract function/") is applicable.

 **Example**
 ```python
def calculate_amount(employee: Employee):
    if employee.seniority < 2: return 0
    if employee.months_unavailable > 12: return 0
    if employee.is_part_time:
        if employee.work_hours > 8:
            return 0

    return 10
 ```
 
 * Merge first 2 conditions with an "or" operator
 ```python    
def calculate_amount(employee: Employee):
    if employee.seniority < 2 \
            or employee.months_unavailable > 12: return 0
    if employee.is_part_time:
        if employee.work_hours > 8:
            return 0

    return 10
 ```

 * Merge last 2 conditions with an "and" operator 
 ```python    
def calculate_amount(employee: Employee):
    if employee.seniority < 2 \
            or employee.months_unavailable > 12: return 0
    
    if employee.is_part_time \
            and employee.work_hours > 8: return 0

    return 10
 ```
 
 * Merge resulting conditions groups
 ```python    
def calculate_amount(employee: Employee):
    if employee.seniority < 2 \
            or employee.months_unavailable > 12 \
            or (employee.is_part_time
                and employee.work_hours > 8): return 0

    return 10
 ```
 
 * Extract function on condition
```python
def condition(employee):
    return employee.seniority < 2 \
           or employee.months_unavailable > 12 \
           or (employee.is_part_time
               and employee.work_hours > 8)


def calculate_amount(employee: Employee):
    if condition(employee):
        return 0

    return 10
```

 * Ternary operation
```python
def calculate_amount(employee: Employee):
    return 0 if condition(employee) else 10
```