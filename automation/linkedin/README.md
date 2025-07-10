# 🚀 Sistema Automatizado de Postagem LinkedIn - RMMS Tech

Sistema para gerar conteúdo semanal sobre FinOps, Cloud Computing e DevOps automaticamente.
**Versão bilingue: Português e Inglês**

## 📋 **Funcionalidades**

- ✅ Geração automática de artigos técnicos em PT-BR e EN
- ✅ Controle de duplicatas por palavras-chave
- ✅ Agendamento semanal (segunda às 9h)
- ✅ Interface para revisão manual
- ✅ Configuração flexível via JSON
- ✅ Visualização completa de artigos

## 🛠️ **Instalação**

### 1. **Pré-requisitos**
```bash
# Python 3.8+
python3 --version

# Pip atualizado
pip3 install --upgrade pip
```

### 2. **Instalar dependências**
```bash
cd automation/linkedin
pip3 install -r requirements.txt
```

### 3. **Configurar API Keys**

#### **OpenAI API Key**
1. Acesse: https://platform.openai.com/api-keys
2. Crie uma nova API key
3. Copie a chave
4. Edite `config/config.json`:
```json
{
  "openai_api_key": "sk-sua_chave_aqui",
  "modelo_gpt": "gpt-4"
}
```

## 🎯 **Como Usar**

### **Comandos Disponíveis**

```bash
# Iniciar sistema agendado (padrão)
python3 main.py

# Gerar conteúdo bilingue manualmente
python3 main.py --gerar

# Listar posts pendentes
python3 main.py --listar

# Ver artigo completo (substitua ID pelo ID real)
python3 main.py --ver abc12345

# Ver ajuda
python3 main.py --ajuda
```

### **Fluxo de Trabalho**

1. **Geração Automática** (segunda às 9h)
   - Sistema gera artigos em PT-BR e EN automaticamente
   - Salva em `posts/pendentes/`

2. **Revisão Manual**
   ```bash
   # Listar posts pendentes
   python3 main.py --listar
   
   # Ver artigo completo
   python3 main.py --ver ID_DO_ARTIGO
   ```

3. **Publicação**
   - Revise o conteúdo gerado (PT-BR e EN)
   - Copie para LinkedIn (pessoa física ou página da empresa)
   - Mova arquivo para `posts/publicados/`

## 📁 **Estrutura de Arquivos**

```
automation/linkedin/
├── main.py                 # Sistema principal
├── generate_article.py     # Gerador de conteúdo bilingue
├── requirements.txt        # Dependências
├── README.md              # Este arquivo
├── .gitignore             # Proteção de dados sensíveis
├── config/
│   └── config.json        # Configurações
└── posts/
    ├── pendentes/         # Posts aguardando revisão
    └── publicados/        # Posts já publicados
```

## ⚙️ **Configuração**

### **config/config.json**
```json
{
  "openai_api_key": "sua_chave_aqui",
  "modelo_gpt": "gpt-4",
  "topicos_finops_pt": [
    "Otimização de custos AWS",
    "Migração de workloads para cloud",
    "Implementação de FinOps"
  ],
  "topicos_finops_en": [
    "AWS Cost Optimization",
    "Workload Migration to Cloud",
    "FinOps Implementation"
  ],
  "palavras_chave_proibidas": []
}
```

### **Personalizar Tópicos**
Edite `config/config.json` para adicionar seus próprios tópicos:

```json
{
  "topicos_finops_pt": [
    "Seu tópico personalizado PT 1",
    "Seu tópico personalizado PT 2"
  ],
  "topicos_finops_en": [
    "Your custom topic EN 1",
    "Your custom topic EN 2"
  ]
}
```

## 🌍 **Publicação no LinkedIn**

### **Onde Publicar:**

#### **1. Como Pessoa Física (renattosanttos)**
- Use o artigo em português
- Foco em networking pessoal
- Tom mais informal

#### **2. Na Página da Empresa (RMMS Tech)**
- Use o artigo em inglês
- Foco em posicionamento empresarial
- Tom mais profissional

### **Estratégia Recomendada:**
- **Segunda:** Postar na página da empresa (inglês)
- **Quarta:** Postar como pessoa física (português)
- **Sexta:** Repostar conteúdo de sucesso

## 🔧 **Agendamento Automático**

### **Opção 1: Usando o sistema interno**
```bash
python3 main.py
# Sistema roda em background e executa toda segunda às 9h
```

### **Opção 2: Usando cron (Linux/Mac)**
```bash
# Editar crontab
crontab -e

# Adicionar linha:
0 9 * * 1 cd /caminho/para/automation/linkedin && python3 main.py --gerar
```

### **Opção 3: Windows Task Scheduler**
1. Abra "Agendador de Tarefas"
2. Crie nova tarefa
3. Configure para executar toda segunda às 9h
4. Ação: `python3 main.py --gerar`

## 📊 **Monitoramento**

### **Logs do Sistema**
- ✅ Conteúdo bilingue gerado com sucesso
- ⚠️ Conteúdo duplicado (gerando novo)
- ❌ Erros de API ou configuração

### **Arquivos de Controle**
- `posts/pendentes/` - Posts aguardando revisão
- `posts/publicados/` - Posts já publicados
- `config/config.json` - Configurações do sistema

## 🚨 **Solução de Problemas**

### **Erro: "API key inválida"**
```bash
# Verificar configuração
cat config/config.json

# Reconfigurar
rm config/config.json
python3 main.py --gerar
```

### **Erro: "Módulo não encontrado"**
```bash
# Instalar dependências
pip3 install -r requirements.txt
```

### **Erro: "Permissão negada"**
```bash
# Dar permissão de execução
chmod +x main.py
chmod +x generate_article.py
```

### **Erro: "Artigo não encontrado"**
```bash
# Verificar ID correto
python3 main.py --listar

# Usar ID correto
python3 main.py --ver ID_CORRETO
```

## 🔒 **Segurança**

### **Proteção de API Keys**
- ✅ Nunca commite `config/config.json` no git
- ✅ Use variáveis de ambiente em produção
- ✅ Rotacione chaves regularmente

### **Backup**
```bash
# Backup dos posts
tar -czf backup_posts_$(date +%Y%m%d).tar.gz posts/

# Backup da configuração
cp config/config.json config/config_backup.json
```

## 📈 **Próximas Funcionalidades**

- [ ] Integração com DALL-E para imagens
- [ ] Publicação automática no LinkedIn
- [ ] Análise de performance dos posts
- [ ] Integração com outras redes sociais
- [ ] Dashboard web para gestão
- [ ] Tradução automática de artigos existentes

## 🤝 **Suporte**

### **Logs Detalhados**
```bash
# Executar com debug
python3 main.py --gerar 2>&1 | tee debug.log
```

### **Verificar Status**
```bash
# Ver posts pendentes
python3 main.py --listar

# Ver configuração
cat config/config.json

# Ver artigo específico
python3 main.py --ver ID_DO_ARTIGO
```

## 💡 **Dicas de Uso**

### **Para LinkedIn Pessoal:**
- Use versão em português
- Adicione hashtags relevantes
- Interaja com comentários

### **Para Página da Empresa:**
- Use versão em inglês
- Foque em métricas e resultados
- Mantenha tom profissional

### **Otimização de Conteúdo:**
- Revise sempre antes de publicar
- Ajuste tom conforme a audiência
- Teste diferentes horários de publicação

---

**Versão:** 2.0 (Bilingue)  
**Data:** Janeiro 2025  
**Autor:** RMMS Tech

> 💡 **Dica:** Teste o sistema manualmente antes de configurar o agendamento automático! 