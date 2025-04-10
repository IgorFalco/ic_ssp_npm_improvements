# Este script gera boxplots a partir de arquivos CSV localizados no diretório "results",
# onde estão armazenados os dados de desempenho (TS, MA, FL) para diferentes sequências.
# Para cada métrica otimizada (TS, MA, FL), ele cria gráficos comparando todas as sequências
# e salva os gráficos no diretório "grafics/{métrica}".

import os
import pandas as pd
import matplotlib.pyplot as plt

RESULTS_DIR = "../results"
OUTPUT_DIR = "../grafics"

METRICS = ["TS", "MA", "FL"]

METRIC_TITLES = {
    "TS": "Tool Switches (TS)",
    "MA": "Makespan (MA)",
    "FL": "Flowtime (FL)",
}


def ensure_output_dirs():
    """
    Garante que os diretórios de saída para os gráficos existam.
    """
    for metric in METRICS:
        metric_dir = os.path.join(OUTPUT_DIR, metric)
        os.makedirs(metric_dir, exist_ok=True)


def load_metric_data(objective_metric):
    """
    Carrega os dados de todas as sequências para cada métrica, 
    quando otimizadas para uma métrica específica (objective_metric).
    """
    data = {m: [] for m in METRICS}
    sequence_labels = []

    for sequence_name in sorted(os.listdir(RESULTS_DIR)):
        sequence_path = os.path.join(RESULTS_DIR, sequence_name)
        if not os.path.isdir(sequence_path):
            continue

        csv_path = os.path.join(
            sequence_path, f"{objective_metric}_results.csv")
        if not os.path.isfile(csv_path):
            continue

        try:
            df = pd.read_csv(csv_path)
            sequence_labels.append(sequence_name)

            for metric in METRICS:
                values = df[metric].values if metric in df.columns else []
                data[metric].append(values)

        except Exception as e:
            print(f"Erro ao ler {csv_path}: {e}")

    return data, sequence_labels


def generate_boxplots_for_metric(objective_metric):
    """
    Gera e salva boxplots para todas as métricas, considerando 
    que a métrica objetivo é a 'objective_metric'.
    """
    data, labels = load_metric_data(objective_metric)
    output_path = os.path.join(OUTPUT_DIR, objective_metric)

    for metric_to_plot in METRICS:
        plt.figure(figsize=(14, 6))
        plt.boxplot(data[metric_to_plot], labels=labels,
                    vert=True, patch_artist=True)

        # Título e eixos
        plt.xticks(rotation=45)
        plt.title(f"Boxplot de {METRIC_TITLES[metric_to_plot]} - Otimizado para {METRIC_TITLES[objective_metric]}",
                  fontsize=14, fontweight="bold")
        plt.xlabel("Sequências")
        plt.ylabel(METRIC_TITLES[metric_to_plot])

        # Caminho de saída do gráfico
        plot_filename = f"{metric_to_plot}_boxplot.png"
        plot_filepath = os.path.join(output_path, plot_filename)

        # Salvar gráfico
        plt.savefig(plot_filepath, dpi=300, bbox_inches="tight")
        plt.close()


def main():
    ensure_output_dirs()

    for metric in METRICS:
        generate_boxplots_for_metric(metric)

    print("Gráficos salvos nas pastas de cada métrica dentro de 'grafics'")


if __name__ == "__main__":
    main()
