Homework1

Q5: If Function vs. Statement

```python
def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result
```

```python
def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())
```

For with_if_statement, the function does not have any formal parameters. So that it does not execute the functions c(), t() and f() at first. It only execute them when encountered. However, for with_if_function, the c(), t() and f() are the formal parameters of if_function. So, it creates a frame first, and then bond these names to the values of c(), t() and f(), leading to executing these three functions firstly. And it does not execute them later any more.