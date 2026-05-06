# Sistema de Gestão para Rede de Cinemas

## Levantamento de Requisitos e Regras de Negócio

Este documento apresenta os requisitos funcionais principais e as regras de negócio essenciais para o desenvolvimento de um sistema de informação voltado ao gerenciamento de uma rede de cinemas.

---

## Requisitos Funcionais

### RF01 – Cadastro de Cinemas
O sistema deve permitir cadastrar cinemas contendo:
- nome da unidade;
- capacidade de público;
- endereço completo.

### RF02 – Cadastro de Filmes
O sistema deve permitir cadastrar filmes contendo:
- título;
- duração;
- gênero;
- diretor;
- elenco.

### RF03 – Gerenciamento de Sessões
O sistema deve permitir cadastrar sessões associando:
- filme;
- cinema;
- data;
- horário de exibição.

### RF04 – Registro de Público
O sistema deve permitir registrar diariamente a quantidade de público presente em cada sessão.

### RF05 – Consulta de Programação
O sistema deve permitir consultar:
- filmes em cartaz;
- sessões disponíveis por cinema.

### RF06 – Relatórios de Público
O sistema deve permitir consultar total de público:
- por sessão;
- por filme;
- por cinema.

### RF07 – Consulta de Informações de Filmes
O sistema deve permitir consultar informações detalhadas dos filmes, incluindo:
- elenco;
- diretor;
- gênero.

---

## Regras de Negócio

### RN01 – Capacidade Máxima do Cinema
A quantidade de público registrada em uma sessão não pode ultrapassar a capacidade máxima do cinema.

### RN02 – Duração da Sessão
O horário de término da sessão deve ser calculado com base no horário de início e duração do filme.

### RN03 – Intervalo Obrigatório
Deve existir um intervalo mínimo obrigatório entre sessões consecutivas no mesmo cinema.

### RN04 – Associação Obrigatória
Toda sessão deve estar obrigatoriamente vinculada a:
- um cinema;
- um filme.

### RN05 – Registro Diário
O público de cada sessão deve ser registrado individualmente a cada dia de exibição.

---

## Objetivo do Sistema

Centralizar e organizar informações da rede de cinemas, permitindo:
- controle de filmes em cartaz;
- gerenciamento de sessões;
- acompanhamento de público;

de forma confiável, estruturada e de fácil manutenção.
