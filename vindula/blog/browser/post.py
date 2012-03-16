# -*- coding: utf-8 -*-
from vindula.blog.browser.base import BaseView
from plone.app.layout.viewlets.comments import CommentsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from AccessControl import getSecurityManager
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer

class PostView(BaseView):
    
    def getPost(self):
        post = self.context
        D = {}
        D['title'] = post.Title()
        D['date'] = self.formatDate(post.getEffectiveDate())
        D['signature'] = self.getPostSignature(post)
        D['text'] = post.getRawContent_text()
        D['subject'] = post.Subject()
        D['image-caption'] = post.getImageCaption()
        if post.getImage():
            D['image'] = post.getImage().absolute_url() + '/image_editorial'
        else:
            D['image'] = ''
        blog = self.getBlogContext(post.aq_inner)
        if blog:
            D['context-blog'] = blog.absolute_url()
            D['portlets'] = blog.getPortlets()
        return D
    
    
class CommentsPost(CommentsViewlet):
    render = ViewPageTemplateFile("templates/comments_blog.pt")
    
    def getComments(self):
        return ManagementCommentsView(self.context, self.context.request).get_comentarios()

    
    def getDescriptionComments(self):
        blog = self.context.aq_parent.context
        return blog.description_coments
    
    def getDescriptionComments(self):
        blog = self.context.aq_parent.context
        return blog.description_coments
    
class ManagementCommentsView(BaseView):
    def addComment(self):  
        comentario=self.context.request.get('comentario',None)
        blog = self.context.aq_parent.context

        
        if self.context.portal_membership.isAnonymousUser():
            return  'nao autenticado'
        
        if not comentario:
            return 'comentario vazio'
        
        tamanho_max = getattr(self.context, 'tamanho_comentario', 500)
        
        if len(comentario) > tamanho_max:
            return 'tamanho maximo do comentario excedido'
        
        login=getSecurityManager().getUser().getUserName()
        
        title=self.get_nome_completo(login)
        new_id = u'comentario-'+title
        normalizer = getUtility(IIDNormalizer)
        new_id = normalizer.normalize(unicode(new_id))
        
        if hasattr(self.context, new_id):
            new_id = self.context.generateUniqueId(new_id)

        self.context.create_new_comment(new_id = new_id, title = title, comentario = comentario)
        
        email_moderador = blog.email_moderation()
        msg = blog.text_email_moderation()
        assunto = 'Novo Comentario no Blog - Post: ' + self.context.Title()
        
        if not msg:
            msq = "Novo comentario adicionado" 
        if email_moderador: 
            self.envia_email(msg, assunto, email_moderador)

        return 'ok'
    
    def get_comentarios(self, review_state='aprovado', context=None):
        if not context:
            context = self.context
        
        #if not hasattr(context, 'comentarios'):
        #    return None
            
        #if not context.comentarios:
        #    return None
        caminho='/'.join(context.getPhysicalPath())
        comentarios = context.portal_catalog(portal_type='Comentario',
                                                  path=caminho,
                                                  review_state=review_state,
                                                  sort_on='created',
                                                  sort_order='descending',)
        return [ {'UID':comentario.UID,
                  'ID':comentario.id,
                  'Titulo':comentario.Title,
                  'Usuario': comentario.Creator,
                  'Texto':comentario.Description,
                  'Data': comentario.created.strftime('%d/%m/%Y - %Hh%M'),
                  'Estado': comentario.review_state,
                  }
                 for comentario in comentarios ]
        
    def get_nome_completo(self, username):
        user=self.context.acl_users.getUserById(username)
        if not user:
            return username
        
        nome=user.getProperty('fullname')
        
        if not nome:
            nome=user.getProperty('cn')
            
        if not nome:
            nome=username
            
        return nome
    
    def aprovaComentarios(self):        
        form = self.request.form
        #UID dos comentarios aprovados
        aprovados = [key for key in form.keys() if form.get(key) == '1']
        #UID dos comentarios reprovados
        reprovados = [key for key in form.keys() if form.get(key) == '0']
        errorMsg = ''
        if aprovados:
            if form.get('enviar_aprovados') == '1' and not form.get('mensagem_aprovados').rstrip(' '):
                return 'Por favor informe a mensagem para ser enviada aos usu√°rios com coment√°rios aprovados.'

        if reprovados:
            if form.get('enviar_reprovados') == '1' and not form.get('mensagem_reprovados').rstrip(' '):
                return 'Por favor informe a mensagem para ser enviada aos usu√°rios com coment√°rios reprovados.'

        usuarios_aprovados = []
        for aprovado in aprovados:
            comentario = self.context.portal_catalog(UID=aprovado)
            if comentario:
                comentario = comentario[0].getObject()
                transitions = self.context.portal_workflow.getTransitionsFor(comentario)
                transition_ids = [t['id'] for t in transitions]
                if 'aprovar' in transition_ids:
                    self.context.portal_workflow.doActionFor(comentario, 'aprovar')
                    usuarios_aprovados.append(comentario.Creator())

        usuarios_reprovados = []
        for reprovado in reprovados:
            comentario = self.context.portal_catalog(UID=reprovado)
            if comentario:
                comentario = comentario[0].getObject()
                transitions = self.context.portal_workflow.getTransitionsFor(comentario)
                transition_ids = [t['id'] for t in transitions]
                if 'reprovar' in transition_ids:
                    self.context.portal_workflow.doActionFor(comentario, 'reprovar')
                    usuarios_reprovados.append(comentario.Creator())


        def getEmail_usuario(user_name):
            email = user_name+'@caixa.gov.br'
            user_data = self.context.restrictedTraverse('@@pas_search').searchUsers(login=user_name)
            if user_data:
                user_data = user_data[0]
                if user_data.has_key('mail'):
                    email= user_data['mail']
                elif user_data.has_key('email'):
                    email= user_data['email']
                elif user_data.has_key('e-mail'):
                    email= user_data['e-mail']
            return email

        email_remetente = self.context.email_moderation() or getattr(self.context, 'email_caixa', 'example@example.com')
        if form.get('enviar_aprovados') == '1':
            for usuario in usuarios_aprovados:
                userEmail = getEmail_usuario(usuario)
                if userEmail:
                    print 'Sent Email aprovado:', userEmail, usuario
                    mail = 'O seu comentário no post "%s" foi aprovado. \n %s \n Mensagem do gestor:\n%s' %(self.context.Title(), self.context.absolute_url(), form.get('mensagem_aprovados'))
                    self.context.MailHost.send(mail.encode('latin1'),
                                               userEmail,
                                               email_remetente,
                                               u'[Blog Caixa] Comentário Aprovado'.encode('latin1'))

        if form.get('enviar_reprovados') == '1':
            for usuario in usuarios_reprovados:
                userEmail = getEmail_usuario(usuario)
                if userEmail:
                    print 'Sent Email reprovado:', userEmail, usuario
                    mail = 'O seu comentário no post "%s" foi aprovado. \n %s \n Mensagem do gestor:\n%s' %(self.context.Title(), self.context.absolute_url(), form.get('mensagem_aprovados'))
                    self.context.MailHost.send(mail.encode('latin1'),
                                               userEmail,
                                               email_remetente, 
                                               u'[Blog Caixa] Comentário Reprovado'.encode('latin1'))

