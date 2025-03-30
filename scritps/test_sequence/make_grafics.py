import os
import pandas as pd
import matplotlib.pyplot as plt

# Diretório base onde estão as pastas com os CSVs
base_dir = "results"
output_base_dir = "grafics"

# Criar as pastas de saída para cada métrica
metrics = ["TS", "MA", "FL"]
titles = {
    "TS": "Tool Switches (TS)",
    "MA": "Makespan (MA)",
    "FL": "Flowtime (FL)",
}

# Processar cada métrica como objetivo
for metric in metrics:
    metric_output_dir = os.path.join(output_base_dir, metric)
    os.makedirs(metric_output_dir, exist_ok=True)
    
    data = {"TS": [], "MA": [], "FL": []}
    labels = []
    
    # Percorrer todas as pastas dentro de "results"
    for folder in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path):
            continue  # Ignorar arquivos que não sejam diretórios
        
        file_path = os.path.join(folder_path, f"{metric}_results.csv")
        
        # Verifica se o arquivo existe antes de processá-lo
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            labels.append(folder)  # Nome da sequência
            
            for metric_plot in metrics:
                if metric_plot in df.columns:
                    data[metric_plot].append(df[metric_plot].values)
                else:
                    data[metric_plot].append([])  # Caso não tenha valores
    
    # Criar gráficos para todas as métricas com base na métrica objetivo
    for metric_plot in metrics:
        plt.figure(figsize=(14, 6))
        plt.boxplot(data[metric_plot], labels=labels, vert=True, patch_artist=True)
        
        # Configurações do gráfico
        plt.xticks(rotation=45)  # Rotacionar os labels para melhor visualização
        plt.title(f"Boxplot de {titles[metric_plot]} - Otimizado para {titles[metric]}", fontsize=14, fontweight="bold")
        plt.xlabel("Sequências")
        plt.ylabel(metric_plot)
        
        # Salvar o gráfico na pasta correspondente à métrica
        output_file = os.path.join(metric_output_dir, f"{metric_plot}_boxplot.png")
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        plt.close()

print("Gráficos salvos nas pastas de cada métrica dentro de 'grafics'")