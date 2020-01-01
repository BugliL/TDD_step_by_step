# Introduce special case
Used when there's a Null special case or something similar that needs to be managed.  
It simplifies code moving behavior in an inherited class instead of widespread testing for that case.

![Schema](./image.png)
 

## How to Introduce special case
 * Create the special case class
 * Add a bool property to both, base class and special case class to distinguish the case
    * is_something True or False in base class
    * is_something False or True in special case class
 * Use Extract Function on if checks for that special case to isolate checking code (can be more than 1)
    * This allow to do transformation checks in few well identified places
 * Use a Factory Method or something to wrap object getter, to isolate the creation process (should be 1 or few)
    * introduce the special case object checking inside this function / class
 * Modify the check function extracted to use the property is_something to check values
 * Use Combine function into class or combine functions into transform to edit code and remove checking statements
 * Use [Inline Function](../Inline%20function) if and where needed
 
**Example** 
For starting code, check the file example.py.  
Following code snippets are made from that one reporting git diff.
 
 * Creating Unknown customer class and adding is_unknown property 
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
+@dataclass
+class UnknownCustomer(Customer):
+    name: str = 'unknown'
+    @property
+    def is_unknown(self) -> bool:
+        return True
+
 ```

 * Apply extract function on if condition 
 ```diff    
+def is_customer_unknown(aCustomer):
+    if type(aCustomer) != Customer and aCustomer != 'unknown':
+        raise ValueError("Value '{}' unsupported".format(aCustomer))
+
+    return aCustomer == "unknown"
+
+
 def client_1(site: Site) -> None:
     aCustomer = site.customer
-    name = aCustomer.name if (aCustomer != "unknown") else "occupant"
+    name = aCustomer.name if not is_customer_unknown(aCustomer) else "occupant"
     print(name)
 
 
 def client_2(site: Site) -> None:
     aCustomer = site.customer
-    plan = BasicPlan if (aCustomer == "unknown") else aCustomer.billing_plan
+    plan = BasicPlan if is_customer_unknown(aCustomer) else aCustomer.billing_plan
     print(plan)
 
 
 def client_3(site: Site) -> None:
     aCustomer = site.customer
-    weeks = 0 if (aCustomer == "unknown") else aCustomer.payment_history['weeks']
+    weeks = 0 if is_customer_unknown(aCustomer) else aCustomer.payment_history['weeks']
     print(weeks)
 ```
 
  * Using UnknownCustomer class in Site class and changing the check function so to use the property
 ```diff    
-@dataclass
 class Site(object):
-    customer = Customer('John Smith')
+    def __init__(self, customer: [str, Customer]):
+        self._customer = customer if customer != 'unknown' else UnknownCustomer()
+
+    @property
+    def customer(self):
+        return self._customer
+def is_customer_unknown(aCustomer):
-    if type(aCustomer) != Customer and aCustomer != 'unknown':
+    if type(aCustomer) not in [Customer, UnknownCustomer]:
         raise ValueError("Value '{}' unsupported".format(aCustomer))
 
-    return aCustomer == "unknown"
+    return aCustomer.is_unknown
```

 *  Apply Combine functions into class
 ```diff
 @dataclass
 class UnknownCustomer(Customer):
-    name: str = 'unknown'
+    name: str = 'occupant'
 
@@
 
 def client_1(site: Site) -> None:
     aCustomer = site.customer
-    name = aCustomer.name if not is_customer_unknown(aCustomer) else "occupant"
+    name = aCustomer.name
     print(name)
 
 
 def client_2(site: Site) -> None:
     aCustomer = site.customer
-    plan = BasicPlan if is_customer_unknown(aCustomer) else aCustomer.billing_plan
+    plan = aCustomer.billing_plan
     print(plan)
 
 
 def client_3(site: Site) -> None:
     aCustomer = site.customer
-    weeks = 0 if is_customer_unknown(aCustomer) else aCustomer.payment_history['weeks']
+    weeks = aCustomer.payment_history['weeks']
     print(weeks)
 ```
 
 * Inline variable
 ```diff
 def client_1(site: Site) -> None:
-    aCustomer = site.customer
-    name = aCustomer.name
+    name = site.customer.name
     print(name)
 
 
 def client_2(site: Site) -> None:
-    aCustomer = site.customer
-    plan = aCustomer.billing_plan
+    plan = site.customer.billing_plan
     print(plan)
 
 
 def client_3(site: Site) -> None:
-    aCustomer = site.customer
-    weeks = aCustomer.payment_history['weeks']
+    weeks = site.customer.payment_history['weeks']
     print(weeks)
 ```