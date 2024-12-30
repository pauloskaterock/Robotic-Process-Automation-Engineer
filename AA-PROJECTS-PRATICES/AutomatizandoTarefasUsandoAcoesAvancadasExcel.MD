# Automatizando Tarefas Avançadas Usando Excel Advanced no Automation Anywhere

## Introdução
Neste tutorial, vamos explorar como usar o Excel Advanced no Automation Anywhere para automatizar tarefas avançadas no Excel. Vamos cobrir operações como leitura e escrita de dados, formatação de células, e uso de fórmulas.

## Pré-requisitos
- Automation Anywhere instalado
- Microsoft Excel instalado
- Conhecimento básico de RPA e Excel

## Passo 1: Configurando o Bot
1. Abra o Automation Anywhere e crie um novo bot.
2. Adicione a ação "Excel Advanced" ao seu bot.

## Passo 2: Abrindo um Arquivo Excel
1. Adicione a ação "Open Workbook" e configure o caminho do arquivo Excel que você deseja abrir.
```python
// filepath: /c:/Robotic-Process-Automation-Engineer/AA-PROJECTS-PRATICES/AutomatizandoTarefasUsandoAcoesAvancadasExcel.MD
Excel Advanced -> Open Workbook
    - File Path: "C:\\caminho\\para\\seu\\arquivo.xlsx"




Passo 3: Lendo Dados de uma Planilha
Adicione a ação "Get Cells" para ler dados de uma célula ou intervalo de células.

Excel Advanced -> Get Cells
    - Sheet Name: "Sheet1"
    - Cell Range: "A1:B10"
    - Save to Variable: $ExcelData$



Passo 4: Escrevendo Dados em uma Planilha
Adicione a ação "Set Cells" para escrever dados em uma célula ou intervalo de células.

Excel Advanced -> Set Cells
    - Sheet Name: "Sheet1"
    - Cell Range: "C1"
    - Value: "Texto de Exemplo"



Passo 5: Aplicando Formatação
Adicione a ação "Format Cells" para aplicar formatação às células.

Excel Advanced -> Format Cells
    - Sheet Name: "Sheet1"
    - Cell Range: "A1:A10"
    - Format: "Bold"



Passo 6: Usando Fórmulas
Adicione a ação "Set Cells" para inserir uma fórmula em uma célula.

Excel Advanced -> Set Cells
    - Sheet Name: "Sheet1"
    - Cell Range: "D1"
    - Value: "=SUM(A1:A10)"


Passo 7: Salvando e Fechando o Arquivo
Adicione a ação "Save Workbook" para salvar as alterações.

Excel Advanced -> Save Workbook

Adicione a ação "Close Workbook" para fechar o arquivo Excel.

Excel Advanced -> Close Workbook



