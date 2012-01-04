# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView

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
                    D = {}
                    D['title'] = obj.Title()
                    D['date'] = self.formatDate(obj.getEffectiveDate())
                    D['signature'] = self.getPostSignature(obj)
                    D['text'] = self.limitTextSize(600, obj.getContent_text())
                    D['subject'] = obj.Subject()
                    D['url'] = obj.absolute_url()
                    L.append(D)
                return L
            else:
                return []
        else:
            return []    