#!/usr/bin/env python3
"""
Sistema Automatizado de Geração de Vídeos TikTok - RMMS Tech
Gera vídeos promocionais sobre casos de sucesso e serviços
"""

import schedule
import time
import json
import os
import hashlib
from datetime import datetime
from generate_video_content import GeradorConteudoTikTok
from video_generator import GeradorVideo

class SistemaVideoTikTok:
    def __init__(self):
        self.gerador = GeradorConteudoTikTok()
        self.gerador_video = GeradorVideo()
        self.verificar_pastas()
    
    def verificar_pastas(self):
        """Cria pastas necessárias se não existirem"""
        pastas = ['videos', 'videos/pendentes', 'videos/publicados', 'config', 'assets']
        for pasta in pastas:
            if not os.path.exists(pasta):
                os.makedirs(pasta)
                print(f"✅ Pasta criada: {pasta}")
    
    def executar_geracao_semanal(self):
        """Executa a geração de vídeos semanal"""
        print(f"🎬 Iniciando geração de vídeos TikTok - {datetime.now()}")
        
        try:
            # Gerar conteúdo de vídeo
            conteudo = self.gerador.gerar_conteudo_video()
            
            if not conteudo:
                print("❌ Erro na geração de conteúdo")
                return
            
            # Extrair palavras-chave
            palavras_chave_pt = self.gerador.extrair_palavras_chave(conteudo['roteiro_pt'], 'pt')
            palavras_chave_en = self.gerador.extrair_palavras_chave(conteudo['roteiro_en'], 'en')
            
            # Verificar duplicatas
            if not self.gerador.verificar_duplicatas(palavras_chave_pt, palavras_chave_en):
                video_id = self.gerador.salvar_video(conteudo, palavras_chave_pt, palavras_chave_en)
                print(f"✅ Conteúdo TikTok gerado com sucesso! ID: {video_id}")
                print(f"📁 Arquivo salvo em: videos/pendentes/{video_id}.json")
                
                # Tentar gerar vídeo automaticamente
                print("🎬 Tentando gerar vídeo automaticamente...")
                video_path = self.gerador_video.gerar_video_automatico(conteudo, video_id)
                
                if video_path:
                    print(f"✅ Vídeo gerado automaticamente: {video_path}")
                    print("📝 Revise o vídeo antes de publicar!")
                else:
                    print("⚠️ Vídeo não foi gerado automaticamente")
                    print("📝 Use o prompt fornecido para criar o vídeo manualmente")
                
                print("🎬 Roteiro, descrição e prompt de vídeo disponíveis")
            else:
                print("⚠️ Conteúdo muito similar aos anteriores, gerando novo...")
                self.executar_geracao_semanal()  # Recursivo
                
        except Exception as e:
            print(f"❌ Erro na geração: {e}")
            print("🔧 Verifique suas configurações em config/config.json")
    
    def listar_videos_pendentes(self):
        """Lista vídeos pendentes de revisão"""
        videos = []
        pasta_pendentes = 'videos/pendentes'
        
        if os.path.exists(pasta_pendentes):
            for arquivo in os.listdir(pasta_pendentes):
                if arquivo.endswith('.json'):
                    with open(f'{pasta_pendentes}/{arquivo}', 'r') as f:
                        videos.append(json.load(f))
        
        return videos
    
    def mostrar_videos_pendentes(self):
        """Interface para visualizar vídeos pendentes"""
        videos = self.listar_videos_pendentes()
        
        if not videos:
            print("📭 Nenhum vídeo pendente encontrado.")
            return
        
        print(f"\n📋 Vídeos pendentes de revisão ({len(videos)} encontrados):")
        print("-" * 70)
        
        for i, video in enumerate(videos, 1):
            data = datetime.fromisoformat(video['data_geracao']).strftime("%d/%m/%Y %H:%M")
            print(f"{i}. ID: {video['id']} | Data: {data}")
            print(f"   🎬 Título PT: {video['titulo_pt'][:60]}...")
            print(f"   🎬 Título EN: {video['titulo_en'][:60]}...")
            print(f"   📝 Tipo: {video['tipo_conteudo']}")
            print(f"   🏷️ Palavras-chave PT: {', '.join(video['palavras_chave_pt'][:3])}")
            print()
    
    def mostrar_video_completo(self, video_id):
        """Mostra um vídeo completo para revisão"""
        pasta_pendentes = 'videos/pendentes'
        arquivo = f'{pasta_pendentes}/{video_id}.json'
        
        if not os.path.exists(arquivo):
            print(f"❌ Vídeo {video_id} não encontrado")
            return
        
        with open(arquivo, 'r', encoding='utf-8') as f:
            video = json.load(f)
        
        print(f"\n🎬 VÍDEO COMPLETO - ID: {video_id}")
        print("=" * 70)
        
        print(f"\n📊 INFORMAÇÕES GERAIS:")
        print(f"Tipo: {video['tipo_conteudo']}")
        print(f"Duração: {video['duracao']} segundos")
        print(f"Gênero: {video['genero']}")
        
        print(f"\n🇧🇷 VERSÃO EM PORTUGUÊS:")
        print("-" * 40)
        print(f"Título: {video['titulo_pt']}")
        print(f"Descrição: {video['descricao_pt']}")
        print(f"\nRoteiro:")
        print(video['roteiro_pt'])
        
        print(f"\n🇺🇸 VERSÃO EM INGLÊS:")
        print("-" * 40)
        print(f"Título: {video['titulo_en']}")
        print(f"Descrição: {video['descricao_en']}")
        print(f"\nRoteiro:")
        print(video['roteiro_en'])
        
        print(f"\n🎨 PROMPT DE VÍDEO:")
        print("-" * 40)
        print(video['prompt_video'])
        
        print(f"\n🎵 CONFIGURAÇÃO DE ÁUDIO:")
        print(f"Gênero: {video['audio_genre']}")
        print(f"BPM: {video['audio_bpm']}")
        print(f"Tom: {video['audio_key']}")
        
        print(f"\n🏷️ PALAVRAS-CHAVE:")
        print(f"PT: {', '.join(video['palavras_chave_pt'])}")
        print(f"EN: {', '.join(video['palavras_chave_en'])}")
        
        print(f"\n📅 Gerado em: {datetime.fromisoformat(video['data_geracao']).strftime('%d/%m/%Y %H:%M')}")
    
    def iniciar_agendamento(self):
        """Inicia o sistema de agendamento"""
        schedule.every().tuesday.at("10:00").do(self.executar_geracao_semanal)
        
        print("🕐 Sistema agendado para executar toda terça às 10h")
        print("📝 Para gerar vídeo manualmente, execute: python3 main.py --gerar")
        print("📋 Para ver vídeos pendentes, execute: python3 main.py --listar")
        print("👁️ Para ver vídeo completo, execute: python3 main.py --ver ID")
        print("⏹️ Pressione Ctrl+C para parar")
        print("-" * 50)
        
        while True:
            schedule.run_pending()
            time.sleep(60)

def main():
    """Função principal"""
    import sys
    
    sistema = SistemaVideoTikTok()
    
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        
        if comando == "--gerar":
            print("🚀 Gerando vídeo TikTok manualmente...")
            sistema.executar_geracao_semanal()
        
        elif comando == "--listar":
            sistema.mostrar_videos_pendentes()
        
        elif comando == "--ver" and len(sys.argv) > 2:
            video_id = sys.argv[2]
            sistema.mostrar_video_completo(video_id)
        
        elif comando == "--ajuda":
            print("""
📖 Comandos disponíveis:
  python3 main.py                    - Inicia sistema agendado
  python3 main.py --gerar            - Gera vídeo TikTok manualmente
  python3 main.py --listar           - Lista vídeos pendentes
  python3 main.py --ver ID           - Mostra vídeo completo (ex: --ver abc12345)
  python3 main.py --ajuda            - Mostra esta ajuda

🎬 Funcionalidades:
  - Geração de roteiros em PT-BR e EN
  - Prompts para criação de vídeo
  - Descrições otimizadas para TikTok
  - Configuração de áudio de fundo
  - Geração automática de vídeo (se APIs configuradas)
  - Agendamento semanal (terça às 10h)

🔧 APIs de Vídeo:
  - Runway ML (text-to-video)
  - Pika Labs (text-to-video)
  - Synthesia (avatar + roteiro)
  - Lumen5 (vídeo com texto)
            """)
        
        else:
            print(f"❌ Comando desconhecido: {comando}")
            print("💡 Use --ajuda para ver comandos disponíveis")
    
    else:
        # Modo agendamento (padrão)
        sistema.iniciar_agendamento()

if __name__ == "__main__":
    main() 