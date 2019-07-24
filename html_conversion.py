import pandas as pd

file="Resources/cities.csv"
df = pd.read_csv(file)

df.to_html(buf="data_raw.html")