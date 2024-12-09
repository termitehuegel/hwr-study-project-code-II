import pandas as pd

count = 10000

df = pd.read_csv('data.csv')
df = df[df['table_char'] == 'ALL']

df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])
df['duration'] = pd.to_timedelta(df['end_time'] - df['start_time']).dt.microseconds

seq_dur =  df[df['script'] == 'sequential'].loc[:, 'duration'].mean()
sched_dur = df[df['script'] == 'scheduler'].loc[:, 'duration'].mean()
par_dur = df[df['script'] == 'parallel execute'].loc[:, 'duration'].mean()

df = pd.DataFrame(
    {
        'script': ['sequential', 'scheduler', 'parallel execute'],
        'count': [count, count, count],
        'avg_duration': [seq_dur, sched_dur, par_dur],
    }
)

df.to_csv('out/avg.csv', sep=',', encoding='utf-8', index=False, header=True)
