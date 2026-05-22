import os
import sys
import argparse
import requests
import time

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {os.environ.get('HF_TOKEN')}"}

def generate_image(prompt, output_path):
    if not os.environ.get('HF_TOKEN'):
        print("HF_TOKEN environment variable not set. Pulando geração de imagem.")
        return

    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": "blurry, low quality, distorted, ugly, pixelated, watermark, text, bad anatomy, deformed",
            "num_inference_steps": 30,
            "guidance_scale": 7.5,
        }
    }

    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"Tentativa {attempt+1} para gerar a imagem...")
            response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
            response.raise_for_status()

            content_type = response.headers.get('content-type', '')
            if 'application/json' in content_type:
                 error_json = response.json()
                 if 'error' in error_json and 'loading' in error_json.get('error', '').lower():
                     estimated_time = error_json.get('estimated_time', 20)
                     print(f"Modelo carregando. Aguardando {estimated_time} segundos...")
                     time.sleep(estimated_time)
                     continue

                 print(f"Erro: Resposta JSON ao invés de imagem: {error_json}")
                 return

            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"Imagem salva em {output_path}")
            return

        except requests.exceptions.RequestException as e:
            print(f"Erro na API: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
            else:
                print("Tentativas esgotadas.")
                pass

def extrair_metadados_texto(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    in_metadata = False
    personagens = ""
    texto = []

    for linha in linhas:
        if linha.strip() == '---':
            in_metadata = not in_metadata
            continue
        if in_metadata:
            if linha.startswith("personagens:"):
                personagens = linha.replace("personagens:", "").strip()
        if not in_metadata and linha.strip() and not linha.startswith('#'):
            texto.append(linha.strip())

    return personagens, " ".join(texto)[:500]

def main():
    parser = argparse.ArgumentParser(description="Gerar imagem para um capítulo inspirado no Nano Banana.")
    parser.add_argument("filepath", help="Caminho para o arquivo markdown do capítulo.")
    args = parser.parse_args()

    filepath = args.filepath
    if not os.path.exists(filepath):
        print(f"Arquivo não encontrado: {filepath}")
        sys.exit(1)

    personagens, trecho = extrair_metadados_texto(filepath)

    base_prompt = "Cyberpunk Noir style, Nano Banana aesthetic, vibrant neon, high contrast, surreal, tech-heavy, intricate details, 8k resolution, cinematic lighting."
    pers_prompt = f" Featuring characters: {personagens}." if personagens else ""
    full_prompt = f"{base_prompt}{pers_prompt} Scene: {trecho}"

    filename = os.path.basename(filepath).replace(".md", ".png")
    output_dir = "docs/public/midia"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    print(f"Gerando imagem para {filename}...")
    generate_image(full_prompt, output_path)

if __name__ == "__main__":
    main()