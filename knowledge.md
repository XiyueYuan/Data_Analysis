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
6. delete/drop & concat/new columns/row
- split & expand
```python
people = {
    'first': ['evan', 'john', 'jason'], 
    'last': ['Das', 'Wachs', 'Li'], 
    'email': ['evandas@gmail.com', 'johnwachs@hotmail.com', 'jasonli@outlook.com'], 
    'gender': ['male', 'male', 'female']
}
df = pd.DataFrame(people)
df['full_name'] = df['first'] + ' ' + df['last'] 

"""
Result
   first   last                  email  gender   full_name
0   evan    Das      evandas@gmail.com    male    evan Das
1   john  Wachs  johnwachs@hotmail.com    male  john Wachs
2  jason     Li    jasonli@outlook.com  female    jason Li
"""
# Or you can use existing columns to expand 
df[['pre', 'suf']] = df['email'].str.split('@', expand = True)
df['suf'] = df['suf'].str.split('.').str[0]

# .str[0] == .apply(lambda x: x[0]), .str is a syntactic sugar in pandas
# can apply to str, list, tuple, etc.

"""
   first   last                  email  gender   full_name        pre      suf
0   evan    Das      evandas@gmail.com    male    evan Das    evandas    gmail
1   john  Wachs  johnwachs@hotmail.com    male  john Wachs  johnwachs  hotmail
2  jason     Li    jasonli@outlook.com  female    jason Li    jasonli  outlook
"""
```
- concat
```python
people = {
    'first': ['evan', 'john', 'jason'], 
    'last': ['Das', 'Wachs', 'Li'], 
    'email': ['evandas@gmail.com', 'johnwachs@hotmail.com', 'jasonli@outlook.com'], 
    'gender': ['male', 'male', 'female']
}
df = pd.DataFrame(people)
new_row = pd.DataFrame(
    {
        'first': ['abi'], 
        'last': ['hachimi'], 
        'gender': ['nonbinary']
    }
)
df = pd.concat([df, new_row], ignore_index = True)
# concat two dataframe
"""
Result
  first     last                  email     gender
0   evan      Das      evandas@gmail.com       male
1   john    Wachs  johnwachs@hotmail.com       male
2  jason       Li    jasonli@outlook.com     female
3    abi  hachimi                    NaN  nonbinary
"""
```
- drop
```python
# first filter, then access to its index
# df.drop(integer), asking for integer

filt = df['first'] == 'abi'
df = df.drop(index = df[filt].index)
```
7. Sort Data
- `sort_values(by = ['col1', 'col2', ...], ascending = [True, False, ...])`, `normalize = True` return proportion

8. Groupby and Aggregate
- `df.groupby...`
- `df.agg(['median', 'mean'])...`

9. Missing Values
- in case there are `str` NA, first replace all of them into `np.nan`: `df.replace(['NA', 'Missing', ...], np.nan)`
- drop na notices two parameters: `subset = [...]`, and `how = 'any' / 'all'`
- `fillna('')` fill `np.nan` values 