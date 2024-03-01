import json
import os
from typing import List

import requests

# set these to your own values.
S3_BUCKET                     = 'tabular-analytics-raw'
TABULAR_ORG_ID                = '2c94428b-c610-46a3-b291-4b41a8c52990'
TABULAR_TARGET_WAREHOUSE_ID   = '03c7ef36-a2f3-48fe-b536-96836e96e760'
TABULAR_TARGET_DATABASE_ID    = '4a5f83d3-911b-47a8-85e6-edaeefd37c22'
TABULAR_CREDENTIAL            = os.environ['TABULAR_CREDENTIAL'] # you can hardcode this if you're struggling with the .env file
TABULAR_BASE_URL              = 'https://api.tabular.io'

S3_PATH = 'raw/hubspot' # leave blank if your raw folders are in the root of your s3 bucket
S3_TARGET_FOLDERS = [ # if you are loading an entire s3 bucket, which you shouldn't be, but if you are just set this to ['']
  'companies',
  'contacts',
  'deal_pipelines',
  'deals',
  'deals_property_history',
  'engagements',
  'engagements_calls',
  'engagements_meetings',
  'engagements_notes',
  'tickets',
]

def get_tabular_token(base_url: str, tabular_credential: str) -> str:
  client_id, client_secret = tabular_credential.split(':')
  url = f"{base_url}/ws/v1/oauth/tokens"
  data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
  }
  headers = {'Content-Type': 'application/x-www-form-urlencoded'}

  resp = requests.post(url, headers=headers, data=data)
  if resp.status_code != 200:
    raise Exception(f"Failed to get token: {resp.content}")

  return resp.json()['access_token']


def bootstrap_tabular_table(
  base_url: str,
  org_id: str, 
  warehouse_id: str, 
  database_id: str, 
  table_name: str, 
  file_loader_paths: List[str],
  auth_token: str,
  file_loader_bucket: str = S3_BUCKET,
  ) -> dict:
  """
  Creates a file-loader-ready table and performs a gapless initial load.

  Just like magic ✨🔮
  """
  url = f"{base_url}/v1/organizations/{org_id}/warehouses/{warehouse_id}/databases/{database_id}/tables"

  headers = {
    'accept': '*/*',
    'Authorization': f'Bearer {auth_token}',
    'Content-Type': 'application/json'
  }

  data = {
    "tableName": table_name,
    "bucket": file_loader_bucket,
    "prefixes": file_loader_paths,
    "mode": "CREATE_AUTO_LOAD",
    "fileLoaderConfig": {
      "fileFormat": 'json'
    }
  }

  print(url)
  print(data)
  print('\n\n')

  response = requests.post(url, headers=headers, data=json.dumps(data))
  if response.status_code != 200:
    raise Exception(f"Failed to execute query: {response.content}")
  return response.json()

def main():
  rest_token = get_tabular_token(TABULAR_BASE_URL, TABULAR_CREDENTIAL)
  for target_folder in HUBSPOT_TARGET_FOLDERS:
    s3_target = f'{S3_PATH}/{target_folder}/'
    tabular_target_table = f'{target_folder}' # TODO: maybe let folks define an s3 target, tablename target tuple
    print(f"\n\nProcessing Tabular autoload target: 's3://{S3_BUCKET}/{s3_target}' into table {tabular_target_table}")
    try:
      bootstrap_tabular_table(
        TABULAR_BASE_URL, 
        TABULAR_ORG_ID,
        TABULAR_TARGET_WAREHOUSE_ID,
        TABULAR_TARGET_DATABASE_ID,
        tabular_target_table,
        [s3_target],
        rest_token,
        S3_BUCKET
        )
    except Exception as ex:
      print(f"Skipping '{target_folder}' due to error: {ex}")


if __name__ == "__main__":
  main()