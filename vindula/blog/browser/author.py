# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView
from Products.CMFCore.utils import getToolByName

class AuthorView(BaseView):
    
    def getAuthor(self):
        return 'author profile'