## Replace primitive with object 
It's common to choose to use basic data structures at start of code development and to change idea during the develop.
Something that initially is a string or a number can be changed in an object using this pattern. 

Shortly: Wrap, add properties, replace modifiers

## How to Replace primitive with object
 - Apply [Encapsulate variable](../Encapsulate%20variable) (if the variable is not encapsulated)
 - Create class to wrap the value (let's call it ClassA):
    - it subclass the type used
    - it takes the value in his constructor
    - it has a getter to the value ??????
 - Update original class 
    - Use a ClassA in attribute
    - Add a setter or update it to use ClassA object 
    - Add a getter or update it to use ClassA object
 - Substitute all clients call to convert the original class getter value to a ClassA object
 - Update the original class getter to return ClassA object
 
    
 **Example**
 ```python
 < Source code >   
 ```
