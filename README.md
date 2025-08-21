# Calculadora de Redes IPv4

Esse projeto conta com a inclusão de duas funções para interação com usuário via console.

## Função 1 - Extração de dados de um endereço IP com máscara conhecida
Nessa primeira função, o usuário irá fornecer dois dados de entrada:
  * Endereço IP em formato de 8 bytes (Ex.: "192.168.0.1");
  * Máscara desse IP, seja em formato inteiro, ou seja, CIDR (Ex.: "24") ou em formato de 8 Bytes, em estrutura de octetos (Ex.: "255.255.255.0").

O sistema vai analisar o IP fornecido em conjunto com a máscara e retornar:
  * Classe do endereço IP;
  * Quantidade de bits direcionados a sub-redes;
  * Quantidade de sub-redes possíveis;
  * Quantidade de bits direcionados a hosts;
  * Quantidade de hosts possíveis (incluindo os reservados);
  * IP da rede da sub-rede que o IP indicado se encontra (reservado);
  * IP de Broadcast da sub-rede que o IP indicado se encontra (reservado);
  * Máscara em formato CIDR e em 8 bytes;
  * Máscara Invertida.

## Função 2 - Calcula de máscara entre dois IPs distintos
Nessa função, o usuário fornece os seguintes dados de entrada: 
  1. Dois IPs distintos em formato de 8 bytes (Ex.: "192.168.0.1");
  2. Quantidade mínima de hosts por sub-rede (caso exista);

A partir desses dados, o sistema vai analisar os dois endereços e retornar alguns dados a depender de duas situações.
* Situação 1: Não existe uma máscara em comum entre os IPs, ou as que existem não atendem a quantidade requerida de hosts, retornando:
  - IPs informados com suas respectivas classes;
  - Quantidade de hosts solicitados, caso exista;
  
* Situação 2: Foi identificada uma máscara entre os dois IPs que atenda a quantidade mínima requerida de hosts (que será zero se não for atribuída), retornando:
  - IPs informados com suas respectivas classes;
  - IP da rede da sub-rede que se encontra cada IP indicado (reservado);
  - IP de Broadcast da sub-rede que se encontra cada IP indicado (reservado);
  - Quantidade de bits direcionados a sub-redes;
  - Quantidade de sub-redes possíveis;
  - Quantidade de bits direcionados a hosts;
  - Quantidade de hosts possíveis (incluindo os reservados);
  - Quantidade de hosts requeridos;
  - IP de gateway para cada IP indicado;
  - Máscara em formato CIDR e em 8 bytes;
  - Máscara Invertida.
