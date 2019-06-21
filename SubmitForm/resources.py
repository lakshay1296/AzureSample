from import_export import resources
from models import Vendor

class VendorResource(resources.ModelResource):
    class Meta:
        model = Vendor
