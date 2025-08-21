Calculadora de Redes IPv4

Esse projeto conta com a inclusão de duas funções para interação com usuário via console.

# Função 1 - Extração de dados de um endereço IP com máscara conhecida
Nessa primeira função, o usuário irá fornecer dois dados de entrada:
  1. Endereço IP em formato de 8 bytes (Ex.: "192.168.0.1");
  2. Máscara desse IP, seja em formato inteiro, ou seja, CIDR (Ex.: "24") ou em formato de 8 Bytes, em estrutura de octetos (Ex.: "255.255.255.0").
O sistema vai analisar o IP fornecido em conjunto com a máscara e retornar:
  1. Classe do endereço IP;
  2. Quantidade de bits direcionados a sub-redes;
  3. Quantidade de sub-redes possíveis;
  4. Quantidade de bits direcionados a hosts;
  5. Quantidade de hosts possíveis (incluindo os reservados);
  6. IP da rede da sub-rede que o IP indicado se encontra (reservado);
  7. IP de Broadcast da sub-rede que o IP indicado se encontra (reservado);
  8. Máscara em formato CIDR e em 8 bytes;
  9. Máscara Invertida.

# Função 2 - Cálcula de máscara entre dois IPs distintos
Nessa função, o usuário fornece os seguintes dados de entrada: 
  1. Dois IPs distintos em formato de 8 bytes (Ex.: "192.168.0.1");
  2. Quantidade mínima de hosts por sub-rede (caso exista);
A partir desses dados, o sistema vai analisar os dois endereços e retornar alguns dados a depender de duas situações:
* Situação 1: Não existe uma máscara em comum entre os IPs, ou as que existem não atendem a quantidade requerida de hosts.
Retornos nessa situação:
  1. IPs informados com suas respectivas classes;
  2. Quantidade de hosts solicitados, caso exista;
* Situação 2: Foi identificada uma máscara entre os dois IPs que atenda a quantidade mínima requerida de hosts (que será zero se não for atribuída)
Retornos nessa situação:
  1. IPs informados com suas respectivas classes;
  2. IP da rede da sub-rede que se encontra cada IP indicado (reservado);
  3. IP de Broadcast da sub-rede que se encontra cada IP indicado (reservado);
  4. Quantidade de bits direcionados a sub-redes;
  5. Quantidade de sub-redes possíveis;
  6. Quantidade de bits direcionados a hosts;
  7. Quantidade de hosts possíveis (incluindo os reservados);
  8. Quantidade de hosts requeridos;
  9. IP de gateway para cada IP indicado;
  10. Máscara em formato CIDR e em 8 bytes;
  11. Máscara Invertida.
