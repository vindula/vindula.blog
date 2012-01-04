# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView

class BlogView(BaseView):
    
    def getPosts(self):
        blog = self.context
        year = self.request.get('blog_year')
        month = self.request.get('blog_month')
        if year and month:
            blog = blog.get('posts').get(year).get(month)

        posts = self.pc(portal_type='Post',
                        review_state='published',
                        path={'query':'/'.join(blog.getPhysicalPath())},
                        sort_on='effective',
                        sort_order='descending',)
    
        if posts:
            L = []
            for post in posts:
                obj = post.getObject()
                D = {}
                D['title'] = obj.Title()
                D['date'] = self.formatDate(obj.getEffectiveDate())
                D['signature'] = self.getPostSignature(obj)
                D['text'] = obj.getRawContent_text()
                D['subject'] = obj.Subject()
                D['url'] = obj.absolute_url()
                D['image-caption'] = obj.getImageCaption()
                if obj.getImage():
                    D['image'] = obj.getImage().absolute_url()
                else:
                    D['image'] = ''
                L.append(D)
            return L
                
    
    def getAbaut(self):
        blog = self.context
        if blog.getMenu_about_blog() is True:
            D = {}
            D['title'] = blog.getTitle_about_blog()
            D['date'] = self.formatDate(blog.getEffectiveDate())
            D['signature'] = blog.getSignature()
            D['text'] = blog.getRawAbout_blog()
            return D
                
                
    def getAuthors(self):
        blog = self.context
        if blog.getMenu_authors() is True:
            authors = self.pc(portal_type='Author',
                              review_state='published',
                              path={'query':'/'.join(blog.getPhysicalPath())},
                              sort_on="getObjPositionInParent")
            if authors:
                L = []
                for author in authors:
                    obj = author.getObject()
                    D = {}
                    D['title'] = obj.Title()
                    D['date'] = self.formatDate(obj.getEffectiveDate())
                    D['signature'] = blog.getSignature()
                    D['text'] = obj.getText()
                    L.append(D)
                return L