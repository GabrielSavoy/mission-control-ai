# Mission Control AI 🚀

Sistema inteligente de monitoramento de missão espacial desenvolvido em Python.

## Descrição

O Mission Control AI simula o monitoramento de uma missão espacial experimental.
O sistema analisa 6 ciclos de monitoramento, classifica cada ciclo, gera alertas
automáticos e apresenta um relatório final com a situação da operação.

## Equipe — The Dreamers

| Nome | RM |
|------|----|
| Gabriel Savoy | 568991 |
| Victor Vidigal | 571318 |


## Sensores monitorados

| Sensor | Normal | Atenção | Crítico |
|--------|--------|---------|---------|
| Temperatura | 18°C a 30°C | abaixo de 18°C ou 30°C a 35°C | acima de 35°C |
| Comunicação | 60% ou mais | 30% a 59% | abaixo de 30% |
| Bateria | 50% ou mais | 20% a 49% | abaixo de 20% |
| Oxigênio | 90% ou mais | 80% a 89% | abaixo de 80% |
| Estabilidade | 70% ou mais | 40% a 69% | abaixo de 40% |

## Pontuação de risco

- NORMAL = 0 ponto
- ATENÇÃO = 1 ponto
- CRÍTICO = 2 pontos
- Pontuação máxima por ciclo: 10 pontos

## Classificação dos ciclos

- 0 a 2 pontos → MISSÃO ESTÁVEL
- 3 a 5 pontos → MISSÃO EM ATENÇÃO
- 6 a 10 pontos → MISSÃO CRÍTICA

## FIAP — GS2026.1
