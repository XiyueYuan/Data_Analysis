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
2. check if specific col is equal to specific val
```python
filt = (df_new['last'] == 'Das') | (df_new['first'] == 'jason')
type(filt) = <class 'pandas.core.series.Series'>
df[filt, 'email']
# return a pandas column in which its last name is Das
df[~filt, 'email']
# bitwise not, can be used as Not here
```
