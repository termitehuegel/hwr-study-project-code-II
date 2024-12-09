import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

seq = df[df['script'] == 'sequential']
sched = df[df['script'] == 'scheduler']
par = df[df['script'] == 'parallel execute']

plt.plot(seq['count'], seq['avg_duration'] / 1000000, label='sequential')
plt.plot(sched['count'], sched['avg_duration'] / 1000000, label='scheduler')
plt.plot(par['count'], par['avg_duration'] / 1000000, label='parallel execute')
plt.xlabel('Einträge pro Tabelle')
plt.ylabel('Laufzeit in s')
plt.title("Laufzeiten der Skripte nach Einträgen pro Tabelle")
plt.legend()
plt.grid(False)
plt.show()
