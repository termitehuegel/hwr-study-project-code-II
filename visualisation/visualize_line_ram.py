import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

seq = df[df['script'] == 'sequential']
sched = df[df['script'] == 'scheduler']
par = df[df['script'] == 'parallel execute']

plt.plot(seq['ram'], seq['avg_duration'] / 1000000, label='sequential')
plt.plot(sched['ram'], sched['avg_duration'] / 1000000, label='scheduler')
plt.plot(par['ram'], par['avg_duration'] / 1000000, label='parallel execute')
plt.xlabel('RAM in GiB')
plt.ylabel('Laufzeit in s')
plt.title("Laufzeiten der Skripte nach verfügbarem RAM")
plt.legend()
plt.grid(False)
plt.show()
