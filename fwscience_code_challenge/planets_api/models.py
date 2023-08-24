import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


class Planet(models.Model):
    # Here I did not make the field `name` unique, since I was not sure if for the challenge purposes we want to be able to insert planets with the same name, but different population, terrains, etc (for some reason)
    name = models.CharField(max_length=250, help_text="The name of the planet")
    population = models.BigIntegerField(null=True)
    _terrains = models.TextField(null=True, db_column="terrains")
    _climates = models.TextField(null=True, db_column="climates")

    # The following properties will allow to manage the terrains and climates as actual lists when interacting with the models, we do not use JSONField, since it is not supported by all the databases engines
    @property
    def terrains(self):
        if self._terrains:
            return json.loads(self._terrains)

    @terrains.setter
    def terrains(self, new_value):
        if new_value:
            self._terrains = json.dumps(new_value, cls=DjangoJSONEncoder)
        else:
            self._terrains = None

    @property
    def climates(self):
        if self._climates:
            return json.loads(self._climates)

    @climates.setter
    def climates(self, new_value):
        if new_value:
            self._climates = json.dumps(new_value, cls=DjangoJSONEncoder)
        else:
            self._climates = None
