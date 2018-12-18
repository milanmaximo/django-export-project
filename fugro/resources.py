from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Project, Utilisation, Car, Author


class FugroResource(resources.ModelResource):
    author = fields.Field(attribute='author', column_name='author', widget=ForeignKeyWidget(Author, 'name'))
    date = fields.Field(attribute='date', column_name='date')
    worktime = fields.Field(attribute='worktime', column_name='worktime')
    code = fields.Field(attribute='code', column_name='code')
    comment = fields.Field(attribute='comment', column_name='comment')
    comment_project = fields.Field(attribute='comment_project', column_name='comment_project')
    comment_equipment = fields.Field(attribute='comment_equipment', column_name='comment_equipment')
    comment_car = fields.Field(attribute='comment_car', column_name='comment_car')

    project = fields.Field(attribute='project', column_name='project', widget=ForeignKeyWidget(Project, 'name'))
    utilisation = fields.Field(attribute='utilisation', column_name='utilisation', widget=ForeignKeyWidget(Utilisation, 'name'))
    car = fields.Field(attribute='car', column_name='car', widget=ForeignKeyWidget(Car, 'name'))
    fields = ('author', 'date', 'worktime', 'code', 'project', 'car', 'utilisation')

class Meta:
    model = Project

