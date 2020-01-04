# Remove flag argument
Flag conditions hide aa little bit the control flow.  
Calling different functions instead of using a flag is clearer.  

## How to remove flag argument
 **Example**
Example in python files

 * Refactoring function
 ```diff    
 def delivery_date(order: Order, is_rush):
-    delivery_time = 4
     if is_rush:
         delivery_time = 3
         if order.delivery_state in ['MA', 'CT']:
             delivery_time = 1
         elif order.delivery_state in ['NY', 'NH']:
             delivery_time = 2
+        return order.placed_on + timedelta(days=delivery_time)
     else:
+        delivery_time = 4
         if order.delivery_state in ['MA', 'CT', 'NY']:
             delivery_time = 2
         elif order.delivery_state in ['ME', 'NH']:
             delivery_time = 3
 
-    return order.placed_on + timedelta(days=delivery_time)
+        return order.placed_on + timedelta(days=delivery_time)
 ```

 * Decompose conditional
 ```diff    
  def delivery_date(order: Order, is_rush):
     if is_rush:
-        delivery_time = 3
-        if order.delivery_state in ['MA', 'CT']:
-            delivery_time = 1
-        elif order.delivery_state in ['NY', 'NH']:
-            delivery_time = 2
-        return order.placed_on + timedelta(days=delivery_time)
+        return rush_delivery_date(order)
     else:
-        delivery_time = 4
-        if order.delivery_state in ['MA', 'CT', 'NY']:
-            delivery_time = 2
-        elif order.delivery_state in ['ME', 'NH']:
-            delivery_time = 3
+        return normal_delivery_date(order)
+
+
+def normal_delivery_date(order):
+    delivery_time = 4
+    if order.delivery_state in ['MA', 'CT', 'NY']:
+        delivery_time = 2
+    elif order.delivery_state in ['ME', 'NH']:
+        delivery_time = 3
+    return order.placed_on + timedelta(days=delivery_time)
+
 
+def rush_delivery_date(order):
+    delivery_time = 3
+    if order.delivery_state in ['MA', 'CT']:
+        delivery_time = 1
+    elif order.delivery_state in ['NY', 'NH']:
+        delivery_time = 2
+    return order.placed_on + timedelta(days=delivery_time)
 ```
 
  * Replace function call
 ```diff    
-    shipment.delivery_date = delivery_date(order, is_rush=True)
+    shipment.delivery_date = rush_delivery_date(order)
     print(shipment.delivery_date)
 
-    shipment.delivery_date = delivery_date(order, is_rush=False)
+    shipment.delivery_date = normal_delivery_date(order)
     print(shipment.delivery_date)
 ```
 
  * Remove unused code
 ```diff
-def delivery_date(order: Order, is_rush):
-    if is_rush:
-        return rush_delivery_date(order)
-    else:
-        return normal_delivery_date(order)
-
-
```