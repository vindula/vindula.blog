# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class BaseView(BrowserView):
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.pc = getToolByName(self.context, 'portal_catalog')