# BIBLIOTECAS
from datetime import date
import time

# SYSTEM
print("=== ASSISTENTE DE ALISTAMENTO MILITAR ===")
time.sleep(1)
ano_nascimento = int(input("Digite o ano em que você nasceu -> "))
time.sleep(1)

print('PROCESSANDO...')
time.sleep(2)

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"\n🎂 Você tem {idade} anos.")
time.sleep(1)
while True:
    print("\n=== GUIAS ===")
    print("[1] Situação do alistamento")
    print("[2] Prazo")
    print("[3] Documentos")
    print("[0] Sair")

    opcao = input("Escolha -> ")


# IF'S e ELIF'S.
    if opcao == "1":
        if idade < 18:
            faltam = 18 - idade
            print("ℹ️ Você ainda não precisa se alistar.")
            print(f"⏳ Faltam {faltam} ano(s) para o alistamento.")
        elif idade == 18:
            print("⚠️ Você deve se alistar este ano.")
        else:
            print("❌ Você pode estar em atraso com o alistamento.")

    elif opcao == "2":
        if idade < 18:
            print("📅 O alistamento é obrigatório no ano em que você completa 18 anos.")
        else:
            print("📅 Prazo padrão: até 30 de junho.")
            print("📅 Em caso de atraso, regularize o quanto antes.")

    elif opcao == "3":
        print("📄 Documentos geralmente solicitados:")
        print("- RG")
        print("- CPF")
        print("- Comprovante de residência")

    elif opcao == "0":
        print("Encerrando o assistente... 👋")
        break

    else:
        print("❌ Opção inválida! Escolha 1, 2, 3 ou 0.")
