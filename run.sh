#!/bin/bash

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' 

print_section() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

run_part() {
    local part=$1
    local script=$2
    
    print_section "Executando Parte $part"
    if python3 "$script"; then
        print_success "Parte $part concluída com sucesso"
    else
        print_error "Erro na execução da Parte $part"
        exit 1
    fi
}

show_menu() {
    echo ""
    echo -e "${YELLOW}Escolha qual parte executar:${NC}"
    echo "1) Parte 1 - Árvore de Decisão Manual"
    echo "2) Parte 2 - Algoritmos de Machine Learning (KNN, SVM, Árvore)"
    echo "3) Parte 3 - Algoritmo Genético"
    echo "4) Parte 4 - Algoritmos de Enxame e Imunológicos"
    echo "5) Executar todas as partes"
    echo "0) Sair"
    echo ""
}

setup_dependencies() {
    if [ ! -d ".venv" ]; then
        print_section "Configurando ambiente virtual"
        python3 -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        print_success "Ambiente configurado"
    else
        source .venv/bin/activate
    fi
}

main() {
    setup_dependencies
    
    if [ $# -eq 0 ]; then
        while true; do
            show_menu
            read -p "Digite sua escolha: " choice
            
            case $choice in
                1)
                    run_part "1" "src/part1_tree_manual/tree_manual.py"
                    ;;
                2)
                    print_section "Parte 2 - Machine Learning"
                    run_part "2.1" "src/part2_ml/train_knn.py"
                    run_part "2.2" "src/part2_ml/svm.py"
                    run_part "2.3" "src/part2_ml/desicion_tree.py"
                    ;;
                3)
                    run_part "3" "src/part3_ga/run_ga.py"
                    ;;
                4)
                    print_section "Parte 4 - Enxame e Imunológico"
                    run_part "4.1" "src/part4_swarm_immune/pso.py"
                    run_part "4.2" "src/part4_swarm_immune/clonalg.py"
                    ;;
                5)
                    print_section "Executando todas as partes"
                    run_part "1" "src/part1_tree_manual/tree_manual.py"
                    run_part "2.1" "src/part2_ml/train_knn.py"
                    run_part "2.2" "src/part2_ml/svm.py"
                    run_part "2.3" "src/part2_ml/desicion_tree.py"
                    run_part "3" "src/part3_ga/run_ga.py"
                    run_part "4.1" "src/part4_swarm_immune/pso.py"
                    run_part "4.2" "src/part4_swarm_immune/clonalg.py"
                    print_success "Todas as partes executadas com sucesso!"
                    ;;
                0)
                    echo "Saindo..."
                    exit 0
                    ;;
                *)
                    print_error "Opção inválida"
                    ;;
            esac
        done
    else
        case $1 in
            part1)
                run_part "1" "src/part1_tree_manual/tree_manual.py"
                ;;
            part2)
                print_section "Parte 2 - Machine Learning"
                run_part "2.1" "src/part2_ml/train_knn.py"
                run_part "2.2" "src/part2_ml/svm.py"
                run_part "2.3" "src/part2_ml/desicion_tree.py"
                ;;
            part3)
                run_part "3" "src/part3_ga/run_ga.py"
                ;;
            part4)
                print_section "Parte 4 - Enxame e Imunológico"
                run_part "4.1" "src/part4_swarm_immune/pso.py"
                run_part "4.2" "src/part4_swarm_immune/clonalg.py"
                ;;
            all)
                print_section "Executando todas as partes"
                run_part "1" "src/part1_tree_manual/tree_manual.py"
                run_part "2.1" "src/part2_ml/train_knn.py"
                run_part "2.2" "src/part2_ml/svm.py"
                run_part "2.3" "src/part2_ml/desicion_tree.py"
                run_part "3" "src/part3_ga/run_ga.py"
                run_part "4.1" "src/part4_swarm_immune/pso.py"
                run_part "4.2" "src/part4_swarm_immune/clonalg.py"
                print_success "Todas as partes executadas com sucesso!"
                ;;
            *)
                print_error "Uso: $0 {part1|part2|part3|part4|all}"
                exit 1
                ;;
        esac
    fi
}

main "$@"
