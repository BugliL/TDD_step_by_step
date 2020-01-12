# Refactoring: Improving the Design of Existing Code
by Martin Fowler

## What is refactoring?
**Refactoring** : editing a software so that the
behavior won't change but the internal structure will improve.
It's cleaning the code while decreasing the probability to introduce
errors.

> The code slowly sinks from engineering to hacking
> Refactoring is the opposite of this practice
>
> Martin Fowler


## Example 1 - The theatre
A theater company participates in many events.
A customer will ask for a certain number of shows and the company
will ask for money based on the paying public and the type of show.
There are 2 types of shows: tragedies and comedies.
The company creates the invoice and assigns credits based on the
public to get discounts on upcoming shows.

The code has to:
 * Print the bill
 * Calculate the credits

## Theory
Theory folder contains refactoring techniques and explanations with sample code 
