# Introduce Assertion
Often, sections of code work only if certain conditions are verified.
Using assertion will raise an AssertionError if the condition specified in its section is False.

## How to Introduce Assertion
 **Example**
 ```python
 def calculate_value(base:float, discount_rate:float):
    return base * (1 - discount_rate)  
 ```
 
 * Introduce the assertion before statement when the condition assumed to be True
 ```python
 def calculate_value(base:float, discount_rate:float):
    assert discount_rate >= 0
    return base * (1 - discount_rate)  
 ```
 