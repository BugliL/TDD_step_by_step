# Extract function
Consist in creating a new function isolating some code part that
make sense. It's useful to shrink function size and to isolate some
function logic making the code cleaner.

Inverse of [Inline function](../Inline%20function/)

![Schema](./image.png)

Shortly: duplicate, adjust, remove duplication
More shortly: Let ide do it for you

## How to Extract a function

**Example**
```python
def print_something(invoice):
    printBanner()
    outstanding = cal_outstanding()

    print(f"name: ${invoice['customer']}")
    print(f"amount: ${outstanding}")
    #...
    print(f"name: ${invoice['customer']}")
    print(f"amount: ${outstanding}")
```

 * Find the code to copy in the function
   ```python
       # Isolating output is a good practice
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
   ```
   
 * Create a new function
   ```python
   def printDetails():
       pass
    
   def print_something(invoice):
       printBanner()
       outstanding = cal_outstanding()
    
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
       #...
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
   ```
   
 * Copy the code in that function
   ```python
   def printDetails():
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
    
   def print_something(invoice):
       printBanner()
       outstanding = cal_outstanding()
    
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
       #...
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
   ```
   
 * Examine the copied code to find out some local variables and
   pass them as parameter or include them as local variable.   
   *If the number of variable is a lot, abort, rollback and try 
   something different.*   
   ```python
   def printDetails(invoice, outstanding):
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
    
   def print_something(invoice):
       printBanner()
       outstanding = cal_outstanding()
    
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
       #...
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
   ```
   
 * Substitute the extracted code with a function call
   ```python   
   def printDetails(invoice, outstanding):
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
   
   def print_something(invoice):
       printBanner()
       outstanding = cal_outstanding()
       printDetails(invoice, outstanding)
       #...
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
   ```
 
 * Look for similar code to extract and replace inline code with
   function call   
   ```python  
   def printDetails(invoice, outstanding):
       print(f"name: ${invoice['customer']}")
       print(f"amount: ${outstanding}")
   
   def print_something(invoice):
       printBanner()
       outstanding = cal_outstanding()
       printDetails(invoice, outstanding)
       #...
       printDetails(invoice, outstanding)
   ```