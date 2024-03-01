# Tabular Table Bootstrapper
This directory holds a python script for bootstrapping file-loader tables from s3 paths into Tabular.

## Config
- create a `.env` file in this directory, but do not commit it to the repo:
```.env
TABULAR_CREDENTIAL=<Tabular credential here -- must have Sec Admin, so probably want a member cred>
```

## Usage
Some quick notes:
- No permissions are set with this script. 
- This doesn't create a database. It expects it to already to exist (and for permissions to be preset already)

Run the setup with the following:
- With your `.env` file, execute `pipenv install` to install dependencies
- run this bootstrapper with `pipenv run python ./tabular_autoload_from_s3.py`