import json
import os
from typing import List

import requests

# set these to your own values.
S3_TARGET                   = 's3://randy-pitcher-workspace--aws--us-west-2/tabular/staged/square_bagels/square_bagel.csv'
TABULAR_ORG_ID              = '6e332d7a-5325-4d1a-8b13-40181e4158d3'
TABULAR_TARGET_WAREHOUSE_ID = '097a7cbb-5095-40ed-bf80-dabafbacd09e'
TABULAR_TARGET_DATABASE_ID  = '2a4fee35-6eef-47f1-aa89-945cd2f252b2'
TABULAR_CREDENTIAL          = os.environ['TABULAR_CREDENTIAL'] # you can hardcode this if you're struggling with the .env file
TABULAR_BASE_URL            = 'https://api.tabular.io'

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
  file_format: str,
  auth_token: str,
  file_loader_bucket: str,
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
    "mode": "CREATE_LOAD",
    "fileLoaderConfig": {
      "fileFormat": file_format
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
  # token exchange 💪
  rest_token = get_tabular_token(TABULAR_BASE_URL, TABULAR_CREDENTIAL)
  
  # parse out the s3 junk
  s3_parts = S3_TARGET.replace('s3://', '').split('/')
  s3_bucket_name = s3_parts[0]
  s3_target_prefix = '/'.join(s3_parts[1:-1]) # folder without bucket name to load data from
  file_format = s3_parts[-1].split('.')[-1] # assumes normal basic csv, json, or parquet file extensions. nothing exotic
  s3_target = f'{s3_bucket_name}/{s3_target_prefix}/'
  tabular_target_table = s3_parts[-2] # assuming the parent folder name of the data files will be the table name
  
  print(f"\n\nProcessing Tabular autoload target: 's3://{s3_target}' into table {tabular_target_table}")
  try:
    bootstrap_tabular_table(
      TABULAR_BASE_URL, 
      TABULAR_ORG_ID,
      TABULAR_TARGET_WAREHOUSE_ID,
      TABULAR_TARGET_DATABASE_ID,
      tabular_target_table,
      [s3_target_prefix],
      file_format,
      rest_token,
      s3_bucket_name
      )
  except Exception as ex:
    print(f"Trouble processing {S3_TARGET} due to error: {ex}")


if __name__ == "__main__":
  main()