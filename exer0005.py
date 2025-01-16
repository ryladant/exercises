import re
import pandas as pd

texto = "O documento é confidencial. Não compartilhe a senha ou o segredo."

mo = re.compile(r'\bsenha|segredo|confidencial\b')

texto_novo = re.sub(mo, "***", texto)

print(texto_novo)
