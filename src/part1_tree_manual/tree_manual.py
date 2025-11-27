def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(f"{pergunta} (s/n): ").strip().lower()
        if resposta in ['s', 'sim', 'y', 'yes']:
            return True
        elif resposta in ['n', 'nao', 'não', 'no']:
            return False
        else:
            print(">> Entrada inválida. Por favor, responda com 's' ou 'n'.")

def avaliar_ocular():
    print("\n--- 1. ABERTURA OCULAR ---")
    if perguntar_sim_nao("Abre os olhos espontaneamente?"):
        return 4
    if perguntar_sim_nao("Abre os olhos ao comando verbal?"):
        return 3
    if perguntar_sim_nao("Abre os olhos à pressão/dor?"):
        return 2
    
    print(">> Resposta: Ausente (1 ponto)")
    return 1

def avaliar_verbal():
    print("\n--- 2. RESPOSTA VERBAL ---")
    if perguntar_sim_nao("O paciente está orientado e conversa?"):
        return 5
    if perguntar_sim_nao("A conversa é confusa?"):
        return 4
    if perguntar_sim_nao("Usa palavras inapropriadas?"):
        return 3
    if perguntar_sim_nao("Emite sons ininteligíveis?"):
        return 2
    
    print(">> Resposta: Ausente (1 ponto)")
    return 1

def avaliar_motora():
    print("\n--- 3. RESPOSTA MOTORA ---")
    if perguntar_sim_nao("Obedece a comandos?"):
        return 6
    if perguntar_sim_nao("Localiza o estímulo doloroso?"):
        return 5
    if perguntar_sim_nao("Apresenta flexão normal (movimento de retirada)?"):
        return 4
    if perguntar_sim_nao("Apresenta flexão anormal (decorticação)?"):
        return 3
    if perguntar_sim_nao("Apresenta extensão anormal (descerebração)?"):
        return 2
    
    print(">> Resposta: Ausente (1 ponto)")
    return 1

def main():
    print("=========================================")
    print("   CALCULADORA DA ESCALA DE GLASGOW")
    print("   Responda as perguntas com 's' ou 'n'")
    print("=========================================")

    
    pontos_ocular = avaliar_ocular()
    pontos_verbal = avaliar_verbal()
    pontos_motora = avaliar_motora()

    
    total = pontos_ocular + pontos_verbal + pontos_motora

    
    classificacao = ""
    acao = ""
    
    if 13 <= total <= 15:
        classificacao = "TRAUMA LEVE"
        cor = "\033[92m" 
    elif 9 <= total <= 12:
        classificacao = "TRAUMA MODERADO"
        cor = "\033[93m" 
    else:
        classificacao = "TRAUMA GRAVE"
        acao = "\n!!! ATENÇÃO: CONSIDERAR INTUBAÇÃO !!!"
        cor = "\033[91m" 
    
    reset_cor = "\033[0m"

    
    print("\n" + "="*40)
    print(f"RESULTADO FINAL: {cor}{total} PONTOS{reset_cor}")
    print(f"CLASSIFICAÇÃO:   {cor}{classificacao}{reset_cor}")
    if acao:
        print(f"{cor}{acao}{reset_cor}")
    
    print(f"\nDetalhamento: Ocular({pontos_ocular}) + Verbal({pontos_verbal}) + Motora({pontos_motora})")
    print("="*40)

if __name__ == "__main__":
    main()