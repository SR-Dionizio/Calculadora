# Documentação da Calculadora com GUI usando Tkinter

Esta documentação descreve o código-fonte fornecido para uma calculadora simples com uma interface gráfica usando a biblioteca Tkinter. A calculadora permite realizar operações básicas de adição, subtração, multiplicação e divisão, além de cálculos de porcentagem.

## Índice

1. [Requisitos](#requisitos)
2. [Instalação](#instalação)
3. [Executando a Calculadora](#executando-a-calculadora)
4. [Visão Geral do Código](#visão-geral-do-código)
5. [Personalização](#personalização)
6. [Considerações de Segurança](#considerações-de-segurança)
7. [Conclusão](#conclusão)

## Requisitos<a name="requisitos"></a>

- Python 3.x
- Biblioteca Tkinter (incluída na instalação padrão do Python)

Certifique-se de ter os requisitos acima atendidos antes de prosseguir.

## Instalação<a name="instalação"></a>

1. Baixe o código-fonte fornecido e salve-o em um arquivo com a extensão `.py`, por exemplo, `calculadora.py`.

## Executando a Calculadora<a name="executando-a-calculadora"></a>

Siga as etapas abaixo para executar a calculadora:

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde você salvou o arquivo `calculadora.py`.
3. Execute o seguinte comando: `python calculadora.py`.

A janela da calculadora será aberta, e você poderá começar a usá-la.

## Visão Geral do Código<a name="visão-geral-do-código"></a>

O código é escrito em Python e usa a biblioteca Tkinter para criar a interface gráfica da calculadora. Ele utiliza uma combinação de frames, labels e botões para construir a interface.

A lógica principal do programa está dividida em três funções principais:

- `entra_valores(valor_digitado)`: Esta função é chamada quando um botão numérico, de operação ou ponto é pressionado. Ela concatena os valores digitados para formar uma expressão matemática completa e atualiza o texto exibido na tela da calculadora.

- `calcula_valores()`: Esta função é chamada quando o botão "=" é pressionado. Ela avalia a expressão matemática atual usando a função `eval()` e exibe o resultado na tela da calculadora.

- `limpa_tela()`: Esta função é chamada quando o botão "C" é pressionado. Ela redefine a expressão matemática para uma string vazia e limpa a tela da calculadora.

Além disso, existem várias outras funções que são chamadas pelos botões da calculadora para realizar ações específicas, como calcular a porcentagem ou realizar operações matemáticas.

## Personalização<a name="personalização"></a>

Você pode personalizar a aparência da calculadora alterando os valores das variáveis de cor no início do código:

- `cor1`: Cor de fundo principal da janela da calculadora.
- `cor2`: Cor de fundo do display da calculadora.
- `cor3`: Cor de fundo dos botões numéricos e de outras oper

ações.
- `cor4`: Cor de fundo do botão de resultado ("=") e das operações de soma e subtração.
- `cor5`: Cor do texto exibido na tela da calculadora.

Sinta-se à vontade para alterar essas cores para atender às suas preferências de design.

## Considerações de Segurança<a name="considerações-de-segurança"></a>

O código fornecido usa a função `eval()` para avaliar a expressão matemática fornecida pelo usuário. É importante ter em mente que o uso da função `eval()` pode representar um risco de segurança se o código for modificado para uso em um ambiente não confiável. A função `eval()` permite a execução de qualquer código Python passado como uma string, o que pode ser explorado por usuários mal-intencionados.

Este código é fornecido apenas como um exemplo educacional para demonstrar como criar uma calculadora simples com Tkinter. Se você planeja usar este código em um ambiente não confiável, é altamente recomendável implementar validações e restrições adequadas para garantir que apenas expressões matemáticas válidas sejam avaliadas.

## Conclusão<a name="conclusão"></a>

O código fornecido para a calculadora com GUI usando Tkinter oferece uma base sólida para a criação de uma calculadora funcional com uma interface gráfica simples. Você pode usá-lo como ponto de partida para desenvolver uma calculadora mais avançada ou personalizá-lo de acordo com suas necessidades.

Espero que esta documentação tenha sido útil para entender o código-fonte e suas funcionalidades. Se você tiver alguma dúvida adicional, não hesite em perguntar.
