# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView
from Products.CMFCore.utils import getToolByName

class BlogOrganizeView(BaseView):
    
    def organize(self, state):
        # Organizes blog files
        obj = state.object
        folder_obj = obj.aq_parent
        folder_blog = self.getBlogContext(folder_obj)
        
        if folder_blog:
            if state.transition.getId() == 'publish': 
                
                # Checks and creates folders
                if obj.portal_type == 'Post':
                    year = str(obj.effective().year())
                    month = str(obj.effective().month())
                    folder_posts = self.getFolder(folder_blog, 'posts', 'Posts', ('Folder',))
                    folder_year = self.getFolder(folder_posts, year, year, ('Folder',))
                    title = self.getNameMonth(int(month))
                    folder_month = self.getFolder(folder_year, month, title, ('Post',)) 
                    # Move post
                    folder_month.manage_pasteObjects(folder_obj.manage_cutObjects(obj.getId()))
                                                     
                elif obj.portal_type == 'Author':
                    folder_authors = self.getFolder(folder_blog, 'autores', 'Autores', ('Author',)) 
                    # Move author
                    folder_authors.manage_pasteObjects(folder_obj.manage_cutObjects(obj.getId()))
                
            elif state.transition.getId() == 'retract':
                
                # Move object
                folder_blog.manage_pasteObjects(folder_obj.manage_cutObjects(obj.getId()))            
                

    def getFolder(self, local, id, title, allowed_types=()):
        # Creates a folder
        if not id in local.objectIds():
            local.invokeFactory('Folder', id=id, title=title)
            folder = local.get(id)
            portal_workflow = getToolByName(folder, 'portal_workflow')
            portal_workflow.doActionFor(folder, 'publish')  
            if allowed_types != ():
                folder.setConstrainTypesMode(1)
                folder.setLocallyAllowedTypes(allowed_types)
        return local.get(id)