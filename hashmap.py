#setup
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data_file="Visualisasi_data/flight_delays.csv"
data=pd.read_csv(data_file,index_col='Month')
print(data)
#plot hash map
plt.figure(figsize=(10,6))
v_data=sns.heatmap(data=data,annot=True)
#data=>data yang dimasukan dalam melakukan proses visualisasi data
#annot =>untuk melakukan ensure/keyakinan atau konfirmasi bahwa beberapa value sudah dicantumkan kedalam map
plt.show()