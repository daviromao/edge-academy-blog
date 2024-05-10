from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.db import models

class SignUpCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Código de Cadastro'
        verbose_name_plural = 'Códigos de Cadastro'
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        codigo = get_random_string(length=20)
        self.code = codigo
        super(SignUpCode, self).save(*args, **kwargs)
        
        message = f"Olá! Você foi convidado a se registrar no nosso site. Para se registrar, acesse o link: http://localhost:8000/register/?code={codigo}"
        
        send_mail('Convite para se registrar no nosso site',
                message,
                'seu_email@gmail.com',
                [self.email])

    def __str__(self):
        return self.email