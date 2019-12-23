# Introduce special case
This widespread testing for a special case, plus a common response

![Schema](./image.png)
 
Shortly: < Short version >

## How to Introduce special case
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
 
  * Using UnknownCustomer class in Site class
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
 ```
 
  * 
 ```diff

 ```