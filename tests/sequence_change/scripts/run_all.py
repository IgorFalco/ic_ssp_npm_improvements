import subprocess
import os

# Caminho base do script (scripts/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_shell_script():
    print("🔁 Executando sequência de experimentos...")
    subprocess.run(["bash", os.path.join(BASE_DIR, "run_all_sequences.sh")], check=True)

def run_csv_formatter():
    print("📄 Formatando resultados CSV...")
    subprocess.run(["python3", os.path.join(BASE_DIR, "csv_formatter.py")], check=True)

def run_plot_results():
    print("📊 Gerando gráficos...")
    subprocess.run(["python3", os.path.join(BASE_DIR, "plot_results.py")], check=True)

if __name__ == "__main__":
    run_shell_script()
    run_csv_formatter()
    run_plot_results()
    print("✅ Tudo finalizado com sucesso!")
