# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView
from Products.CMFCore.utils import getToolByName

class BlogView(BaseView):
    
    def getPosts(self):
        return 'posts'