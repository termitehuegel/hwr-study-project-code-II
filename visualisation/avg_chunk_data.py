import pandas as pd
import numpy as np

chunk_size = 100000

df = pd.read_csv('data.csv')
df = df[df['table_char'] == 'ALL']

df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])
df['duration'] = pd.to_timedelta(df['end_time'] - df['start_time']).astype(np.int64) / int(1e3)

avg_duration =  df.loc[:, 'duration'].mean()

df = pd.DataFrame(
    {
        'chunk_size': [chunk_size],
        'avg_duration': [avg_duration],
    }
)

df.to_csv('out/avg.csv', sep=',', encoding='utf-8', index=False, header=True)
