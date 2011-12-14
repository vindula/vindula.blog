# -*- coding: utf-8 -*-
from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = 'vindula.blog'

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner'))
ADD_CONTENT_PERMISSIONS = {
    'Blog': 'vindula.blog: Add Blog',
    'Post': 'vindula.blog: Add Post',
    'Author': 'vindula.blog: Add Author',
}

setDefaultRoles('vindula.blog: Add Blog', ('Manager','Owner'))
setDefaultRoles('vindula.blog: Add Post', ('Manager','Owner'))
setDefaultRoles('vindula.blog: Add Author', ('Manager','Owner'))

product_globals = globals()