# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView

class MacrosView(BaseView):
    
    def getBlogTop(self):
        # Returns the title, the image and the menu of the blog
        context = self.getBlogContext()
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
        
        
    def getBlogFooter(self):
        # Returns the blog bottom contents
        context = self.getBlogContext()
        if context:
            if context.getFooter():
                return context.getFooter()
        
        
    def getBlogFiles(self):
        # Returns a list of the folders on the blog
        blog = self.getBlogContext()
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
                            D = {}
                            D['name'] = month.Title().title()
                            D['number'] = month.getId()
                            D['posts'] = len(month.objectValues())
                            if D['posts'] > 0:
                                L.append(D)
                        if L != []:
                            files.append({'year': year.Title(), 
                                          'months': L})
                files.reverse()
                return {'blog':blog.absolute_url(), 
                        'files': files}
                
                
    def getURLBlog(self):
        ctx = self.context
        while ctx.portal_type != 'Blog':
            ctx = ctx.aq_inner.aq_parent
        return ctx.absolute_url()
        
        
        