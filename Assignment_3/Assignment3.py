import pandas as pd
from pandas import DataFrame
import seaborn as sns

file_path='C:\Users\Haravindan\Downloads\data.csv'
df = pd.read_csv(file_path)

pivot = df.pivot_table(index=['Age'], values=['Ratio'], columns=['Year'])  //creating pivot table
print pivot

sns.heatmap(pivot).get_figure().savefig('heatmap5.png')   //using seaborn for heat map generation