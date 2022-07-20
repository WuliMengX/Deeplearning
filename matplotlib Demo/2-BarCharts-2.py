import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use("fivethirtyeight")

# with open("sources/data.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

data = pd.read_csv("sources/data.csv")
ids = data['Responder_id']
lang_response = data['LanguagesWorkedWith']

languages_counter = Counter()
for response in lang_response:
    languages_counter.update(response.split(';'))

languages = []
popularity = []

for item in languages_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title('Most Popular Languages')
plt.xlabel('Number of people who use')
plt.tight_layout()
plt.show()
