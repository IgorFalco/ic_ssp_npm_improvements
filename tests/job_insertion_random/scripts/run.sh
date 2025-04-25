#!/bin/bash

# Caminhos e executável
BASE_DIR="../../../"
BIN_DIR="$BASE_DIR/bin"
EXE="ssp_npm_solver.out"
INSTANCE="ins320_m=4_j=60_t=60_sw=h_dens=d_var=20.txt"
INSTANCE_PATH="$BASE_DIR/data/instancias_txt/SSP-NPM-II/$INSTANCE"

# Verificações
if [[ ! -x "$BIN_DIR/$EXE" ]]; then
  echo "❌ Erro: Executável '$BIN_DIR/$EXE' não encontrado ou sem permissão de execução."
  exit 1
fi

if [[ ! -f "$INSTANCE_PATH" ]]; then
  echo "❌ Erro: Instância '$INSTANCE_PATH' não encontrada."
  exit 1
fi

run_script() {
  local sequence="$1"
  output_dir="../__output/random"

  # Caminhos absolutos para evitar bugs no Git Bash
  BIN_ABS=$(realpath "$BIN_DIR/$EXE")
  INSTANCE_ABS=$(realpath "$INSTANCE_PATH")

  mkdir -p "$output_dir"/{TS,MA,FL}

  for objective in 1 2 3; do
    case $objective in
      1) method="TS" ;;
      2) method="MA" ;;
      3) method="FL" ;;
    esac

    CMD="$BIN_ABS --instance \"$INSTANCE_ABS\" --output \"$output_dir/$method/$INSTANCE\" --objective $objective --iterations 1000 --runs 1 --sequence $sequence"

    echo "🚀 Rodando: $CMD"
    if ! eval $CMD; then
      echo "❌ Erro na execução"
    fi
  done
}

run_script "2"