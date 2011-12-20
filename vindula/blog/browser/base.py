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
        if context.portal_type == 'Blog':
            return context
        
    
    def getBlogTop(self, context):
        # Returns the title, the image and the menu of the blog
        context = self.getBlogContext(context)
        if context:
            D = {}
            D['title'] = context.Title()
            D['url'] = context.absolute_url()
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
        
        
    def blogOrganize(self, state):
        # Organizes blog files
        obj = state.object
        folder_obj = obj.aq_parent
        folder_blog = self.getBlogContext(folder_obj)
        
        if folder_blog:
            if state.transition.getId() == 'publish': 
                
                # Checks and creates folders
                if obj.portal_type == 'Post':
                    year = str(obj.effective().year())
                    month = str(obj.effective().month())
                    folder_posts = self.getFolder(folder_blog, 'posts', 'Posts', ('Folder',))
                    folder_year = self.getFolder(folder_posts, year, year, ('Folder',))
                    title = self.getNameMonth(int(month))
                    folder_month = self.getFolder(folder_year, month, title, ('Post',)) 
                    # Move post
                    folder_month.manage_pasteObjects(folder_obj.manage_cutObjects(obj.getId()))
                                                     
                elif obj.portal_type == 'Author':
                    folder_authors = self.getFolder(folder_blog, 'autores', 'Autores', ('Author',)) 
                    # Move author
                    folder_authors.manage_pasteObjects(folder_obj.manage_cutObjects(obj.getId()))
                
            elif state.transition.getId() == 'retract':
                
                # Move object
                folder_blog.manage_pasteObjects(folder_obj.manage_cutObjects(obj.getId()))
                    
                

    def getFolder(self, local, id, title, allowed_types=()):
        # Creates a folder
        if not id in local.objectIds():
            local.invokeFactory('Folder', id=id, title=title)
            folder = local.get(id)
            portal_workflow = getToolByName(folder, 'portal_workflow')
            portal_workflow.doActionFor(folder, 'publish')  
            if allowed_types != ():
                folder.setConstrainTypesMode(1)
                folder.setLocallyAllowedTypes(allowed_types)
        return local.get(id)
    
    
    def getBlogFiles(self, context):
        # Returns the list of files
        blog = self.getBlogContext(context)
        if blog:
            folder_posts = blog.get('posts')
            years = folder_posts.objectValues()
            if years:
                files = []
                for year in years:
                    months = year.objectValues()
                    if months:
                        L = []
                        for month in months:
                            number_posts = len(month.objectValues())
                            text = month.Title().title() + ' (' + str(number_posts) + ')'
                            if number_posts > 0:
                                L.append(text)
                        if L != []:
                            files.append({'year': year.Title(), 'months': L})
                return files