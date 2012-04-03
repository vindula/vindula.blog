# -*- coding: utf-8 -*-
from zExceptions import Redirect

from vindula.blog.utils import (
    get_parent_folder,
    create_contents,
)

def organize_object(context, event):
    # obtendo nivel acima
    folder = context.aq_parent
    # se estou na raiz do blog
    if folder.Type() == 'Blog':
        parent_name = ['autores', 'posts'][context.Type()=='Post']
        #verifico se tem as pastas de autores e posts
        if not hasattr(folder, parent_name):
            #se nao houver eu crio
            contents = [
                {
                    'type_name': 'Folder',
                    'id': 'autores',
                    'title': 'Autores',
                    'options': {
                        'do_workflow': 'publish',
                        'allowed_types': ['Author', 'Folder'],
                    },
                },
                {
                    'type_name': 'Folder',
                    'id': 'posts',
                    'title': 'Posts',
                    'options': {
                        'do_workflow': 'publish',
                        'allowed_types': ['Post', 'Folder'],
                    },
                },
            ]
            create_contents(folder, contents)
        folder = folder[parent_name]

    import pdb ; pdb.set_trace()

    if context.Type()=='Post':
        folder = get_parent_folder(folder)
        
    
    if folder != context.aq_parent:
        #recortando da origem e colocando no destino correto
        #objects = context.aq_parent.manage_cutObjects(ids=[context.id])
        #folder.manage_pasteObjects(objects)
        folder.manage_pasteObjects(context.aq_parent.manage_cutObjects(ids=[context.id]))
        #return context.REQUEST.RESPONSE.redirect(context.portal_url())


def create_folder_structure(context, event):
    contents = [
        {
            'type_name': 'Folder',
            'id': 'posts',
            'title': 'Posts',
            'options': {
                'do_workflow': 'publish',
                'allowed_types': ['Post', 'Folder'],
             },
        },
        {
            'type_name': 'Folder',
            'id': 'autores',
            'title': 'Autores',
            'options': {
                'do_workflow': 'publish',
                'allowed_types': ['Author', 'Folder'],
             },
        },
        {
            'type_name': 'Folder',
            'id': 'imagens',
            'title': 'Imagens',
            'options': {
                'do_workflow': 'publish',
                'allowed_types': ['Image', 'Folder'],
             },
        },
        {
            'type_name': 'Folder',
            'id': 'multimidia',
            'title': 'Multimidia',
            'options': {
                'do_workflow': 'publish',
                'allowed_types': ['LiberiunStreaming', 'Folder'],
             },
        },
        {    'type_name': 'Topic',
             'id': 'feeds',
             'title': 'Feeds',
             'options': {
                 'do_workflow': 'publish'},
        },
    ]
    create_contents(context, contents)

