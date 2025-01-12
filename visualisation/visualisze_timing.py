import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])


df['micro_to_start'] = (df['start_time'] - df['start_time'].min()).astype(np.int64) / int(1e3)
df['micro_to_end'] = (df['end_time'] - df['start_time'].min()).astype(np.int64) / int(1e3)
df['task_duration'] = df['micro_to_end'] - df['micro_to_start'] + 1

plt.barh(y=df['table_char'], width=df['task_duration'], left=df['micro_to_start'])
plt.xlabel('Zeit t seit Skriptstart $t_{0}$ in μs')
plt.ylabel('Verarbeitete Tabelle')
plt.title("Zeitlicher Ablauf der Ausführung")
plt.show()
