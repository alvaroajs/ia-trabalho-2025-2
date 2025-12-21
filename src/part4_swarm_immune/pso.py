import numpy as np
import matplotlib.pyplot as plt

# ================= 1. CONFIGURAÇÃO DO CENÁRIO =================
NUM_ANTENAS = 10
RAIO_COBERTURA = 30
AREA_SIZE = 100
NUM_CLIENTES = 80


MARGEM = 10  
LIMITE_MIN = MARGEM
LIMITE_MAX = AREA_SIZE - MARGEM


clientes = np.random.rand(NUM_CLIENTES, 2) * AREA_SIZE

def calcular_fitness(posicoes_flat):
    antenas = posicoes_flat.reshape(-1, 2)
    cobertos = 0
    for cx, cy in clientes:
        dists = np.sqrt(np.sum((antenas - np.array([cx, cy]))**2, axis=1))
        if np.min(dists) <= RAIO_COBERTURA:
            cobertos += 1
    return cobertos / NUM_CLIENTES


class PSO:
    def __init__(self, n_particulas=30, iteracoes=50):
        self.n_particulas = n_particulas
        self.iteracoes = iteracoes
        self.dim = NUM_ANTENAS * 2 
        
        self.w = 0.7  
        self.c1 = 1.5 
        self.c2 = 1.5 

    def executar(self):
        
        X = np.random.uniform(LIMITE_MIN, LIMITE_MAX, (self.n_particulas, self.dim))
        
        V = np.random.randn(self.n_particulas, self.dim) * 0.1
        
        pbest_X = X.copy()
        pbest_score = np.array([calcular_fitness(x) for x in X])
        
        gbest_X = pbest_X[np.argmax(pbest_score)]
        gbest_score = np.max(pbest_score)
        
        history = []
        
        for i in range(self.iteracoes):
            r1 = np.random.rand(self.n_particulas, self.dim)
            r2 = np.random.rand(self.n_particulas, self.dim)
            
            V = (self.w * V) + (self.c1 * r1 * (pbest_X - X)) + (self.c2 * r2 * (gbest_X - X))
            
            X = X + V
             
            X = np.clip(X, LIMITE_MIN, LIMITE_MAX) 
            
            scores = np.array([calcular_fitness(x) for x in X])
            
            mask = scores > pbest_score
            pbest_X[mask] = X[mask]
            pbest_score[mask] = scores[mask]
            
            if np.max(scores) > gbest_score:
                gbest_score = np.max(scores)
                gbest_X = X[np.argmax(scores)].copy()
                
            history.append(gbest_score)
            
        return gbest_X, gbest_score, history

pso = PSO(n_particulas=40, iteracoes=100)
best_pos, best_fit, hist = pso.executar()

print(f"Melhor Cobertura: {best_fit:.2%}")

# ================= PLOTAGEM =================
coords = best_pos.reshape(-1, 2)
fig, ax = plt.subplots(figsize=(8, 8))


ax.set_xlim(0, AREA_SIZE)
ax.set_ylim(0, AREA_SIZE)


rect = plt.Rectangle((MARGEM, MARGEM), AREA_SIZE - 2*MARGEM, AREA_SIZE - 2*MARGEM, 
                     linewidth=1, edgecolor='red', facecolor='none', linestyle='--', label='Área Permitida')
ax.add_patch(rect)

# Clientes
ax.scatter(clientes[:,0], clientes[:,1], c='red', s=30, label='Clientes')

# Antenas
for i, (x, y) in enumerate(coords):
    # Círculo de cobertura
    circle = plt.Circle((x, y), RAIO_COBERTURA, color='green', alpha=0.2)
    ax.add_patch(circle)
    # Centro da antena
    ax.scatter(x, y, c='green', marker='X', s=100, edgecolor='black')
    ax.text(x, y+2, f"A{i+1}", color='green', fontweight='bold')

plt.title(f"Antenas com Margem de {MARGEM}m (Cob: {best_fit:.2%})")
plt.legend(loc='upper right')
plt.savefig("pso_dinamico.png")
print("Gráfico salvo como 'pso_dinamico.png'")