# Encapsulate variable
Data is more difficult to modify than functions.  
This refactoring pattern let data be wrapped in functions to manage it better.
It can be used in legacy code or in global variables.

## How to Encapsulate variable 
This pattern can be made in different ways, it depends on situation

 **Example**
 ```python
default_owner = {'first_name': 'John', 'last_name': 'Smith'}
 ```
 
### Only Getting
 **Example**
 ```python    
 spaceship.owner = default_owner
 ```
 * Create a wrapper  
 ```python    
 def get_default_owner():
    return default_owner
 ```
 
 * Replace the variable assignment
 ```python    
 spaceship_owner = get_default_owner()
 ```
 
 * Reduce variable visibility by moving it in another module and importing it locally
  ```python
  # Module variables.py
  default_owner = {'first_name': 'John', 'last_name': 'Smith'}
  ```
  ```python
    def get_default_owner():
        from variables import default_owner
        return default_owner
  ```

### Setting too
**Example**
```python
default_owner = {'first_name': 'John', 'last_name': 'Smith'}
```

 * Follow **Only getting** section: step 1 and step 2
 
 * Create a setter
 ```python
 def set_default_owner(owner):
     import variables
     variables.default_owner = owner
```
 
 * Replace assignments with setter calls
 ```python 
 set_default_owner( {'first_name': 'Jane', 'last_name': 'Smith'})
```
  
 * Move the variable in another module and use it in methods
 ```python
 def set_default_owner(owner):
     import variables
     variables.default_owner = owner
 
 def get_default_owner():
     from variables import default_owner
     return default_owner
 ```
 
 * Edit Getter to return a copy of original variable 
 ```python
    def get_default_owner():
        from variables import default_owner
        return copy.deepcopy(default_owner)
```