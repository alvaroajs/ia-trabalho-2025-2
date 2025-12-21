import numpy as np
import matplotlib.pyplot as plt
from ga import GA

# --- CONFIGURAÇÕES ---
N_CLIENTES = 80        # Quantidade de clientes
N_ANTENAS_MAX = 10     # Máximo de antenas permitidas
RAIO_LIMITE = 100.0    # Raio do campo de operação
ALCANCE_ANTENA = 30.0  # Raio de sinal de cada antena
# ---------------------

# Geração de clientes aleatórios dentro do raio circular
def gerar_clientes(n, raio):
    clientes = []
    while len(clientes) < n:
        x, y = np.random.uniform(-raio, raio, 2)
        if np.sqrt(x**2 + y**2) <= raio:
            clientes.append([x, y])
    return np.array(clientes)

clientes = gerar_clientes(N_CLIENTES, RAIO_LIMITE)

def fitness_cobertura(individuo):
    antenas = individuo.reshape(-1, 3)
    ativas = antenas[antenas[:, 2] > 0.5] # Status > 0.5 = ativa
    
    if len(ativas) == 0: return -1000
    
    cobertos = 0
    for c in clientes:
        # Verifica se o cliente está no raio de qualquer antena ativa
        dists = np.sqrt(np.sum((ativas[:, :2] - c)**2, axis=1))
        if np.any(dists <= ALCANCE_ANTENA):
            cobertos += 1
            
    # Penalidade por antenas fora do raio limite
    fora = np.sum(np.sqrt(np.sum(ativas[:, :2]**2, axis=1)) > RAIO_LIMITE)
    
    # Fitness prioriza cobertura, penaliza excesso de antenas e posições inválidas
    return cobertos - (len(ativas) * 0.5) - (fora * 50)

def criar_individuo():
    return np.random.uniform(-RAIO_LIMITE, RAIO_LIMITE, N_ANTENAS_MAX * 3)

def plotar_resultado(melhor_ind, score):
    import os
    antenas = melhor_ind.reshape(-1, 3)
    ativas = antenas[antenas[:, 2] > 0.5]
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Desenhar limite do terreno
    circ_limite = plt.Circle((0, 0), RAIO_LIMITE, color='black', fill=False, linestyle='--', alpha=0.3)
    ax.add_patch(circ_limite)
    
    # Plotar clientes
    ax.scatter(clientes[:, 0], clientes[:, 1], c='blue', s=10, label='Clientes', alpha=0.6)
    
    # Plotar antenas e raios de cobertura
    for i, a in enumerate(ativas):
        # Círculo de cobertura
        cobertura = plt.Circle((a[0], a[1]), ALCANCE_ANTENA, color='green', alpha=0.2)
        ax.add_patch(cobertura)
        # Ponto da antena
        ax.scatter(a[0], a[1], c='red', marker='^', s=100, label='Antena' if i == 0 else "")

    plt.title(f"Distribuição de Antenas\nClientes Cobertos: {int(score)} de {len(clientes)}")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    # Salvar gráfico em arquivo
    output_path = os.path.join(os.path.dirname(__file__), 'distribuicao_antenas.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Gráfico salvo em: {output_path}")
    plt.close()

if __name__ == "__main__":
    ag = GA(pop_size=100, cx_rate=0.8, mut_rate=0.2, 
            fitness_fn=fitness_cobertura, create_ind=criar_individuo, max_iters=1000)
    
    print("Otimizando distribuição...")
    melhor, score = ag.run()
    
    print(f"Resultado Final: {int(score)} clientes cobertos.")
    plotar_resultado(melhor, score)