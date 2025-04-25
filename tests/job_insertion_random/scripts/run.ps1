# Caminhos e executável
$BASE_DIR = "..\..\..\"
$BIN_DIR = Join-Path $BASE_DIR "bin"
$EXE = "ssp_npm_solver.exe"
$INSTANCE = "ins320_m=4_j=60_t=60_sw=h_dens=d_var=20.txt"
$INSTANCE_PATH = Join-Path $BASE_DIR "data\instancias_txt\SSP-NPM-II\$INSTANCE"

# Verificações
if (-Not (Test-Path "$BIN_DIR\$EXE")) {
  Write-Host "❌ Erro: Executável '$BIN_DIR\$EXE' não encontrado."
  exit 1
}

if (-Not (Test-Path "$INSTANCE_PATH")) {
  Write-Host "❌ Erro: Instância '$INSTANCE_PATH' não encontrada."
  exit 1
}

function Run-Script {
  param (
    [string]$sequence
  )

  $output_dir = "..\__output\normal"
  New-Item -ItemType Directory -Force -Path "$output_dir\TS", "$output_dir\FL" | Out-Null

  $BIN_ABS = Resolve-Path "$BIN_DIR\$EXE"
  $INSTANCE_ABS = Resolve-Path "$INSTANCE_PATH"

  foreach ($objective in 1, 3) {
    switch ($objective) {
      1 { $method = "TS" }
      3 { $method = "FL" }
    }

    $output_file = "$output_dir\$method\$INSTANCE"
    $CMD = "$BIN_ABS --instance `"$INSTANCE_ABS`" --output `"$output_file`" --objective $objective --iterations 1000 --runs 30 --sequence $sequence"

    Write-Host "🚀 Rodando: $CMD"
    try {
      iex $CMD
    } catch {
      Write-Host "❌ Erro na execução"
    }
  }
}

Run-Script -sequence "2"
