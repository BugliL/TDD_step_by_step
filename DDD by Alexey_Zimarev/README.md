# Domain Driven Design

Domain-driven design (DDD) is an approach to software development for complex needs by connecting the implementation 
to an evolving model.  

This section follow the book and try to implement the same code of the book but in Python using different data 
structures but trying to follow the logic and the method.

References:
 * **The C# book** : "Hands-On Domain-Driven Design with .NET Core" by Alexey Zimarev
 * **The Blue book** : "Domain-Driven Design : Tackling complexity in the heart of software" by Eric Evans 

## The Application
Directly from the book, the software to be developed solve the problem:
> selling stuff online for private individuals. We'll be building an application to publish classified ads and 
> something that might be necessary to support this type of activity. If you aren't familiar with the terminology, 
> think about a bunch of stuff you have in your storage room or in the basement, which you would be delighted to remove. 
> You can publish a small ad online, and other people might buy things that you no longer need. 
>
> The C# book p66


### Useful notes
There are lots of conceptual code changes, here there are the most notable
 1. Use ```@dataclasses``` with ```froze=True``` as **value objects**
 
       
#### 1.Use ```@dataclasses``` with ```froze=True``` as **value objects**
Value objects are objects:
> objects that represents a descriptive aspect of the domain with no concemptual identity
> The Blue Book p98

Value objects should be immutable since they have no behavior involved