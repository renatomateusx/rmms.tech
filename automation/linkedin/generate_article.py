#!/usr/bin/env python3
"""
Gerador de Artigos FinOps - RMMS Tech
Gera conteúdo técnico sobre cloud computing, FinOps e DevOps
Versão bilingue: Português e Inglês
"""

import openai
import json
import os
import hashlib
from datetime import datetime

class GeradorConteudoFinOps:
    def __init__(self):
        self.config = self.carregar_config()
        self.palavras_chave_usadas = self.carregar_palavras_chave()
    
    def carregar_config(self):
        """Carrega configurações do arquivo config.json"""
        config_path = 'config/config.json'
        
        if not os.path.exists(config_path):
            # Criar configuração padrão
            config_padrao = {
                "openai_api_key": "",
                "modelo_gpt": "gpt-4",
                "topicos_finops_pt": [
                    "Otimização de custos AWS",
                    "Migração de workloads para cloud",
                    "Implementação de FinOps",
                    "Monitoramento de custos em tempo real",
                    "Estratégias de reserva na nuvem",
                    "Governança de recursos cloud",
                    "Automação de shutdown de recursos",
                    "Análise de custos por serviço",
                    "Otimização de instâncias EC2",
                    "Implementação de tags de custo"
                ],
                "topicos_finops_en": [
                    "AWS Cost Optimization",
                    "Workload Migration to Cloud",
                    "FinOps Implementation",
                    "Real-time Cost Monitoring",
                    "Cloud Reservation Strategies",
                    "Cloud Resource Governance",
                    "Resource Shutdown Automation",
                    "Cost Analysis by Service",
                    "EC2 Instance Optimization",
                    "Cost Tag Implementation"
                ],
                "palavras_chave_proibidas": [
                    "palavra1", "palavra2"
                ]
            }
            
            os.makedirs('config', exist_ok=True)
            with open(config_path, 'w') as f:
                json.dump(config_padrao, f, indent=2)
            
            print("⚠️ Arquivo config/config.json criado!")
            print("🔧 Configure sua API key do OpenAI antes de usar")
            return config_padrao
        
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def carregar_palavras_chave(self):
        """Carrega palavras-chave já utilizadas de pendentes E publicados"""
        palavras_chave = set()
        
        # Verificar pasta pendentes
        pasta_pendentes = 'posts/pendentes'
        if os.path.exists(pasta_pendentes):
            for arquivo in os.listdir(pasta_pendentes):
                if arquivo.endswith('.json'):
                    with open(f'{pasta_pendentes}/{arquivo}', 'r') as f:
                        post = json.load(f)
                        palavras_chave.update(post.get('palavras_chave_pt', []))
                        palavras_chave.update(post.get('palavras_chave_en', []))
        
        # Verificar pasta publicados (IMPORTANTE!)
        pasta_publicados = 'posts/publicados'
        if os.path.exists(pasta_publicados):
            for arquivo in os.listdir(pasta_publicados):
                if arquivo.endswith('.json'):
                    with open(f'{pasta_publicados}/{arquivo}', 'r') as f:
                        post = json.load(f)
                        palavras_chave.update(post.get('palavras_chave_pt', []))
                        palavras_chave.update(post.get('palavras_chave_en', []))
        
        print(f"📊 Carregadas {len(palavras_chave)} palavras-chave únicas (pendentes + publicados)")
        return palavras_chave
    
    def gerar_artigo_pt(self):
        """Gera um artigo técnico em português"""
        topicos = self.config['topicos_finops_pt']
        topico = topicos[datetime.now().weekday() % len(topicos)]
        
        prompt = f"""
        Crie um artigo técnico PROFISSIONAL e AUTORITÁRIO em PORTUGUÊS sobre: {topico}
        
        IMPORTANTE: Este artigo deve ser escrito como um especialista com 20+ anos de experiência em cloud computing e transformação digital.
        
        REQUISITOS OBRIGATÓRIOS:
        - 800-1200 palavras (conteúdo rico e detalhado)
        - Linguagem técnica mas acessível para CTOs e diretores
        - INCLUIR CASOS REAIS da RMMS Tech (fictícios mas realistas)
        - Métricas específicas e números concretos
        - Exemplos práticos de implementação
        - Call-to-action forte para consultoria especializada
        - Tom de autoridade e expertise real
        
        ESTRUTURA OBRIGATÓRIA:
        1. INTRODUÇÃO: Problema real que empresas enfrentam (com números)
        2. CASO REAL RMMS: Exemplo específico de cliente que resolvemos
        3. SOLUÇÃO TÉCNICA: Detalhes técnicos específicos da implementação
        4. RESULTADOS MENSURÁVEIS: Métricas concretas e ROI
        5. IMPLEMENTAÇÃO PRÁTICA: Passos específicos para replicar
        6. CALL-TO-ACTION: Convite para diagnóstico gratuito
        
        EXEMPLO DE CASO REAL (use como referência):
        "Recentemente, trabalhamos com uma fintech brasileira que estava gastando R$ 180.000/mês em infraestrutura AWS. Após nossa implementação de FinOps, reduzimos os custos em 65% (R$ 117.000 de economia anual) e melhoramos a performance em 40%."
        
        TOME: Especialista técnico com autoridade, não vendedor. Foque em valor real e resultados mensuráveis.
        
        EMPRESA: RMMS Tech - Consultoria em Cloud, IA Aplicada e Automação Estratégica
        ESPECIALISTA: Renato Santos (20+ anos de experiência)
        """
        
        try:
            # Criar cliente OpenAI sem configurações de proxy
            client = openai.OpenAI(
                api_key=self.config['openai_api_key'],
                timeout=60.0
            )
            response = client.chat.completions.create(
                model=self.config['modelo_gpt'],
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"❌ Erro ao gerar artigo em português: {e}")
            return None
    
    def gerar_artigo_en(self):
        """Gera um artigo técnico em inglês"""
        topicos = self.config['topicos_finops_en']
        topico = topicos[datetime.now().weekday() % len(topicos)]
        
        prompt = f"""
        Create a PROFESSIONAL and AUTHORITATIVE technical article in ENGLISH about: {topico}
        
        IMPORTANT: This article should be written as an expert with 20+ years of experience in cloud computing and digital transformation.
        
        MANDATORY REQUIREMENTS:
        - 800-1200 words (rich and detailed content)
        - Technical but accessible language for CTOs and directors
        - INCLUDE REAL RMMS TECH CASES (fictional but realistic)
        - Specific metrics and concrete numbers
        - Practical implementation examples
        - Strong call-to-action for specialized consulting
        - Tone of authority and real expertise
        
        MANDATORY STRUCTURE:
        1. INTRODUCTION: Real problem companies face (with numbers)
        2. REAL RMMS CASE: Specific example of client we solved
        3. TECHNICAL SOLUTION: Specific technical details of implementation
        4. MEASURABLE RESULTS: Concrete metrics and ROI
        5. PRACTICAL IMPLEMENTATION: Specific steps to replicate
        6. CALL-TO-ACTION: Invitation for free diagnosis
        
        REAL CASE EXAMPLE (use as reference):
        "Recently, we worked with a Brazilian fintech that was spending $35,000/month on AWS infrastructure. After our FinOps implementation, we reduced costs by 65% ($273,000 annual savings) and improved performance by 40%."
        
        TONE: Technical expert with authority, not salesperson. Focus on real value and measurable results.
        
        COMPANY: RMMS Tech - Cloud, Applied AI and Strategic Automation Consulting
        EXPERT: Renato Santos (20+ years of experience)
        """
        
        try:
            # Criar cliente OpenAI sem configurações de proxy
            client = openai.OpenAI(
                api_key=self.config['openai_api_key'],
                timeout=60.0
            )
            response = client.chat.completions.create(
                model=self.config['modelo_gpt'],
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"❌ Erro ao gerar artigo em inglês: {e}")
            return None
    
    def gerar_artigo(self):
        """Gera artigos em português e inglês"""
        print("🌍 Gerando artigos em português e inglês...")
        
        artigo_pt = self.gerar_artigo_pt()
        artigo_en = self.gerar_artigo_en()
        
        if not artigo_pt or not artigo_en:
            print("❌ Erro na geração de artigos")
            return None
        
        return {
            'pt': artigo_pt,
            'en': artigo_en
        }
    
    def extrair_palavras_chave(self, texto, idioma='pt'):
        """Extrai palavras-chave do texto"""
        if not texto:
            return set()
        
        # Palavras comuns para remover
        stop_words_pt = {
            'para', 'com', 'uma', 'mais', 'como', 'mas', 'seu', 'sua',
            'ser', 'ter', 'estar', 'fazer', 'poder', 'dever', 'querer',
            'este', 'esta', 'isto', 'esse', 'essa', 'isso', 'aquele',
            'aquela', 'aquilo', 'que', 'qual', 'quem', 'onde', 'quando',
            'porque', 'porquê', 'como', 'quanto', 'tanto', 'muito',
            'pouco', 'bem', 'mal', 'melhor', 'pior', 'maior', 'menor'
        }
        
        stop_words_en = {
            'the', 'and', 'for', 'with', 'are', 'but', 'not', 'you',
            'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out',
            'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new',
            'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did',
            'its', 'let', 'put', 'say', 'she', 'too', 'use'
        }
        
        stop_words = stop_words_pt if idioma == 'pt' else stop_words_en
        
        # Limpar e tokenizar
        palavras = texto.lower().replace('\n', ' ').split()
        palavras = [p for p in palavras if len(p) > 4 and p not in stop_words]
        
        # Filtrar palavras-chave técnicas
        palavras_tecnicas = [
            'cloud', 'aws', 'azure', 'gcp', 'finops', 'devops', 'infrastructure',
            'cost', 'optimization', 'migration', 'monitoring', 'automation',
            'scalability', 'performance', 'security', 'governance'
        ]
        
        palavras_chave = set()
        for palavra in palavras:
            if any(tecnica in palavra for tecnica in palavras_tecnicas):
                palavras_chave.add(palavra)
        
        return palavras_chave
    
    def extrair_titulo(self, texto):
        """Extrai o título do artigo"""
        linhas = texto.split('\n')
        for linha in linhas:
            linha = linha.strip()
            if linha and ('Título:' in linha or 'Title:' in linha):
                return linha.replace('Título:', '').replace('Title:', '').strip()
            elif linha and len(linha) < 100 and not linha.startswith('1.') and not linha.startswith('2.'):
                return linha
        return "Artigo RMMS Tech"
    
    def verificar_duplicatas(self, palavras_chave_pt, palavras_chave_en):
        """Verifica se o conteúdo é muito similar aos anteriores"""
        if not palavras_chave_pt or not palavras_chave_en:
            return False
        
        # Verificar duplicatas em português
        palavras_repetidas_pt = palavras_chave_pt.intersection(self.palavras_chave_usadas)
        palavras_repetidas_en = palavras_chave_en.intersection(self.palavras_chave_usadas)
        
        # Critérios mais rigorosos
        duplicatas_pt = len(palavras_repetidas_pt) > 2  # Reduzido de 3 para 2
        duplicatas_en = len(palavras_repetidas_en) > 2  # Reduzido de 3 para 2
        
        if duplicatas_pt or duplicatas_en:
            print(f"⚠️ Duplicatas detectadas:")
            if duplicatas_pt:
                print(f"   🇧🇷 PT: {palavras_repetidas_pt}")
            if duplicatas_en:
                print(f"   🇺🇸 EN: {palavras_repetidas_en}")
            return True
        
        return False
    
    def mostrar_estatisticas_duplicatas(self):
        """Mostra estatísticas detalhadas de palavras-chave e duplicatas"""
        print(f"\n📊 ESTATÍSTICAS DE PALAVRAS-CHAVE")
        print("=" * 50)
        
        # Contar artigos em cada pasta
        pendentes = 0
        publicados = 0
        
        pasta_pendentes = 'posts/pendentes'
        if os.path.exists(pasta_pendentes):
            pendentes = len([f for f in os.listdir(pasta_pendentes) if f.endswith('.json')])
        
        pasta_publicados = 'posts/publicados'
        if os.path.exists(pasta_publicados):
            publicados = len([f for f in os.listdir(pasta_publicados) if f.endswith('.json')])
        
        print(f"📁 Artigos pendentes: {pendentes}")
        print(f"📁 Artigos publicados: {publicados}")
        print(f"📊 Total de palavras-chave únicas: {len(self.palavras_chave_usadas)}")
        
        # Mostrar palavras-chave mais comuns
        if self.palavras_chave_usadas:
            print(f"\n🔝 Palavras-chave mais utilizadas:")
            for palavra in sorted(self.palavras_chave_usadas)[:10]:
                print(f"   • {palavra}")
        
        print(f"\n💡 Sistema verifica duplicatas em AMBAS as pastas (pendentes + publicados)")
        print(f"🎯 Critério: máximo 2 palavras-chave repetidas por idioma")
    
    def salvar_post(self, artigos, palavras_chave_pt, palavras_chave_en):
        """Salva o post gerado"""
        if not artigos or not artigos['pt'] or not artigos['en']:
            return None
        
        # Gerar ID único baseado no conteúdo em português
        post_id = hashlib.md5(artigos['pt'].encode()).hexdigest()[:8]
        
        # Extrair título do artigo para gerar imagem
        titulo_pt = self.extrair_titulo(artigos['pt'])
        titulo_en = self.extrair_titulo(artigos['en'])
        
        # Gerar imagens
        imagem_pt = self.gerar_imagem_artigo(titulo_pt, 'pt')
        imagem_en = self.gerar_imagem_artigo(titulo_en, 'en')
        
        post_data = {
            'id': post_id,
            'artigo_pt': artigos['pt'],
            'artigo_en': artigos['en'],
            'titulo_pt': titulo_pt,
            'titulo_en': titulo_en,
            'imagem_pt': imagem_pt,
            'imagem_en': imagem_en,
            'palavras_chave_pt': list(palavras_chave_pt),
            'palavras_chave_en': list(palavras_chave_en),
            'data_geracao': datetime.now().isoformat(),
            'status': 'pendente_revisao'
        }
        
        # Salvar arquivo
        os.makedirs('posts/pendentes', exist_ok=True)
        with open(f'posts/pendentes/{post_id}.json', 'w', encoding='utf-8') as f:
            json.dump(post_data, f, indent=2, ensure_ascii=False)
        
        # Atualizar palavras-chave usadas
        self.palavras_chave_usadas.update(palavras_chave_pt)
        self.palavras_chave_usadas.update(palavras_chave_en)
        
        return post_id

    def gerar_imagem_artigo(self, titulo_artigo, idioma='pt'):
        """Gera uma imagem para o artigo usando DALL-E 3"""
        try:
            # Criar prompt para imagem baseado no título
            if idioma == 'pt':
                prompt_imagem = f"""
                Crie uma imagem profissional e moderna que represente: {titulo_artigo}
                
                Estilo: 
                - Design corporativo e tecnológico
                - Cores: azul, branco, cinza (paleta profissional)
                - Elementos: gráficos, dashboards, ícones de cloud
                - Tom: profissional, confiável, inovador
                - Formato: 1024x1024px (quadrado, ideal para redes sociais)
                
                NÃO incluir texto na imagem. Apenas elementos visuais.
                """
            else:
                prompt_imagem = f"""
                Create a professional and modern image representing: {titulo_artigo}
                
                Style:
                - Corporate and technological design
                - Colors: blue, white, gray (professional palette)
                - Elements: charts, dashboards, cloud icons
                - Tone: professional, reliable, innovative
                - Format: 1024x1024px (square, ideal for social media)
                
                DO NOT include text in the image. Visual elements only.
                """
            
            client = openai.OpenAI(
                api_key=self.config['openai_api_key'],
                timeout=60.0
            )
            
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt_imagem,
                size="1024x1024",
                quality="standard",
                n=1
            )
            
            # Salvar imagem
            image_url = response.data[0].url
            image_id = hashlib.md5(titulo_artigo.encode()).hexdigest()[:8]
            image_path = f"posts/pendentes/{image_id}_image.png"
            
            # Baixar imagem
            import requests
            img_response = requests.get(image_url)
            with open(image_path, 'wb') as f:
                f.write(img_response.content)
            
            print(f"✅ Imagem gerada: {image_path}")
            return image_path
            
        except Exception as e:
            print(f"❌ Erro ao gerar imagem: {e}")
            return None

# Função de compatibilidade para scripts antigos
def gerar_artigo_finops():
    gerador = GeradorConteudoFinOps()
    return gerador.gerar_artigo()

def gerar_imagem(texto):
    """Placeholder para geração de imagem"""
    # TODO: Implementar integração com DALL-E ou Stable Diffusion
    return "caminho_para_imagem.png"