#!/usr/bin/env python3
"""
Gerador de Conteúdo para Vídeos TikTok - RMMS Tech
Gera roteiros, descrições e prompts para vídeos promocionais
"""

import json
import os
import hashlib
import random
from datetime import datetime
from typing import Dict, List, Optional

class GeradorConteudoTikTok:
    def __init__(self):
        self.config = self.carregar_config()
        self.casos_sucesso = self.carregar_casos_sucesso()
        self.templates = self.carregar_templates()
    
    def carregar_config(self) -> Dict:
        """Carrega configurações do sistema"""
        config_path = 'config/config.json'
        
        if not os.path.exists(config_path):
            # Criar configuração padrão
            config = {
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
            
            os.makedirs('config', exist_ok=True)
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def carregar_casos_sucesso(self) -> List[Dict]:
        """Carrega casos de sucesso da empresa"""
        return [
            {
                "empresa": "Fintech Brasileira",
                "desafio": "Escalar processamento de pagamentos e garantir decisões rápidas",
                "solucao": "IA para análise preditiva de fraudes e automação em multicloud",
                "resultados": ["Crescimento de 300% em 18 meses", "Decisões em milissegundos", "Zero incidentes críticos"]
            },
            {
                "empresa": "Rede Varejista Nacional",
                "desafio": "Reduzir custos e aumentar eficiência durante picos de demanda",
                "solucao": "IA para previsão de demanda e automação de escalonamento",
                "resultados": ["Redução de 35% nos custos", "60% mais velocidade", "Análises em tempo real"]
            },
            {
                "empresa": "Empresa de Saúde",
                "desafio": "Garantir segurança e conformidade de dados sensíveis",
                "solucao": "Arquitetura cloud-native com IA para monitoramento",
                "resultados": ["Zero vazamentos", "99,99% disponibilidade", "Conformidade total"]
            },
            {
                "empresa": "Plataforma SaaS B2B",
                "desafio": "Aumentar retenção e performance em picos de uso",
                "solucao": "IA para análise de churn e automação de incidentes",
                "resultados": ["28% mais retenção", "40% menos tempo de resposta", "Escalabilidade garantida"]
            }
        ]
    
    def carregar_templates(self) -> Dict:
        """Carrega templates de roteiros"""
        return {
            "caso_sucesso": {
                "pt": {
                    "titulo": "Como a {empresa} transformou {desafio_curto} com tecnologia de ponta! 🚀",
                    "descricao": "💡 Caso real: {empresa} estava com {desafio}. Nossa solução: {solucao_curta}. Resultado: {resultado_principal}.\n\n🏆 {empresa_nome} - Especialistas em Cloud, IA e Automação\n📈 Resultados mensuráveis e ROI comprovado\n💼 Transformação digital que funciona\n\n#transformacaodigital #cloudcomputing #ia #automacao #tech #business #resultados",
                    "roteiro": """🎬 ROTEIRO - CASO DE SUCESSO

[0-3s] HOOK - "Empresa {empresa} estava perdendo dinheiro com {desafio_curto}..."

[3-8s] PROBLEMA - Mostrar estatísticas/gráficos do problema
- "Custos aumentando 40%"
- "Tempo de resposta lento"
- "Processos manuais"

[8-15s] SOLUÇÃO RMMS TECH - Apresentar nossa solução
- "Implementamos {solucao_curta}"
- "Migração para cloud"
- "IA para automação"

[15-25s] RESULTADOS - Mostrar números impressionantes
- "{resultado_principal}"
- "Redução de custos"
- "Aumento de eficiência"

[25-30s] CTA - Chamada para ação
- "Quer resultados similares?"
- "Agende uma consultoria gratuita"
- "Link na bio"

[30-35s] CRÉDITOS - Logo RMMS Tech + contato""",
                    "prompt_video": "Criar vídeo profissional mostrando transformação digital. Cena 1: Empresa com problemas (gráficos vermelhos). Cena 2: Equipe RMMS Tech trabalhando. Cena 3: Resultados positivos (gráficos verdes, números). Cena 4: Logo RMMS Tech. Estilo: moderno, corporativo, cores azul/branco. Duração: 35s."
                },
                "en": {
                    "titulo": "How {company} transformed {challenge_short} with cutting-edge technology! 🚀",
                    "descricao": "💡 Real case: {company} was struggling with {challenge}. Our solution: {solution_short}. Result: {main_result}.\n\n🏆 {company_name} - Cloud, AI and Automation Specialists\n📈 Measurable results and proven ROI\n💼 Digital transformation that works\n\n#digitaltransformation #cloudcomputing #ai #automation #tech #business #results",
                    "roteiro": """🎬 SCRIPT - SUCCESS CASE

[0-3s] HOOK - "{Company} was losing money with {challenge_short}..."

[3-8s] PROBLEM - Show problem statistics/graphs
- "Costs increasing 40%"
- "Slow response time"
- "Manual processes"

[8-15s] RMMS TECH SOLUTION - Present our solution
- "We implemented {solution_short}"
- "Cloud migration"
- "AI for automation"

[15-25s] RESULTS - Show impressive numbers
- "{main_result}"
- "Cost reduction"
- "Efficiency increase"

[25-30s] CTA - Call to action
- "Want similar results?"
- "Schedule a free consultation"
- "Link in bio"

[30-35s] CREDITS - RMMS Tech logo + contact""",
                    "prompt_video": "Create professional video showing digital transformation. Scene 1: Company with problems (red charts). Scene 2: RMMS Tech team working. Scene 3: Positive results (green charts, numbers). Scene 4: RMMS Tech logo. Style: modern, corporate, blue/white colors. Duration: 35s."
                }
            },
            "servico_destaque": {
                "pt": {
                    "titulo": "Descobrimos como reduzir custos de cloud em 40%! 💰",
                    "descricao": "🔥 Dica exclusiva: {servico_destaque} pode economizar milhares na sua empresa.\n\n💡 Como fazemos:\n- Análise completa da infraestrutura\n- Otimização automática\n- Monitoramento contínuo\n\n🏆 {empresa_nome} - Especialistas em Cloud Computing\n📞 Agende uma consultoria gratuita\n\n#cloudcomputing #economia #otimizacao #tech #business #dicas",
                    "roteiro": """🎬 ROTEIRO - SERVIÇO EM DESTAQUE

[0-3s] HOOK - "Você sabia que pode economizar 40% em cloud?"

[3-8s] PROBLEMA - Mostrar custos altos
- "Empresas gastam demais"
- "Recursos subutilizados"
- "Falta de otimização"

[8-15s] SOLUÇÃO - Apresentar nosso serviço
- "{servico_destaque}"
- "Análise especializada"
- "Otimização automática"

[15-25s] BENEFÍCIOS - Mostrar vantagens
- "Economia de 40%"
- "Performance melhor"
- "Segurança garantida"

[25-30s] CTA - Chamada para ação
- "Quer economizar também?"
- "Diagnóstico gratuito"
- "Link na bio"

[30-35s] CRÉDITOS - Logo RMMS Tech""",
                    "prompt_video": "Criar vídeo educativo sobre economia em cloud. Cena 1: Gráfico de custos altos. Cena 2: Equipe analisando. Cena 3: Gráfico de economia. Cena 4: Logo RMMS Tech. Estilo: educativo, profissional, cores azul/verde. Duração: 35s."
                },
                "en": {
                    "titulo": "We discovered how to reduce cloud costs by 40%! 💰",
                    "descricao": "🔥 Exclusive tip: {featured_service} can save thousands in your company.\n\n💡 How we do it:\n- Complete infrastructure analysis\n- Automatic optimization\n- Continuous monitoring\n\n🏆 {company_name} - Cloud Computing Specialists\n📞 Schedule a free consultation\n\n#cloudcomputing #savings #optimization #tech #business #tips",
                    "roteiro": """🎬 SCRIPT - FEATURED SERVICE

[0-3s] HOOK - "Did you know you can save 40% on cloud?"

[3-8s] PROBLEM - Show high costs
- "Companies overspend"
- "Underutilized resources"
- "Lack of optimization"

[8-15s] SOLUTION - Present our service
- "{featured_service}"
- "Specialized analysis"
- "Automatic optimization"

[15-25s] BENEFITS - Show advantages
- "40% savings"
- "Better performance"
- "Guaranteed security"

[25-30s] CTA - Call to action
- "Want to save too?"
- "Free diagnosis"
- "Link in bio"

[30-35s] CREDITS - RMMS Tech logo""",
                    "prompt_video": "Create educational video about cloud savings. Scene 1: High cost chart. Scene 2: Team analyzing. Scene 3: Savings chart. Scene 4: RMMS Tech logo. Style: educational, professional, blue/green colors. Duration: 35s."
                }
            }
        }
    
    def gerar_conteudo_video(self) -> Optional[Dict]:
        """Gera conteúdo completo para um vídeo TikTok"""
        try:
            # Escolher tipo de conteúdo
            tipo_conteudo = random.choice(["caso_sucesso", "servico_destaque"])
            
            if tipo_conteudo == "caso_sucesso":
                return self.gerar_caso_sucesso()
            else:
                return self.gerar_servico_destaque()
                
        except Exception as e:
            print(f"❌ Erro na geração de conteúdo: {e}")
            return None
    
    def gerar_caso_sucesso(self) -> Dict:
        """Gera conteúdo baseado em caso de sucesso"""
        caso = random.choice(self.casos_sucesso)
        template = self.templates["caso_sucesso"]
        
        # Preparar dados para template
        dados = {
            "empresa": caso["empresa"],
            "empresa_nome": "RMMS Tech",
            "desafio": caso["desafio"],
            "desafio_curto": caso["desafio"].split()[0:3],
            "solucao": caso["solucao"],
            "solucao_curta": caso["solucao"].split()[0:4],
            "resultado_principal": caso["resultados"][0],
            "company": caso["empresa"],
            "challenge": caso["desafio"],
            "challenge_short": " ".join(caso["desafio"].split()[0:3]),
            "solution": caso["solucao"],
            "solution_short": " ".join(caso["solucao"].split()[0:4]),
            "main_result": caso["resultados"][0]
        }
        
        return {
            "tipo_conteudo": "caso_sucesso",
            "duracao": 35,
            "genero": "business",
            "titulo_pt": template["pt"]["titulo"].format(**dados),
            "titulo_en": template["en"]["titulo"].format(**dados),
            "descricao_pt": template["pt"]["descricao"].format(**dados),
            "descricao_en": template["en"]["descricao"].format(**dados),
            "roteiro_pt": template["pt"]["roteiro"].format(**dados),
            "roteiro_en": template["en"]["roteiro"].format(**dados),
            "prompt_video": template["pt"]["prompt_video"],
            "audio_genre": random.choice(self.config["audio"]["generos"]),
            "audio_bpm": random.randint(*self.config["audio"]["bpm_range"]),
            "audio_key": random.choice(self.config["audio"]["keys"]),
            "dados_caso": caso
        }
    
    def gerar_servico_destaque(self) -> Dict:
        """Gera conteúdo destacando um serviço específico"""
        servicos = [
            {
                "nome": "Otimização de Custos Cloud",
                "nome_en": "Cloud Cost Optimization",
                "destaque": "redução de 40% nos custos",
                "destaque_en": "40% cost reduction"
            },
            {
                "nome": "Implementação de IA",
                "nome_en": "AI Implementation",
                "destaque": "automação de processos críticos",
                "destaque_en": "critical process automation"
            },
            {
                "nome": "Migração para Cloud",
                "nome_en": "Cloud Migration",
                "destaque": "migração sem downtime",
                "destaque_en": "zero-downtime migration"
            }
        ]
        
        servico = random.choice(servicos)
        template = self.templates["servico_destaque"]
        
        dados = {
            "servico_destaque": servico["nome"],
            "empresa_nome": "RMMS Tech",
            "featured_service": servico["nome_en"],
            "company_name": "RMMS Tech"
        }
        
        return {
            "tipo_conteudo": "servico_destaque",
            "duracao": 35,
            "genero": "educational",
            "titulo_pt": template["pt"]["titulo"],
            "titulo_en": template["en"]["titulo"],
            "descricao_pt": template["pt"]["descricao"].format(**dados),
            "descricao_en": template["en"]["descricao"].format(**dados),
            "roteiro_pt": template["pt"]["roteiro"].format(**dados),
            "roteiro_en": template["en"]["roteiro"].format(**dados),
            "prompt_video": template["pt"]["prompt_video"],
            "audio_genre": random.choice(self.config["audio"]["generos"]),
            "audio_bpm": random.randint(*self.config["audio"]["bpm_range"]),
            "audio_key": random.choice(self.config["audio"]["keys"]),
            "servico": servico
        }
    
    def extrair_palavras_chave(self, texto: str, idioma: str) -> List[str]:
        """Extrai palavras-chave do texto"""
        palavras_comuns = {
            "pt": ["a", "o", "e", "de", "da", "do", "em", "um", "uma", "com", "para", "por", "que", "se", "não", "mais", "como", "mas", "foi", "são", "está", "pode", "ser", "tem", "ao", "ele", "das", "tem", "à", "seu", "sua", "ou", "ser", "quando", "muito", "há", "nos", "já", "estão", "você", "também", "só", "pelo", "pela", "até", "isso", "ela", "entre", "era", "depois", "sem", "mesmo", "aos", "ter", "seus", "suas", "minha", "têm", "naquele", "neles", "vocês", "essa", "num", "nem", "ele", "com", "essa", "num", "nem", "ele", "com", "essa", "num", "nem", "ele", "com"],
            "en": ["the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did", "will", "would", "could", "should", "may", "might", "can", "this", "that", "these", "those", "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them", "my", "your", "his", "her", "its", "our", "their", "mine", "yours", "his", "hers", "ours", "theirs"]
        }
        
        # Limpar texto e dividir em palavras
        texto_limpo = texto.lower().replace('\n', ' ').replace('\t', ' ')
        palavras = [palavra.strip('.,!?()[]{}":;') for palavra in texto_limpo.split()]
        
        # Filtrar palavras comuns e vazias
        palavras_filtradas = [palavra for palavra in palavras 
                            if palavra and len(palavra) > 2 
                            and palavra not in palavras_comuns[idioma]]
        
        # Contar frequência
        frequencia = {}
        for palavra in palavras_filtradas:
            frequencia[palavra] = frequencia.get(palavra, 0) + 1
        
        # Retornar top 10 palavras-chave
        return sorted(frequencia.items(), key=lambda x: x[1], reverse=True)[:10]
    
    def verificar_duplicatas(self, palavras_chave_pt: List, palavras_chave_en: List) -> bool:
        """Verifica se o conteúdo é muito similar aos anteriores"""
        pasta_publicados = 'videos/publicados'
        pasta_pendentes = 'videos/pendentes'
        
        videos_anteriores = []
        
        # Verificar vídeos publicados
        if os.path.exists(pasta_publicados):
            for arquivo in os.listdir(pasta_publicados):
                if arquivo.endswith('.json'):
                    with open(f'{pasta_publicados}/{arquivo}', 'r') as f:
                        videos_anteriores.append(json.load(f))
        
        # Verificar vídeos pendentes
        if os.path.exists(pasta_pendentes):
            for arquivo in os.listdir(pasta_pendentes):
                if arquivo.endswith('.json'):
                    with open(f'{pasta_pendentes}/{arquivo}', 'r') as f:
                        videos_anteriores.append(json.load(f))
        
        # Comparar palavras-chave
        for video in videos_anteriores:
            palavras_pt_video = set(video.get('palavras_chave_pt', []))
            palavras_en_video = set(video.get('palavras_chave_en', []))
            
            # Calcular similaridade
            palavras_pt_atual = set([palavra for palavra, _ in palavras_chave_pt])
            palavras_en_atual = set([palavra for palavra, _ in palavras_chave_en])
            
            similaridade_pt = len(palavras_pt_atual.intersection(palavras_pt_video)) / len(palavras_pt_atual.union(palavras_pt_video)) if palavras_pt_atual.union(palavras_pt_video) else 0
            similaridade_en = len(palavras_en_atual.intersection(palavras_en_video)) / len(palavras_en_atual.union(palavras_en_video)) if palavras_en_atual.union(palavras_en_video) else 0
            
            # Se mais de 70% similar, considerar duplicata
            if similaridade_pt > 0.7 or similaridade_en > 0.7:
                return True
        
        return False
    
    def salvar_video(self, conteudo: Dict, palavras_chave_pt: List, palavras_chave_en: List) -> str:
        """Salva o vídeo gerado"""
        video_id = hashlib.md5(f"{datetime.now()}{conteudo['titulo_pt']}".encode()).hexdigest()[:8]
        
        video_data = {
            "id": video_id,
            "data_geracao": datetime.now().isoformat(),
            **conteudo,
            "palavras_chave_pt": [palavra for palavra, _ in palavras_chave_pt],
            "palavras_chave_en": [palavra for palavra, _ in palavras_chave_en]
        }
        
        # Salvar arquivo
        arquivo_path = f'videos/pendentes/{video_id}.json'
        with open(arquivo_path, 'w', encoding='utf-8') as f:
            json.dump(video_data, f, indent=2, ensure_ascii=False)
        
        return video_id 