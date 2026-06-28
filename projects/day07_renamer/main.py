import os
from pathlib import Path

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_pasta():
    while True:
        caminho = input("Digite o caminho da pasta (ex: C:/Users/Meu/Docs): ").strip()
        pasta = Path(caminho)
        if pasta.exists() and pasta.is_dir():
            return pasta
        print("❌ Pasta Invalida!")

def obter_operacao():
    print("\n📂 Escolha a operação:")
    print("1 - Adicionar Prefixo (ex: 'foto_' -> foto_viagem.jpg)")
    print("2 - Adicionar Sufixo (ex: '_2025' -> viagem_2025.jpg)")
    print("3 - Substituir espaços por underscores (espaço -> _)")


    while True:
        opcao = input("\nDigite 1, 2 ou 3: ").strip()
        if opcao in ['1', '2', '3']:
            return opcao
        print("❌ Opcao Invalida!")

def main():
    limpar_tela()
    print("="*50)
    print("🚀 RENOMEADOR AUTOMÁTICO DE ARQUIVOS - DIA 7")
    print("="*50)

    pasta = obter_pasta()

    arquivos = [arq for arq in pasta.iterdir() if arq.is_file()]

    if not arquivos:
        print("⚠️ Nenhum arquivo encontrado nesta pasta.")
        return

    print(f"\n 📄 Encontrados {len(arquivos)} arquivos na pasta.")


    op = obter_operacao()
    prefixo = sufixo = ""

    if op == '1':
        prefixo = input("Digite o prefixo que quer adicionar: ").strip()
    elif op == '2':
        sufixo = input("Digite o sufixo (antes da extensao): ").strip()

    preview = []
    for arquivo in arquivos:
        nome_base = arquivo.stem
        extensao = arquivo.suffix

        novo_nome = nome_base

        if op == '1':
            novo_nome = f"{prefixo}{novo_nome}"
        elif op == '2':
            novo_nome = f"{novo_nome}{sufixo}"
        elif op == '3':
            novo_nome = novo_nome.replace(" ", "_")

        novo_caminho = arquivo.with_name(f"{novo_nome}(extensao)")

        if novo_caminho != arquivo:
            preview.append((arquivo, novo_caminho))
        else:
            print(f"ℹ️ Ignorado (ja esta igual): {arquivo.name}")

    if not preview:
        print("\n✅ Nenhuma alteracao necessaria.")
        return

    print("\n" + "="*60)
    print("📋 PRÉVIA DAS RENOMEAÇÕES:")
    for antigo, novo in preview:
        print(f"  🔹 {antigo.name}  ➜  {novo.name}")
    print("="*60)

    confirmacao = input("\n🎈 Deseja realmente aplicar essas alteracoes? (S/N): ").strip().lower()

    if confirmacao != 's':
        print("❌ Operacao cancelada pelo usuario")
        return

    print("\n⏳ Renomeando arquivos...")
    count = 0
    for antigo_caminho, novo_caminho in preview:
        try:
            antigo_caminho.rename(novo_caminho)
            count += 1
            print(f"✅ {antigo_caminho.name} -> {novo_caminho.name}")
        except PermissionError:
            print(f"❌ Sem permissao para renomear: {antigo_caminho.name}")
        except FileExistsError:
            print(f"❌ Ja existe um arquivo com o nome: {novo_caminho.name}")
        except Exception as e:
            print(f"❌ Erro inesperado em {antigo_caminho.name}: {e}")

    print(f"\n🎉 {count} arquivos renomeados com sucesso!")


if __name__ == "__main__":
    main()