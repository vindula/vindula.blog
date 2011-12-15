# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView

class PostView(BaseView):
    
    def getPost(self):
        post = self.context
        D = {}
        D['title'] = post.Title()
        D['date'] = self.formatDate(post.getEffectiveDate())
        D['signature'] = self.getPostSignature(post)
        D['text'] = post.getText()
        D['subject'] = post.Subject()
        D['image-caption'] = post.getImageCaption()
        if post.getImage():
            D['image'] = post.getImage().absolute_url()
        else:
            D['image'] = ''
        return D