### Pandas
`import pandas as pd`
1. set index while creating dataframe
```python
people = {
    'first': ['evan', 'john', 'jason'], 
    'last': ['Das', 'Wachs', 'Li'], 
    'email': ['evandas@gmail.com', 'johnwachs@hotmail.com', 'jasonli@outlook.com']
}
df = pd.DataFrame(people, index = people['email'])
```
2. Check if specific Column is equal to specific Value
```python
filt = (df_new['last'] == 'Das') | (df_new['first'] == 'jason')
type(filt) = <class 'pandas.core.series.Series'>
df[filt, 'email']
# return a pandas column in which its last name is Das
df[~filt, 'email']
# bitwise not, can be used as Not here
```
3. `loc` and `iloc`
- `iloc(integer, [integer])` no matter what index you set, it always goes with the index number, i.e. 'direction oriented', and return that __row__
- `loc(str | int, [str | int])` cannot use index number if set another index at first, loc('row_name')
```python
people = {
    'first': ['evan', 'john', 'jason'], 
    'last': ['Das', 'Wachs', 'Li'], 
    'email': ['evandas@gmail.com', 'johnwachs@hotmail.com', 'jasonli@outlook.com'], 
    'gender': ['male', 'male', 'female']
}

df = pd.DataFrame(people)
print(df.loc[0, ['first', 'email']])
print(df.iloc[0, [0, 2]])
# both get the same result

"""
Output: 
first                 evan
email    evandas@gmail.com
Name: 0, dtype: object
"""
```

4. `apply()` and `map()` function
- `apply(func)` can used for both __Series__ and __DataFrame__; `map(func)` can only be used in __Series__

Using apply and map to modify elements in a chosen column
```python
people = {
    'first': ['evan', 'john', 'jason'], 
    'last': ['Das', 'Wachs', 'Li'], 
    'email': ['evandas@gmail.com', 'johnwachs@hotmail.com', 'jasonli@outlook.com']
}
df = pd.DataFrame(people)
df['first'] = df['first'].map(lambda x: x.upper())

"""
Output:
0     EVAN
1     JOHN
2    JASON
"""
len_summary = df.apply(len)
"""
Output:
first    3
last     3
email    3
"""
```
5. `replace` function in pandas
- `replace(dict)` function requires to pass a `dict`, in which key is the original one, value is the modified value
```python
people = {
    'first': ['evan', 'john', 'jason'], 
    'last': ['Das', 'Wachs', 'Li'], 
    'email': ['evandas@gmail.com', 'johnwachs@hotmail.com', 'jasonli@outlook.com'], 
    'gender': ['male', 'male', 'female']
}
df = pd.DataFrame(people)
df['gender'] = df['gender'].replace({'male': False, 'female': True})
```