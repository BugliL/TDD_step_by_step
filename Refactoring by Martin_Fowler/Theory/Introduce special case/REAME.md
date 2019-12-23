# Introduce special case
This widespread testing for a special case, plus a common response

![Schema](./image.png)
 
Shortly: < Short version >

## How to Introduce special case
For starting code, check the file example.py.  
Following code snippets are made from that one reporting git diff.
 
 * < Operation 1 >
 ```diff  
 @dataclass
 class Customer(object):
     name: str
     payment_history = {'weeks': 0}
     billing_plan = BasicPlan
    
+    @property
+    def is_unknown(self) -> bool:
+        return False
+
+
+class UnknownCustomer(Customer):
+    @property
+    def is_unknown(self) -> bool:
+        return True
+
 ```

 * < Operation 2 >
 ```diff    
 < Source code >
 ```
 
  * < Operation 3 >
 ```diff    
 < Source code >
 ```