import requests
import pandas as pd


url = "https://randomuser.me/api/?results=500"
response = requests.get(url)

if response.status_code == 200:
    print("it works")
    data = response.json()
    users_list = data['results']
    df = pd.DataFrame(users_list)
    print(df.head(['name']))
else:
    print("smth went wrong", response.status_code)

