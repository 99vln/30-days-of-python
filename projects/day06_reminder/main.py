import datetime
import time
import os
import sys
from dataclasses import dataclass
from typing import Tuple, Optional

@dataclass
class Lembrete:
    hora_alvo: datetime.datetime
    mensagem: str

    def calcular_segundos_restantes(self) -> float:
        agora = datetime.datetime.now()
        return (self.hora_alvo - agora).total_seconds()

    def iniciar_monitoramento(self) -> None:
        segundos_espera = self.calcular_segundos_restantes()
        print(f"\n⏳ Lembrete agendado para {self.hora_alvo.strftime('%H:%M')}.")
        print(f"Aguardando {int(segundos_espera // 60)} minutos e {int(segundos_espera % 60)} segundos...")

        while True:
            restante = self.calcular_segundos_restantes()

            if restante <= 0:
                break

            if restante > 60:
                print(f"🕒 Faltam {int(restante // 60)} minutos... ", end='\r')

                time.sleep(10)

        self._disparar_alarme()

    def _disparar_alarme(self) -> None:
        print("\n" + "=" * 50)
        print(f"🔔 {self.mensagem.upper()} 🔔")
        print("=" * 50)
        print('\a')

def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def processar_input_hora(hora_input: str) -> Optional[Tuple[int, int]]:
    try:
        horas_str, minutos_str = hora_input.split(':')
        horas, minutos = int(horas_str), int(minutos_str)
        if 0 <= horas <= 23 and 0 <= minutos <= 59:
            return horas, minutos
    except ValueError:
        pass

    return None


def main() -> None:
    limpar_tela()
    print("⏰ Sistema de Lembrete")

    while True:
        hora_input = input("\nDigite a hora (%H:%M) ou 'sair' para encerrar: ").strip().lower()

        if hora_input == 'sair':
            print("Encerrando o programa.")
            sys.exit(0)

        horario_valido = processar_input_hora(hora_input)
        if horario_valido:
            horas, minutos = horario_valido
            break
        else:
            print("❌ Formato invalido!")

    mensagem = input("Digite a mensagem do lembrete: ").strip()
    if not mensagem:
        mensagem = "ALERTA! Horario Chegou!"

    agora = datetime.datetime.now()
    hora_lembrete = datetime.datetime(agora.year, agora.month, agora.day, horas, minutos)

    if hora_lembrete <= agora:
        print(f"\n⚠️ O horario {hora_input} ja passou hoje.")
        opcao = input("Deseja agendar para amanha no mesmo horario? (S/N)").strip().upper()

        if opcao == 'S':
            hora_lembrete += datetime.timedelta(days=1)
        else:
            print("Opcao cancelada. Encerrando...")
            return

    lembrete = Lembrete(hora_alvo=hora_lembrete, mensagem=mensagem)

    lembrete.iniciar_monitoramento()

if __name__ == "__main__":
    main()