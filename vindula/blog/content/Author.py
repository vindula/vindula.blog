# -*- coding: utf-8 -*-
from zope.interface import implements

from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.blog.config import *
from vindula.blog.content.interfaces import IAuthor

author_schema = ATNewsItem.schema.copy() + Schema((
    
        


))

finalizeATCTSchema(author_schema, moveDiscussion=True)

class Author(ATNewsItem):
    """ Object Author """
    
    implements(IAuthor)    
    portal_type = 'Author'
    _at_rename_after_creation = True
    schema = author_schema

registerType(Author, PROJECTNAME)          