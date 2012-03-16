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

    def _get_posts_in_folder(self, folder):
        return self.context.portal_catalog(
            portal_type='Post', 
            review_state='published',
            path='/'.join(folder.getPhysicalPath()),
        )
 
        
    def getBlogFiles(self):
        # Returns a list of the folders on the blog
        blog = self.getBlogContext()
        files = []
        if blog and hasattr(blog, 'posts'):
            folder_posts = blog.get('posts')
            years = folder_posts.objectValues()
            if years:
                for year in years:
                    months = year.objectValues()
                    if months:
                        L = []
                        for month in months:
                            D = {}
                            D['name'] = month.Title().title()
                            D['number'] = month.getId()
                            D['posts'] = len(self._get_posts_in_folder(month))
                            D['link'] = month.absolute_url()
                            if D['posts'] > 0:
                                L.append(D)
                        if L != []:
                            files.append({'year': year.Title(), 
                                          'months': L})
                files.reverse()
                
        return {'blog':blog.absolute_url(), 
                'files': files}
                
                
    def getURLBlog(self):
        #import pdb
        #pdb.set_trace()
        blog = self.getBlogContext()
        ctx = self.context
        while ctx.portal_type != 'Blog':
            ctx = ctx.aq_inner.aq_parent
        return ctx.absolute_url()
        
        
        
