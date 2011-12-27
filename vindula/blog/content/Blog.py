# -*- coding: utf-8 -*-
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.blog.config import *
from vindula.blog.content.interfaces import IBlog

blog_schema = ATFolder.schema.copy() + Schema((
                                               
    # Fieldset "Padrão"
    
    BooleanField(
        name='menu_initial',
        default=True,
        required=False,
        widget=BooleanWidget(
            label="Ativar menu: Início",
            description="Se esta opção estiver marcada, o menu Início ficará visível.",
            label_msgid='vindula.blog_label_number_menu_initial',
            description_msgid='vindula.blog_help_number_menu_initial',
            i18n_domain='vindula.blog',
        ),
    ), 
    
    ImageField(
        name='image',
        required=False,
        widget=ImageWidget(
            label="Imagem",
            description="Banner que será apresentado no topo, tem como função reforçar a proposta editorial do blog.",
            label_msgid='vindula.blog_label_image',
            description_msgid='vindula.blog_help_image',
            i18n_domain='vindula.blog',
        ),
     ),
         
    TextField(
        name='signature',
        required=False,
        widget=StringWidget(
            label="Assinatura corporativa",
            description="Será apresentada abaixo do título de cada post.",
            label_msgid='vindula.blog_label_signature',
            description_msgid='vindula.blog_help_signature',
            i18n_domain='vindula.blog',
        ),
    ),

    IntegerField(
        name='number_posts',
        default=10,
        required=True,
        widget=IntegerWidget(
            label="Número de posts",
            description="Quantidade de posts que serão apresentados na página inicial do blog.",
            label_msgid='vindula.blog_label_number_posts',
            description_msgid='vindula.blog_help_number_posts',
            i18n_domain='vindula.blog',
        ),
    ),      
    
    TextField(
        name='footer',
        required=False,
        widget=StringWidget(
            label="Rodapé",
            description="Insira uma frase para aparecer no rodapé.",
            label_msgid='vindula.blog_label_number_footer',
            description_msgid='vindula.blog_help_number_footer',
            i18n_domain='vindula.blog',
        ),
    ),
    
    # Fieldset "Sobre o Blog"
    
    BooleanField(
        name='menu_about_blog',
        default=True,
        required=False,
        #schemata = "Sobre o Blog",         
        widget=BooleanWidget(
            label="Ativar menu: Sobre o Blog",
            description="Se esta opção estiver marcada, o menu Sobre o Blog ficará visível.",
            label_msgid='vindula.blog_label_number_menu_about_blog',
            description_msgid='vindula.blog_help_number_menu_about_blog',
            i18n_domain='vindula.blog',
        ),
    ), 
    
    TextField(
        name='title_about_blog',
        required=False,
        #schemata = "Sobre o Blog", 
        widget=StringWidget(
            label="Título",
            description="Título da página de apresentação do blog.",
            label_msgid='vindula.blog_label_title_about_blog',
            description_msgid='vindula.blog_help_title_about_blog',
            i18n_domain='vindula.blog',
        ),
    ),
    
    TextField(
        name='about_blog',
        required=False,     
        #schemata = "Sobre o Blog",  
        widget=RichWidget(
            label="Sobre o blog",
            description="Conteúdo livre para apresentação do blog.",
            label_msgid='vindula.blog_label_number_about_blog',
            description_msgid='vindula.blog_help_number_about_blog',
            i18n_domain='vindula.blog',
        ),
    ),
    
    # Fieldset "Autores"
    
    BooleanField(
        name='menu_authors',
        default=True,
        required=False,
        #schemata = "Autores",         
        widget=BooleanWidget(
            label="Ativar menu: Autores",
            description="Se esta opção estiver marcada, o menu Autores ficará visível.",
            label_msgid='vindula.blog_label_number_menu_authors',
            description_msgid='vindula.blog_help_number_menu_authors',
            i18n_domain='vindula.blog',
        ),
    ), 
    

    # Fieldset "Portlets"

    BooleanField(
        name='portlets',
        default=False,
        required=False,
        #schemata = "Portlets",         
        widget=BooleanWidget(
            label="Mostrar portlets abaixo do menu",
            description="Se esta opção estiver marcada, os portlets serão exibidos abaixo do menu do blog.",
            label_msgid='vindula.blog_label_number_portlets',
            description_msgid='vindula.blog_help_number_portlets',
            i18n_domain='vindula.blog',
        ),
    ), 
    
    
))

invisivel = {'view':'invisible','edit':'invisible',}
blog_schema['description'].widget.visible = invisivel

finalizeATCTSchema(blog_schema, folderish=True)

class Blog(ATFolder):
    """ Object Blog """
    
    implements(IBlog)    
    portal_type = 'Blog'
    _at_rename_after_creation = True
    schema = blog_schema

registerType(Blog, PROJECTNAME)          