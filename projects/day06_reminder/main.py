import datetime
import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("⏰ Lembrete de Tarefas")

    while True:
        hora_input = input("Digite a hora para o lembrete (HH:MM) ou 'sair' para encerrar: ").strip()

        try:
            horas, minutos = map(int, hora_input.split(':'))
            if 0 <= horas <= 23 and 0 <= minutos <= 59:
                break
            else:
                print("Horario invalido!")
        except ValueError:
            print("Formato invalido!")

    mensagem = input("Digite a mensagem do lembrete: ").strip()
    if not mensagem:
        mensagem = "ALERTA! Horario Chegou!"

    agora = datetime.datetime.now()
    hora_lembrete = datetime.datetime(
        agora.year, agora.month, agora.day, horas, minutos
    )
    if hora_lembrete <= agora:
        print(f"\n⚠️ O horario {hora_input} ja passou hoje.")

        opcao = input("Deseja agendar para amanha no mesmo horario? (S/N)").strip().upper()
        if opcao == 'S':
            hora_lembrete += datetime.timedelta(days=1)
            print(f"Lembrete agendado para amanha as {hora_lembrete.strftime('%H:%M')}.")
        else:
            print("Encerrando o programa.")
            return

    segundos_espera = (hora_lembrete - agora).total_seconds()
    print(f"\n⏳ Lembrete agendado para {hora_lembrete.strftime('%H:%M')}.")
    print(f"Aguardando {int(segundos_espera // 60)} minutos e {int(segundos_espera % 60)} segundos...")

    while True:
        agora = datetime.datetime.now()
        if agora >= hora_lembrete:
            break
        restante = (hora_lembrete - agora).total_seconds()
        if restante > 60:
            print(f"🕒 Faltam {int(restante // 60)}minutos...", end='\r')
        time.sleep(30)

    print("\n" + "="*50)
    print(f"🔔 {mensagem.upper()} 🔔")
    print("="*50)
    print('\a')


if __name__ == "__main__":
    main()