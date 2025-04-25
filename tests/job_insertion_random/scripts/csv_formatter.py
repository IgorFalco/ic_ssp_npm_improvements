# Este script percorre os diretórios de saída contendo os resultados de execução de algoritmos
# para diferentes sequências de ferramentas e objetivos (TS, MA, FL).
# Ele extrai as métricas de cada execução a partir de arquivos de log, organiza os dados por RUN
# e gera arquivos CSV separados para cada objetivo por sequência.
# Os resultados são salvos em pastas dentro de "results/{sequência}/".

import os
import csv
import re

# Diretório base onde estão localizados os resultados das execuções
BASE_DIR = "../__output"

CSV_HEADERS = ["RUN", "TS", "MA", "FL", "RunningTime", "Iterations"]

CATEGORIES = ["FL", "TS"]

# Padrões para extração de métricas com expressões regulares
LOG_PATTERNS = {
    "TOTAL TOOL SWITCHES": r"TOTAL TOOL SWITCHES : (\d+)",
    "HIGHEST MAKESPAN": r"HIGHEST MAKESPAN : (\d+)",
    "TOTAL FLOWTIME": r"TOTAL FLOWTIME : (\d+)",
    "COMPLETED ITERATIONS": r"COMPLETED ITERATIONS : (\d+)",
    "RUNNING TIME": r"RUNNING TIME : ([\d\.]+)",
}


def extract_metrics_from_log(log_file_path):
    """
    Lê um arquivo de log e extrai as métricas definidas em LOG_PATTERNS,
    agrupadas por RUN.
    """
    extracted_results = []

    try:
        with open(log_file_path, "r", encoding="utf-8") as log_file:
            content = log_file.read()

        # Encontra blocos de execução (RUN)
        run_pattern = re.compile(
            r"RUN : (\d+) - (.*?)(?=\nRUN : \d+|$)", re.DOTALL)
        run_blocks = run_pattern.findall(content)

        for run_id, run_text in run_blocks:
            run_data = {"RUN": run_id}

            for metric_name, regex in LOG_PATTERNS.items():
                match = re.search(regex, run_text)
                run_data[metric_name] = match.group(1) if match else "N/A"

            extracted_results.append(run_data)

    except Exception as e:
        print(f"Erro ao processar o arquivo {log_file_path}: {e}")

    return extracted_results


def process_all_sequences():
    """
    Percorre todas as sequências no diretório base, processa os logs e
    gera arquivos CSV com os resultados agregados por objetivo.
    """
    for sequence_name in os.listdir(BASE_DIR):
        sequence_path = os.path.join(BASE_DIR, sequence_name)
        if not os.path.isdir(sequence_path):
            continue  # Ignora arquivos que não são diretórios

        output_directory = os.path.join("../results", sequence_name)
        os.makedirs(output_directory, exist_ok=True)

        aggregated_results = {}

        for category in CATEGORIES:
            category_path = os.path.join(sequence_path, category)
            if not os.path.isdir(category_path):
                continue

            csv_output_path = os.path.join(
                output_directory, f"{category}_results.csv")

            for log_filename in os.listdir(category_path):
                log_file_path = os.path.join(category_path, log_filename)
                if not os.path.isfile(log_file_path):
                    continue

                run_metrics_list = extract_metrics_from_log(log_file_path)

                for run_metrics in run_metrics_list:
                    run_id = run_metrics.get("RUN", "N/A")
                    if run_id == "N/A":
                        continue

                    if run_id not in aggregated_results:
                        aggregated_results[run_id] = {"RUN": run_id}

                    # Armazena os dados extraídos, associando com a categoria atual
                    aggregated_results[run_id]["TS"] = run_metrics["TOTAL TOOL SWITCHES"]
                    aggregated_results[run_id]["MA"] = run_metrics["HIGHEST MAKESPAN"]
                    aggregated_results[run_id]["FL"] = run_metrics["TOTAL FLOWTIME"]
                    aggregated_results[run_id]["RT"] = run_metrics["RUNNING TIME"]
                    aggregated_results[run_id]["IT"] = run_metrics["COMPLETED ITERATIONS"]

            write_results_to_csv(csv_output_path, aggregated_results)


def write_results_to_csv(csv_path, results_dict):
    """
    Escreve os dados agregados de todas as RUNs em um arquivo CSV ordenado por RUN.
    """
    valid_run_ids = [run_id for run_id in results_dict if run_id.isdigit()]
    valid_run_ids.sort(key=int)

    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(CSV_HEADERS)

        for run_id in valid_run_ids:
            run_data = results_dict[run_id]
            writer.writerow([
                run_data.get("RUN", "N/A"),
                run_data.get("TS", "N/A"),
                run_data.get("MA", "N/A"),
                run_data.get("FL", "N/A"),
                run_data.get("RT", "N/A"),
                run_data.get("IT", "N/A"),
            ])

    print(f"Arquivo CSV gerado: {csv_path}")


if __name__ == "__main__":
    process_all_sequences()
