from Products.Archetypes.Registry import registerWidget
from Products.SingleKeywordWidget.widget import SingleKeywordWidget as BaseSingleKeywordWidget
from raptus.multilanguagefields.widgets import MultilanguageWidgetMixin

class SingleKeywordWidget(MultilanguageWidgetMixin, BaseSingleKeywordWidget):
    _properties = BaseSingleKeywordWidget._properties.copy()
    _properties.update({
        'macro' : 'multilanguage_singlekeyword',
        })

registerWidget(SingleKeywordWidget,
               title='Multilanguage Single Keyword',
               description='Renders a HTML widget for choosing a sinle keyword',
               used_for=('raptus.multilanguagefields.fields.StringField',)
               )
