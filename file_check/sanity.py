from os import path, stat
import pandas as pd
from pandas.errors import EmptyDataError


csv_filepath = 'data/test.csv'

if path.exists(csv_filepath):
    print(f'{csv_filepath} exists')
else:
    print(f'{csv_filepath} does not exist')

if stat(csv_filepath).st_size==0:
    print(f'{csv_filepath} is empty')
else:
    print(f'{csv_filepath} is not empty: {stat(csv_filepath).st_size}')

try:
    df = pd.DataFrame(pd.read_csv(csv_filepath))
    print(f'{csv_filepath} was imported successfully')
except EmptyDataError:
    raise EmptyDataError('File does not contain data')

