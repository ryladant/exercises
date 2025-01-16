import re
import pandas as pd

emails = [
    "usuario@gmail.com", "usuario@hotmail.co",
    "email_invalido@", "outro.email@dominio.org",
    "nao_valido@site@com"
]

regex = re.compile(r'[a-zA-Z0-9_\.-]+@[a-z0-9]+\.[a-z]+\.?[a-z]?')

valido = []

for email in emails:
    mo = regex.search(email)
    valido = valido + ["true" if mo else "false"]

data = {
    "email": emails,
    "valido": valido
}

df = pd.DataFrame(data)

print(df)
