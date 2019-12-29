# Encapsulate record 
To manage mutable data, objects are better than records:  
it's possible to encapsulate all data and expose them throw methods and manipulation.  
It allows to change internal object behaviors without changing it's interface and to introduce defensive copies.  
This pattern explain how to move a data structure inside a class.
 
## How to Encapsulate record
The example is in the example file

 * Extract variable
```diff
+
+def get_raw_records():
+    return raw_records
+
+
 # Update example
-records['9201']['usages'][2016][2] = 42
+get_raw_records()['9201']['usages'][2016][2] = 42
 
 
 # Reading example
 def compare_usage(customer_id, year, month):
-    year_value = records[customer_id]['usages'][year][month]
-    last_year_value = records[customer_id]['usages'][year - 1][month]
+    year_value = get_raw_records()[customer_id]['usages'][year][month]
+    last_year_value = get_raw_records()[customer_id]['usages'][year - 1][month]
     return {'amount': year_value, 'difference': year_value - last_year_value}
 ```
 
 * Create class to wrap data
 ```diff
+class RecordData():
+    def __init__(self, records):
+        self._records = records
+
+    def get_records(self):
+        return self._records
+
+
 def get_raw_records():
     return raw_records
 ```

 * Update the getter function to use the class 
 ```diff
+record_data_object = RecordData(records=raw_records)
+
+
 def get_raw_records():
-    return raw_records
+    return record_data_object.get_records()
 ```
 
  * Create update function
 ```diff
  # Update example
+def set_usage_value(customer_id, year, month, value):
+    get_raw_records()[customer_id]['usages'][year][month] = value
+
+
 get_raw_records()['9201']['usages'][2016][2] = 42
 ```
 
 * Using the update function
 ```diff
 -get_raw_records()['9201']['usages'][2016][2] = 42
 +set_usage_value(customer_id='9201', year=2016, month=2, value=42)
 ```
 * Create function to return object
 ```diff
+def get_records_object():
+    return record_data_object
+
+
 # Update example
 def set_usage_value(customer_id, year, month, value):
     get_raw_records()[customer_id]['usages'][year][month] = value
 ``` 
 * Using object function 
 ```diff
 def get_records_object():
     return record_data_object
 
 
 # Update example
 def set_usage_value(customer_id, year, month, value):
-    get_raw_records()[customer_id]['usages'][year][month] = value
+    get_records_object().get_records()[customer_id]['usages'][year][month] = value
 
 
 set_usage_value(customer_id='9201', year=2016, month=2, value=42)
@@ -63,8 +63,8 @@ set_usage_value(customer_id='9201', year=2016, month=2, value=42)
 
 # Reading example
 def compare_usage(customer_id, year, month):
-    year_value = get_raw_records()[customer_id]['usages'][year][month]
-    last_year_value = get_raw_records()[customer_id]['usages'][year - 1][month]
+    year_value = get_records_object().get_records()[customer_id]['usages'][year][month]
+    last_year_value = get_records_object().get_records()[customer_id]['usages'][year - 1][month]
     return {'amount': year_value, 'difference': year_value - last_year_value}
 ```
 * Add getters and setters to class
 ```diff
      def get_records(self):
         return self._records
 
+    def set_usage_value(self, customer_id, year, month, value):
+        self._records[customer_id]['usages'][year][month] = value
+
+    def get_usage_value(self, customer_id, year, month):
+        return self._records[customer_id]['usages'][year][month]
+
 ```
 * Using class methods
 ```diff
 # Update example
 def set_usage_value(customer_id, year, month, value):
-    get_records_object().get_records()[customer_id]['usages'][year][month] = value
+    get_records_object().set_usage_value(customer_id, year, month, value)
 
 
-set_usage_value(customer_id='9201', year=2016, month=2, value=42)
+get_records_object().set_usage_value(customer_id='9201', year=2016, month=2, value=42)
 
 
 # Reading example
 def compare_usage(customer_id, year, month):
-    year_value = get_records_object().get_records()[customer_id]['usages'][year][month]
-    last_year_value = get_records_object().get_records()[customer_id]['usages'][year - 1][month]
+    year_value = get_records_object().get_usage_value(customer_id, year, month)
+    last_year_value = get_records_object().get_usage_value(customer_id, year - 1, month)
     return {'amount': year_value, 'difference': year_value - last_year_value}
 
```
 * Remove unused code
```diff
# Update example
-def set_usage_value(customer_id, year, month, value):
-    get_records_object().set_usage_value(customer_id, year, month, value)
-
- 
```

### Protecting raw data
To protect inner data is possible to:
 - use a proxy
 - apply ti pattern recursively and remove access to raw data
 - defensive copies
 
The 3rd is the simpler and the straight one
```diff
+import copy
@@
     def get_records(self):
-        return self._records
+        return copy.deepcopy(self._records)
```