# -*- coding: utf-8 -*-
from vindula.blog.utils import (
    get_parent_folder,
    create_contents,
)

def organize_object(context, event):
    folder = context.aq_parent
    if folder.Type() == 'Blog':
        parent_name = ['autores', 'posts'][context.Type()=='Post']
        if not hasattr(folder, parent_name):
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
    if context.Type()=='Post':
        folder = get_parent_folder(folder)
        
    if folder != context.aq_parent:
        objects = context.aq_parent.manage_cutObjects(ids=[context.id])
        folder.manage_pasteObjects(objects)


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
        
    ]
    create_contents(context, contents)

