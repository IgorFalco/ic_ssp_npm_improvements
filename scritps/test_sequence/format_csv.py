import os
import csv
import re

# Diretório base onde estão as sequências
BASE_DIR = "../../imp/output/sequence/"
CSV_HEADERS = ["RUN", "TS", "MA", "FL", "RunningTime", "Iterations"]  # Cabeçalho do CSV

# Exemplo de definição de PATTERNS - defina de acordo com os valores que você deseja extrair
PATTERNS = {
    "TOTAL TOOL SWITCHES": r"TOTAL TOOL SWITCHES : (\d+)",
    "HIGHEST MAKESPAN": r"HIGHEST MAKESPAN : (\d+)",
    "TOTAL FLOWTIME": r"TOTAL FLOWTIME : (\d+)",
    "COMPLETED ITERATIONS": r"COMPLETED ITERATIONS : (\d+)",
    "RUNNING TIME": r"RUNNING TIME : ([\d\.]+)",
}

def extract_values(file_path):
    results = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex para capturar cada RUN, agora incluindo o número da RUN separadamente
        pattern = re.compile(r"RUN : (\d+) - (.*?)(?=\nRUN : \d+|$)", re.DOTALL)
        runs = pattern.findall(content)

        for run_number, run_content in runs:
            values = {"RUN": run_number}  # Adiciona o número da RUN
            for key, pattern in PATTERNS.items():
                match = re.search(pattern, run_content)
                values[key] = match.group(1) if match else "N/A"
            
            results.append(values)
    
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")
    
    return results

def process_results():
    for sequence in os.listdir(BASE_DIR):
        sequence_path = os.path.join(BASE_DIR, sequence)
        if not os.path.isdir(sequence_path):
            continue  # Pula arquivos que não são diretórios

        output_dir = os.path.join("results", sequence)
        os.makedirs(output_dir, exist_ok=True)  # Criar pasta para cada sequência        
        
        aggregated_results = {}

        # Percorre os diretórios FL, MA e TS dentro de cada sequência
        for category in ["FL", "MA", "TS"]:
            csv_file = os.path.join(output_dir, category +  "_results.csv")
            category_path = os.path.join(sequence_path, category)
            if not os.path.isdir(category_path):
                continue

            for file in os.listdir(category_path):
                file_path = os.path.join(category_path, file)
                if not os.path.isfile(file_path):
                    continue  # Pula se não for um arquivo

                run_results = extract_values(file_path)
                for run_data in run_results:
                    run_id = run_data["RUN"]
                    if run_id == "N/A":
                        continue  # Ignora RUNs inválidas
                    
                    if run_id not in aggregated_results:
                        aggregated_results[run_id] = {"RUN": run_id}
                    
                    # Associa os valores da categoria correta
                    aggregated_results[run_id]["TS"] = run_data["TOTAL TOOL SWITCHES"]
                    aggregated_results[run_id]["MA"] = run_data["HIGHEST MAKESPAN"]
                    aggregated_results[run_id]["FL"] = run_data["TOTAL FLOWTIME"]
                    aggregated_results[run_id]["RT"] = run_data["RUNNING TIME"]
                    aggregated_results[run_id]["IT"] = run_data["COMPLETED ITERATIONS"]

            # Filtra apenas IDs numéricos para evitar erro ao ordenar
            valid_run_ids = [run_id for run_id in aggregated_results.keys() if run_id.isdigit()]
            
            # Salva os resultados no CSV
            with open(csv_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(CSV_HEADERS)  # Escreve o cabeçalho
                for run_id in sorted(valid_run_ids, key=int):  # Ordena pelo número da RUN
                    row = aggregated_results[run_id]
                    writer.writerow([
                        row.get("RUN", "N/A"),
                        row.get("TS", "N/A"),
                        row.get("MA", "N/A"),
                        row.get("FL", "N/A"),
                        row.get("RT", "N/A"),
                        row.get("IT", "N/A")
                    ])

            print(f"Arquivo CSV gerado: {csv_file}")

# Executa o script
if __name__ == "__main__":
    process_results()

