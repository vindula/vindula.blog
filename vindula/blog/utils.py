from datetime import datetime

from Products.CMFCore.WorkflowCore import WorkflowException
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import getUtility

def get_parent_folder(obj):
    data = datetime.now()
    meses= ('','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho',
            'Agosto','Setembro','Outubro','Novembro','Dezembro')
    folder = get_and_create(
        'Folder',
        obj,
        [
            str(data.year),
            meses[data.month],
            str(data.day)
        ]
    )
    return folder

def get_and_create(portal_type, folder, sub_folders):
    normalizer = getUtility(IIDNormalizer)
    for sub_folder in sub_folders:
        sub_folder_id = normalizer.normalize(sub_folder.decode('utf-8'))
        if not hasattr(folder, sub_folder_id):
            folder.invokeFactory(portal_type, id=sub_folder_id, title=sub_folder)
            folder.portal_workflow.doActionFor(folder[sub_folder_id], 'publish')
        folder = getattr(folder, sub_folder_id)

    return folder

def create_contents(context, contents):
    for content in contents:
        options = None
        if 'options' in content.keys():
            options = content.pop('options')

        if not hasattr(context, content['id']):
            context.invokeFactory(**content)
            if options:
                folder = getattr(context, content['id'])
                for opt, val in options.items():
                    if opt == 'allowed_types':
                        folder.setConstrainTypesMode(True)
                        folder.setLocallyAllowedTypes(val)
                    elif opt == 'do_workflow':
                        try:
                            context.portal_workflow.doActionFor(folder, val)
                        except WorkflowException:
                            print '[Warning] WorkflowException: Can\'t %s %s' %(val, folder.id)
                    elif opt == 'view_template':
                        folder.setLayout(val)
