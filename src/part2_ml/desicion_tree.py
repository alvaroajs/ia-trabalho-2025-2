import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import cross_val_score, train_test_split, StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report


df = pd.read_csv("../../data/heart.csv")


X = df[['Age', 'RestingBP', 'Cholesterol']].values
y = df['HeartDisease'].values


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)


depths = list(range(1, 16))
scores = []
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for d in depths:
    clf = DecisionTreeClassifier(max_depth=d, random_state=42, criterion='entropy')
    score = cross_val_score(clf, X_train, y_train, cv=cv).mean()
    scores.append(score)

best_depth = depths[int(np.argmax(scores))]


plt.figure(figsize=(10, 6))
plt.plot(depths, scores, marker='o')
plt.xlabel("Max Depth")
plt.ylabel("Acurácia (CV)")
plt.title("Acurácia da Árvore de Decisão por Profundidade")
plt.xticks(depths)
plt.grid(True)
plt.savefig("tree_depth_analysis.png")
plt.close() 


tree_model = DecisionTreeClassifier(max_depth=best_depth, random_state=42, criterion='entropy')
tree_model.fit(X_train, y_train)


plt.figure(figsize=(20, 10))
plot_tree(tree_model, 
          feature_names=['Age', 'RestingBP', 'Cholesterol'], 
          class_names=['Normal', 'HeartDisease'], 
          filled=True, 
          rounded=True,
          fontsize=10)
plt.title(f"Árvore de Decisão (Profundidade {best_depth})")
plt.savefig("tree_structure.png")
plt.close()


y_pred = tree_model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='binary', zero_division=0)
recall = recall_score(y_test, y_pred, average='binary', zero_division=0)

print(f"Acurácia:  {accuracy:.2f}")
print(f"Precisão:  {precision:.2f}")
print(f"Recall:    {recall:.2f}")
print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred, zero_division=0))