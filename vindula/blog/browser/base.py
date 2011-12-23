# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class BaseView(BrowserView):
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.pc = getToolByName(self.context, 'portal_catalog')

        
    def getBlogContext(self, context=None):
        # Returns the blog context
        if context is None:
            context = self.context
        while context.portal_type not in ['Blog', 'Plone Site']:
            context = context.aq_parent
            try:
                type = context.portal_type
            except:
                context = context.aq_parent
        if context.portal_type == 'Blog':
            return context

        
    def getPostSignature(self, post):
        # Get the signature of the article or blog
        if post.getSignature():
            return post.getSignature()
        else:
            blog = self.getBlogContext(post.aq_inner)
            if blog:
                return blog.getSignature()
            else:
                return ''
        
    
    def formatDate(self, date):
        # Get format the effective date 
        if date is not None:
            month = self.getNameMonth(date.month())
            return str(date.day()) + ' de ' + month + ' de ' + date.strftime('%Y, %Hh%M %p')
        else:
            return 'Não publicado'
        
    
    def getNameMonth(self, int):
        # Returns the names of months in Portuguese
        int -= 1
        if int >= 0 and int <= 11:
            months = ['janeiro', 
                      'fevereiro', 
                      'março', 
                      'abril', 
                      'maio', 
                      'junho', 
                      'julho', 
                      'agosto', 
                      'setembro', 
                      'outubro', 
                      'novembro', 
                      'dezembro'] 
            return months[int]
        
        
    def limitTextSize(self, size, text):
        # Restricts the amount of characters of a text
        if len(text) > size:
            i = size
            while text[i] != " ":
                i += 1              
            return text[:i]+'...'
        else:
            return text    