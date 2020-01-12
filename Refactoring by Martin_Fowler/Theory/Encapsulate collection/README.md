# Encapsulate collection 
Exposing collections outside of a class is source of bugs, it's better if a class provide methods to control elements
in the collection.
Encapsulate collection explain how to change an exposed collection to a wrapped one.
 
Short version: wrap, use methods, return copy
 
## How to Encapsulate collection
 - Apply [Encapsulate variable](../Encapsulate%20variable)
 - Add managing method to add and remove elements from collection
 - Remove setter for variable or introduce defensive copy during setting
 - Replace all direct reference to collection with updating methods
 - Update getter to return a copy or a proxy
 
 
 **Example**
Example code in python file
  
 * Added methods to manipulate collection 
 ```diff
+    def add_course(self, course: Course):
+        self.__courses.append(course)
+
+    @staticmethod
+    def if_not_present():
+        raise ValueError('Element not found')
+
+    def remove_course(self, course):
+        try:
+            self.__courses.remove(course)
+        except ValueError:
+            self.if_not_present()
+
 ```

 * Replace setter with method calls 
 ```diff    
     x = Person("John Wick")
-    x.courses = [course1, course2]
+    x.add_course(course1)
+    x.add_course(course2)
+    x.add_course(course2)
+    x.remove_course(course2)
     n = get_number_of_advanced_courses(x)
 ```
 
  * Remove setter
 ```diff
-    @courses.setter
-    def courses(self, courses: List[Course]):
-        self.__courses = courses
-
     def add_course(self, course: Course):
         self.courses.append(course)

 ```
 
  *  Defensive copy
  ```diff
+import copy
 from dataclasses import dataclass, field
 from typing import List
 
@@ -27,7 +28,7 @@ class Person:
 
     @property
     def courses(self):
-        return self.__courses
+        return copy.deepcopy(self.__courses)
 
     def add_course(self, course: Course):
         self.courses.append(course)


  ```