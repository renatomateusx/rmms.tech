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
        openai.api_key = self.config['openai_api_key']
        self.palavras_chave_usadas = self.carregar_palavras_chave()
    
    def carregar_config(self):
        """Carrega configurações do arquivo config.json"""
        config_path = 'config/config.json'
        
        if not os.path.exists(config_path):
            # Criar configuração padrão
            config_padrao = {
                "openai_api_key": "sua_chave_openai_aqui",
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
        """Carrega palavras-chave já utilizadas"""
        palavras_chave = set()
        pasta_pendentes = 'posts/pendentes'
        
        if os.path.exists(pasta_pendentes):
            for arquivo in os.listdir(pasta_pendentes):
                if arquivo.endswith('.json'):
                    with open(f'{pasta_pendentes}/{arquivo}', 'r') as f:
                        post = json.load(f)
                        palavras_chave.update(post.get('palavras_chave_pt', []))
                        palavras_chave.update(post.get('palavras_chave_en', []))
        
        return palavras_chave
    
    def gerar_artigo_pt(self):
        """Gera um artigo técnico em português"""
        topicos = self.config['topicos_finops_pt']
        topico = topicos[datetime.now().weekday() % len(topicos)]
        
        prompt = f"""
        Crie um artigo técnico em PORTUGUÊS sobre: {topico}
        
        Requisitos:
        - 400-600 palavras
        - Linguagem técnica mas acessível
        - Incluir dicas práticas e exemplos
        - Call-to-action sutil para consultoria
        - Foco em resultados mensuráveis
        - Evitar jargões excessivos
        - Incluir métricas e números quando possível
        
        Estrutura:
        1. Introdução do problema/oportunidade
        2. Solução técnica detalhada
        3. Implementação prática com passos
        4. Resultados esperados e métricas
        5. Call-to-action para consultoria
        
        Tome: RMMS Tech - Consultoria em Cloud, IA Aplicada e Automação Estratégica
        """
        
        try:
            response = openai.ChatCompletion.create(
                model=self.config['modelo_gpt'],
                messages=[{"role": "user", "content": prompt}],
                max_tokens=800,
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
        Create a technical article in ENGLISH about: {topico}
        
        Requirements:
        - 400-600 words
        - Technical but accessible language
        - Include practical tips and examples
        - Subtle call-to-action for consulting
        - Focus on measurable results
        - Avoid excessive jargon
        - Include metrics and numbers when possible
        
        Structure:
        1. Introduction of the problem/opportunity
        2. Detailed technical solution
        3. Practical implementation with steps
        4. Expected results and metrics
        5. Call-to-action for consulting
        
        Tone: RMMS Tech - Cloud, Applied AI and Strategic Automation Consulting
        """
        
        try:
            response = openai.ChatCompletion.create(
                model=self.config['modelo_gpt'],
                messages=[{"role": "user", "content": prompt}],
                max_tokens=800,
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
    
    def verificar_duplicatas(self, palavras_chave_pt, palavras_chave_en):
        """Verifica se o conteúdo é muito similar aos anteriores"""
        if not palavras_chave_pt or not palavras_chave_en:
            return False
        
        # Se mais de 3 palavras-chave já foram usadas em qualquer idioma, considera duplicado
        palavras_repetidas_pt = palavras_chave_pt.intersection(self.palavras_chave_usadas)
        palavras_repetidas_en = palavras_chave_en.intersection(self.palavras_chave_usadas)
        
        return len(palavras_repetidas_pt) > 3 or len(palavras_repetidas_en) > 3
    
    def salvar_post(self, artigos, palavras_chave_pt, palavras_chave_en):
        """Salva o post gerado"""
        if not artigos or not artigos['pt'] or not artigos['en']:
            return None
        
        # Gerar ID único baseado no conteúdo em português
        post_id = hashlib.md5(artigos['pt'].encode()).hexdigest()[:8]
        
        post_data = {
            'id': post_id,
            'artigo_pt': artigos['pt'],
            'artigo_en': artigos['en'],
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

# Função de compatibilidade para scripts antigos
def gerar_artigo_finops():
    gerador = GeradorConteudoFinOps()
    return gerador.gerar_artigo()

def gerar_imagem(texto):
    """Placeholder para geração de imagem"""
    # TODO: Implementar integração com DALL-E ou Stable Diffusion
    return "caminho_para_imagem.png"