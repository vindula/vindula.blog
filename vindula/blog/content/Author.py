# -*- coding: utf-8 -*-
from zope.interface import implements

from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.blog.config import *
from vindula.blog.content.interfaces import IAuthor

author_schema = ATNewsItem.schema.copy() + Schema((
     

))

# Change field 'description'
descriptionField = author_schema['description']
descriptionField.widget.description = 'Texto que descreve brevemente sobre quem é o autor.'

invisivel = {'view':'invisible','edit':'invisible',}
author_schema['image'].widget.visible = invisivel
author_schema['imageCaption'].widget.visible = invisivel

finalizeATCTSchema(author_schema, moveDiscussion=True)

class Author(ATNewsItem):
    """ Object Author """
    
    implements(IAuthor)    
    portal_type = 'Author'
    _at_rename_after_creation = True
    schema = author_schema

registerType(Author, PROJECTNAME)          