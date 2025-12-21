.PHONY: setup part1 part2 part3 part4 clean

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

part1:
	python3 src/part1_tree_manual/tree_manual.py

part2:
	python3 src/part2_ml/train_knn.py && \
	python3 src/part2_ml/svm.py && \
	python3 src/part2_ml/desicion_tree.py

part3:
	python3 src/part3_ga/run_ga.py

part4:
	python3 src/part4_swarm_immune/pso.py && \
	python3 src/part4_swarm_immune/clonalg.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	rm -f src/part2_ml/*.model
