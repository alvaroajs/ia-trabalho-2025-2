# Documentação do Trabalho 02 - Inteligência Artificial (2025.2)

## Sumário Executivo

Este trabalho implementa diferentes técnicas de Inteligência Artificial para resolução de problemas reais. O projeto está organizado em 4 partes principais, cada uma explorando um paradigma ou algoritmo específico da IA. O conjunto de dados utilizado é o **Heart Disease Dataset**, contendo informações médicas para classificação de doenças cardíacas.

---

## 1. Estrutura do Projeto

```
ia-trabalho-2025-2/
├── data/
│   └── heart.csv                 # Dataset de doenças cardíacas
├── src/
│   ├── part1_tree_manual/        # Árvore de decisão manual (Glasgow Scale)
│   ├── part2_ml/                 # Algoritmos de Machine Learning
│   ├── part3_ga/                 # Algoritmo Genético
│   └── part4_swarm_immune/       # Algoritmos de Enxame/Imunológicos
├── notebook/                     # Notebooks Jupyter (documentação interativa)
└── DOCUMENTACAO_TRABALHO.md     # Este arquivo
```

---

## 2. Part 1: Árvore de Decisão Manual - Escala de Glasgow

### Objetivo
Implementar manualmente uma árvore de decisão para avaliar o nível de traumatismo craniano de um paciente utilizando a **Escala de Coma de Glasgow (GCS)**.

### Arquivo: `src/part1_tree_manual/tree_manual.py`

### Descrição Técnica

A Escala de Glasgow é uma ferramenta clínica que avalia três componentes neurológicos:

1. **Abertura Ocular (1-4 pontos)**
   - 4 pontos: Abre espontaneamente
   - 3 pontos: Abre ao comando verbal
   - 2 pontos: Abre à pressão/dor
   - 1 ponto: Ausente

2. **Resposta Verbal (1-5 pontos)**
   - 5 pontos: Orientado e conversa
   - 4 pontos: Conversa confusa
   - 3 pontos: Palavras inapropriadas
   - 2 pontos: Sons ininteligíveis
   - 1 ponto: Ausente

3. **Resposta Motora (1-6 pontos)**
   - 6 pontos: Obedece a comandos
   - 5 pontos: Localiza estímulo doloroso
   - 4 pontos: Flexão normal (retirada)
   - 3 pontos: Flexão anormal (decorticação)
   - 2 pontos: Extensão anormal (descerebração)
   - 1 ponto: Ausente

### Classificação Final
- **13-15 pontos**: Trauma Leve (verde)
- **9-12 pontos**: Trauma Moderado (amarelo)
- **3-8 pontos**: Trauma Grave (vermelho) - Considerar Intubação

### Funções Principais

- `perguntar_sim_nao(pergunta)`: Interface interativa para coleta de respostas
- `avaliar_ocular()`: Avalia componente ocular
- `avaliar_verbal()`: Avalia componente verbal
- `avaliar_motora()`: Avalia componente motor
- `main()`: Orquestra a avaliação completa e exibe resultado com código de cores

### Fluxo de Execução

```
Início
  ↓
Avaliação Ocular → Coleta 1-4 pontos
  ↓
Avaliação Verbal → Coleta 1-5 pontos
  ↓
Avaliação Motora → Coleta 1-6 pontos
  ↓
Soma: Total (3-15 pontos)
  ↓
Classificação: Leve/Moderado/Grave
```

### Como Usar

```bash
cd src/part1_tree_manual
python tree_manual.py
```

Responda às perguntas com "s" ou "n" conforme as condições clínicas do paciente.

### Arquivo Relacionado
- `tree_diagram.md`: Diagrama Mermaid da árvore de decisão

---

## 2. Part 2: Algoritmos de Machine Learning

### Objetivo
Implementar e comparar três algoritmos clássicos de Machine Learning para classificação de doenças cardíacas.

### 2.1 Árvore de Decisão com Scikit-learn

**Arquivo**: `src/part2_ml/desicion_tree.py`

#### Descrição
Implementa uma Árvore de Decisão utilizando a biblioteca Scikit-learn para classificação binária do dataset de doenças cardíacas.

#### Features Utilizadas
- Age (Idade)
- RestingBP (Pressão Arterial em Repouso)
- Cholesterol (Colesterol)

#### Processo

1. **Carregamento de Dados**
   ```python
   df = pd.read_csv("../../data/heart.csv")
   X = df[['Age', 'RestingBP', 'Cholesterol']].values
   y = df['HeartDisease'].values
   ```

2. **Divisão Train/Test**
   - 80% treino, 20% teste
   - Estratificação: mantém proporção de classes
   - Random state: 42 (reproducibilidade)

3. **Busca de Hiperparâmetro Ótimo**
   - Testeando profundidades de 1 a 15
   - Validação Cruzada: StratifiedKFold (5 splits)
   - Critério: Entropia
   - Métrica: Acurácia média

4. **Treinamento e Avaliação**
   - Métricas: Acurácia, Precisão, Recall
   - Relatório de classificação completo
   - Visualizações salvas:
     - `tree_depth_analysis.png`: Gráfico da acurácia por profundidade
     - `tree_structure.png`: Árvore de decisão final

#### Saída Esperada
```
Acurácia:  XX.XX
Precisão:  XX.XX
Recall:    XX.XX
```

---

### 2.2 K-Nearest Neighbors (KNN)

**Arquivo**: `src/part2_ml/train_knn.py`

#### Descrição
Implementa o algoritmo KNN com seleção automática do melhor valor de k através de validação cruzada.

#### Features Utilizadas
- Age (Idade)
- RestingBP (Pressão Arterial em Repouso)
- Cholesterol (Colesterol)

#### Processo

1. **Carregamento e Pré-processamento**
   ```python
   X = df[['Age', 'RestingBP', 'Cholesterol']].values
   y = df['HeartDisease'].values
   ```

2. **Pipeline de Processamento**
   - Normalização: StandardScaler
   - Algoritmo: KNeighborsClassifier
   - Protege contra data leakage usando pipeline

3. **Seleção de k Ótimo**
   - Range: k de 1 a 30
   - Validação Cruzada: StratifiedKFold (5 splits)
   - Método: Encontra k com maior acurácia média

4. **Treinamento Final**
   - Escalonamento dos dados
   - Treinamento com k ótimo
   - Avaliação no conjunto de teste

#### Saída Esperada
```
Melhor k (CV no treino): XX
Acurácia:  XX.XX
Precisão:  XX.XX (binary)
Recall:    XX.XX (binary)
```

#### Diagrama de Fluxo
```
Dataset → Divisão Train/Test
   ↓
Normalização (StandardScaler)
   ↓
Busca de k ótimo (Validação Cruzada 1-30)
   ↓
Treinamento com k ótimo
   ↓
Predição no conjunto teste
   ↓
Cálculo de métricas
```

---

### 2.3 Support Vector Machine (SVM)

**Arquivo**: `src/part2_ml/svm.py`

#### Descrição
Implementa SVM com redução de dimensionalidade utilizando PCA para classificação de doenças cardíacas.

#### Features Utilizadas
- Age (Idade)
- RestingBP (Pressão Arterial em Repouso)
- Cholesterol (Colesterol)

#### Processo

1. **Carregamento e Normalização**
   - StandardScaler: Padroniza os dados (essencial para SVM e PCA)
   - Split: 75% treino, 25% teste
   - Random state: 42

2. **Redução de Dimensionalidade**
   ```python
   pca = PCA(n_components=3)
   X_train_pca = pca.fit_transform(X_train)
   X_test_pca = pca.transform(X_test)
   ```
   - Mantém 3 componentes principais
   - Reduz ruído e tempo de processamento

3. **Treinamento do SVM**
   - Kernel 1: Polinomial (treinamento inicial)
   - Kernel 2: RBF com gamma='scale' (validação cruzada)

4. **Avaliação e Persistência**
   - Acurácia no conjunto teste
   - Salva modelo em `svm.model` (Pickle)
   - Validação cruzada com 5 folds
   - Comparação: SVM simples vs. SVM com CV

#### Saída Esperada
```
Acurácia: XX.XX
Cross-validation scores: [...]
Mean cross-validation score: XX.XX
Acurácia com cross-validation: XX.XX
```

#### Técnicas Aplicadas
- **Padronização**: Crítica para SVM (distância sensível)
- **PCA**: Redução de dimensionalidade e visualização
- **Persistência**: Salva modelo treinado para reuso
- **Validação Cruzada**: Evita overfitting

---

## 3. Part 3: Algoritmo Genético

### Objetivo
Implementar um Algoritmo Genético (GA) genérico e aplicá-lo ao problema de otimização de cobertura de rede de antenas.

### 3.1 Módulo GA Genérico

**Arquivo**: `src/part3_ga/ga.py`

#### Descrição
Implementa a classe `GA` que encapsula os operadores genéticos para resolução de problemas de otimização contínua.

#### Componentes Principais

1. **Inicialização**
   ```python
   GA(pop_size, cx_rate, mut_rate, fitness_fn, create_ind, max_iters, seed)
   ```
   - `pop_size`: Tamanho da população
   - `cx_rate`: Taxa de cruzamento [0,1]
   - `mut_rate`: Taxa de mutação [0,1]
   - `fitness_fn`: Função de avaliação
   - `create_ind`: Função geradora de indivíduos
   - `seed`: Reproducibilidade

2. **Operador de Seleção**
   ```python
   def select(self, k=2)
   ```
   - Método: Seleção por Torneio
   - Seleção determinística: k indivíduos aleatórios
   - Retorna o melhor entre k candidatos

3. **Operador de Cruzamento**
   ```python
   def crossover(self, p1, p2)
   ```
   - Tipo: Cruzamento Aritmético
   - Fórmula:
     - c₁ = α·p₁ + (1-α)·p₂
     - c₂ = (1-α)·p₁ + α·p₂
   - Parâmetro α: Uniforme em [0,1]

4. **Operador de Mutação**
   ```python
   def mutate(self, ind)
   ```
   - Tipo: Mutação Gaussiana
   - Fórmula: ind' = ind + N(0, σ²)
   - Desvio padrão: σ = 5.0

5. **Evolução por Geração**
   ```python
   def step(self)
   ```
   - Loop de reprodução:
     1. Seleciona dois pais
     2. Copia pais para descendentes
     3. Aplica cruzamento com probabilidade `cx_rate`
     4. Aplica mutação com probabilidade `mut_rate` (em cada filho)
     5. Mantém população em tamanho fixo

6. **Execução Principal**
   ```python
   def run(self)
   ```
   - Executa `max_iters` gerações
   - Rastreia melhor indivíduo encontrado
   - Retorna (melhor_indivíduo, fitness_value)

#### Pseudocódigo do Algoritmo
```
1. Inicializar população aleatória
2. ENQUANTO não convergiu OU max_iters não atingido:
   a. Selecionar pai 1 e pai 2
   b. Copiar para descendentes
   c. SE random < cx_rate: Cruzar
   d. SE random < mut_rate: Mutar filho 1
   e. SE random < mut_rate: Mutar filho 2
   f. Adicionar à nova população
   g. Substituir população antiga
3. Retornar melhor indivíduo
```

---

### 3.2 Aplicação: Otimização de Cobertura de Rede de Antenas

**Arquivo**: `src/part3_ga/run_ga.py`

#### Problema
Otimizar a distribuição de antenas em uma área circular para maximizar cobertura de clientes minimizando o número de antenas.

#### Configurações
```python
N_CLIENTES = 60              # Quantidade de clientes
N_ANTENAS_MAX = 6            # Máximo de antenas
RAIO_LIMITE = 50.0           # Raio do terreno
ALCANCE_ANTENA = 15.0        # Raio de cobertura de cada antena
```

#### Representação do Indivíduo
```python
individuo = [x₁, y₁, status₁, x₂, y₂, status₂, ..., x₆, y₆, status₆]
            └─────────────────────────────────────────────────────┘
                    6 antenas × 3 parâmetros = 18 valores
```
- `xᵢ, yᵢ`: Coordenadas da antena i
- `statusᵢ`: Ativação (0-1), > 0.5 = ativa

#### Função de Fitness
```python
def fitness_cobertura(individuo):
    antenas_ativas = filtrar_status > 0.5
    
    IF len(antenas_ativas) == 0: return -1000
    
    cobertos = contar_clientes_em_raio(antenas_ativas, ALCANCE_ANTENA)
    fora_raio = contar_antenas_fora_do_limite(antenas_ativas)
    
    RETURN cobertos - 0.5*len(antenas_ativas) - 50*fora_raio
```

**Componentes da Fitness:**
1. **Cobertura**: Número de clientes cobertos (maximize)
2. **Penalidade de Antenas**: -0.5 por antena ativa (minimize quantidade)
3. **Penalidade de Posição**: -50 por antena fora do limite (respeitar restrições)

#### Geração de Clientes
```python
def gerar_clientes(n, raio):
    # Gera n pontos aleatórios dentro do círculo de raio r
    # Método: Aceitação-rejeição (descarta pontos fora do círculo)
    RETURN lista_de_n_clientes
```

#### Visualização do Resultado
```python
def plotar_resultado(melhor_ind, score):
    # Círculo de limite do terreno
    # Scatter plot de clientes (azul)
    # Triângulos para antenas (vermelho)
    # Círculos de cobertura (verde semi-transparente)
    # Título com número de clientes cobertos
```

#### Como Executar
```bash
cd src/part3_ga
python run_ga.py
```

**Saída:**
- Número de clientes cobertos no resultado final
- Gráfico interativo mostrando:
  - Distribuição de clientes (pontos azuis)
  - Posições de antenas (triângulos vermelhos)
  - Raios de cobertura (círculos verdes)
  - Limite do terreno (linha tracejada preta)

#### Hiperparâmetros do GA (em run_ga.py)
```python
pop_size = 100        # População
cx_rate = 0.8         # 80% de cruzamentos
mut_rate = 0.2        # 20% de mutações
max_iters = 1000      # 1000 gerações
```

#### Considerações de Design
- **Representação**: Contínua (coordenadas e status)
- **Seleção**: Torneio de tamanho 2
- **Cruzamento**: Aritmético para melhor exploração contínua
- **Mutação**: Gaussiana para busca local
- **Convergência**: Rastreia melhor indivíduo global

---

## 4. Part 4: Algoritmos de Enxame e Imunológicos

### Diretório
`src/part4_swarm_immune/`

**Status**: Estrutura criada, implementação futura.

Este módulo será dedicado a:
- **Algoritmos de Enxame**: PSO (Particle Swarm Optimization), ACO (Ant Colony Optimization)
- **Algoritmos Imunológicos**: CLONALG, opt-aiNET

---

## 5. Dataset: Heart Disease

### Localização
`data/heart.csv`

### Descrição
Dataset público de doenças cardíacas contendo informações clínicas de pacientes.

### Features Utilizadas no Trabalho
| Feature | Descrição | Tipo |
|---------|-----------|------|
| Age | Idade do paciente | Inteiro (anos) |
| RestingBP | Pressão arterial em repouso | Inteiro (mmHg) |
| Cholesterol | Nível de colesterol | Inteiro (mg/dl) |
| HeartDisease | Presença de doença cardíaca (alvo) | Binário (0/1) |

### Pré-processamento
- Seleção de 3 features relevantes
- Normalização quando aplicável (KNN, SVM)
- Divisão estratificada train/test
- Sem tratamento de valores faltantes neste trabalho

---

## 6. Executando o Projeto

### Pré-requisitos
```bash
# Ambiente Python 3.8+
# Dependências:
pip install pandas numpy scikit-learn matplotlib
```

### Execução Individual

#### Part 1: Escala de Glasgow
```bash
cd src/part1_tree_manual
python tree_manual.py
```

#### Part 2: Machine Learning
```bash
# Árvore de Decisão
cd src/part2_ml
python desicion_tree.py

# KNN
python train_knn.py

# SVM
python svm.py
```

#### Part 3: Algoritmo Genético
```bash
cd src/part3_ga
python run_ga.py
```

---

## 7. Análise Comparativa dos Algoritmos

### Part 2: Comparação de Classifiers

| Aspecto | Decision Tree | KNN | SVM |
|---------|---------------|-----|-----|
| **Complexidade** | O(log n) | O(n) | O(n²) ou O(n³) |
| **Interpretabilidade** | Excelente | Baixa | Baixa |
| **Hiperparâmetros** | Profundidade | k | Kernel, C, γ |
| **Escalabilidade** | Alta | Média | Baixa |
| **Resistência Outliers** | Alta | Baixa | Alta |
| **Força** | Regras simples | Flexível | Teórico robusto |

### Part 3: Algoritmo Genético

**Vantagens:**
- Não requer gradientes
- Busca global (evita ótimos locais)
- Paralelizável naturalmente
- Aplicável a problemas discretos e contínuos

**Desvantagens:**
- Convergência pode ser lenta
- Necessita bom design de fitness
- Computacionalmente custoso para grandes populações

---

## 8. Técnicas Utilizadas

### Machine Learning
- ✅ Divisão Train/Test com estratificação
- ✅ Validação Cruzada (k-fold)
- ✅ Normalização de features (StandardScaler)
- ✅ PCA para redução de dimensionalidade
- ✅ Hyperparameter tuning

### Computational Intelligence
- ✅ Algoritmo Genético (seleção, cruzamento, mutação)
- ✅ Operadores de busca meta-heurística
- ✅ Representação contínua
- ✅ Fitness shaping e penalidades

### Software Engineering
- ✅ Separação de responsabilidades (GA genérico vs. aplicação)
- ✅ Reutilização de código
- ✅ Documentação inline
- ✅ Reproducibilidade (seeds fixas)

---

## 9. Resultados Esperados

### Part 1: Escala de Glasgow
- Interface interativa e intuitiva
- Saída colorida (ANSI codes)
- Classificação clínica precisa

### Part 2: Machine Learning
- **Decision Tree**: Acurácia ~75-85%
- **KNN**: Acurácia ~70-80% (sensível a normalização)
- **SVM**: Acurácia ~75-85% (melhor com PCA)

### Part 3: Algoritmo Genético
- Convergência em ~200-400 gerações
- Cobertura de ~45-55 clientes em 60 (75-90%)
- Distribuição otimizada de antenas

---

## 10. Estrutura de Código e Convenções

### Nomeação
- Variáveis: `snake_case`
- Funções: `snake_case`
- Classes: `PascalCase`
- Constantes: `UPPER_CASE`

### Modularização
- **Parte 1**: Script único (aplicação específica)
- **Parte 2**: Scripts independentes (cada algoritmo)
- **Parte 3**: Módulo genérico (ga.py) + aplicação (run_ga.py)

### Documentação
- Docstrings em português
- Comentários para lógica complexa
- Type hints onde relevante

---

## 11. Possíveis Extensões

### Part 1
- Validação contra escalas padrão
- Interface gráfica (tkinter/Qt)
- Histórico de avaliações

### Part 2
- Ensemble methods (Random Forest, Gradient Boosting)
- Balanced classes (SMOTE)
- Feature engineering avançado

### Part 3
- Evolução multi-objetivo (NSGA-II)
- Island models para paralelização
- Operadores adaptativos

### Part 4
- Implementação de PSO e ACO
- Algoritmos imunológicos completos
- Híbridos GA+PSO

---

## 12. Referências e Recursos

### Bibliotecas Utilizadas
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica
- **Scikit-learn**: Machine Learning
- **Matplotlib**: Visualização

### Conceitos Teóricos
- Escalas clínicas (Glasgow)
- Árvores de decisão (ID3, C4.5)
- KNN e algoritmos de distância
- SVM e kernels
- Algoritmos genéticos (Holland, 1975)
- Validação cruzada (Kfold stratificada)

---

## 13. Conclusão

Este trabalho demonstra a aplicação prática de técnicas de Inteligência Artificial em problemas reais, desde sistemas de apoio à decisão clínica até otimização de redes. A combinação de algoritmos clássicos (Machine Learning) com técnicas mais modernas (Computação Evolucionária) ilustra a diversidade de ferramentas disponíveis para diferentes tipos de problemas.

**Pontos-chave:**
1. ✅ Implementação correta de algoritmos fundamentais
2. ✅ Validação rigorosa com métricas apropriadas
3. ✅ Code reuse e modularização
4. ✅ Documentação clara e reproducibilidade
5. ✅ Aplicações práticas com dados reais

---

**Data de Conclusão**: Dezembro de 2025  
**Disciplina**: Inteligência Artificial  
**Semestre**: 2025.2  
**Autor**: [Seu Nome]

