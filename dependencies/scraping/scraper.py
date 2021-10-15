from fredapi import Fred
import pandas as pd
import json

fred = Fred(api_key='b1a18826bad1f7a681246d3dc256cfab')


#scrape metadata
metadata = fred.search_by_category(33446)

# scraping data
id = metadata['id']
data_df = pd.DataFrame()
data1 = pd.DataFrame()
for i in id:
    data_df[i] = fred.get_series(i)
    pd.concat([data1,data_df])


# Converting metadata and data into json serialized data
#store metadata into json 
metadata_response = metadata.to_json(orient='records')
# to load and show json (metadata)
metadata_parsed = json.loads(metadata_response)
json.dumps(metadata_parsed, indent=4)  

#store data into json 
result = data_df.to_json(orient='records')
#to load and show json (data)
parsed = json.loads(result)
json.dumps(parsed, indent=4)  

# Functions for main and __init__

def scrape_excel():
    print("\nsaving metadata as metadata.xlsx\n")
    metadata.to_excel('metadata.xlsx')                          # To store metadata into json file as metadata.xlsx

    print("\nsaving data as data.xlsx\n")
    data_df.to_excel('data.xlsx')                               # To store data into json file as data.xlsx


def scrape_json():
    print("\nsaving metadata as metadata.json\n")
    with open('metadata.json', 'w') as f:
        json.dump(metadata_parsed, f, ensure_ascii=False)           # To store metadata into json file as metadata.json

    print("\nsaving data as data.json\n")
    with open('data.json', 'w') as f:
        json.dump(parsed, f, ensure_ascii=False)                    # To store data into json file as data.json


def scrape_both():
    scrape_excel()
    scrape_json()


#check if the json file is serializable or not
def is_jsonable(x):
    try:
        json.dumps(x)
        return "The data is serialized"                     # True for serializable
    except (TypeError, OverflowError):
        return " Sorry!!! The data is not serialized"       # False for not serializable

def check_json_serialize():
    print(is_jsonable(parsed),"For data json")                  # Check for data json
    print(is_jsonable(metadata_response),"For metadata json")   #check for metadata json

    