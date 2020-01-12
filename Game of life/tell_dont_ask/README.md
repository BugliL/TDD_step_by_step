# Tell don't ask
A better explanation on [Martin Fawler blog](https://martinfowler.com/bliki/TellDontAsk.html)

Short version: tell objects what to do on data instead of asking for values and do things.
Instead of asking for a value from an object to check it or to modify it, this principle move that behavior
inside the class containing data.

Consequences are that both, logic and data are encapsulated in the same object.  