import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

plt.plot(df['chunk_size'], df['avg_duration'] / 1000000)
plt.xlabel('Größe der Chunks')
plt.ylabel('Laufzeit in s')
plt.title("Laufzeiten der Skripte nach der gewählten Chunk-Größe")
plt.grid(False)
plt.show()
