# # # # # # # # # #
#   Bibliotecas   #
# # # # # # # # # #
import os
from enum import Enum
import math

# # # # # # # # # # 
#      Classes    #
# # # # # # # # # # 
class TMenuOption(Enum):
  Exit = 0
  DetalharIP = 1
  CalcularMaskIP = 2

class TOptionMask(Enum):
  Indefinido = 0
  Inteira = 1
  MaskFormat = 2

class TEnumClassIPV4(Enum):
  A = 8
  B = 16
  C = 24

# # # # # # # # # # 
#   Constantes    #
# # # # # # # # # # 
BITS_TOTAL_IPV4 = 32
BITS_OCTETO = 8
MAX_VALUE_OCTETO = 255

# # # # # # # # # # # # # # # # # # # # # # 
#     Funções úteis de contexto geral     #
# # # # # # # # # # # # # # # # # # # # # # 
def clear_output():
    os.system('cls')

def convertBinToDec(valueBin):
  valueDecInt = 0
  exp = 0
  for i in range(len(valueBin)-1, -1, -1):
    if valueBin[i] == "1":
      valueDecInt += 2**exp
    exp += 1
  return str(valueDecInt)

def convertDecToBin(valueDec, qtdForcedChars=None):
  valueDecInt = int(valueDec)
  valueBin = ""
  while valueDecInt > 1:
    valueBin = str(valueDecInt % 2) + valueBin
    valueDecInt = valueDecInt // 2
  if valueDecInt == 1:
    valueBin = "1" + valueBin
  if qtdForcedChars:
    valueBin = valueBin.rjust(qtdForcedChars, "0")
  return valueBin

def somarBinarios(valueBin1, valueBin2):
  valueBin1 = str(valueBin1)
  valueBin2 = str(valueBin2)
  return convertDecToBin(int(valueBin1, 2) + int(valueBin2, 2))

def bitwiseOr(valueBin1, valueBin2):
  valueBin1 = str(valueBin1)
  valueBin2 = str(valueBin2)
  maxLen = max(len(valueBin1), len(valueBin2))
  valueBin1 = valueBin1.rjust(maxLen, "0")
  valueBin2 = valueBin2.rjust(maxLen, "0")
  result = ""
  for i in range(maxLen):
    if valueBin1[i] == "1" or valueBin2[i] == "1":
      result += "1"
    else:
      result += "0"
  return result

def bitwiseAnd(valueBin1, valueBin2):
  valueBin1 = str(valueBin1)
  valueBin2 = str(valueBin2)
  maxLen = max(len(valueBin1), len(valueBin2))
  valueBin1 = valueBin1.rjust(maxLen, "0")
  valueBin2 = valueBin2.rjust(maxLen, "0")
  result = ""
  for i in range(maxLen):
    if valueBin1[i] == "1" == valueBin2[i]:
      result += "1"
    else:
      result += "0"
  return result

def concatStr(listParts=[]):
  result = ""
  for part in listParts:
    result += str(part)
  return result

def concatStrWithDot(listParts=[]):
  result = ""
  for i in range(len(listParts)):
    result += str(listParts[i])
    if i < len(listParts)-1:
      result += "."
  return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   Funções de contexto específico para endereçamentos IP   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def convertIpDecToBin(addressIP):
  addressIPTupla = addressIP.split(".")
  addressIPBin = concatStr([convertDecToBin(addressIPTupla[0], BITS_OCTETO),
                           convertDecToBin(addressIPTupla[1], BITS_OCTETO),
                           convertDecToBin(addressIPTupla[2], BITS_OCTETO),
                           convertDecToBin(addressIPTupla[3], BITS_OCTETO)])
  return addressIPBin

def convertIpDecToBinWithDot(addressIP):
  addressIPTupla = addressIP.split(".")
  addressIPBin = concatStrWithDot([convertDecToBin(addressIPTupla[0], BITS_OCTETO),
                                  convertDecToBin(addressIPTupla[1], BITS_OCTETO),
                                  convertDecToBin(addressIPTupla[2], BITS_OCTETO),
                                  convertDecToBin(addressIPTupla[3], BITS_OCTETO)])
  return addressIPBin

def convertIpBinToDec(addressIP):
  if "." in addressIP:
    addressIPTupla = addressIP.split(".")
  else:
    addressIP = addressIP.rjust(BITS_TOTAL_IPV4, "0")
    addressIPTupla = [addressIP[i:i+8] for i in range(0, len(addressIP), 8)]

  print(f"addressIPTupla: {addressIPTupla}")

  addressIPDec = concatStrWithDot([convertBinToDec(addressIPTupla[0]),
                                  convertBinToDec(addressIPTupla[1]),
                                  convertBinToDec(addressIPTupla[2]),
                                  convertBinToDec(addressIPTupla[3])])
  return addressIPDec

def getMask(qtdBits):
  mask_bin = ""
  for i in range(qtdBits):
    mask_bin += "1"
  mask_bin = mask_bin.ljust(BITS_TOTAL_IPV4, "0")
  mask_dec_str = ""
  for i in range(0, BITS_TOTAL_IPV4, 8):
    if i > 0:
      mask_dec_str += "."
    mask_dec_str += convertBinToDec(mask_bin[i:i+8])
  return mask_dec_str

def getInverseMask(qtdBits):
  inverseMask_bin = ""
  for i in range(qtdBits):
    inverseMask_bin += "0"
  inverseMask_bin = inverseMask_bin.ljust(BITS_TOTAL_IPV4, "1")
  inverseMask_dec_str = ""
  for i in range(0, BITS_TOTAL_IPV4, 8):
    if i > 0:
      inverseMask_dec_str += "."
    inverseMask_dec_str += convertBinToDec(inverseMask_bin[i:i+8])
  return inverseMask_dec_str

def getBitsMask(maskDec):
  maskDecTupla = maskDec.split(".")
  bitsMask = 0
  for octetoDec in maskDecTupla:
    octetoBin = convertDecToBin(octetoDec)
    for char in octetoBin:
      if char == "1":
        bitsMask += 1
  return bitsMask

def obterClasseIp(addressIp):
  addressIpTupla = addressIp.split(".")
  firstOctetoBin = convertDecToBin(addressIpTupla[0], BITS_OCTETO)
  classeIp = TEnumClassIPV4.A
  if firstOctetoBin[0:2] == "11":
    classeIp = TEnumClassIPV4.C
  elif firstOctetoBin[0:2] == "10":
    classeIp = TEnumClassIPV4.B
  return classeIp

def obterAddressIpBase(addressIp, bitsMask):
  addressIpBin = convertIpDecToBin(addressIp)
  bitagemMask = "1"*int(bitsMask)
  bitagemMask = bitagemMask.ljust(BITS_TOTAL_IPV4, "0")
  result = bitwiseAnd(addressIpBin, bitagemMask).rjust(BITS_TOTAL_IPV4, "0")
  result = convertIpBinToDec(result)
  return result

def getDadosSubRede(bitsHosts, bitsMask, addressBase, addressIp):
  addressIpBin = convertIpDecToBin(addressIp)
  addressBaseIpBin = convertIpDecToBin(addressBase)
  bitagemHosts = "1"*int(bitsHosts)
  bitagemHosts = bitagemHosts.rjust(BITS_TOTAL_IPV4, "0")
  auxBroadcastBin = bitwiseOr(addressBaseIpBin, bitagemHosts).rjust(BITS_TOTAL_IPV4, "0")
  auxBroadcastDec = convertIpBinToDec(auxBroadcastBin)
  bitagemMask = "1"*int(bitsMask)
  bitagemMask = bitagemMask.ljust(BITS_TOTAL_IPV4, "0")
  auxAddressRedeBin = bitwiseAnd(addressBaseIpBin, bitagemMask).rjust(BITS_TOTAL_IPV4, "0")
  auxAddressRedeDec = convertIpBinToDec(auxAddressRedeBin)
  return auxAddressRedeDec, auxBroadcastDec

def detalharDadosIp(addressIp=None, bitsMask=None, maskDec=None):
  if not addressIp:
    addressIp = input("Digite um endereço IPV4 com pontos separando os 4 octetos ( Ex.: 192.168.0.1 ): " )
    op = TOptionMask.Indefinido
    while op not in (TOptionMask.Inteira, TOptionMask.MaskFormat):
      op = TOptionMask(int(input("Formato para apresentação da mascara: \n1 - Inteira \n2 - Formatada \nOpção: ")))
    if op == TOptionMask.Inteira:
      bitsMask = int(input("Digite o número inteiro correspondente a máscara do IP: " ))
    elif op == TOptionMask.MaskFormat:
      maskDec = input("Digite a máscara do IP com pontos separando os 4 octetos ( Ex.: 255.255.255.0 ): " )

  if bitsMask:
    maskDec = getMask(bitsMask)
  elif maskDec:
    bitsMask = getBitsMask(maskDec)

  maskDecInverse = getInverseMask(bitsMask)
  classeIp = obterClasseIp(addressIp)
  bitsSubRede = bitsMask - classeIp.value
  if bitsSubRede < 0:
    bitsSubRede = 0
  bitsHost = BITS_TOTAL_IPV4 - bitsMask
  qtdSubRedes = 2**bitsSubRede
  qtdHosts = 2**bitsHost
  addressBase = obterAddressIpBase(addressIp, bitsMask)
  addressRede, addressBroadcast = getDadosSubRede(bitsHost, bitsMask, addressBase, addressIp)
  showDadosFunc1(addressIp, bitsMask, maskDec, maskDecInverse, classeIp, bitsSubRede, bitsHost, addressRede, addressBroadcast)

def getMaskBetweenIps():
  addressIp1 = input("Digite o endereço IP1 com pontos separando os 4 octetos ( Ex.: 192.168.0.1 ): " )
  addressIp2 = input("Digite o endereço IP2 com pontos separando os 4 octetos ( Ex.: 192.168.0.1 ): " )
  addressIp1Bin = convertIpDecToBin(addressIp1)
  addressIp2Bin = convertIpDecToBin(addressIp2)
  classeIp1 = obterClasseIp(addressIp1)
  classeIp2 = obterClasseIp(addressIp2)

  qtdHostsRequired = 0
  if input("É necessário uma quantidade mínima de hosts por subrede? (S/N) ").upper() == "S":
    qtdHostsRequired = int(input("Digite a quantidade mínima de hosts por subrede: "))

  bitsHostRequired = 0
  if qtdHostsRequired:
    bitsHostRequired = math.log2(qtdHostsRequired)

  dictBitsCommon = {}
  if classeIp1 == classeIp2:
    for i in range(0, BITS_TOTAL_IPV4):
      isBitCommon = addressIp1Bin[i] == addressIp2Bin[i]
      if (isBitCommon==True) and (i > 0):
        isBitCommon = dictBitsCommon.get(i-1) != None
      if isBitCommon == True:
        dictBitsCommon[i] = True
      else:
        break
  else:
    for i in range(1, BITS_TOTAL_IPV4+1):
      if addressIp1Bin[-i] == "1" == addressIp2Bin[-i]:
        dictBitsCommon[BITS_TOTAL_IPV4-i] = True

  error = len(dictBitsCommon) == 0
  if not error:
    error = True
    maskDec = ""
    listBitsCommon = list(dictBitsCommon.keys())
    listBitsCommon.sort(reverse=True)
    for bitCommon in listBitsCommon:
      if error == True:
        bitsMask = bitCommon+1
        bitsHost = BITS_TOTAL_IPV4 - bitsMask
        error = (bitsHostRequired > 0) and (bitsHost < bitsHostRequired)

  if not error:
    if bitsHostRequired:
      if bitsHost < bitsHostRequired:
        error = True

  if not error:
    maskDec = getMask(bitsMask)
    maskDecInverse = getInverseMask(bitsMask)
    bitsSubRede1 = bitsMask - classeIp1.value
    bitsSubRede2 = bitsMask - classeIp2.value

    if bitsSubRede1 < 0:
      bitsSubRede1 = 0
    if bitsSubRede2 < 0:
      bitsSubRede2 = 0

    qtdSubRedes1 = 2**bitsSubRede1
    qtdSubRedes2 = 2**bitsSubRede2
    qtdHosts = 2**bitsHost
    addressBase1 = obterAddressIpBase(addressIp1, bitsMask)
    addressBase2 = obterAddressIpBase(addressIp2, bitsMask)
    addressRede1, addressBroadcast1 = getDadosSubRede(bitsHost, bitsMask, addressBase1, addressIp1)
    addressRede2, addressBroadcast2 = getDadosSubRede(bitsHost, bitsMask, addressBase2, addressIp2)
    addressRede1Tupla = addressRede1.split(".")
    addressRede2Tupla = addressRede2.split(".")
    gateway1 = concatStrWithDot(addressRede1Tupla[0:3]) + "." + str(int(addressRede1Tupla[3])+1)
    gateway2 = concatStrWithDot(addressRede2Tupla[0:3]) + "." + str(int(addressRede2Tupla[3])+1)
    showDadosFunc2(addressIp1, addressIp2, classeIp1, classeIp2,
                   addressRede1, addressRede2, addressBroadcast1, addressBroadcast2,
                   bitsSubRede1, bitsSubRede2, qtdSubRedes1, qtdSubRedes2,
                   gateway1, gateway2, maskDec, maskDecInverse,
                   bitsMask, bitsHost, qtdHosts, qtdHostsRequired)
  else:
    clear_output()
    print(f"IPs Informados: ")
    print(f"{addressIp1} - Classe {classeIp1.name}")
    print(f"{addressIp2} - Classe {classeIp2.name}")
    print(f"Quantidade de Hosts solicitados: {qtdHostsRequired}")
    print(f"Quantidade de Hosts disponíveis: {2**bitsHost}")
    print("\nNão foi possível calcular uma máscara em comum entre os IPs informados!")
    pause = input("\nPressione qualquer tecla para retornar ao Menu ...")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#    Funções em "frontend", de impressões para o usuário  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def showMenu():
  clear_output()
  print("+ - - - - - - - - - - - - - - - - - - - - +");
  print("| * * *  Informe a opção desejada * * * * |");
  print("+ - - - - - - - - - - - - - - - - - - - - +");
  print("|    1 - Detalhar IP e Máscara            |");
  print("|    2 - Calcular Máscara entre IPs       |");
  print("|                                         |");
  print("|    0 - Sair                             |");
  print("+ - - - - - - - - - - - - - - - - - - - - +");
  op = input()
  try:
    op_enum = TMenuOption(int(op))
    clear_output()
    print(f"Opção Selecionada: {op_enum.value} -> {op_enum.name}")
    return op_enum
  except ValueError:
    print("Opção inválida!")
    print("\nPressione qualquer tecla para retornar ao Menu ...")
    input()
    return showMenu

def showDadosFunc1(addressIp, bitsMask, maskDec, maskDecInverse, classeIp, bitsSubRede, bitsHost, addressRede, addressBroadcast):
  clear_output()
  print(f"Endereço IP: {addressIp}/{bitsMask} - Classe: {classeIp.name}")
  print(f"\n* * Subredes * *")
  print(f"- Bits: {bitsSubRede}")
  print(f"- Quantidade: {2**bitsSubRede}")
  print(f"\n* * Hosts * *")
  print(f"- Bits: {bitsHost}")
  print(f"- Quantidade: {2**bitsHost}")
  print(f"\n* * IPs e máscara da subrede * *")
  print(f"- IP da Rede: {addressRede}")
  print(f"- IP de Broadcast: {addressBroadcast}")
  print(f"- Máscara: {maskDec}")
  print(f"- Máscara Invertida: {maskDecInverse}")
  pause = input("\nPressione qualquer tecla para retornar ao Menu ...\n")

def showDadosFunc2(addressIp1, addressIp2, classeIp1, classeIp2,
                   addressRede1, addressRede2, addressBroadcast1, addressBroadcast2,
                   bitsSubRede1, bitsSubRede2, qtdSubRedes1, qtdSubRedes2,
                   gateway1, gateway2, maskDec, maskDecInverse,
                   bitsMask, bitsHost, qtdHosts, qtdHostsRequired):
  clear_output()
  print(f"# Dados Originais: ")
  print(f"- {addressIp1}   [Classe {classeIp1.name} /{classeIp1.value}]")
  print(f"- {addressIp2}   [Classe {classeIp2.name} /{classeIp2.value}]")
  print(f"\n# Dados Calculados:")
  print(f"- IP: {addressIp1} /{bitsMask}")
  print(f"  IP Rede: {addressRede1}")
  print(f"  IP Broadcast: {addressBroadcast1}")
  print(f"  Bits Subrede: {bitsSubRede1}")
  print(f"  Qtd Subredes: {qtdSubRedes1}")
  print(f"  Bits Host: {bitsHost}")
  print(f"  Qtd Hosts: {qtdHosts}")
  print(f"  Qtd Hosts Required: {qtdHostsRequired}")
  print(f"- IP: {addressIp2} /{bitsMask}")
  print(f"  IP Rede: {addressRede2}")
  print(f"  IP Broadcast: {addressBroadcast2}")
  print(f"  Bits Subrede: {bitsSubRede2}")
  print(f"  Qtd Subredes: {qtdSubRedes2}")
  print(f"  Bits Host: {bitsHost}")
  print(f"  Qtd Hosts: {qtdHosts}")
  print(f"  Qtd Hosts Required: {qtdHostsRequired}")
  print(f"\n# Configuração:")
  print(f"- IP: {addressIp1} /{bitsMask}")
  print(f"  Gateway: {gateway1}")
  print(f"  Máscara: {maskDec}")
  print(f"  Máscara Invertida: {maskDecInverse}")
  print(f"- IP: {addressIp2} /{bitsMask}")
  print(f"  Gateway: {gateway2}")
  print(f"  Máscara: {maskDec}")
  print(f"  Máscara Invertida: {maskDecInverse}")
  pause = input("\nPressione qualquer tecla para retornar ao Menu ...\n")

# # # # # # # # # # # # # # #
#   Bloco de funçao "main"  #
# # # # # # # # # # # # # # #
running = True
while running:
  op = showMenu()
  running = op != TMenuOption.Exit

  if op == TMenuOption.DetalharIP:
    detalharDadosIp()
  elif op == TMenuOption.CalcularMaskIP:
    getMaskBetweenIps()

print("\nA Aplicação foi encerrada!")