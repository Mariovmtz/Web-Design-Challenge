import pandas as pd

df = pd.read_csv('resources/cities.csv', index_col=0)
df.to_html('resources/cities.html')