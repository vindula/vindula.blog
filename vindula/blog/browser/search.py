# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView
from vindula.blog.browser.post import ManagementCommentsView

class BlogSearchView(BaseView):
    
    def searchPosts(self):
        blog = self.getBlogContext(self.context.aq_inner)
        term = self.request.get('search-word', '')
        subject = self.request.get('search-subject', '')
    
        if term or subject:
            posts = self.pc(portal_type='Post',
                            review_state='published',
                            path={'query':'/'.join(blog.getPhysicalPath())},
                            sort_on='effective',
                            sort_order='descending',
                            SearchableText=term,
                            Subject=subject)
            if posts:
                L = []
                for post in posts:
                    obj = post.getObject()
                    comments =  ManagementCommentsView(self.context, self.context.request).get_comentarios(context=obj)
                    D = {}
                    D['title'] = obj.Title()
                    D['date'] = self.formatDate(obj.getEffectiveDate())
                    D['signature'] = self.getPostSignature(obj)
                    D['text'] = self.limitTextSize(600, obj.getContent())
                    D['subject'] = obj.Subject()
                    D['url'] = obj.absolute_url()
                    D['comments'] = len(comments)
                    L.append(D)
                return L