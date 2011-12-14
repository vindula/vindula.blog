# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView
from Products.CMFCore.utils import getToolByName

class PostView(BaseView):
    
    def getPost(self):
        return 'post info'