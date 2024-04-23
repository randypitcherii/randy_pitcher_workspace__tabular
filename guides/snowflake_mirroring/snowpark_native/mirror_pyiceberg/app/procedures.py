from snowflake.snowpark import Session
import _snowflake

from pyiceberg.catalog import load_catalog

def mirror_pyiceberg(session: Session): 
  TABULAR_CREDENTIAL       = _snowflake.get_generic_secret_string('tabular_credential_rpw')
  TABULAR_TARGET_WAREHOUSE = 'enterprise_data_warehouse' # replace this with your tabular warehouse name
  TABULAR_CATALOG_URI      = 'https://api.tabular.io/ws' # unless you're a single tenant user, you don't need to change this
  
  catalog_properties = {
    'uri':        TABULAR_CATALOG_URI,
    'credential': TABULAR_CREDENTIAL,
    'warehouse':  TABULAR_TARGET_WAREHOUSE
  }
  catalog = load_catalog(**catalog_properties)
  
  return f"PyIceberg list_namespaces response:\n{catalog.list_namespaces()}"
  