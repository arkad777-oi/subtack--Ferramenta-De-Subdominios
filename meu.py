import subprocess

def criar_e_executar():
    nome = "meuambiente"
    print(f"[+] Criando ambiente virtual '{nome}'...")
    subprocess.run(["python3", "-m", "venv", nome])
    print(f"[+] Ambiente '{nome}' criado com sucesso!")

if __name__ == "__main__":
    criar_e_executar()
