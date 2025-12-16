
# Solucion item d

import matplotlib.pyplot as plt

variables = ['age', 'bmi', 'cholesterol_level']

fig, ax = plt.subplots(1, 3, figsize=(18, 6))

for i, var in enumerate(variables):
    ax[i].boxplot(df[var], vert=True, patch_artist=True,
                  boxprops=dict(facecolor="skyblue", color="black"),
                  medianprops=dict(color="red", linewidth=2))
    ax[i].set_title(f'Boxplot de {var}')
    ax[i].set_ylabel(var)

plt.tight_layout()
plt.show()
