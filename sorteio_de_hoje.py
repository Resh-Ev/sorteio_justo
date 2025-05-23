import random
from collections import Counter
import textwrap

# Variáveis globais para histórico e contagem
historico_vencedores = []
contagem_vitorias = {
    "exercicio": 0,
    "curso": 0,
    "canal dark": 0
}

def sorteio_justo(opcoes, n_rodadas=3):
    resultados = []

    for i in range(1, n_rodadas + 1):
        valores_embaralhados = random.sample(list(opcoes.values()), len(opcoes))
        participante = random.choice(valores_embaralhados)
        resultados.append(participante)
        print(f"Rodada {i}: {participante}")

    contagem = Counter(resultados)
    max_aparicoes = max(contagem.values())
    empatados = [p for p, count in contagem.items() if count == max_aparicoes]

    if len(empatados) > 1:
        ganhador = random.choice(empatados)
    else:
        ganhador = empatados[0]

    # Atualiza histórico e contagem
    historico_vencedores.append(ganhador)
    contagem_vitorias[ganhador] += 1

    mensagem = textwrap.dedent(f""" 
                            
        🔥🔥🔥 Que rufem os tambores!!!       
        Sorteios realizados: {resultados}       
        O campeão (melhor de 3) é: {ganhador.upper()} 🎆🎆🎆🧨🔥    
    """)
    print(mensagem)

def mostrar_historico():
    print("\n=== Histórico de vencedores ===")
    if not historico_vencedores:
        print("Nenhum sorteio realizado ainda.")
    else:
        for i, vencedor in enumerate(historico_vencedores, 1):
            print(f"Sorteio {i}: {vencedor}")
        print("\nContagem total de vitórias:")
        for chave, valor in contagem_vitorias.items():
            print(f"{chave.capitalize()}: {valor}")

def definir_participantes():
    return {
        "1": "exercicio",
        "2": "curso",
        "3": "canal dark"
    }

def main():
    participantes = definir_participantes()
    while True:
        print("\nEscolha uma opção:")
        print("1 - Realizar sorteio")
        print("2 - Mostrar histórico de vencedores")
        print("3 - Sair")

        escolha = input("Opção: ")

        if escolha == "1":
            sorteio_justo(participantes)
        elif escolha == "2":
            mostrar_historico()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
