# -*- coding: utf-8 -*-
from zope.interface import Interface

class IBlog(Interface):
    """ Interface for Blog content type """
    
class IPost(Interface):
    """ Interface for Post content type """

class IAuthor(Interface):
    """ Interface for Author content type """