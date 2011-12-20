## Script (Python) "blogOrganize"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=state
##title=
##

view = context.restrictedTraverse('@@blog_base_view');
view.blogOrganize(state)