# -*- coding: utf-8 -*-
from zope.interface import implements

from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.blog.config import *
from vindula.blog.content.interfaces import IPost

post_schema = ATNewsItem.schema.copy() + Schema((
    
        


))

finalizeATCTSchema(post_schema, moveDiscussion=True)

class Post(ATNewsItem):
    """ Object Post """
    
    implements(IPost)    
    portal_type = 'Post'
    _at_rename_after_creation = True
    schema = post_schema

registerType(Post, PROJECTNAME)          