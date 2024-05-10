import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from django.core.validators import validate_email
from myauth.models import *
from django.contrib.auth.models import User

while((email := input()) != 'exit'):    

    if validate_email(email):
        print(f'Email {email} inválido')
        continue
    
    if User.objects.filter(email=email).exists() or SignUpCode.objects.filter(email=email).exists():
        print(f'Usuário com email {email} já cadastrado')
        continue
    SignUpCode.objects.create(email=email)
    print(f'Email {email} cadastrado com sucesso')