#!/usr/bin/env python3
"""
Gerador de Vídeo com APIs - RMMS Tech
Integra com APIs de geração de vídeo automática
"""

import os
import json
import requests
import base64
from typing import Dict, Optional
from datetime import datetime

class GeradorVideo:
    def __init__(self):
        self.config = self.carregar_config_apis()
    
    def carregar_config_apis(self) -> Dict:
        """Carrega configurações das APIs"""
        config_path = 'config/api_config.json'
        
        if not os.path.exists(config_path):
            # Configuração padrão (sem chaves)
            config = {
                "apis": {
                    "runway": {
                        "enabled": False,
                        "api_key": "",
                        "base_url": "https://api.runwayml.com/v1"
                    },
                    "pika_labs": {
                        "enabled": False,
                        "api_key": "",
                        "base_url": "https://api.pika.art/v1"
                    },
                    "synthesia": {
                        "enabled": False,
                        "api_key": "",
                        "base_url": "https://api.synthesia.io/v2"
                    },
                    "lumen5": {
                        "enabled": False,
                        "api_key": "",
                        "base_url": "https://api.lumen5.com/v1"
                    }
                },
                "video_settings": {
                    "resolution": "1080x1920",  # TikTok vertical
                    "fps": 30,
                    "duration": 35,
                    "format": "mp4"
                }
            }
            
            os.makedirs('config', exist_ok=True)
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def gerar_video_runway(self, prompt: str, video_id: str) -> Optional[str]:
        """Gera vídeo usando Runway ML API"""
        if not self.config["apis"]["runway"]["enabled"]:
            print("⚠️ API Runway não configurada")
            return None
        
        try:
            api_key = self.config["apis"]["runway"]["api_key"]
            base_url = self.config["apis"]["runway"]["base_url"]
            
            # Preparar payload para Runway
            payload = {
                "prompt": prompt,
                "negative_prompt": "low quality, blurry, distorted",
                "width": 1080,
                "height": 1920,
                "duration": 35,
                "fps": 30,
                "guidance_scale": 7.5,
                "num_frames": 1050  # 35s * 30fps
            }
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            print("🎬 Gerando vídeo via Runway ML...")
            response = requests.post(
                f"{base_url}/video/generations",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                result = response.json()
                video_url = result.get("video_url")
                
                if video_url:
                    # Baixar vídeo
                    video_path = f"videos/pendentes/{video_id}_video.mp4"
                    self.baixar_video(video_url, video_path)
                    print(f"✅ Vídeo gerado: {video_path}")
                    return video_path
            
            print(f"❌ Erro na API Runway: {response.status_code}")
            return None
            
        except Exception as e:
            print(f"❌ Erro na geração Runway: {e}")
            return None
    
    def gerar_video_pika(self, prompt: str, video_id: str) -> Optional[str]:
        """Gera vídeo usando Pika Labs API"""
        if not self.config["apis"]["pika_labs"]["enabled"]:
            print("⚠️ API Pika Labs não configurada")
            return None
        
        try:
            api_key = self.config["apis"]["pika_labs"]["api_key"]
            base_url = self.config["apis"]["pika_labs"]["base_url"]
            
            # Preparar payload para Pika
            payload = {
                "prompt": prompt,
                "negative_prompt": "low quality, blurry, text, watermark",
                "width": 1080,
                "height": 1920,
                "duration": 35,
                "fps": 30,
                "guidance_scale": 7.5
            }
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            print("🎬 Gerando vídeo via Pika Labs...")
            response = requests.post(
                f"{base_url}/video/generations",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                result = response.json()
                video_url = result.get("video_url")
                
                if video_url:
                    # Baixar vídeo
                    video_path = f"videos/pendentes/{video_id}_video.mp4"
                    self.baixar_video(video_url, video_path)
                    print(f"✅ Vídeo gerado: {video_path}")
                    return video_path
            
            print(f"❌ Erro na API Pika: {response.status_code}")
            return None
            
        except Exception as e:
            print(f"❌ Erro na geração Pika: {e}")
            return None
    
    def gerar_video_synthesia(self, roteiro: str, video_id: str) -> Optional[str]:
        """Gera vídeo usando Synthesia API (com avatar)"""
        if not self.config["apis"]["synthesia"]["enabled"]:
            print("⚠️ API Synthesia não configurada")
            return None
        
        try:
            api_key = self.config["apis"]["synthesia"]["api_key"]
            base_url = self.config["apis"]["synthesia"]["base_url"]
            
            # Preparar payload para Synthesia
            payload = {
                "input": [
                    {
                        "scriptText": roteiro,
                        "avatar": "anna_costume1_cameraA",
                        "background": "off_white",
                        "voice": "en-US-JennyNeural"
                    }
                ],
                "test": False,
                "title": f"RMMS Tech Video {video_id}",
                "description": "Vídeo promocional RMMS Tech"
            }
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            print("🎬 Gerando vídeo via Synthesia...")
            response = requests.post(
                f"{base_url}/videos",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                result = response.json()
                video_url = result.get("download_url")
                
                if video_url:
                    # Baixar vídeo
                    video_path = f"videos/pendentes/{video_id}_video.mp4"
                    self.baixar_video(video_url, video_path)
                    print(f"✅ Vídeo gerado: {video_path}")
                    return video_path
            
            print(f"❌ Erro na API Synthesia: {response.status_code}")
            return None
            
        except Exception as e:
            print(f"❌ Erro na geração Synthesia: {e}")
            return None
    
    def gerar_video_lumen5(self, prompt: str, video_id: str) -> Optional[str]:
        """Gera vídeo usando Lumen5 API (vídeo com texto)"""
        if not self.config["apis"]["lumen5"]["enabled"]:
            print("⚠️ API Lumen5 não configurada")
            return None
        
        try:
            api_key = self.config["apis"]["lumen5"]["api_key"]
            base_url = self.config["apis"]["lumen5"]["base_url"]
            
            # Preparar payload para Lumen5
            payload = {
                "title": f"RMMS Tech - {video_id}",
                "script": prompt,
                "aspectRatio": "9:16",  # TikTok vertical
                "duration": 35,
                "style": "modern",
                "branding": {
                    "logo": "https://rmms.tech/images/logo.png",
                    "colors": ["#007bff", "#ffffff"]
                }
            }
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            print("🎬 Gerando vídeo via Lumen5...")
            response = requests.post(
                f"{base_url}/videos",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                result = response.json()
                video_url = result.get("download_url")
                
                if video_url:
                    # Baixar vídeo
                    video_path = f"videos/pendentes/{video_id}_video.mp4"
                    self.baixar_video(video_url, video_path)
                    print(f"✅ Vídeo gerado: {video_path}")
                    return video_path
            
            print(f"❌ Erro na API Lumen5: {response.status_code}")
            return None
            
        except Exception as e:
            print(f"❌ Erro na geração Lumen5: {e}")
            return None
    
    def baixar_video(self, url: str, path: str) -> bool:
        """Baixa vídeo da URL"""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            with open(path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            return True
        except Exception as e:
            print(f"❌ Erro ao baixar vídeo: {e}")
            return False
    
    def gerar_video_automatico(self, conteudo_video: Dict, video_id: str) -> Optional[str]:
        """Tenta gerar vídeo usando APIs disponíveis com seleção inteligente"""
        print(f"🎬 Iniciando geração automática de vídeo: {video_id}")
        
        # Estratégia: Pika Labs (mais barato) -> Runway ML (qualidade) -> Lumen5 (fallback)
        tipo_conteudo = conteudo_video.get("tipo_conteudo", "caso_sucesso")
        
        # Priorizar APIs baseado no custo (mais baratas primeiro)
        apis_prioridade = [
            ("pika_labs", self.gerar_video_pika, "prompt_video"),  # $3.50
            ("runway", self.gerar_video_runway, "prompt_video"),    # $7.00
            ("lumen5", self.gerar_video_lumen5, "prompt_video")     # $19.00 (fallback)
        ]
        
        # Verificar quais APIs estão disponíveis
        apis_disponiveis = []
        for nome_api, funcao, campo in apis_prioridade:
            if self.config["apis"][nome_api]["enabled"]:
                apis_disponiveis.append((nome_api, funcao, campo))
        
        if not apis_disponiveis:
            print("⚠️ Nenhuma API configurada. Configure as APIs em config/api_config.json")
            print("💡 Recomendado: Pika Labs ($3.50) + Runway ML ($7.00) = $10.50/vídeo")
            return None
        
        # Tentar APIs na ordem de prioridade
        for nome_api, funcao_geracao, campo in apis_disponiveis:
            print(f"🔄 Tentando API: {nome_api} (prioridade para {tipo_conteudo})")
            
            # Usar o campo apropriado (prompt_video para Pika/Lumen5)
            conteudo = conteudo_video.get(campo, conteudo_video.get("prompt_video"))
            resultado = funcao_geracao(conteudo, video_id)
            
            if resultado:
                print(f"✅ Vídeo gerado com sucesso via {nome_api}")
                return resultado
        
        print("❌ Nenhuma API conseguiu gerar o vídeo")
        return None
    
    def configurar_api(self, nome_api: str, api_key: str) -> bool:
        """Configura uma API específica"""
        try:
            config_path = 'config/api_config.json'
            
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            if nome_api in config["apis"]:
                config["apis"][nome_api]["enabled"] = True
                config["apis"][nome_api]["api_key"] = api_key
                
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=2, ensure_ascii=False)
                
                print(f"✅ API {nome_api} configurada com sucesso!")
                return True
            else:
                print(f"❌ API {nome_api} não encontrada")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao configurar API: {e}")
            return False
    
    def listar_apis_disponiveis(self):
        """Lista APIs disponíveis e status"""
        print("\n🔧 APIs Disponíveis:")
        print("-" * 40)
        
        for nome_api, config in self.config["apis"].items():
            status = "✅ Configurada" if config["enabled"] else "❌ Não configurada"
            print(f"{nome_api.upper()}: {status}")
        
        print("\n📋 Como configurar:")
        print("1. Obtenha API key no site da API")
        print("2. Execute: python3 video_generator.py --config API_NAME API_KEY")
        print("3. Teste: python3 video_generator.py --test API_NAME")

def main():
    """Função principal para testes"""
    import sys
    
    gerador = GeradorVideo()
    
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        
        if comando == "--config" and len(sys.argv) > 3:
            api_name = sys.argv[2]
            api_key = sys.argv[3]
            gerador.configurar_api(api_name, api_key)
        
        elif comando == "--list":
            gerador.listar_apis_disponiveis()
        
        elif comando == "--test" and len(sys.argv) > 2:
            api_name = sys.argv[2]
            print(f"🧪 Testando API: {api_name}")
            # Aqui você pode adicionar testes específicos
        
        else:
            print("""
📖 Comandos disponíveis:
  python3 video_generator.py --config API_NAME API_KEY
  python3 video_generator.py --list
  python3 video_generator.py --test API_NAME

🔧 APIs suportadas:
  - runway (Runway ML)
  - pika_labs (Pika Labs)
  - synthesia (Synthesia)
  - lumen5 (Lumen5)
            """)
    
    else:
        gerador.listar_apis_disponiveis()

if __name__ == "__main__":
    main() 