
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
from sajari_client.api.collections_api import CollectionsApi
from sajari_client.api.events_api import EventsApi
from sajari_client.api.pipelines_api import PipelinesApi
from sajari_client.api.promotions_api import PromotionsApi
from sajari_client.api.records_api import RecordsApi
from sajari_client.api.redirects_api import RedirectsApi
from sajari_client.api.schema_api import SchemaApi
