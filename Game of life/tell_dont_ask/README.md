# Tell don't ask
A better explanation on [Medium](https://medium.com/dailyjs/the-state-of-immutability-169d2cd11310)

Immutability means that objects can not be modified during the execution flow.  
Objects are created and if they needs to be changed a new object must be created.

> The opportunity of mutation provides no guaranty that something will stay unchanged.  
> The worst scenario takes place when some structure is used in separate parts of the application, 
> then any mutation in one component can create a bug in the other one.
> Such bug is really hard to track, because the source of the problem lies out of the scope of the failure. This is an example of a bad side effect.

They are thread safe because many threads can act on data represented by immutable objects
without concern of the data being changed by others.  