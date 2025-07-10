# Sistema Automatizado de Vídeos TikTok - RMMS Tech

Sistema completo para geração de vídeos promocionais do TikTok, incluindo roteiros, descrições otimizadas e prompts para criação de vídeo.

## 🎬 Funcionalidades

- **Geração de Roteiros**: Cria roteiros profissionais em português e inglês
- **Casos de Sucesso**: Vídeos baseados em projetos reais da RMMS Tech
- **Serviços em Destaque**: Vídeos educativos sobre cloud, IA e automação
- **Descrições Otimizadas**: Textos otimizados para engajamento no TikTok
- **Prompts de Vídeo**: Instruções detalhadas para criação visual
- **Configuração de Áudio**: Sugestões de música de fundo
- **Controle de Duplicatas**: Evita conteúdo repetitivo
- **Geração Automática de Vídeo**: Integração com APIs de IA (Runway, Pika, Synthesia, Lumen5)
- **Agendamento Semanal**: Geração automática toda terça às 10h

## 📁 Estrutura do Projeto

```
automation/tiktok/
├── main.py                    # Sistema principal
├── generate_video_content.py  # Gerador de conteúdo
├── requirements.txt           # Dependências
├── README.md                 # Este arquivo
├── config/
│   └── config.json           # Configurações do sistema
├── videos/
│   ├── pendentes/            # Vídeos aguardando revisão
│   └── publicados/           # Vídeos já publicados
└── assets/                   # Recursos (imagens, áudios)
```

## 🚀 Instalação

1. **Instalar dependências**:
```bash
pip install -r requirements.txt
```

2. **Configurar APIs (recomendado)**:
```bash
python3 setup_apis.py
```

3. **Executar pela primeira vez**:
```bash
python3 main.py --gerar
```

## 📋 Comandos Disponíveis

### Geração Manual
```bash
python3 main.py --gerar
```
Gera um vídeo TikTok manualmente com roteiro, descrição e prompt.

### Listar Vídeos Pendentes
```bash
python3 main.py --listar
```
Mostra todos os vídeos aguardando revisão.

### Ver Vídeo Completo
```bash
python3 main.py --ver abc12345
```
Mostra detalhes completos de um vídeo específico.

### Sistema Agendado
```bash
python3 main.py
```
Inicia o sistema agendado (executa toda terça às 10h).

### Ajuda
```bash
python3 main.py --ajuda
```
Mostra todos os comandos disponíveis.

## 🎯 Tipos de Conteúdo

### 1. Casos de Sucesso
- **Fintech Brasileira**: Crescimento de 300% em 18 meses
- **Rede Varejista**: Redução de 35% nos custos
- **Empresa de Saúde**: Zero vazamentos, 99,99% disponibilidade
- **Plataforma SaaS**: 28% mais retenção de clientes

### 2. Serviços em Destaque
- **Otimização de Custos Cloud**: Economia de 40%
- **Implementação de IA**: Automação de processos críticos
- **Migração para Cloud**: Migração sem downtime

## 📝 Estrutura do Conteúdo Gerado

Cada vídeo inclui:

### 🇧🇷 Versão em Português
- **Título**: Otimizado para engajamento
- **Descrição**: Com hashtags e CTA
- **Roteiro**: Estrutura detalhada por segundos
- **Prompt de Vídeo**: Instruções para criação visual

### 🇺🇸 Versão em Inglês
- **Title**: Engagement-optimized
- **Description**: With hashtags and CTA
- **Script**: Detailed structure by seconds
- **Video Prompt**: Visual creation instructions

### 🎵 Configuração de Áudio
- **Gênero**: electronic, corporate, upbeat
- **BPM**: 120-140 (ritmo ideal para TikTok)
- **Tom**: C, D, E, F, G

## 🎬 Estrutura dos Vídeos

### Duração: 35 segundos
- **[0-3s]**: Hook impactante
- **[3-8s]**: Apresentação do problema
- **[8-15s]**: Solução RMMS Tech
- **[15-25s]**: Resultados impressionantes
- **[25-30s]**: Chamada para ação
- **[30-35s]**: Créditos e contato

## 📊 Controle de Qualidade

### Verificação de Duplicatas
- Analisa palavras-chave de vídeos anteriores
- Evita conteúdo muito similar (>70% similaridade)
- Gera novo conteúdo automaticamente se necessário

### Palavras-chave Extraídas
- Remove palavras comuns (stop words)
- Foca em termos técnicos e de negócio
- Gera hashtags relevantes automaticamente

## 🔧 Configuração

### Arquivo config/config.json
```json
{
  "empresa": {
    "nome": "RMMS Tech",
    "especialidade": "Cloud Computing, IA Aplicada e Automações",
    "diferencial": "Resultados mensuráveis e ROI comprovado"
  },
  "video": {
    "duracao_padrao": 60,
    "generos": ["tech", "business", "educational"],
    "estilos": ["modern", "professional", "engaging"]
  },
  "audio": {
    "generos": ["electronic", "corporate", "upbeat"],
    "bpm_range": [120, 140],
    "keys": ["C", "D", "E", "F", "G"]
  }
}
```

## 📈 Workflow Recomendado

### Modo Manual (Sem APIs)
1. **Geração Semanal**: Sistema roda automaticamente
2. **Revisão Manual**: Verificar conteúdo gerado
3. **Criação de Vídeo**: Usar prompt fornecido
4. **Publicação**: TikTok pessoal (PT) e empresa (EN)
5. **Acompanhamento**: Monitorar engajamento

### Modo Automático (Com APIs)
1. **Geração Semanal**: Sistema roda automaticamente
2. **Geração de Vídeo**: APIs criam vídeo automaticamente
3. **Revisão Manual**: Verificar vídeo gerado
4. **Publicação**: TikTok pessoal (PT) e empresa (EN)
5. **Acompanhamento**: Monitorar engajamento

## 🎯 Dicas de Publicação

### TikTok Pessoal (Português)
- Foco em casos de sucesso brasileiros
- Linguagem mais informal e acessível
- Hashtags em português

### TikTok Empresa (Inglês)
- Foco em serviços e expertise global
- Linguagem mais profissional
- Hashtags internacionais

## 🔧 Configuração de APIs

### APIs Suportadas

#### 1. Pika Labs (Text-to-Video) - RECOMENDADO
- **Custo**: $0.10 por segundo ($3.50 por vídeo de 35s)
- **Qualidade**: Boa qualidade, rápida geração
- **Configuração**: `python3 video_generator.py --config pika_labs YOUR_API_KEY`

#### 2. Runway ML (Text-to-Video) - QUALIDADE
- **Custo**: $0.20 por segundo ($7.00 por vídeo de 35s)
- **Qualidade**: Alta qualidade, vídeos realistas
- **Configuração**: `python3 video_generator.py --config runway YOUR_API_KEY`

#### 3. Synthesia (Avatar + Roteiro)
- **Custo**: $22 por vídeo
- **Qualidade**: Avatar falando o roteiro
- **Configuração**: `python3 video_generator.py --config synthesia YOUR_API_KEY`

#### 4. Lumen5 (Vídeo com Texto)
- **Custo**: $19 por vídeo
- **Qualidade**: Vídeo com texto e imagens
- **Configuração**: `python3 video_generator.py --config lumen5 YOUR_API_KEY`

### Como Configurar (Recomendado)

#### 🚀 Configuração Rápida (Pika Labs + Runway ML)
```bash
# Configuração automática das APIs recomendadas
python3 setup_apis.py

# Ou configuração individual
python3 setup_apis.py --individual
```

#### 🔧 Configuração Manual
```bash
# Listar APIs disponíveis
python3 video_generator.py --list

# Configurar API (exemplo: Pika Labs)
python3 video_generator.py --config pika_labs YOUR_API_KEY

# Testar API
python3 video_generator.py --test pika_labs
```

## 🔄 Próximos Passos

1. **Configurar APIs**: Escolher e configurar APIs de vídeo
2. **Análise de Performance**: Métricas de engajamento
3. **Personalização Avançada**: A/B testing de formatos
4. **Expansão de Templates**: Mais tipos de conteúdo

## 📞 Suporte

Para dúvidas ou sugestões:
- Email: contato@rmms.tech
- WhatsApp: +55 (71) 99130-6561
- LinkedIn: linkedin.com/in/renattosanttos

---

**RMMS Tech** - Transformação Digital com Resultados Mensuráveis 🚀 