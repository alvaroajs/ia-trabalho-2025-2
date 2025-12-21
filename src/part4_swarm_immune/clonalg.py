import numpy as np
import matplotlib.pyplot as plt

# ================= 1. CONFIGURAÇÃO DO CENÁRIO =================
NUM_ANTENAS = 10
RAIO_COBERTURA = 30
AREA_SIZE = 100
NUM_CLIENTES = 80


# Restrições de Borda (Margem de Segurança)
MARGEM = 10
LIMITE_MIN = MARGEM
LIMITE_MAX = AREA_SIZE - MARGEM

# Geração de Clientes Aleatórios (Sem seed fixa = Novos dados sempre)
clientes = np.random.rand(NUM_CLIENTES, 2) * AREA_SIZE

# ================= 2. FUNÇÃO DE AFINIDADE (FITNESS) =================
def calcular_afinidade(anticorpo_flat):
    antenas = anticorpo_flat.reshape(-1, 2)
    cobertos = 0
    for cx, cy in clientes:
        dists = np.sqrt(np.sum((antenas - np.array([cx, cy]))**2, axis=1))
        if np.min(dists) <= RAIO_COBERTURA:
            cobertos += 1
    return cobertos / NUM_CLIENTES

# ================= 3. ALGORITMO CLONALG =================
class Clonalg:
    def __init__(self, n_populacao=40, iteracoes=100):
        self.n_pop = n_populacao
        self.iteracoes = iteracoes
        self.dim = NUM_ANTENAS * 2 
        
        # Parâmetros Específicos do CLONALG
        self.n_select = 10       # Quantos melhores serão clonados
        self.fator_clones = 0.5  # Multiplicador para quantidade de clones
        self.rho = 2.0           # Taxa base de mutação (raio da perturbação)
        self.n_random = 5        # Inserção de novos aleatórios (Receptor Editing)

    def executar(self):
        # 1. Inicialização (com restrição de margem)
        populacao = np.random.uniform(LIMITE_MIN, LIMITE_MAX, (self.n_pop, self.dim))
        
        history = []
        melhor_solucao_global = None
        melhor_fitness_global = 0

        for it in range(self.iteracoes):
            # Avaliar Afinidade
            fitness = np.array([calcular_afinidade(ind) for ind in populacao])
            
            # Ordenar (do melhor para o pior)
            indices_ordenados = np.argsort(fitness)[::-1]
            populacao = populacao[indices_ordenados]
            fitness = fitness[indices_ordenados]
            
            # Atualizar Melhor Global
            if fitness[0] > melhor_fitness_global:
                melhor_fitness_global = fitness[0]
                melhor_solucao_global = populacao[0].copy()
            
            history.append(melhor_fitness_global)
            
            # 2. Seleção e Clonagem
            # Seleciona os 'n_select' melhores para clonar
            clones = []
            fitness_clones_pai = [] # Para calcular taxa de mutação
            
            for i in range(self.n_select):
                # Quantidade de clones proporcional ao rank (melhores clonam mais)
                qtd_clones = int(self.fator_clones * self.n_pop / (i + 1)) + 1
                
                # Criar clones do individuo i
                for _ in range(qtd_clones):
                    clones.append(populacao[i].copy())
                    fitness_clones_pai.append(fitness[i])
            
            clones = np.array(clones)
            fitness_clones_pai = np.array(fitness_clones_pai)

            # 3. Hipermutação (Maturação de Afinidade)
            # A mutação é inversamente proporcional à qualidade (fitness)
            # Fitness alto (perto de 1.0) -> exp(-fit) pequeno -> pouca mutação
            # Fitness baixo -> muita mutação
            
            # Normalizar fitness para evitar log(0) ou exp extremos
            # Fator de decaimento exponencial
            fator_mutacao = np.exp(-5.0 * fitness_clones_pai) # O 5.0 ajusta a curva de decaimento
            
            noise = np.random.randn(*clones.shape)
            # Aplica mutação: Ruído * Taxa Base * Fator Específico
            clones += noise * self.rho * fator_mutacao[:, np.newaxis] * 10 
            
            # IMPORTANTE: Aplicar restrições de borda nos clones mutados
            clones = np.clip(clones, LIMITE_MIN, LIMITE_MAX)
            
            # 4. Seleção dos Sobreviventes (Reselection)
            # Avaliar os clones mutados
            fit_clones = np.array([calcular_afinidade(c) for c in clones])
            
            # Combinar população original + clones mutados
            pop_total = np.vstack((populacao, clones))
            fit_total = np.concatenate((fitness, fit_clones))
            
            # Ordenar todos e pegar os melhores para manter o tamanho da população
            indices_total = np.argsort(fit_total)[::-1]
            populacao = pop_total[indices_total[:self.n_pop]]
            
            # 5. Receptor Editing (Diversidade)
            # Substituir os piores indivíduos por novos aleatórios para evitar estagnação
            # (Exceto se a população for muito pequena)
            if self.n_random > 0:
                novos = np.random.uniform(LIMITE_MIN, LIMITE_MAX, (self.n_random, self.dim))
                # Substitui os últimos 'n_random' indivíduos (os piores, pois está ordenado)
                populacao[-self.n_random:] = novos

        return melhor_solucao_global, melhor_fitness_global, history

# ================= EXECUÇÃO =================
print("Rodando CLONALG (Sist. Imune)...")
clonalg = Clonalg(n_populacao=40, iteracoes=100)
best_pos, best_fit, hist = clonalg.executar()

print(f"Melhor Cobertura: {best_fit:.2%}")

# ================= PLOTAGEM =================
coords = best_pos.reshape(-1, 2)
fig, ax = plt.subplots(figsize=(8, 8))

# Configurar Área e Margem
ax.set_xlim(0, AREA_SIZE)
ax.set_ylim(0, AREA_SIZE)

# Desenhar Margem
rect = plt.Rectangle((MARGEM, MARGEM), AREA_SIZE - 2*MARGEM, AREA_SIZE - 2*MARGEM, 
                     linewidth=1, edgecolor='purple', facecolor='none', linestyle='--', label='Área Permitida')
ax.add_patch(rect)

# Clientes
ax.scatter(clientes[:,0], clientes[:,1], c='red', s=30, label='Clientes')

# Antenas
for i, (x, y) in enumerate(coords):
    circle = plt.Circle((x, y), RAIO_COBERTURA, color='purple', alpha=0.2)
    ax.add_patch(circle)
    ax.scatter(x, y, c='purple', marker='D', s=80, edgecolor='black') # Marcador diferente do PSO
    ax.text(x, y+2, f"A{i+1}", color='purple', fontweight='bold')

plt.title(f"CLONALG: 5 Antenas (Cob: {best_fit:.2%})")
plt.legend(loc='upper right')
plt.savefig("clonalg_antennas.png")
print("Gráfico salvo como 'clonalg_antennas.png'")