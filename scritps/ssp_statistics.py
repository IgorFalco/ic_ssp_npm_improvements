import re
import numpy as np

# Expressões regulares para extrair valores
patterns = {
    'FMAX': r'HIGHEST\s*MAKESPAN\s*:\s*(\d+)',
    'TFT': r'TOTAL\s*FLOWTIME\s*:\s*(\d+)',
    'TTS': r'TOTAL\s*TOOL\s*SWITCHES\s*:\s*(\d+)',
    'run': r'RUN\s*:\s*(\d+)'
}

def extract_values(content: str):
    """Extrai todos os valores numéricos necessários do conteúdo."""
    highest_makespan = [int(v) for v in re.findall(patterns['FMAX'], content)]
    total_flowtime = [int(v) for v in re.findall(patterns['TFT'], content)]
    total_tool_switches = [int(v) for v in re.findall(patterns['TTS'], content)]
    runs = re.findall(patterns['run'], content)
    
    # Criar uma lista de dicionários para associar os valores a cada instância
    instances = []
    for i in range(len(runs)):
        instances.append({
            'run': int(runs[i]),
            'FMAX': highest_makespan[i],
            'TFT': total_flowtime[i],
            'TTS': total_tool_switches[i]
        })

    return instances

def calculate_averages(instances):
    """Calcula as médias dos valores extraídos."""
    avg_fmax = np.mean([inst['FMAX'] for inst in instances])
    avg_tft = np.mean([inst['TFT'] for inst in instances])
    avg_tts = np.mean([inst['TTS'] for inst in instances])
    return avg_fmax, avg_tft, avg_tts

def find_best_instance(instances):
    """Encontra a melhor instância com base na menor TTS, depois FMAX e depois TFT."""
    return min(instances, key=lambda inst: (inst['TTS'], inst['FMAX'], inst['TFT']))

if __name__ == '__main__':
    input_path = '../../imp/saida_4321.txt'
    output_path = 'output_4321.txt'
    
    with open(input_path, 'r') as file:
        content = file.read()

    instances = extract_values(content)
    avg_fmax, avg_tft, avg_tts = calculate_averages(instances)
    best_instance = find_best_instance(instances)

    # Criando o conteúdo do arquivo de saída
    output_content = (
        f"AVG HIGHEST MAKESPAN: {avg_fmax:.2f}\n"
        f"AVG TOTAL FLOWTIME: {avg_tft:.2f}\n"
        f"AVG TOTAL TOOL SWITCHES: {avg_tts:.2f}\n\n"
        f"Best Instance:\n"
        f"RUN: {best_instance['run']}, TTS: {best_instance['TTS']}, "
        f"FMAX: {best_instance['FMAX']}, TFT: {best_instance['TFT']}\n"
    )

    # Salvando no arquivo
    with open(output_path, 'w') as output_file:
        output_file.write(output_content)

    print(f"Resultados salvos em {output_path}")
