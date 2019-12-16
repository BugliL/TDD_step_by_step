# Decompose conditional

Used to simplify an if statement.  
It consists in applying [Extract function]("../Extract function/") to the if condition and to both if branches.

<!-- ![Schema](./image.png) -->

## How to Decompose conditional
* Apply Extract function on:
  - Condition
  - Then branch
  - Else branch

* Refactor remaining code

### Example
**Original code**
 ```python
def function_to_refactor(selected_date: dt, plan: Plan, qty):
    result = 0

    if plan.summer_start_date < selected_date < plan.summer_end_date:
        result = qty * plan.summer_rate
    else:
        result = qty * plan.regular_rate

    return result
 ```
 
 * Apply "Extract function" on condition
 ```python    
 def function_to_refactor(selected_date: dt, plan: Plan, qty):
    def is_summer():
        return plan.summer_start_date < selected_date < plan.summer_end_date

    result = 0

    if is_summer():
        result = qty * plan.summer_rate
    else:
        result = qty * plan.regular_rate

    return result
 ```

 * Apply "Extract function" on "then" branch
 ```python    
 def function_to_refactor(selected_date: dt, plan: Plan, qty):
    def is_summer():
        return plan.summer_start_date < selected_date < plan.summer_end_date

    def summer_charge():
        result = qty * plan.summer_rate
        return result

    result = 0

    if is_summer():
        result = summer_charge()
    else:
        result = qty * plan.regular_rate

    return result
 ```
 
 * Apply "Extract function" on "else" branch
 ```python    
 def function_to_refactor(selected_date: dt, plan: Plan, qty):
    def is_summer():
        return plan.summer_start_date < selected_date < plan.summer_end_date

    def summer_charge():
        result = qty * plan.summer_rate
        return result

    def regular_charge():
        result = qty * plan.regular_rate
        return result

    result = 0

    if is_summer():
        result = summer_charge()
    else:
        result = regular_charge()

    return result
 ```
 
## One line code 
Use ternary operator to simply core code
```python

def function_to_refactor(selected_date: dt, plan: Plan, qty):
    def is_summer():
        return plan.summer_start_date < selected_date < plan.summer_end_date

    def summer_charge():
        result = qty * plan.summer_rate
        return result

    def regular_charge():
        result = qty * plan.regular_rate
        return result

    return summer_charge() if is_summer() else regular_charge()
```