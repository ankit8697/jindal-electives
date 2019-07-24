from import_export import resources, fields
from .models import Elective


class ElectiveResource(resources.ModelResource):

    class Meta:
        model = Elective
        import_id_fields = ('id',)
        fields = ('id', 'name', 'professor', 'credit', 'school', 'cross',)
        
