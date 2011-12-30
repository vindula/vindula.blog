# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView
from plone.app.layout.viewlets.comments import CommentsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class PostView(BaseView):
    
    def getPost(self):
        post = self.context
        D = {}
        D['title'] = post.Title()
        D['date'] = self.formatDate(post.getEffectiveDate())
        D['signature'] = self.getPostSignature(post)
        D['text'] = post.getRawContent()
        D['subject'] = post.Subject()
        D['image-caption'] = post.getImageCaption()
        if post.getImage():
            D['image'] = post.getImage().absolute_url()
        else:
            D['image'] = ''
        blog = self.getBlogContext(post.aq_inner)
        if blog:
            D['context-blog'] = blog.absolute_url()
            D['portlets'] = blog.getPortlets()
        return D
    
class CommentsPost(CommentsViewlet):
    render = ViewPageTemplateFile("templates/comments.pt")