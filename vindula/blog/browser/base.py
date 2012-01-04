# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

# Import para envio de E-mail
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

class BaseView(BrowserView):
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.pc = getToolByName(self.context, 'portal_catalog')

        
    def getBlogContext(self, context=None):
        # Returns the blog context
        if context is None:
            context = self.context
        while context.portal_type not in ['Blog', 'Plone Site']:
            context = context.aq_parent
            try:
                type = context.portal_type
            except:
                context = context.aq_parent
        if context.portal_type == 'Blog':
            return context

        
    def getPostSignature(self, post):
        # Get the signature of the article or blog
        if post.getSignature():
            return post.getSignature()
        else:
            blog = self.getBlogContext(post.aq_inner)
            if blog:
                return blog.getSignature()
            else:
                return ''
        
    
    def formatDate(self, date):
        # Get format the effective date 
        if date is not None:
            month = self.getNameMonth(date.month())
            return str(date.day()) + ' de ' + month + ' de ' + date.strftime('%Y, %Hh%M %p')
        else:
            return 'Não publicado'
        
    
    def getNameMonth(self, int):
        # Returns the names of months in Portuguese
        int -= 1
        if int >= 0 and int <= 11:
            months = ['janeiro', 
                      'fevereiro', 
                      'março', 
                      'abril', 
                      'maio', 
                      'junho', 
                      'julho', 
                      'agosto', 
                      'setembro', 
                      'outubro', 
                      'novembro', 
                      'dezembro'] 
            return months[int]
        
        
    def limitTextSize(self, size, text):
        # Restricts the amount of characters of a text
        if len(text) > size:
            i = size
            while text[i] != " ":
                i += 1              
            return text[:i]+'...'
        else:
            return text
        
        
    def envia_email(self, msg, assunto, mail_para):
        """Retirado do LiberiunNews

        Parte do codigo retirado de:
            - http://dev.plone.org/collective/browser/ATContentTypes/branches/release-1_0-branch/lib/imagetransform.py?rev=10162
            - http://www.thescripts.com/forum/thread22918.html
            - http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/473810

        """

        urltool = getToolByName(self, 'portal_url')
        portal = urltool.getPortalObject()

        # Cria a mensagem raiz, configurando os campos necessarios para envio da mensagem.
        mensagem = MIMEMultipart('related')
        mensagem['Subject'] = assunto

        #Pega os remetentes do email pelas configurações do zope @@mail-controlpanel
        mensagem['From'] = '%s <%s>' % (portal.getProperty('email_from_name'),
                                        portal.getProperty('email_from_address'))
        mensagem['To'] = mail_para
        mensagem.preamble = 'This is a multi-part message in MIME format.'
        mensagem.attach(MIMEText(msg, 'html', 'utf-8'))
        mail_de = mensagem['From']

        #Pegando SmtpHost Padrão do Plone
        smtp_host   = self.context.MailHost.smtp_host
        smtp_port   = self.context.MailHost.smtp_port
        smtp_userid = self.context.MailHost.smtp_userid
        smtp_pass   = self.context.MailHost.smtp_pass
        server_all  = '%s:%s'%(smtp_host,smtp_port)
        
        smtp = smtplib.SMTP()
        try:
            smtp.connect(server_all)
            #Caso o Usuario e Senha estejam preenchdos faz o login
            if smtp_userid and smtp_pass:
                smtp.login(smtp_userid, smtp_pass)
            smtp.sendmail(mail_de, mail_para, mensagem.as_string())
            smtp.quit()
        except:
            return False

        return True    