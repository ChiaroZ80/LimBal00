# lim_bal - Comunicação Serial & Visualização de Dados

**README em:** [English](../README.md) | [Português](README_pt-br.md) | [Español](README_es.md) | [Deutsch](README_de.md) | [Français](README_fr.md)

---

## Visão Geral

lim_bal é uma aplicação desktop para comunicação serial e visualização de dados em tempo real. Conecte-se a Arduino ou outros dispositivos seriais, colete medidas numéricas e crie gráficos. A interface está disponível em inglês, português, espanhol, alemão e francês.

![lim_bal screenshot](shot.png)

![lim_bal screenshot](shot_stacked.png)

## Recursos

### 🌍 **Múltiplos Idiomas**
- Disponível em inglês, português, espanhol, alemão e francês
- Altere o idioma pelo menu (requer reinicialização)
- Todas as configurações preservadas ao trocar idiomas

### 📡 **Conexão Serial Fácil**
- Conecte a dispositivos seriais reais (Arduino, sensores, etc.)
- Modo de simulação integrado para testes sem hardware
- Detecção automática de portas com atualização em um clique
- Compatibilidade completa com taxas de transmissão do Arduino IDE (300-2000000 bps)
- Baudrate padrão: 9600
- Comandos rápidos: SI, SIR, Zerar e Tara
- Envio de texto personalizado com CRLF acrescentado

### 📊 **Visualização de Dados Profissional**
- **Gráficos de Série Temporal**: Plote até 5 colunas de dados simultaneamente
- **Gráficos de Área Empilhada**: Compare dados como valores absolutos ou porcentagens
- **Aparência Personalizável**: Escolha cores, marcadores e tipos de linha para cada série de dados
- **Atualizações em Tempo Real**: Taxas de atualização configuráveis (1-30 FPS)
- **Exportação**: Salve gráficos como imagens PNG de alta qualidade
- **Controles Interativos**: Pause/retome gráficos, zoom e panorâmica
- **Controles do Dispositivo**: Botões SI, SIR e Stop na aba Gráfico

### 💾 **Gerenciamento Inteligente de Dados**
- **Salvar/Carregar Manual**: Exporte e importe seus dados a qualquer momento
- **Backup Automático**: Salvamento automático opcional com nomes de arquivo com timestamp
- **Segurança de Dados**: Limpe dados com confirmações
- **Todas as Configurações Salvas**: Preferências automaticamente preservadas entre sessões
- **Plot data**: Escolha se medidas recebidas serão gravadas em Dados e usadas nos gráficos
- **Receive data**: Veja todas as linhas recebidas, com contador e tempo desde a conexão

## Primeiros Passos

### Requisitos
- Python 3.7 ou mais recente
- Conexão com a internet para instalação de dependências

### Instalação
```bash
# Clonar o repositório
git clone https://github.com/ChiaroZ80/LimBal00.git
cd LimBal00

# Criar e ativar um ambiente virtual
python -m venv .venv
# Prompt de Comando: .venv\Scripts\activate.bat
# PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

# Instalar dependências e executar lim_bal
python -m pip install matplotlib pyserial PyYAML
python lim_bal.py
```

### Primeiros Passos
1. **Idioma**: Escolha seu idioma no menu Idioma
2. **Conexão**: Em Configuração, selecione a porta serial e o baudrate e conecte
3. **Recepção**: Veja as linhas e o tempo decorrido em Receive data
4. **Dados**: Ative Plot data para gravar medidas numéricas em Dados e usá-las nos gráficos
5. **Visualização**: Use Gráfico para plotar ou enviar SI, SIR e Stop

## Como Usar

### Aba Configuração
- **Modo**: Escolha "Hardware" para dispositivos reais, "Simulado" para testes
- **Porta**: Selecione sua porta serial (clique em Atualizar para atualizar a lista)
- **Taxa de Transmissão**: Defina a velocidade (padrão: 9600; combine com o dispositivo)
- **Plot data**: Ative/desative o registro dos valores recebidos em Dados
- **SI / SIR / Zerar / Tara**: Envie o comando correspondente ao dispositivo
- **Enviar dados**: Envie texto personalizado seguido de CRLF
- **Receive data**: Veja todas as linhas recebidas com contador e tempo em segundos
- **Conectar / Desconectar**: Inicie ou encerre a conexão de hardware

### Aba Dados
- **Ver Dados**: Veja medidas numéricas, contador e tempo quando Plot data está ativo
- **Salvar Dados**: Exporte dados atuais para um arquivo de texto
- **Carregar Dados**: Importe arquivos de dados salvos anteriormente
- **Limpar Dados**: Redefina o conjunto de dados atual (com confirmação)
- **Salvamento Automático**: Ative/desative backup automático com nomes de arquivo com timestamp

### Aba Gráfico
- **Escolher Colunas**: Selecione eixo X e até 5 colunas do eixo Y dos seus dados
- **Tipos de Gráfico**:
  - **Série Temporal**: Gráficos de linha/dispersão individuais para cada série de dados
  - **Área Empilhada**: Gráficos em camadas mostrando dados cumulativos ou porcentagens
- **Personalizar**: Expanda "Mostrar Opções Avançadas" para alterar cores, marcadores, taxa de atualização
- **Exportar**: Salve seus gráficos como imagens PNG
- **Controle**: Pause/retome atualizações em tempo real a qualquer momento
- **SI / SIR**: Envie comandos ao dispositivo pela aba Gráfico
- **Stop**: Envia `@` seguido de CRLF; a próxima linha não entra em Dados, mas continua visível em Receive data

### Menu Idioma
- **Trocar Idioma**: Selecione entre 5 idiomas disponíveis
- **Reinicialização Necessária**: A aplicação solicitará reinicialização para mudança de idioma
- **Configurações Preservadas**: Todas as suas preferências são mantidas ao trocar idiomas

## Formato de Dados

Seu dispositivo serial deve enviar dados em formato de texto simples:

```
# Linhas de dados numéricos (separadas por espaço ou tab)
1.0 3.3 0.125 25.4
2.0 3.2 0.130 25.6
3.0 3.4 0.122 25.2
```

**Formatos suportados:**
- Colunas separadas por espaço ou tab
- Números em qualquer coluna
- Linhas de protocolo/status sem medidas numéricas não são adicionadas a Dados
- Streaming em tempo real ou carregamento de dados em lote

## Solução de Problemas

**Problemas de Conexão:**
- Certifique-se de que seu dispositivo está conectado e ligado
- Verifique se nenhum outro programa está usando a porta serial
- Tente diferentes taxas de transmissão se os dados aparecerem corrompidos
- Use o modo Simulado para testar a interface sem hardware

**Problemas de Dados:**
- Certifique-se de que os dados estão separados por espaço ou tab
- Verifique se os números estão em formato padrão (use . para decimais)
- Verifique se seu dispositivo está enviando dados continuamente
- Tente salvar e recarregar dados para verificar o formato

**Performance:**
- Diminua a taxa de atualização se os gráficos estiverem lentos
- Reduza o tamanho da janela de dados para melhor performance
- Feche outros programas se o sistema ficar lento

## Desenvolvimento

Esta aplicação é construída com Python e usa tkinter para a interface e matplotlib para gráficos.

**Para desenvolvedores:**
- A base de código usa uma arquitetura modular com componentes separados para GUI, gerenciamento de dados e visualização
- Traduções são armazenadas em arquivos YAML no diretório `languages/`
- A configuração usa um sistema de preferências hierárquico salvo em `config/prefs.yml`
- O sistema de atualização de gráficos é desacoplado da chegada de dados para performance ótima

## Licença

Desenvolvido por CBPF-LIM (Centro Brasileiro de Pesquisas Físicas - Laboratório de Luz e Matéria).

---

**lim_bal** - Comunicação serial e visualização de dados.