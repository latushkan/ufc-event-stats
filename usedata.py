import json
import pandas as pd

keys = ['DATE','W/L','NAME','STR','TD','SUB','PASS','WEIGHTCLASS','METHOD',
        'TECHNIQUE','ROUND','TIME','LOCATION','ATTENDANCE','EVENT']

# Load JSON file
with open('eventstats.json', 'r') as f:
    data = json.load(f)

# Store data as a Pandas dataframe
df = pd.DataFrame(data = data, columns = keys)

print(df)
