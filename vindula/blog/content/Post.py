# -*- coding: utf-8 -*-
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.blog.config import *
from vindula.blog.content.interfaces import IPost

post_schema = ATFolder.schema.copy() + Schema((
    
    ImageField(
        name='image',
        required=False,
        widget=ImageWidget(
            label="Imagem destaque",
            description="Imagem principal, será centralizada do topo do post.",
            label_msgid='vindula.blog_label_signature',
            description_msgid='vindula.blog_help_signature',
            i18n_domain='vindula.blog',
        ),
    ),
    
    TextField(
        name='imageCaption',
        required=False,
        widget=StringWidget(
            label="Legenda da imagem",
            description="Texto que será apresentado abaixo da imagem.",
            label_msgid='vindula.blog_label_imageCaption',
            description_msgid='vindula.blog_help_imageCaption',
            i18n_domain='vindula.blog',
        ),
    ),
    
    TextField(
        name='signature',
        required=False,
        widget=StringWidget(
            label="Assinatura corporativa",
            description="Será apresentada abaixo do título de cada post. Caso preenchido, este post irá ignorar a assinatura padrão do blog.",
            label_msgid='vindula.blog_label_signature',
            description_msgid='vindula.blog_help_signature',
            i18n_domain='vindula.blog',
        ),
    ),
    
    TextField(
        name='content',
        required=False,     
        searchable=True,
        widget=RichWidget(
            label="Corpo do texto",
            label_msgid='vindula.blog_label_number_content',
            description_msgid='vindula.blog_help_number_content',
            i18n_domain='vindula.blog',
        ),
    ),

))

# Change field 'description'
descriptionField = post_schema['description']
descriptionField.widget.description = 'Resumo do post ou apresentação de seu conteúdo.'

invisivel = {'view':'invisible','edit':'invisible',}

finalizeATCTSchema(post_schema, moveDiscussion=True, folderish=True)

class Post(ATFolder):
    """ Object Post """
    
    implements(IPost)    
    portal_type = 'Post'
    _at_rename_after_creation = True
    schema = post_schema

registerType(Post, PROJECTNAME)          