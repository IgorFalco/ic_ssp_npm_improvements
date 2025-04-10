#!/bin/bash

# Caminhos e executável
BASE_DIR="../../../"

BIN_DIR="$BASE_DIR/bin"
EXE="ssp_npm_solver.out"

INSTANCE="ins160_m=3_j=20_t=20_var=20.txt"
INSTANCE_PATH="$BASE_DIR/data/instancias_txt/SSP-NPM-I/$INSTANCE"

# Verificações iniciais
if [[ ! -x "$BIN_DIR/$EXE" ]]; then
  echo "❌ Erro: Executável '$BIN_DIR/$EXE' não encontrado ou sem permissão de execução."
  exit 1
fi

if [[ ! -f "$INSTANCE_PATH" ]]; then
  echo "❌ Erro: Instância '$INSTANCE_PATH' não encontrada."
  exit 1
fi

# Função para gerar permutações da sequência
permute() {
  local items="$1"
  local out="$2"
  local i
  [[ -z "$items" ]] && {
    echo "▶️  Executando para sequência: $out"
    run_script "$out"
    return
  }
  for ((i = 0; i < ${#items}; i++)); do
    permute "${items:0:i}${items:i+1}" "$out${items:i:1}"
  done
}

# Função para rodar o programa com uma sequência
run_script() {
  local sequence="$1"
  output_dir="../__output/$sequence"

  # Criar diretórios de saída
  for method in TS MA FL; do
    mkdir -p "$output_dir/$method"
  done

  # Comandos com verificação de erro
  for objective in 1 2 3; do
    case $objective in
      1) method="TS" ;;
      2) method="MA" ;;
      3) method="FL" ;;
    esac

    CMD="$BIN_DIR/$EXE --instance $INSTANCE_PATH --output $output_dir/$method/$INSTANCE --objective $objective --iterations 1000 --runs 10 --sequence $sequence"

    echo "🚀 Rodando: $CMD"
    if ! $CMD; then
      echo "❌ Erro na execução com sequência '$sequence', objetivo $objective"
    fi
  done
}

Testa todas as permutações de "1234"
permute "1234" ""