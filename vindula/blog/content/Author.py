# -*- coding: utf-8 -*-
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.blog.config import *
from vindula.blog.content.interfaces import IAuthor

author_schema = ATNewsItem.schema.copy() + Schema((
     

))

# Change field 'description'
descriptionField = author_schema['description']
descriptionField.widget.description = 'Texto que descreve brevemente sobre quem é o autor.'

invisivel = {'view':'invisible','edit':'invisible',}
author_schema['image'].widget.visible = invisivel
author_schema['imageCaption'].widget.visible = invisivel

finalizeATCTSchema(author_schema, moveDiscussion=True)

class Author(ATNewsItem):
    """ Object Author """
    
    implements(IAuthor)    
    portal_type = 'Author'
    _at_rename_after_creation = True
    schema = author_schema
    
    
    def at_post_create_script(self):
        self.verifica_pastaautores()

    def at_post_edit_script(self):
        self.verifica_pastaautores()
        
    def verifica_pastaautores(self):
        #verificar se estou na raiz do blog
        import pdb; pdb.set_trace();
        if self.aq_parent.Type() == 'Blog':
            #se estiver:
            # 1- pegar a pasta autores
            blog_folder = self.aq_parent
            autores_folder = getattr(blog_folder, 'autores', None)
            if autores_folder:
                # 2- recortar o objeto autor
                objects = blog_folder.manage_cutObjects(ids=[self.id])
                # 3- colar o objeto autor
                autores_folder.manage_pasteObjects(objects)
                #self.REQUEST.RESPONSE.redirect(autores_folder.absolute_url() + '/' + self.id)
                #raise self.REQUEST.RESPONSE.redirect(autores_folder.absolute_url() + '/' + self.id)
            
registerType(Author, PROJECTNAME)          