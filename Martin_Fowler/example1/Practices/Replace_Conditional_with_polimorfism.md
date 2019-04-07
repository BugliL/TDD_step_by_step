# Replace conditional with polimorphism
When there's a switch or a condition that executes the same logic except for a condition is possible to
use polimorphism to replace that code conditions.
Each code block of the condition is demanded in an object that execute the logic and the main condition is substituted 
with a function call.

**example**
```python
class Bird(object):
    "......."
    pass

def getPlumage(bird):
    if bird.type == "EuropeanSwallow":
        return "average"
    elif bird.type == "AfricanSwallow":
        return "tired" if bird.numberOfCoconuts > 2 else "average"
    elif bird.type == "NorvegianParrot":
        return "scorched" if bird.voltage > 100 else "beatiful"    
    else:
        return "unknown"
```

```python
class Bird(object):    
    "......."
    def plumage(self):
        return "uknown"
    
class EuropeanSwallow(Bird):
    @property
    def plumage(self):
        return "average"
        
class AfricanSwallow(Bird):
    @property
    def plumage(self):
        return "tired" if self.numberOfCoconuts > 2 else "average" 
        
class NorvegianParrot(Bird):
    @property
    def plumage(self):        
        return "scorched" if self.voltage > 100 else "beatiful"
        
def getPlumage(bird):
    return bird.plumage  
```

## How to Replace conditional with polimorphism
 * Create a superclass and classes to substitute the condition
    * The superclass must have a method, that should be overrided in each subclass,
    containing the default return value of the condition   
 * By the condition, extract functions by condition code blocks and put each one in 
   a subclass
 * Use a factory or instantiate the correct subclass in the main code
 