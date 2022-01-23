# Strawberry
One-class one-file Python testing library.

## Installation
You can include the strawberry.py file in your source and import it.
```python 
from strawberry import test
```

## Usage
Strawberry uses decorators to mark functions for testing. The decorator takes in one argument which signifies the expected return value of the function.
```python 
from strawberry import test

@test(4)
def sqr(num=2):
  return num**2

# You can also use lists as arguments.
@test(9, [3])
def sqr(num=2):
  return num**2
 
 test.run()
```
## Contribution
You can contribute by forking this repo and sending pull-requests.
