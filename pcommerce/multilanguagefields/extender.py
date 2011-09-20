from zope.interface import implements
from zope.component import adapts

from Products.CMFPlone import PloneMessageFactory as _p
from Products.validation import V_REQUIRED
from Products.Archetypes.atapi import AnnotationStorage
from Products.ATContentTypes.configuration import zconf

from archetypes.schemaextender.interfaces import ISchemaExtender

from pcommerce.core import PCommerceMessageFactory as _
from pcommerce.core.interfaces import IProduct, IVariation
from pcommerce.multilanguagefields.widget import SingleKeywordWidget
from raptus.multilanguagefields import widgets
import fields

IMAGE_SIZES = {'large'   : (768, 768),
               'preview' : (400, 400),
               'mini'    : (200, 200),
               'thumb'   : (128, 128),
               'tile'    :  (64, 64),
               'icon'    :  (32, 32),
               'listing' :  (16, 16),
                }
try: # remove sizes if plone.app.imaging is available
    import plone.app.imaging
    IMAGE_SIZES = None
except ImportError:
    pass

base_fields = [
    fields.StringField(
        name='title',
        required=1,
        searchable=1,
        default='',
        accessor='Title',
        widget=widgets.StringWidget(
            label = _p(u'label_title', default=u'Title'),
            visible={'view' : 'invisible'},
            i18n_domain='plone',
        ),
        schemata='default',
    ),
    fields.TextField(
        'description',
        default='',
        searchable=1,
        accessor="Description",
        default_content_type = 'text/plain',
        allowable_content_types = ('text/plain',),
        widget=widgets.TextAreaWidget(
            label=_p(u'label_description', default=u'Description'),
            description=_p(u'help_description',
                           default=u'A short summary of the content.'),
        ),
        schemata='default',
    ),
    fields.ImageField(
        name='image',
        languageIndependent=True,
        swallowResizeExceptions=True,
        max_size='no',
        sizes=IMAGE_SIZES,
        validators=(('isNonEmptyFile', V_REQUIRED),
                    ('checkImageMaxSize', V_REQUIRED),),
        widget=widgets.ImageWidget(
            label= _p(u'label_news_image', default=u'Image'),
            show_content_type = False,),
    ),
    fields.StringField(
        name='imageCaption',
        required = False,
        searchable = True,
        widget = widgets.StringWidget(
            description = '',
            label = _p(u'label_image_caption', default=u'Image Caption'),
            size = 40)
    ),
    fields.TextField('text',
        required=False,
        searchable=True,
        primary=True,
        storage = AnnotationStorage(migrate=True),
        default_output_type = 'text/x-html-safe',
        widget = widgets.RichWidget(
            description = '',
            label = _p(u'label_body_text', default=u'Body Text'),
            rows = 25,
            allow_file_upload = zconf.ATDocument.allow_document_upload),
        schemata='default',
    ),
]

class ProductExtender(object):
    implements(ISchemaExtender)
    adapts(IProduct)

    fields = base_fields

    def __init__(self, context):
         self.context = context

    def getFields(self):
        return self.fields

class VariationExtender(object):
    implements(ISchemaExtender)
    adapts(IVariation)

    fields = base_fields + [
        fields.StringField(
            name='type',
            required=1,
            searchable=True,
            accessor='getType',
            widget=SingleKeywordWidget(
                label=_(u'Type'),
                format='radio',
            )
        ),
    ]

    def __init__(self, context):
         self.context = context

    def getFields(self):
        return self.fields
