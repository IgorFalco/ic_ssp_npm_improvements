#!/bin/bash

# Função para gerar permutações da sequência
permute() {
  local items="$1"
  local out="$2"
  local i
  [[ "$items" == "" ]] && {
    echo "$out"
    run_script "$out"
    return
  }
  for ((i = 0; i < ${#items}; i++)); do
    permute "${items:0:i}${items:i+1}" "$out${items:i:1}"
  done
}

# Função para substituir a sequência nos comandos e rodá-los
run_script() {
  local sequence=$1

  echo "Executando para sequência: $sequence" # Exibe qual sequência está sendo executada

  # Criar o diretório de saída se não existir
  mkdir -p output/sequence/$sequence/TS
  mkdir -p output/sequence/$sequence/MA
  mkdir -p output/sequence/$sequence/FL


  # Os comandos que você deseja executar com cada sequência gerada

  ../../imp/testManager --instance instancias_txt/SSP-NPM-I/ins160_m=3_j=20_t=20_var=20.txt --output output/sequence/$sequence/TS/ins160_m=3_j=20_t=20_var=20.txt --objective 1 --iterations 1000 --runs 30 --sequence $sequence
  ../../imp/testManager --instance instancias_txt/SSP-NPM-I/ins160_m=3_j=20_t=20_var=20.txt --output output/sequence/$sequence/MA/ins160_m=3_j=20_t=20_var=20.txt --objective 2 --iterations 1000 --runs 30 --sequence $sequence
  ../../imp/testManager --instance instancias_txt/SSP-NPM-I/ins160_m=3_j=20_t=20_var=20.txt --output output/sequence/$sequence/FL/ins160_m=3_j=20_t=20_var=20.txt --objective 3 --iterations 1000 --runs 30 --sequence $sequence

  # ../../imp/testManager --instance instancias_txt/SSP-NPM-II/ins180_m=4_j=40_t=60_sw=l_dens=s_var=20.txt --output output/sequence/$sequence/TS/ins180_m=4_j=40_t=60_sw=l_dens=s_var=20.txt --objective 1 --iterations 1000 --runs 30 --sequence $sequence
  # ../../imp/testManager --instance instancias_txt/SSP-NPM-II/ins180_m=4_j=40_t=60_sw=l_dens=s_var=20.txt --output output/sequence/$sequence/MA/ins180_m=4_j=40_t=60_sw=l_dens=s_var=20.txt --objective 2 --iterations 1000 --runs 1 --sequence $sequence
  # ../../imp/testManager --instance instancias_txt/SSP-NPM-II/ins180_m=4_j=40_t=60_sw=l_dens=s_var=20.txt --output output/sequence/$sequence/FL/ins180_m=4_j=40_t=60_sw=l_dens=s_var=20.txt --objective 3 --iterations 1000 --runs 1 --sequence $sequence

  # ../../imp/testManager --instance instancias_txt/SSP-NPM-II/ins500_m=6_j=80_t=120_sw=l_dens=s_var=20.txt --output output/sequence/$sequence/TS/ins500_m=6_j=80_t=120_sw=l_dens=s_var=20.txt --objective 1 --iterations 1000 --runs 1 --sequence $sequence
  # ../../imp/testManager --instance instancias_txt/SSP-NPM-II/ins500_m=6_j=80_t=120_sw=l_dens=s_var=20.txt --output output/sequence/$sequence/MA/ins500_m=6_j=80_t=120_sw=l_dens=s_var=20.txt --objective 2 --iterations 1000 --runs 1 --sequence $sequence
  # ../../imp/testManager --instance instancias_txt/SSP-NPM-II/ins500_m=6_j=80_t=120_sw=l_dens=s_var=20.txt --output output/sequence/$sequence/FL/ins500_m=6_j=80_t=120_sw=l_dens=s_var=20.txt --objective 3 --iterations 1000 --runs 1 --sequence $sequence
}

# Gerar todas as permutações da sequência "1234"
permute "1234" ""
