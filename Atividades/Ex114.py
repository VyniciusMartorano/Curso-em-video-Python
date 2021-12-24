import urllib
import urllib.request
#Testar se o site esta acessivel pelo computador
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('ERRO!O site esta inacessivel!')
else:
    print('Consegui acessar o site :)')
    print(site.read())