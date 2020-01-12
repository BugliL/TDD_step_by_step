# Replace nested conditional with guard clause
A *guard clause* is an if that returns directly a value breaking function execution.  
This pattern consist in replacing each if/else condition with a *guard clause*.  
This pattern is made to make code clearer on each case.
It's used when there's a variable returned or used only after the if structure.

## How to Replace nested conditional with guard clause
- Take the most external if clause and chang it in a guard clause.
  - If nested IF are present, change them in 2 different if statements, 
  one with the positive condition, the other one with negated condition.  
  Than to extract both if statements with their parent condition in it 
- Repeat until no more if conditions are present

If possible use [Consolidate conditional expression](../Consolidate%20conditional%20expression)

 **Example**
 ```python
 def pay_amount(employee: Employee):
    if employee.is_separated:
        result = {'amount': 0, 'reason_code': "SEP"}
    else:
        if employee.is_retired:
            if employee.age < 60:
                result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
            else:
                result = {'amount': 0, 'reason_code': "RET"}
        else:
            result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}

    return result
 ```
 
 * Change most external clause in a guard clause
 ```python    
def pay_amount(employee: Employee):
    if employee.is_separated:
        return {'amount': 0, 'reason_code': "SEP"}

    if employee.is_retired:
        if employee.age < 60:
            result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
        else:
            result = {'amount': 0, 'reason_code': "RET"}
    else:
        result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}

    return result


 ```

 * Again
 ```python    
def pay_amount(employee: Employee):
    if employee.is_separated:
        return {'amount': 0, 'reason_code': "SEP"}

    result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
    if employee.is_retired:
        if employee.age < 60:
            result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
        else:
            result = {'amount': 0, 'reason_code': "RET"}

    return result
 ```
 
  * Half step of nested if, making else and then statements mutual exclusive
 ```python    
 
def pay_amount(employee: Employee):
    if employee.is_separated:
        return {'amount': 0, 'reason_code': "SEP"}

    result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
    if employee.is_retired:
        if employee.age < 60:
            result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
        
        if not employee.age < 60:
            result = {'amount': 0, 'reason_code': "RET"}

    return result
 ```
  
  * Copy condition in nested if, and removing result variable 
 ```python    
def pay_amount(employee: Employee):
    if employee.is_separated:
        return {'amount': 0, 'reason_code': "SEP"}

    if employee.is_retired and employee.age < 60:
        return {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}

    if employee.is_retired and not employee.age < 60:
        return {'amount': 0, 'reason_code': "RET"}

    return {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
 ```
  
  * Moving if statements to group return values  
 ```python    
def pay_amount(employee: Employee):
    if employee.is_separated:
        return {'amount': 0, 'reason_code': "SEP"}

    if employee.is_retired and not employee.age < 60:
        return {'amount': 0, 'reason_code': "RET"}

    if employee.is_retired and employee.age < 60:
        return {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}

    return {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
 ```
  
  * Removing if statement
 ```python    
def pay_amount(employee: Employee):
    if employee.is_separated:
        return {'amount': 0, 'reason_code': "SEP"}

    if employee.is_retired and not employee.age < 60:
        return {'amount': 0, 'reason_code': "RET"}

    return {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
 ```
