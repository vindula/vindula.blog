# -*- coding: utf-8 -*-
from zope.interface import implements
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IPortletBlogRss(IPortletDataProvider):
    """A portlet """


class Assignment(base.Assignment):
    """Portlet assignment """

    implements(IPortletBlogRss)

    def __init__(self):
        pass

    @property
    def title(self):
        return "Portlet RSS no Blog"


class Renderer(base.Renderer):
    """Portlet renderer """

    render = ViewPageTemplateFile('portlet_blogrss.pt')
          
    
class AddForm(base.NullAddForm):
    """Portlet add form """
    
    def create(self):
       return Assignment()