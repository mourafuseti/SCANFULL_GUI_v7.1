# 👋🏻 Leonardo de Moura Fuseti

Estudante de Defesa Cibernetica no Polo Estacio Piumhi MG . Formação tecnica em Tecnico em Redes de Computadores no IFMG Bambui MG , intusiasta na programação gostando muito de Python e evoluindo dia a dia .

### Conecte-se comigo

[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://www.dio.me/users/mourafuseti)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:mourafuseti@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=30A3DC)](https://www.linkedin.com/in/leonardo-moura-fuseti-4052b0359/)

### Habilidades

![HTML](https://img.shields.io/badge/HTML-000?style=for-the-badge&logo=html5&logoColor=30A3DC)
![CSS3](https://img.shields.io/badge/CSS3-000?style=for-the-badge&logo=css3&logoColor=E94D5F)
![JavaScript](https://img.shields.io/badge/JavaScript-000?style=for-the-badge&logo=javascript&logoColor=F0DB4F)
![Sass](https://img.shields.io/badge/SASS-000?style=for-the-badge&logo=sass&logoColor=CD6799)
![Bootstrap](https://img.shields.io/badge/bootstrap-000?style=for-the-badge&logo=bootstrap&logoColor=553C7B)
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)

### GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=mourafuseti&theme=transparent&bg_color=000&border_color=30A3DC&show_icons=true&icon_color=30A3DC&title_color=E94D5F&text_color=FFF)

Aqui está um **README.md** profissional, completo e bem formatado para o seu projeto **SCANFULL v7.1**, com base no código fornecido:

---
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-Proprietary-red)
![Version](https://img.shields.io/badge/Version-7.1-orange)

```markdown
# SCANFULL v7.1



> **Ferramenta de Reconhecimento e Varredura de Rede com Interface Gráfica (GUI)**  
> Desenvolvida por **Leonardo de Moura Fuseti**  
> Copyright © 2025 - Todos os direitos reservados

---

## Descrição

O **SCANFULL v7.1** é uma ferramenta de segurança da informação com interface gráfica (GUI) desenvolvida em **Python 3** utilizando **Tkinter**. Ela integra comandos populares de reconhecimento, varredura de rede e análise de vulnerabilidades web em um único ambiente intuitivo.

Ideal para **pentesters**, **analistas de segurança** e **entusiastas de cibersegurança** que desejam automatizar tarefas comuns de forma organizada e com relatórios estruturados.

---

## Funcionalidades

| Aba | Funcionalidade | Ferramenta |
|-----|----------------|-----------|
| **Reconhecimento** | Consulta de IP, Geolocalização, Whois, Traceroute | `curl`, `whois`, `traceroute` |
| **Nmap** | Varredura de host (rápida, média, completa) e rede local | `nmap` |
| **Web Vulnerabilidades** | Varredura automatizada com Nikto em portas comuns | `nikto` |

> Todos os resultados são **salvos automaticamente** em arquivos `.txt` e `.xml` com timestamp.

---

## Interface Gráfica

![Interface SCANFULL](https://via.placeholder.com/1000x700.png?text=SCANFULL+v7.1+GUI)  
*(Captura de tela da interface - em breve)*

- Design **dark mode** com cores verde neon
- Logs em tempo real com rolagem
- Abas organizadas por funcionalidade
- Botões intuitivos e campos de entrada destacados

---

## Requisitos do Sistema

```bash
Kali Linux (recomendado) ou qualquer distro com:
- Python 3.8+
- Tkinter (incluso no Python)
- Ferramentas: nmap, nikto, whois, traceroute, curl
```

### Instalação das Dependências (Kali Linux)

```bash
sudo apt update
sudo apt install -y nmap nikto whois traceroute curl python3 python3-tk
```

---

## Como Usar

1. **Salve o script** como `scanfull.py`
2. **Dê permissão de execução**:

```bash
chmod +x scanfull.py
```

3. **Execute**:

```bash
./scanfull.py
```

> Ou: `python3 scanfull.py`

---

## Estrutura de Saída

Todos os relatórios são salvos em:

```
/home/kali/forcabruta/
```

### Exemplos de arquivos gerados:

```
scanfull_geo_192.0.2.1_20250405_143022.txt
scanfull_whois_example.com_20250405_144510.txt
scanfull_nmap_192.0.2.1_fast_20250405_150000.txt
scanfull_nmap_192.0.2.1_fast_20250405_150000.xml
scanfull_nikto_example.com_20250405_152300.txt
scanfull_nikto_example.com_20250405_152300.html
```

---

## Recursos por Aba

### 1. Reconhecimento
- **Consultar IP**: Geolocalização via [ip-api.com](http://ip-api.com)
- **Meu IP**: Mostra seu IP público
- **Whois**: Informações de registro de domínio
- **Traceroute**: Rota até o destino

### 2. Nmap
- **Scan Host**:
  - Rápido: `-F --open -T5` (top 100 portas)
  - Médio: `-p 1-1000 --open -T5`
  - Completo: `-p- --open -sV -T4` (todas as portas + versão)
- **Scan Rede Local**: Detecta gateway e escaneia `/24`

### 3. Web Vulnerabilidades
- **Nikto Scan**:
  - Detecta portas web abertas (`80, 443, 8080, 8443`)
  - Executa Nikto em HTTP/HTTPS
  - Gera relatórios em `.txt` e `.html`

---

## Personalização

- **Pasta de saída**: Alterar `OUTPUT_DIR` no código
- **Ícone**: Substituir `scanfull.ico` na mesma pasta
- **Cores**: Modificar variáveis `BG`, `FG`, etc.

---

## Avisos Legais

> **USO ÉTICO E AUTORIZADO SOMENTE**  
> Esta ferramenta foi desenvolvida para **testes de penetração autorizados** e **aprendizado em segurança da informação**.  
> O autor **não se responsabiliza** por uso indevido, ilegal ou não autorizado.

---

## Capturas de Tela

*(Adicione aqui screenshots reais da interface)*

---

## Contribuição

Contribuições são bem-vindas!  
Abra uma issue ou envie um pull request com melhorias.

---

## Licença

**Proprietária - Todos os direitos reservados**  
Código-fonte não pode ser redistribuído ou modificado sem permissão expressa do autor.

---

## Autor

**Leonardo de Moura Fuseti**  
- Segurança da Informação | Pentest | Automação  
- © 2025

---

> **"A melhor defesa começa com o melhor reconhecimento."**
```

---

