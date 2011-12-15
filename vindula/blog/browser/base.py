# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class BaseView(BrowserView):
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.pc = getToolByName(self.context, 'portal_catalog')
        
    
    def getBlogTop(self, context):
        # Returns the title, the image and the menu of the blog
        while context.portal_type not in ['Blog', 'Plone Site']:
            context = context.aq_parent
            
        if context.portal_type == 'Blog':
            D = {}
            D['title'] = context.Title()
            if context.getImage():
                D['image'] = context.getImage().absolute_url()
            else:
                D['image'] = ''
            D['menu_initial'] = context.getMenu_initial()
            D['menu_abaut'] = context.getMenu_about_blog()
            D['menu_authors'] = context.getMenu_authors()
            return D  
        
        
    def getPostSignature(self, post):
        # Get the signature of the article or blog
        if post.getSignature():
            return post.getSignature()
        else:
            context = post
            while context.portal_type not in ['Blog', 'Plone Site']:
                context = context.aq_parent
            if context.portal_type == 'Blog':
                return context.getSignature()
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