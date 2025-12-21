# Trabalho 02 - Inteligência Artificial (2025.2)

**CEFET-MG - Campus Divinópolis - Departamento de Computação**  
**Engenharia de Computação - 2025/2**  
**Disciplina:** Inteligência Artificial  
**Professor:** Tiago Alves de Oliveira

---

## 📋 Índice

1. [Sumário Executivo](#sumário-executivo)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Requisitos e Instalação](#requisitos-e-instalação)
4. [Como Executar](#como-executar)
5. [Descrição das Partes](#descrição-das-partes)
6. [Dataset](#dataset)
7. [Resultados](#resultados)
8. [Contribuidores](#contribuidores)

---

## 📝 Sumário Executivo

Este trabalho implementa diferentes técnicas de Inteligência Artificial para resolver problemas da vida real, incluindo:

- **Parte 1:** Árvore de Decisão Manual (Escala de Glasgow)
- **Parte 2:** Algoritmos de Machine Learning (KNN, SVM, Árvore de Decisão)
- **Parte 3:** Algoritmo Genético (Otimização)
- **Parte 4:** Algoritmos de Enxame e Imunológicos (PSO e CLONALG)

O conjunto de dados utilizado é o **Heart Disease Dataset**, contendo informações médicas para classificação de doenças cardíacas.

---

## 📁 Estrutura do Projeto

```
ia-trabalho-2025-2/
├── data/
│   └── heart.csv                        # Dataset de doenças cardíacas
├── src/
│   ├── common/                          # Funções compartilhadas
│   ├── part1_tree_manual/               # Árvore de decisão manual
│   │   ├── tree_diagram.md              # Diagrama da árvore
│   │   └── tree_manual.py               # Implementação
│   ├── part2_ml/                        # Machine Learning
│   │   ├── train_knn.py                 # KNN
│   │   ├── svm.py                       # SVM
│   │   ├── desicion_tree.py             # Árvore de Decisão
│   │   ├── svm.model                    # Modelo treinado
│   │   └── Results.txt                  # Resultados
│   ├── part3_ga/                        # Algoritmo Genético
│   │   ├── ga.py                        # Implementação GA
│   │   ├── run_ga.py                    # Execução
│   │   └── distribuicao_antenas.png     # Gráfico salvo
│   └── part4_swarm_immune/              # Enxame e Imunológico
│       ├── pso.py                       # PSO (Particle Swarm)
│       ├── clonalg.py                   # CLONALG (Algoritmo Clonal)
│       └── run_ga.py                    # Execução
├── notebook/                            # Notebooks Jupyter
├── requirements.txt                     # Dependências Python
├── Makefile                             # Atalhos de execução
├── run.sh                               # Script interativo
└── README.md                            # Este arquivo
```

---

## 🛠️ Requisitos e Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

#### Opção 1: Usando Make (Recomendado)

```bash
# Setup: criar ambiente virtual e instalar dependências
make setup

# Ativar ambiente virtual
source .venv/bin/activate
```

#### Opção 2: Manual

```bash
# Criar ambiente virtual
python3 -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Dependências

```
numpy
pandas
matplotlib
scikit-learn
scipy
seaborn
```

---

## ▶️ Como Executar

### Opção 1: Usando Make

```bash
# Executar Parte 1
make part1

# Executar Parte 2
make part2

# Executar Parte 3
make part3

# Executar Parte 4
make part4

# Limpar arquivos temporários
make clean
```

### Opção 2: Usando Shell Script

```bash
# Interface interativa
./run.sh

# Ou executar diretamente
./run.sh part1    # Parte 1
./run.sh part2    # Parte 2
./run.sh part3    # Parte 3
./run.sh part4    # Parte 4
./run.sh all      # Todas as partes
```

### Opção 3: Execução Manual

```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Executar scripts
python3 src/part1_tree_manual/tree_manual.py
python3 src/part2_ml/train_knn.py
python3 src/part2_ml/svm.py
python3 src/part2_ml/desicion_tree.py
python3 src/part3_ga/run_ga.py
python3 src/part4_swarm_immune/pso.py
python3 src/part4_swarm_immune/clonalg.py
```

---

## 📚 Descrição das Partes

### Parte 1: Árvore de Decisão Manual - Escala de Glasgow

**Arquivo**: `src/part1_tree_manual/tree_manual.py`

**Objetivo**: Implementar uma árvore de decisão interativa para avaliar o nível de traumatismo craniano usando a **Escala de Coma de Glasgow (GCS)**.

**Como Executar**:
```bash
make part1
```

---

### Parte 2: Algoritmos de Machine Learning

**Arquivos**:
- `src/part2_ml/desicion_tree.py` - Árvore de Decisão
- `src/part2_ml/train_knn.py` - KNN (K-Nearest Neighbors)
- `src/part2_ml/svm.py` - Support Vector Machine

**Objetivo**: Classificar doenças cardíacas usando 3 algoritmos clássicos de ML

**Features utilizadas**: Age, RestingBP, Cholesterol

**Como Executar**:
```bash
make part2
```

---

### Parte 3: Algoritmo Genético

**Arquivos**:
- `src/part3_ga/ga.py` - Implementação genérica do GA
- `src/part3_ga/run_ga.py` - Aplicação: Otimização de cobertura de rede de antenas

**Objetivo**: Otimizar distribuição de antenas em uma área circular

**Como Executar**:
```bash
make part3
```

**Saída**: Gráfico salvo em `src/part3_ga/distribuicao_antenas.png`

---

### Parte 4: Algoritmos de Enxame e Imunológicos

**Arquivos**:
- `src/part4_swarm_immune/pso.py` - PSO (Particle Swarm Optimization)
- `src/part4_swarm_immune/clonalg.py` - CLONALG (Algoritmo Clonal)

**Como Executar**:
```bash
make part4
```

---

## 📊 Dataset

**Arquivo**: `data/heart.csv`

Dataset de doenças cardíacas com informações clínicas de pacientes.

---

## 🧹 Limpeza

Remover arquivos temporários e cache:
```bash
make clean
```

---

## 📦 Variáveis de Ambiente

Nenhuma variável de ambiente é necessária para este projeto.

---

## ✅ Checklist de Implementação

- [x] Estrutura de pastas criada
- [x] requirements.txt com dependências
- [x] Makefile com atalhos
- [x] Script run.sh interativo
- [x] README.md documentado
- [x] Part 1: Árvore de Glasgow
- [x] Part 2: ML (KNN, SVM, Decision Tree)
- [x] Part 3: Algoritmo Genético
- [x] Part 4: PSO e CLONALG (estrutura)

---

## 📄 Análise Comparativa dos Algoritmos

### Part 2: Comparação de Classifiers

| Aspecto | Decision Tree | KNN | SVM |
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

