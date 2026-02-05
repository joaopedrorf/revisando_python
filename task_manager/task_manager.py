import json
import os

ARQUIVO_TAREFAS = "tasks.json"


def carregar_tarefas():
    pass


def salvar_tarefas(tarefas):
    pass


def listar_tarefas(tarefas):
    pass


def adicionar_tarefa(tarefas):
    pass


def concluir_tarefa(tarefas):
    pass


def remover_tarefa(tarefas):
    pass


def menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")


def main():
    tarefas = carregar_tarefas()

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
