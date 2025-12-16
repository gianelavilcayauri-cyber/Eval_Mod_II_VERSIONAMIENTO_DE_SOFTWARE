
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Cancer', fontsize=16, fontweight='bold')

# 1. Histograma de la edad
axs[0, 0].hist(df['age'], bins=5, color='skyblue', edgecolor='black', alpha=0.5)
axs[0, 0].set_title('Distribucion de la edad')
axs[0, 0].set_xlabel('Edad')
axs[0, 0].set_ylabel('Frecuencia')

# 2. Gráfico de pastel del género
gender_counts = df['gender'].value_counts()
axs[0, 1].pie(gender_counts.values,
              labels=gender_counts.index,
              autopct='%1.1f%%',
              startangle=90)
axs[0, 1].set_title('Distribucion del genero')
axs[0, 1].axis('equal')

# 3. Distribución de países en barras
country_counts = df['country'].value_counts()
axs[1, 0].bar(country_counts.index, country_counts.values, color='lightcoral')
axs[1, 0].set_title('Pacientes por pais')
axs[1, 0].set_ylabel('Numero de pacientes')
axs[1, 0].tick_params(axis='x', rotation=90)

# 4. Distribución de la etapa del cáncer
stage_counts = df['cancer_stage'].value_counts()
axs[1, 1].bar(stage_counts.index, stage_counts.values, color='lightgreen')
axs[1, 1].set_title('Distribucion de la etapa del cancer')
axs[1, 1].set_ylabel('Numero de observaciones')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
