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

try:
    from raptus.multilanguagefields.fields import BlobImageField
    class ImageField(ExtensionField, BlobImageField):
        """ ImageField
        """
except ImportError: # no blob support
    class ImageField(ExtensionField, fields.ImageField):
        """ ImageField
        """