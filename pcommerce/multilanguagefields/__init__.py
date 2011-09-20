""" Patching __bobo_traverse__ method to allow transparent access to multilanguage image scales
"""
from raptus.multilanguagefields.patches.traverse import __bobo_traverse__
from pcommerce.core.content.product import Product
from pcommerce.core.content.variation import Variation
Product.__bobo_traverse__ = __bobo_traverse__
Variation.__bobo_traverse__ = __bobo_traverse__