import re
import pandas as pd

telefones = "Meus contatos são: (11) 98888-7777, (11) 4321-1234 e (21) 99999-9999 ou também: (31)97528-8471"

mo = re.compile(r'\([0-9]{2}\)\s{0,1}9?[0-9]{4}-[0-9]{4}')

result = mo.findall(telefones)

print(result)
