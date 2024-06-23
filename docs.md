# NFL Docs (v1.0.0)

### format_number()

The ```format_number()``` function needs 2 arguments

- ```format``` In here put the format you want to convert a number to.
- ```number``` Here you need to put the number you want to format.

#### Options for the ```format``` argument

The format argument has following options

- ```simplified``` 400000 = 400.0k
- ```simplified_2``` 400000 = 400.00k
- ```simplified_3``` 400000 = 400.000k
- ```normal``` 400000 = 400.000
- ```space``` 400000 = 400 000

### Example

#### example.py
```python
# Importing the module
import nfl

my_number        = 400000
my_number_format = nfl.format_number(format='simplified',
                                     number=my_number)

print(my_number_format)
```