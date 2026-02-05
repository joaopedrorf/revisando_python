import json
import os

ARQUIVO_TAREFAS = "tasks.json"


def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []

    try:
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, IOError):
        print("Erro ao carregar tarefas. Iniciando lista vazia.")
        return []


def salvar_tarefas(tarefas):
    try:
        with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    except IOError:
        print("Erro ao salvar tarefas.")


def listar_tarefas(tarefas):
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔️" if tarefa["concluida"] else "❌"
        print(f"{i}. [{status}] {tarefa['titulo']}")


def adicionar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ").strip()

    if not titulo:
        print("❌ O título não pode ser vazio.")
        return

    tarefa = {
        "titulo": titulo,
        "concluida": False
    }

    tarefas.append(tarefa)
    print("✅ Tarefa adicionada com sucesso.")


def concluir_tarefa(tarefas):
    if not tarefas:
        print("⚠️ Não há tarefas para concluir.")
        return
    
    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1

        if indice < 0 or indice >= len(tarefas):
            print("❌ Número inválido.")
            return

        if tarefas[indice]["concluida"]:
            print("⚠️ Esta tarefa já está concluída.")
            return
        
        tarefas[indice]["concluida"] = True
        print("✅ Tarefa marcada como concluída.")

    except ValueError:
        print("❌ Digite um número válido.")

    


def remover_tarefa(tarefas):
    if not tarefas:
        print("📭 Nenhuma tarefa para remover.")
        return

    listar_tarefas(tarefas)

    try:
        numero = int(input("\nDigite o número da tarefa a remover: "))

        indice = numero - 1

        if indice < 0 or indice >= len(tarefas):
            print("\nNúmero inválido.\n")
            return

        tarefa_removida = tarefas.pop(indice)
        print(f"\nTarefa '{tarefa_removida['titulo']}' removida com sucesso.\n")

    except ValueError:
        print("\nPor favor, digite um número válido.\n")


def menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")


def main():
    tarefas = carregar_tarefas()
    
    listar_tarefas(tarefas)


    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)         
            salvar_tarefas(tarefas)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
