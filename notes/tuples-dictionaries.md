# Topics

- Tuple datatype
  - Constructing Tuple
  - Methods
  - Properties
- Dictionary datatype
- Sets datatype

## Constructing Tuple

- A tuple in python can be defined using: () for e.g. (1, 2, 3)
- Tuples is an immutable datatype. Therefore it doesn't support append andd extend operations.

## Methods in Tuple

- index()
- count()

# Dictionaries 

- A dictionary is created using {'key': 'value'} pair structure
- Keys should always be of immutable datatype such as tuple, strings, numbers etc
- In dictionaries, the order in which the elements are inserted is retained. 
Nested dict:

```python
sample_dict = {
    "employee": {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}
```
## Methods in dict

- keys()
- values()
- items()

## Sets datatype

- Set doesn't allow duplicates in the dataset
- The order of insertion in set is not retained
- To add elements to a set, we use `add()` method

## Typecasting

- Changing the datatypee of a variable i.e. list > tuple or list > set etc

## Booleans

- True and False are only the two possible values that can be for booleans

## Comparisions

- `==` > compares whether two values are equal or not and returns true if equal and false if not
- `!=` > not equal to i.e. compares whether two values are equal or not
- >, <, >=, <=

## Chained Comparisions

- `and` > If both the conditions are True only then the result will be true
- `or` > If one of the condition is True, the result will be True
- E.g 1 < 2 < 3 --> (1 < 2) and (2 < 3) Therefore the result is True

## Conditions

- If-else statement
- If-elif-else statement
