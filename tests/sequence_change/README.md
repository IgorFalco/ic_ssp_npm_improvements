# Teste de Sequências - VND

Avalia como a ordem das buscas locais no VND (Variable Neighborhood Descent)
influencia os resultados de otimização.

## Objetivo

Identificar a melhor sequência de buscas locais para cada métrica de otimização.

## Estrutura

O VND utiliza 4 buscas locais aplicadas conforme uma sequência:

1. jobExchangeLocalSearch()
2. jobInsertionLocalSearch()
3. swapLocalSearch()
4. twoOptLocalSearch()

A cada melhoria, a sequência reinicia. Caso contrário, segue para a próxima.

## Métricas Otimizadas

- TS: Tool Switches
- MA: Makespan
- FL: Flowtime

## Análise

- Cada sequência é testada com diferentes objetivos.
- Os resultados são extraídos dos logs e salvos em CSVs.
- Boxplots são gerados para comparação de desempenho entre as sequências.

## Diretórios

```plaintext
results/
  └─ {sequência}/
       ├─ TS_results.csv
       ├─ MA_results.csv
       └─ FL_results.csv

grafics/
  └─ TS/
       ├─ TS_boxplot.png
       ├─ MA_boxplot.png
       └─ FL_boxplot.png
  └─ MA/
       ├─ TS_boxplot.png
       ├─ MA_boxplot.png
       └─ FL_boxplot.png
  └─ FL/
       ├─ TS_boxplot.png
       ├─ MA_boxplot.png
       └─ FL_boxplot.png
```
