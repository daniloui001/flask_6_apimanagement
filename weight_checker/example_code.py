import requests 
import pandas as pd 

df = pd.DataFrame({
    'weight': [100, 121, 131, 140],
    'height': [184, 160, 150, 175]
})

df[:1]['weight']


analysis = requests.get(
    url = 'https://us-east1-hants-504-2023.cloudfunctions.net/azure_function_dani',
    params = ({
        "weight": df[:1]['weight'],
        "height": df[:1]['height']
    })
)

analysis.text