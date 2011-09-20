from archetypes.schemaextender.field import ExtensionField
from raptus.multilanguagefields import fields

class StringField(ExtensionField, fields.StringField):
    """ StringField
    """

class LinesField(ExtensionField, fields.LinesField):
    """ LinesField
    """

class TextField(ExtensionField, fields.TextField):
    """ TextField
    """

class ImageField(ExtensionField, fields.ImageField):
    """ ImageField
    """