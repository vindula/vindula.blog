# -*- coding: utf-8 -*-
from zope.interface import implements

from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.blog.config import *
from vindula.blog.content.interfaces import IBlog

blog_schema = ATFolder.schema.copy() + Schema((
    
        


))

finalizeATCTSchema(blog_schema, folderish=True)

class Blog(ATFolder):
    """ Object Blog """
    
    implements(IBlog)    
    portal_type = 'Blog'
    _at_rename_after_creation = True
    schema = blog_schema

registerType(Blog, PROJECTNAME)          