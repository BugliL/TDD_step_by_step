# Extract function
Consist in creating a new function isolating some code part that
make sense. It's useful to shrink function size and to isolate some
function logic part making the code cleaner.

**Example**
```python
def print_something(invoice):
    printBanner()
    outstanding = cal_outstanding()

    # code to extract
    print(f"name: ${invoice['customer']}")
    print(f"amount: ${outstanding}")
```

```python
# extracted function
def printDetails(invoice, outstanding):
    print(f"name: ${invoice['customer']}")
    print(f"amount: ${outstanding}")

def print_something(invoice):
    printBanner()
    outstanding = cal_outstanding()
    printDetails(invoice, outstanding)
```

## How to Extract a function
 * Find the code to copy in the function
 * Create a new function
 * Copy the code in that function
 * Examine the copied code to find out some local variables and
   pass them as parameter
   * if the variable is used only in the extracted code but is declared
   in the function copy the declaration too and remove that var from
   being a parameter.
   * if the number of variable is a lot, abort this refactory pattern,
   revert all changes and try out some other refactory technique
 * Substitute the extracted code with a function call
 * Look for similar code to extract and replace inline code with
   function call