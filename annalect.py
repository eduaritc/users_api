import requests
import pandas as pd
import sqlite3
import json


"""
we're specifying specifically to the API that we want to get 100 items.
Another option would be to get the number of items we want to get from the API
with an input, and then add it to the query string
"""

url = 'https://random-data-api.com/api/v2/users?size=100'
response = requests.get(url)
content = json.loads(response.content)

lst = []

for i in content:
    if response.status_code == 200:
        user = {}
        user["country"] = i["address"]["country"]
        user["name"] = i["first_name"]
        user["surname"] = i["last_name"]
        user["gender"] = i["gender"]
        lst.append(user)
    else:
        print('Error:', response.status_code)


df = pd.DataFrame()

for i in lst:
    df2 = pd.DataFrame.from_dict(i, orient='index').T
    df = pd.concat([df, df2], ignore_index=True)

print(df)

###### FOR WRITING THE DATA TO CSV #################

df.to_csv('output.csv')

###### FOR SAVING THE DATA TO SQLite ###################

connlite = sqlite3.connect('records.db')
df.to_sql('users', connlite, if_exists='replace', index=False)
connlite.commit()
connlite.close()

"""
For scalability and putting it on AWS.
--> If we were to use Spark instead of Pandas.
    -Run Spark on EMR
    -Put the data into an RDS database running Postgres, that would scale out as much as a job like this would need to scale.
--> If we are just trying to scale it locally. 
    -We can still run the job with basic Python, but use a robust SQL database like Postgres instead of just SQLite
"""
