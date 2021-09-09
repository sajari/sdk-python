
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.collections_api import CollectionsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from com.sajari.client.api.collections_api import CollectionsApi
from com.sajari.client.api.events_api import EventsApi
from com.sajari.client.api.pipelines_api import PipelinesApi
from com.sajari.client.api.records_api import RecordsApi
from com.sajari.client.api.schema_api import SchemaApi
