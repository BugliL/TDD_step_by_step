# Split phase
Divide a function/module that manage 2 different things in separated functions/modules.  
This separation help clearance and behavior separation.
the most common case is when there's no function data object and data creation is demanded to function
instead of being "outside" of it.

**example**
```Python
order_string = "Item1-4|Item21-1"
order_data = order_string.split("|")
product_price = price_list[order_data[0].split("-")[1]]
order_price = eval(order_data[1]) * product_price
```

```Python
def ParseOrder(order_string):
    values = order_string.split("|")
    return {
        "productID" : values[0].split("-")[1],
        "qty" : eval(values[1])
    }

def GetPrice(order, price_list):
    return order['qty'] * price_list[order['productID']]

order_string = "Item1-4|Item21-1"
order_record = ParseOrder(order_string)
order_price = GetPrice(order_record, price_list)
```

## How to split phase
### Input split example
 * Apply "Extract function" to code that elaborates input
 * Apply "Change signature" to pass a structure to the function containing data
 * Apply "Extract function" to code that prepare data to output the structure used earlier
 * Apply eventual "Change signature" to remove not needed parameters to both functions.
