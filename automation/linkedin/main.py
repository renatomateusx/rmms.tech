#!/usr/bin/env python3
"""
Sistema Automatizado de Postagem LinkedIn - RMMS Tech
Gera conteúdo semanal sobre FinOps, Cloud e DevOps
Versão bilingue: Português e Inglês
"""

import schedule
import time
import json
import os
import hashlib
from datetime import datetime
from generate_article import GeradorConteudoFinOps

class SistemaPostagemAutomatico:
    def __init__(self):
        self.gerador = GeradorConteudoFinOps()
        self.verificar_pastas()
    
    def verificar_pastas(self):
        """Cria pastas necessárias se não existirem"""
        pastas = ['posts', 'posts/pendentes', 'posts/publicados', 'config']
        for pasta in pastas:
            if not os.path.exists(pasta):
                os.makedirs(pasta)
                print(f"✅ Pasta criada: {pasta}")
    
    def executar_geracao_semanal(self):
        """Executa a geração de conteúdo semanal"""
        print(f"🔄 Iniciando geração de conteúdo - {datetime.now()}")
        
        try:
            # Gerar artigos em português e inglês
            artigos = self.gerador.gerar_artigo()
            
            if not artigos:
                print("❌ Erro na geração de artigos")
                return
            
            # Extrair palavras-chave para ambos os idiomas
            palavras_chave_pt = self.gerador.extrair_palavras_chave(artigos['pt'], 'pt')
            palavras_chave_en = self.gerador.extrair_palavras_chave(artigos['en'], 'en')
            
            # Verificar duplicatas
            if not self.gerador.verificar_duplicatas(palavras_chave_pt, palavras_chave_en):
                post_id = self.gerador.salvar_post(artigos, palavras_chave_pt, palavras_chave_en)
                print(f"✅ Conteúdo bilingue gerado com sucesso! ID: {post_id}")
                print(f"📁 Arquivo salvo em: posts/pendentes/{post_id}.json")
                print("📝 Revise o conteúdo antes de publicar!")
                print("🌍 Artigos disponíveis em português e inglês")
            else:
                print("⚠️ Conteúdo muito similar aos anteriores, gerando novo...")
                self.executar_geracao_semanal()  # Recursivo
                
        except Exception as e:
            print(f"❌ Erro na geração: {e}")
            print("🔧 Verifique suas configurações em config/config.json")
    
    def listar_posts_pendentes(self):
        """Lista posts pendentes de revisão"""
        posts = []
        pasta_pendentes = 'posts/pendentes'
        
        if os.path.exists(pasta_pendentes):
            for arquivo in os.listdir(pasta_pendentes):
                if arquivo.endswith('.json'):
                    with open(f'{pasta_pendentes}/{arquivo}', 'r') as f:
                        posts.append(json.load(f))
        
        return posts
    
    def mostrar_posts_pendentes(self):
        """Interface para visualizar posts pendentes"""
        posts = self.listar_posts_pendentes()
        
        if not posts:
            print("📭 Nenhum post pendente encontrado.")
            return
        
        print(f"\n📋 Posts pendentes de revisão ({len(posts)} encontrados):")
        print("-" * 60)
        
        for i, post in enumerate(posts, 1):
            data = datetime.fromisoformat(post['data_geracao']).strftime("%d/%m/%Y %H:%M")
            print(f"{i}. ID: {post['id']} | Data: {data}")
            print(f"   🇧🇷 PT: {post['artigo_pt'][:80]}...")
            print(f"   🇺🇸 EN: {post['artigo_en'][:80]}...")
            print(f"   🏷️ Palavras-chave PT: {', '.join(post['palavras_chave_pt'][:3])}")
            print(f"   🏷️ Palavras-chave EN: {', '.join(post['palavras_chave_en'][:3])}")
            print()
    
    def mostrar_artigo_completo(self, post_id):
        """Mostra um artigo completo para revisão"""
        pasta_pendentes = 'posts/pendentes'
        arquivo = f'{pasta_pendentes}/{post_id}.json'
        
        if not os.path.exists(arquivo):
            print(f"❌ Artigo {post_id} não encontrado")
            return
        
        with open(arquivo, 'r', encoding='utf-8') as f:
            post = json.load(f)
        
        print(f"\n📄 ARTIGO COMPLETO - ID: {post_id}")
        print("=" * 60)
        
        print("\n🇧🇷 VERSÃO EM PORTUGUÊS:")
        print("-" * 30)
        print(post['artigo_pt'])
        
        print("\n🇺🇸 VERSÃO EM INGLÊS:")
        print("-" * 30)
        print(post['artigo_en'])
        
        print("\n🏷️ PALAVRAS-CHAVE:")
        print(f"PT: {', '.join(post['palavras_chave_pt'])}")
        print(f"EN: {', '.join(post['palavras_chave_en'])}")
        
        print(f"\n📅 Gerado em: {datetime.fromisoformat(post['data_geracao']).strftime('%d/%m/%Y %H:%M')}")
    
    def iniciar_agendamento(self):
        """Inicia o sistema de agendamento"""
        schedule.every().monday.at("09:00").do(self.executar_geracao_semanal)
        
        print("🕐 Sistema agendado para executar toda segunda às 9h")
        print("📝 Para gerar conteúdo manualmente, execute: python3 main.py --gerar")
        print("📋 Para ver posts pendentes, execute: python3 main.py --listar")
        print("👁️ Para ver artigo completo, execute: python3 main.py --ver ID")
        print("⏹️ Pressione Ctrl+C para parar")
        print("-" * 50)
        
        while True:
            schedule.run_pending()
            time.sleep(60)

def main():
    """Função principal"""
    import sys
    
    sistema = SistemaPostagemAutomatico()
    
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        
        if comando == "--gerar":
            print("🚀 Gerando conteúdo bilingue manualmente...")
            sistema.executar_geracao_semanal()
        
        elif comando == "--listar":
            sistema.mostrar_posts_pendentes()
        
        elif comando == "--ver" and len(sys.argv) > 2:
            post_id = sys.argv[2]
            sistema.mostrar_artigo_completo(post_id)
        
        elif comando == "--ajuda":
            print("""
📖 Comandos disponíveis:
  python3 main.py                    - Inicia sistema agendado
  python3 main.py --gerar            - Gera conteúdo bilingue manualmente
  python3 main.py --listar           - Lista posts pendentes
  python3 main.py --ver ID           - Mostra artigo completo (ex: --ver abc12345)
  python3 main.py --ajuda            - Mostra esta ajuda

🌍 Funcionalidades:
  - Geração automática em português e inglês
  - Controle de duplicatas por palavras-chave
  - Interface para revisão manual
  - Agendamento semanal (segunda às 9h)
            """)
        
        else:
            print(f"❌ Comando desconhecido: {comando}")
            print("💡 Use --ajuda para ver comandos disponíveis")
    
    else:
        # Modo agendamento (padrão)
        sistema.iniciar_agendamento()

if __name__ == "__main__":
    main()