
# 

---

# PROJETO DE BASE DE DADOS

## 1. Levantamento e Análise de Requisitos

### Compreensão das Necessidades do Negócio

- Primeiro passo crucial
- Compreender o propósito da base de dados, dados a armazenar e utilização
- Realizar entrevistas, analisar sistemas existentes, rever documentação


### Definição dos Requisitos de Dados

- Identificar entidades (ex: clientes, produtos, encomendas)
- Determinar atributos de cada entidade
- Definir relações entre entidades


### Definição dos Requisitos Funcionais

- Especificar operações suportadas pela base de dados
- Delinear requisitos de interface do utilizador


### Definição dos Requisitos Não Funcionais

- Abordar desempenho, segurança, escalabilidade e fiabilidade
- Considerar volume de dados, carga de utilizadores e políticas de segurança


## 2. Desenho Conceptual da Base de Dados

### Modelação Entidade-Relacionamento (ER)

- Criar diagrama ER para representação visual
- Fornecer visão geral de alto nível da estrutura


### Modelação de Dados

- Refinar modelo ER
- Definir tipos de dados, restrições e relações com maior precisão


## 3. Desenho Lógico da Base de Dados

### Esquema Relacional

- Traduzir modelo conceptual em esquema relacional
- Escolher tipos de dados apropriados
- Definir chaves primárias e estrangeiras


### Normalização

- Aplicar técnicas de normalização (1FN, 2FN, 3FN)
- Reduzir redundância e melhorar integridade dos dados


## 4. Desenho Físico da Base de Dados

### Seleção do Sistema de Gestão de Base de Dados (SGBD)

- Escolher SGBD adequado (ex: SQLite, MySQL, PostgreSQL, Oracle)


### Otimização de Armazenamento

- Determinar estruturas de armazenamento ideais
- Considerar volume de dados, padrões de acesso e recursos de hardware


### Implementação de Segurança

- Definir funções e permissões de utilizadores
- Implementar medidas de segurança para dados sensíveis


### Cópia de Segurança e Recuperação

- Planear cópia de segurança e recuperação de desastres


## 5. Implementação da Base de Dados

### Criação da Base de Dados

- Utilizar SGBD para criar esquema e tabelas
- Definir restrições, índices e outros objetos


### Carregamento de Dados

- Preencher base de dados com dados iniciais


### Desenvolvimento de Aplicações

- Criar aplicações que interajam com a base de dados


### Criação de Triggers e Procedimentos Armazenados

- Automatizar tarefas e impor lógica de negócio


## 6. Testes e Validação

### Testes Unitários

- Testar componentes individuais


### Testes de Integração

- Testar interações entre componentes


### Testes de Desempenho

- Avaliar desempenho sob várias cargas


### Testes de Aceitação do Utilizador (UAT)

- Permitir testes pelos utilizadores finais


## 7. Implementação e Manutenção

### Implementação

- Implementar base de dados e aplicações em produção


### Monitorização

- Monitorizar desempenho e disponibilidade


### Manutenção

- Realizar tarefas de manutenção regulares


### Atualizações e Melhorias

- Atualizar base de dados conforme mudança de requisitos

