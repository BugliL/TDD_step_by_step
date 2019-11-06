# Inline Function
Consist in expliciting a function body where called removing the function itself.  
It's used when a function is just delegating something else or when expliciting 
code is more expressive than having a wrapping function. 

Inverse of [Extract function](../Extract%20function/)
Shortly: find, substitute
More shortly: Let ide do it for you

![Schema](./image.png)

 **Example**
 ```python
 def functionB(x:int):
    y = 10 if x % 5 else x
    return range(y, y+100, 2)     
    
 def functionA(x:int):
    return functionB(x)
    
 if __name__=='__main__':
    print(functionA(10))
    print(functionA(20))   
 ```
 
## How to inline function
 * Find all function/method calls
 ```python    
 # Don't you say?!   
 if __name__=='__main__':
    print(functionA(10))
    print(functionA(20))
 ```
 
 * Replace all function/method calls testing for each substitution
 ```python      
 if __name__=='__main__':
    print(functionB(10))  # Test OK
    print(functionB(20))  # Test OK
 ```
 
 * Remove function
 ```python
 def functionB(x:int):
    y = 10 if x % 5 else x
    return range(y, y+100, 2)     
    
 if __name__=='__main__':
    print(functionB(10))
    print(functionB(20))   
 ```