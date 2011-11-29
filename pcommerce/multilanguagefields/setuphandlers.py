from pcommerce.multilanguagefields import extender

from Products.CMFCore.utils import getToolByName

extenders = [extender.ProductExtender,
             extender.VariationExtender]

def install(context):
    if context.readDataFile('pcommerce.multilanguagefields_install.txt') is None:
        return
    
    portal = context.getSite()
    sm = portal.getSiteManager()
    for extender in extenders:
        sm.registerAdapter(extender, name='MultilanguagePcommerce%s' % extender.__name__)

def uninstall(context):
    if context.readDataFile('pcommerce.multilanguagefields_install.txt') is None and \
       context.readDataFile('pcommerce.multilanguagefields_uninstall.txt') is None:
        return
    
    portal = context.getSite()
    sm = portal.getSiteManager()
    for extender in extenders:
        sm.unregisterAdapter(extender, name='MultilanguagePcommerce%s' % extender.__name__)
