# Split loop
Split loop is used to separate 2 or more different code part executed
in the same loop in many loops .
Split loop it's very useful before function extract

**example**
```python
average_age = 0
total_salary = 0
for p in people:
    average_age += p.age
    total_salary += p.salary
average_age = average_age / len(people)
```

```python
average_age = 0
total_salary = 0

for p in people:
    total_salary += p.salary

for p in people:
    average_age += p.age
average_age = average_age / len(people)
```

## How to split loop
 * Copy the loop
 * Identify duplicated side effects
 * Remove duplicated side effects so that each loop contain
 only 1 behavior