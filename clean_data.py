import os
import re
import pandas as pd

df = pd.read_json('./data.json')


df = df.dropna(subset=['url' ])



df.to_json('./cleaned_data.json', orient="records")

