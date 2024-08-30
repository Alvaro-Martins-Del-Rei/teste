"""
CONSTANTE = "Variáveis" q não vou mudar
muitas condições no mesmo if (ruim)
      <- Contagem de complexidade (ruim)
"""
velocidade = 61
local_carro = 99

#para vc declara uma coisa q não vai mudar no código como velo máxima ou conexão com banco de dados
#vc põe em maiúsculo como abaixo
RADAR_1 = 60 #velocidade máxima do radar1
LOCAL_1 = 100 #local onde o radar1 está
RADAR_RANGE = 1 #a distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 + vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou no radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')