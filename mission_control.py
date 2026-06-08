#Cabeçario
nome_missao = "Big step"
nome_equipe = "The dreamers"

print ("=" * 40 )
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print ("=" * 40 )

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
    ]
print()

#Matriz de dados
dados_missao = [
 [24, 92, 88, 96, 90],
 [27, 80, 72, 94, 85],
 [31, 65, 58, 91, 70],
 [36, 42, 38, 87, 55],
 [39, 28, 19, 78, 35],
 [34, 55, 32, 82, 50]
    ]

#Funções
#Analisa se é Normal Atençao ou Critico e da os valores dos pontos
def analisar_temperatura(temperatura):
    if temperatura < 18:
        return "Atenção", 1, "Temperatura elevada"
    elif temperatura >= 18 and temperatura <= 30:
        return "Normal", 0, "Temperatura estável"
    elif temperatura >= 30 and temperatura <= 35:
        return "Atenção", 1, "Temperatura elevada"
    elif temperatura > 35:
        return "Crítico", 2, "Risco de superaquecimento"

def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return "Crítico", 2, "Comunicação com a base em nive crítico"
    elif comunicacao >= 30 and comunicacao <=59:
        return "Atenção", 1, "Comunicação instável"
    elif comunicacao >= 60:
        return "Normal", 0, "Comunicação estável"

def analisar_bateria(bateria):
    if bateria < 20:
        return "Crítico", 2, "Bateria em nivel crítico"
    elif bateria >= 20 and bateria <=49:
        return "Atenção", 1, "Bateria abaixo do recomendado"
    elif bateria >= 50:
        return "Normal", 0, "Energia estável"

def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return "Crítico", 2, "Oxigênio em nivel crítico"
    elif oxigenio >= 80 and oxigenio <= 89:
        return "Atenção", 1, "Oxigênio abaixo do recomendado"
    elif oxigenio >= 90:
        return "Normal", 0, "Oxigênio estável"

def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return "Crítico", 2, "Estabilidade em nivel crítico"
    elif estabilidade >= 40 and estabilidade <= 69:
        return "Atenção", 1, "Estabilidade operacional reduzida"
    elif estabilidade >=70:
        return "Normal", 0, "Estabilidade estável"

#Classificar ciclo
def classificar_ciclo(pontos):
    if pontos <= 2:
        return "Missão estável"
    elif pontos >=3 and pontos <=5:
        return "Missão em atenção"
    elif pontos >=6 and pontos <=10:
        return "Missão crítica"

#Analisar tendencia
def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "Missão piorou"
    elif riscos[-1] < riscos[0]:
        return "Missão melhorou"
    elif riscos [-1] == riscos[0]:
        return "Missão estavel"

#Recomendacoes
def gerar_recomendacao(cls_temp, cls_com, cls_bat, cls_ox, cls_est):

    indicador_geral = "AINDA NAO ANALISADO"

    print("Recomendações:")

    if cls_temp == "Crítico" or cls_temp == "Atenção":
        print("* Verificar controle térmico da missão.")
        indicador_geral = "PROBLEMA"

    if cls_com == "Crítico" or cls_com == "Atenção":
        print ("* Tentar restabelecer contato com a base.")
        indicador_geral = "PROBLEMA"

    if cls_bat == "Crítico" or cls_bat == "Atenção":
        print ("* Ativar modo de economia de energia.")
        indicador_geral = "PROBLEMA"

    if cls_ox == "Crítico" or cls_ox == "Atenção":
        print ("* Acionar protocolo de Atenção à vida.")
        indicador_geral = "PROBLEMA"

    if cls_est == "Crítico" or cls_est == "Atenção":
        print  ("* Reduzir operações não essenciais.\n")
        indicador_geral = "PROBLEMA"

    if indicador_geral != "PROBLEMA":
        print("* Manter operação normal e continuar monitoramento." )


#Identificar area mais afetada
def indentificar_area_mais_afetada(area_mais_afetada):
    maior_valor = area_mais_afetada[0]
    local = 0

    if area_mais_afetada [1] > maior_valor:
        maior_valor = area_mais_afetada[1]
        local = 1

    if area_mais_afetada [2] > maior_valor:
        maior_valor = area_mais_afetada[2]
        local = 2

    if area_mais_afetada [3] > maior_valor:
        maior_valor = area_mais_afetada[3]
        local = 3

    if area_mais_afetada [4] > maior_valor:
        maior_valor = area_mais_afetada[4]
        local = 4

    return local

#Relatorio final
def gerar_relatorio_final(riscos, area_mais_afetada):
    print("=" * 40)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 40)
    print(f"Analise C1 para C6: {analisar_tendencia(riscos)}")
    local = indentificar_area_mais_afetada(area_mais_afetada)
    print(f"Área mais afetada: {areas_monitoradas[local]}")

riscos = []
area_mais_afetada = [0,0,0,0,0]
#diz qual ciclo é 3
numero_ciclo = 1

#medias da betria
media_temp = 0
media_comu = 0
media_bat = 0
media_ox = 0
media_est = 0


for ciclo in dados_missao:
    print("-" * 40)
    print(f"CICLO {numero_ciclo}")
    numero_ciclo = numero_ciclo + 1

    temperatura = ciclo [0]
    media_temp = media_temp + temperatura
    cls_temp, pts_temp, diag_temp = analisar_temperatura(temperatura)
    print (f"Temperatura: {temperatura}ºC | {cls_temp} | {diag_temp}")

    comunicacao = ciclo [1]
    media_comu = media_comu + comunicacao
    cls_com, pts_com, diag_com = analisar_comunicacao(comunicacao)
    print (f"Comunicação: {comunicacao}% | {cls_com} | {diag_com}")

    bateria = ciclo [2]
    media_bat = media_bat + bateria
    cls_bat, pts_bat, diag_bat = analisar_bateria(bateria)
    print (f"Bateria: {bateria}% | {cls_bat} | {diag_bat}")

    oxigenio = ciclo [3]
    media_ox = media_ox + oxigenio
    cls_ox, pts_ox, diag_ox = analisar_oxigenio(oxigenio)
    print (f"Oxigênio {oxigenio}% | {cls_ox} | {diag_ox}")

    estabilidade = ciclo [4]
    media_est = media_est + estabilidade
    cls_est, pts_est, diag_est = analisar_estabilidade(estabilidade)
    print (f"Estabilidade: {estabilidade}% | {cls_est} | {diag_est}\n")

    #Contas os pontos
    pontuacao_ciclo = pts_temp + pts_com + pts_est + pts_ox + pts_bat
    status_ciclo = classificar_ciclo(pontuacao_ciclo)
    print(f"Pontuação risco do ciclo: {pontuacao_ciclo}")
    print(f"Status do ciclo: {status_ciclo}\n")

    #Analise de tendência
    riscos = riscos + [pontuacao_ciclo]
    gerar_recomendacao(cls_temp, cls_com, cls_bat, cls_ox, cls_est)

    #Area mais afetada
    area_mais_afetada[0] = area_mais_afetada[0] + pts_temp
    area_mais_afetada[1] = area_mais_afetada[1] + pts_com
    area_mais_afetada[2] = area_mais_afetada[2] + pts_bat
    area_mais_afetada[3] = area_mais_afetada[3] + pts_ox
    area_mais_afetada[4] = area_mais_afetada[4] + pts_est

gerar_relatorio_final(riscos, area_mais_afetada)
print()
print(f"Média da temperatura: {media_temp/numero_ciclo:.2f} ºC")
print(f"Média da comunicação: {media_comu/numero_ciclo:.2f} %")
print (f"Média da bateria: {media_bat/numero_ciclo:.2f} %")
print (f"Média da oxigenio: {media_ox/numero_ciclo:.2f} %")
print (f"Média da estabilidade: {media_est/numero_ciclo:.2f} %")
