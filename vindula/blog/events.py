# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

from zope.component import adapter
from zope.app.container.interfaces import IObjectAddedEvent

from vindula.blog.content.interfaces import IBlog

@adapter(IBlog, IObjectAddedEvent)
def create_banco_imagens(context, event):
    site = getSite()
    portal_workflow = getToolByName(site, 'portal_workflow')
    if not 'banco-de-imagens' in context.objectIds():
       context.invokeFactory('Folder', 
                             id='banco-de-imagens',
                             title='Banco de Imagens',
                             description='Pasta que guarda todas as imagens do portal.',
                             excludeFromNav = True)
       
       folder_images_data = context['banco-de-imagens']
       folder_images_data.setConstrainTypesMode(1)
       folder_images_data.setLocallyAllowedTypes(('Image', 'Folder'))
       portal_workflow.doActionFor(folder_images_data, 'publish')