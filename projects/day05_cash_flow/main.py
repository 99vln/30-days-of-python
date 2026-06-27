import os
from dataclasses import dataclass
from typing import List

@dataclass
class Transacao:
    tipo: str
    valor: float
    descricao: str

class GerenciadorFinanceiro:
    def __init__(self) -> None:
        self.transacoes: List[Transacao] = []
        self.saldo_total: float = 0.0

    def adicionar_transacao(self, tipo: str, valor: float, descricao: str) -> None:
        nova_transacao = Transacao(tipo, valor, descricao)
        self.transacoes.append(nova_transacao)

        if tipo == "receita":
            self.saldo_total += valor
        else:
            self.saldo_total -= valor

    def obter_extrato(self) -> List[Transacao]:
        return self.transacoes



def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def solicitar_valor_valido(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Por favor, insira um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def main() -> None:
    gerenciador = GerenciadorFinanceiro()

    while True:
        limpar_tela()
        print(f"💰 Saldo Total: R$ {gerenciador.saldo_total:.2f}")
        print("-" * 25)
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("\nEscolha:")

        match opcao:
            case "1":
                valor = solicitar_valor_valido("Valor do Ganho (R$): ")
                descricao = input("Descrição do Ganho: ").strip()
                gerenciador.adicionar_transacao("receita", valor, descricao)

            case "2":
                valor = solicitar_valor_valido("Valor do Gasto (R$): ")
                descricao = input("Descrição do Gasto: ").strip()
                gerenciador.adicionar_transacao("despesa", valor, descricao)

            case "3":
                print("\n 📄 Extrato: ")
                transacoes = gerenciador.obter_extrato()
                if not transacoes:
                    print("Nenhuma transação registrada.")
                else:
                    for t in transacoes:
                        sinal = "[+]" if t.tipo == "receita" else "[-]"
                        print(f"{sinal} {t.descricao}: R$ {t.valor:.2f}")

                input("\nPressione Enter para continuar...")

            case "4":
                print("👋 Até a próxima!")
                break

            case _:
                print("Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()