
# Solucion item b

import pandas as pd

# Descargar y extraer archivo
!wget "https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/Cancer_Pulmon.zip" -O cancer.zip
!unzip -o cancer.zip

# Cargar dataset
df = pd.read_csv("Cancer_Pulmon.csv")
df.info()
