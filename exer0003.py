import re
import pandas as pd

texto = "As reuniões aconteceram em 12/01/2023, 25/12/2021 e 01/01/2020."

mo = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')

result = mo.findall(texto)

print(result)
