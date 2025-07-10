#!/usr/bin/env python3
"""
Configurador Rápido de APIs - RMMS Tech TikTok
Configura as APIs recomendadas de forma simples
"""

import os
import json
import sys
from video_generator import GeradorVideo

def configurar_apis_recomendadas():
    """Configura as APIs recomendadas (Pika Labs + Lumen5)"""
    print("🚀 Configurador de APIs - RMMS Tech TikTok")
    print("=" * 50)
    
    gerador = GeradorVideo()
    
    print("\n🏆 COMBINAÇÃO RECOMENDADA:")
    print("📊 Pika Labs + Runway ML")
    print("💰 Custo: ~$10.50 por vídeo")
    print("🎯 Estratégia: Pika (mais barato) -> Runway (qualidade) -> Lumen5 (fallback)")
    print()
    
    # Configurar Pika Labs
    print("🔧 CONFIGURANDO PIKA LABS")
    print("- Custo: $3.50 por vídeo (35s)")
    print("- Qualidade: Boa, rápida geração")
    print("- Ideal para: Casos de sucesso dinâmicos")
    print()
    
    pika_key = input("📝 Digite sua API Key do Pika Labs (ou Enter para pular): ").strip()
    
    if pika_key:
        if gerador.configurar_api("pika_labs", pika_key):
            print("✅ Pika Labs configurado com sucesso!")
        else:
            print("❌ Erro ao configurar Pika Labs")
    else:
        print("⏭️ Pika Labs não configurado")
    
    print()
    
    # Configurar Runway ML
    print("🔧 CONFIGURANDO RUNWAY ML")
    print("- Custo: $7.00 por vídeo (35s)")
    print("- Qualidade: Alta qualidade, vídeos realistas")
    print("- Ideal para: Casos de sucesso com qualidade premium")
    print()
    
    runway_key = input("📝 Digite sua API Key do Runway ML (ou Enter para pular): ").strip()
    
    if runway_key:
        if gerador.configurar_api("runway", runway_key):
            print("✅ Runway ML configurado com sucesso!")
        else:
            print("❌ Erro ao configurar Runway ML")
    else:
        print("⏭️ Runway ML não configurado")
    
    print()
    
    # Configurar Lumen5 (opcional)
    print("🔧 CONFIGURANDO LUMEN5 (OPCIONAL)")
    print("- Custo: $19 por vídeo")
    print("- Qualidade: Vídeo com texto e imagens")
    print("- Ideal para: Fallback se outras falharem")
    print()
    
    lumen5_key = input("📝 Digite sua API Key do Lumen5 (ou Enter para pular): ").strip()
    
    if lumen5_key:
        if gerador.configurar_api("lumen5", lumen5_key):
            print("✅ Lumen5 configurado com sucesso!")
        else:
            print("❌ Erro ao configurar Lumen5")
    else:
        print("⏭️ Lumen5 não configurado")
    
    print()
    
    # Mostrar status final
    print("📊 STATUS FINAL:")
    gerador.listar_apis_disponiveis()
    
    print("\n🎯 PRÓXIMOS PASSOS:")
    print("1. Teste o sistema: python3 main.py --gerar")
    print("2. Verifique os vídeos gerados")
    print("3. Ajuste configurações se necessário")
    
    # Verificar se pelo menos uma API está configurada
    config_path = 'config/api_config.json'
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        apis_ativas = sum(1 for api in config["apis"].values() if api["enabled"])
        
        if apis_ativas > 0:
            print(f"\n✅ {apis_ativas} API(s) configurada(s)! Sistema pronto para geração automática.")
        else:
            print("\n⚠️ Nenhuma API configurada. O sistema funcionará apenas com prompts manuais.")

def configurar_api_individual():
    """Configura uma API específica"""
    print("🔧 Configuração Individual de API")
    print("=" * 40)
    
    gerador = GeradorVideo()
    
    print("\n📋 APIs disponíveis:")
    print("1. pika_labs - Pika Labs ($3.50/vídeo)")
    print("2. lumen5 - Lumen5 ($19/vídeo)")
    print("3. runway - Runway ML ($7/vídeo)")
    print("4. synthesia - Synthesia ($22/vídeo)")
    print()
    
    api_name = input("📝 Digite o nome da API: ").strip()
    api_key = input("📝 Digite a API Key: ").strip()
    
    if api_name and api_key:
        if gerador.configurar_api(api_name, api_key):
            print(f"✅ API {api_name} configurada com sucesso!")
        else:
            print(f"❌ Erro ao configurar API {api_name}")
    else:
        print("❌ Nome da API e API Key são obrigatórios")

def mostrar_ajuda():
    """Mostra ajuda do sistema"""
    print("""
🎬 Sistema de Vídeos TikTok - RMMS Tech

📋 Comandos disponíveis:
  python3 setup_apis.py                    - Configuração recomendada (Pika + Lumen5)
  python3 setup_apis.py --individual       - Configuração individual de API
  python3 setup_apis.py --ajuda            - Mostra esta ajuda

🏆 COMBINAÇÃO RECOMENDADA:
  📊 Pika Labs + Runway ML
  💰 Custo: ~$10.50 por vídeo
  🎯 Estratégia: Pika (mais barato) -> Runway (qualidade) -> Lumen5 (fallback)

🔧 APIs suportadas:
  - pika_labs: $3.50/vídeo (text-to-video)
  - lumen5: $19/vídeo (texto + imagens)
  - runway: $7/vídeo (alta qualidade)
  - synthesia: $22/vídeo (avatar)

📈 Workflow:
  1. Configure as APIs
  2. Execute: python3 main.py --gerar
  3. Revise os vídeos gerados
  4. Publique no TikTok
    """)

def main():
    """Função principal"""
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        
        if comando == "--individual":
            configurar_api_individual()
        elif comando == "--ajuda":
            mostrar_ajuda()
        else:
            print(f"❌ Comando desconhecido: {comando}")
            mostrar_ajuda()
    else:
        # Configuração recomendada (padrão)
        configurar_apis_recomendadas()

if __name__ == "__main__":
    main() 