import re

texto = "Olá meus senhores obrigado por assinar. Agora entre em contato com: andre.travessa@gmail.com ou jornelio.marquinha@gmail.com ou se preferir: vasefuder.vcmsm_paspalho@uol.com.br"

regex = re.compile(r'[a-z\._]+@[a-z]+\.[a-z]+\.?[a-z]+')

mo = regex.findall(texto)

print(mo)
