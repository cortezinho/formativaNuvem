# 💼 Sistema de Gestão Modular - Vida+ Saúde

Este projeto implementa um sistema de gestão modular baseado em microserviços para uma rede de clínicas médicas em expansão. A arquitetura foi projetada para oferecer **escalabilidade**, **manutenibilidade** e **integração** com parceiros externos.

## 🔧 Tecnologias Utilizadas

- **Python + Flask**: desenvolvimento de APIs RESTful
- **Docker + Docker Compose**: containerização e orquestração dos serviços
- **HTML + JavaScript**: interface web simples para testar o sistema
- **Requests**: comunicação entre microserviços
- **Integração Horizontal**: comunicação entre serviços internos
- **Integração Vertical**: comunicação com serviço externo simulado

---

## 🧱 Arquitetura

O sistema é composto pelos seguintes microserviços:

| Serviço      | Porta | Função Principal                             |
|--------------|-------|----------------------------------------------|
| Paciente     | 5001  | Cadastro e consulta de pacientes             |
| Consulta     | 5002  | Agendamento e listagem de consultas          |
| Prontuário   | 5003  | Registro e consulta de diagnósticos médicos  |
| Faturamento  | 5004  | Geração de faturas e validação de cobertura  |
| Plano Saúde (Mock) | 5005 | Serviço externo para simular operadora de plano |

Todos os serviços são executados em containers separados via Docker Compose e se comunicam usando chamadas HTTP com JSON.

---

## 🚀 Como Executar o Sistema

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/sistema-clinica-modular.git
cd sistema-clinica-modular
# 💼 Sistema de Gestão Modular - Vida+ Saúde

Este projeto implementa um sistema de gestão modular baseado em microserviços para uma rede de clínicas médicas em expansão. A arquitetura foi projetada para oferecer **escalabilidade**, **manutenibilidade** e **integração** com parceiros externos.

## 🔧 Tecnologias Utilizadas

- **Python + Flask**: desenvolvimento de APIs RESTful
- **Docker + Docker Compose**: containerização e orquestração dos serviços
- **HTML + JavaScript**: interface web simples para testar o sistema
- **Requests**: comunicação entre microserviços
- **Integração Horizontal**: comunicação entre serviços internos
- **Integração Vertical**: comunicação com serviço externo simulado

---

## 🧱 Arquitetura

O sistema é composto pelos seguintes microserviços:

| Serviço      | Porta | Função Principal                             |
|--------------|-------|----------------------------------------------|
| Paciente     | 5001  | Cadastro e consulta de pacientes             |
| Consulta     | 5002  | Agendamento e listagem de consultas          |
| Prontuário   | 5003  | Registro e consulta de diagnósticos médicos  |
| Faturamento  | 5004  | Geração de faturas e validação de cobertura  |
| Plano Saúde (Mock) | 5005 | Serviço externo para simular operadora de plano |

Todos os serviços são executados em containers separados via Docker Compose e se comunicam usando chamadas HTTP com JSON.

---

## 🚀 Como Executar o Sistema

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/cortezinho/formativaNuvem
