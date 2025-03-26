import os
import pandas as pd
import matplotlib.pyplot as plt

# Diretório base onde estão as pastas com os CSVs
base_dir = "results"
output_dir = "grafics"

# Criar a pasta de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Definir os tipos de métricas que queremos processar
metrics = ["TS", "MA", "FL"]
titles = {
    "TS": "Tool Switches (TS)",
    "MA": "Makespan (MA)",
    "FL": "Flowtime (FL)",
}
output_files = {
    "TS": os.path.join(output_dir, "TS_boxplot.png"),
    "MA": os.path.join(output_dir, "MA_boxplot.png"),
    "FL": os.path.join(output_dir, "FL_boxplot.png"),
}

# Processar cada métrica separadamente
for metric in metrics:
    data = []
    labels = []

    # Percorrer todas as 24 pastas
    for folder in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder)
        file_path = os.path.join(folder_path, f"{metric}_results.csv")

        # Verifica se o arquivo existe antes de processá-lo
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            data.append(df[metric].values)  # Pega os valores da métrica
            labels.append(folder)  # Guarda o nome da sequência

    if data:
        # Criar a figura do boxplot com Matplotlib
        plt.figure(figsize=(14, 6))
        plt.boxplot(data, labels=labels, vert=True, patch_artist=True)

        # Configurações do gráfico
        plt.xticks(rotation=45)  # Rotacionar os labels para melhor visualização
        plt.title(f"Boxplot de {titles[metric]}", fontsize=14, fontweight="bold")
        plt.xlabel("Sequências")
        plt.ylabel(metric)

        # Salvar o gráfico na pasta de saída
        plt.savefig(output_files[metric], dpi=300, bbox_inches="tight")
        plt.close()

print("Gráficos salvos na pasta grafics")
