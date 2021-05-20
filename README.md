# eTest
One-class one-file Python testing library.

## Installation
You can include the eTest.py file in your source and import it.
```python 
from eTest import test
```

## Usage
eTest uses decorators to mark functions for testing. The decorator takes in one argument which signifies the expected return value of the function.
```python 
from eTest import test

@test(4)
def sqr(num=2):
  return num**2
 
 test.run()
```
## Contribution
You can contribute by forking this repo and sending pull-requests.
