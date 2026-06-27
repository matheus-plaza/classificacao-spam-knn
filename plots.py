import matplotlib.pyplot as plt

k_values = [1, 3, 5, 7, 9]

acc_base = [88.7762, 88.6314, 89.6452, 88.9211, 89.5728]
acc_noise_5 = [82.2592, 86.9660, 87.7625, 87.1108, 87.3280]
acc_noise_10 = [80.3041, 85.1557, 86.0246, 85.5902, 86.4591]
acc_noise_20 = [72.4113, 77.5525, 80.3765, 81.8972, 82.3316]



# FUNÇÃO PARA GERAR GRÁFICOS INDIVIDUAIS
def plot_individual(k_vals, acc_vals, title, filename, color):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(k_vals, acc_vals, marker='o', linestyle='-', color=color)

    ax.set_title(title)
    ax.set_xlabel('Número de Vizinhos (K)')
    ax.set_ylabel('Acurácia (%)')
    ax.set_xticks(k_vals)
    ax.grid(True, linestyle='--', alpha=0.7)

    # Adicionando os valores em cima de cada ponto
    for i, v in enumerate(acc_vals):
        ax.text(k_vals[i], v + 0.2, f"{v:.2f}%", ha='center', va='bottom', fontsize=9)

    # Ajustando o eixo Y para os rótulos não cortarem
    ax.set_ylim(min(acc_vals) - 2, max(acc_vals) + 2)

    fig.tight_layout()
    plt.savefig(filename)
    plt.close('all')

# 4 GRÁFICOS INDIVIDUAIS

plot_individual(k_values, acc_base, 'Desempenho do Modelo Base (Sem Ruído)', 'grafico_indiv_base.png', 'blue')
plot_individual(k_values, acc_noise_5, 'Desempenho do Modelo com Ruído de 5%', 'grafico_indiv_ruido_5.png', 'green')
plot_individual(k_values, acc_noise_10, 'Desempenho do Modelo com Ruído de 10%', 'grafico_indiv_ruido_10.png', 'orange')
plot_individual(k_values, acc_noise_20, 'Desempenho do Modelo com Ruído de 20%', 'grafico_indiv_ruido_20.png', 'red')

# GRÁFICO COMPARATIVO GERAL

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(k_values, acc_base, marker='o', linestyle='-', color='black', label='Sem Ruído')
ax.plot(k_values, acc_noise_5, marker='s', linestyle='-', color='green', label='Ruído 5%')
ax.plot(k_values, acc_noise_10, marker='^', linestyle='-', color='orange', label='Ruído 10%')
ax.plot(k_values, acc_noise_20, marker='D', linestyle='-', color='red', label='Ruído 20%')

ax.set_title('Comparativo de Acurácia: Todos os Cenários de Treino')
ax.set_xlabel('Número de Vizinhos (K)')
ax.set_ylabel('Acurácia (%)')
ax.set_xticks(k_values)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()
fig.tight_layout()
plt.savefig('grafico_comparativo_geral.png')
plt.close('all')

# GRÁFICO DE DEGRADAÇÃO (K=1 VS K=9)

noise_levels = [0, 5, 10, 20]
acc_k1 = [acc_base[0], acc_noise_5[0], acc_noise_10[0], acc_noise_20[0]]
acc_k9 = [acc_base[4], acc_noise_5[4], acc_noise_10[4], acc_noise_20[4]]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(noise_levels, acc_k1, marker='o', linestyle='--', color='red', label='k = 1 (Alta Sensibilidade)')
ax.plot(noise_levels, acc_k9, marker='s', linestyle='-', color='blue', label='k = 9 (Maior Suavização)')

ax.set_title('Queda de Acurácia: K=1 vs K=9 ao Aumentar o Ruído')
ax.set_xlabel('Nível de Ruído Injetado (%)')
ax.set_ylabel('Acurácia (%)')
ax.set_xticks(noise_levels)
ax.grid(True, linestyle='--', alpha=0.7)

for i, v in enumerate(acc_k1):
    ax.text(noise_levels[i], v - 1.2, f"{v:.1f}%", ha='center', va='top', fontsize=9, color='red')
for i, v in enumerate(acc_k9):
    ax.text(noise_levels[i], v + 0.5, f"{v:.1f}%", ha='center', va='bottom', fontsize=9, color='blue')

ax.legend()
fig.tight_layout()
plt.savefig('grafico_degradacao_ruido.png')
plt.close('all')

print("Todos os 6 gráficos foram gerados com sucesso na pasta atual!")