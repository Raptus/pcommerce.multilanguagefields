from pcommerce.multilanguagefields import extender

from Products.CMFCore.utils import getToolByName

extenders = [extender.ProductExtender,
             extender.VariationExtender]

indexes = ('SearchableText', 'Subject', 'Title', 'Description', 'sortable_title',)

def reindex(portal):
    catalog = getToolByName(portal, 'portal_catalog')
    for index in indexes:
        catalog.reindexIndex(index, portal.REQUEST)

def install(context):
    if context.readDataFile('pcommerce.multilanguagefields_install.txt') is None:
        return
    
    portal = context.getSite()
    sm = portal.getSiteManager()
    for extender in extenders:
        sm.registerAdapter(extender, name='MultilanguagePcommerce%s' % extender.__name__)
    
    reindex(portal)

def uninstall(context):
    if context.readDataFile('pcommerce.multilanguagefields_install.txt') is None and \
       context.readDataFile('pcommerce.multilanguagefields_uninstall.txt') is None:
        return
    
    portal = context.getSite()
    sm = portal.getSiteManager()
    for extender in extenders:
        sm.unregisterAdapter(extender, name='MultilanguagePcommerce%s' % extender.__name__)
    
    reindex(portal)
