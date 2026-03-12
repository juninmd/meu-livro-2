import os
import sys
import re
import time
import requests

API_URL = "https://router.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {os.environ.get('HF_TOKEN')}"}

def extract_metadata_and_text(filepath):
    try:
        if os.path.islink(filepath): raise Exception("Symbolic links are not allowed")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        personagens = "Cyberpunk city, shadows, neon lights"
        texto = ""

        # Extract metadata
        match = re.search(r'---(.*?)---(.*)', content, re.DOTALL)
        if match:
            metadata = match.group(1)
            char_match = re.search(r'personagens:\s*(.*)', metadata, re.IGNORECASE)
            if char_match:
                personagens = char_match.group(1).strip()

            # Extract up to 300 characters of the actual narrative text, removing markdown headers
            raw_text = match.group(2).strip()
            # Remove Markdown headers like # or ##
            clean_text = re.sub(r'^#.*$', '', raw_text, flags=re.MULTILINE).strip()
            texto = clean_text[:300].replace('\n', ' ')
        return personagens, texto
    except Exception as e:
        print(f"Erro ao ler metadados: {e}")
    return "Cyberpunk city, shadows, neon lights", ""

def query(payload):
    max_retries = 5
    for attempt in range(max_retries):
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            return response.content

        if response.status_code == 503:
            print("Modelo carregando (503)... esperando 20 segundos.")
            time.sleep(20)
            continue

        print(f"Erro da API ({response.status_code}): {response.text}")
        return None

    print("Tempo limite excedido aguardando o modelo.")
    return None

def main():
    if len(sys.argv) < 2:
        print("Uso: python gerar_imagem_opensource.py <caminho_do_arquivo.md>")
        sys.exit(1)

    filepath = sys.argv[1]
    filename = os.path.basename(filepath).replace('.md', '.png')
    out_dir = os.path.join('docs', 'static', 'midia')
    out_path = os.path.join(out_dir, filename)

    os.makedirs(out_dir, exist_ok=True)

    personagens, texto = extract_metadata_and_text(filepath)

    # Ensure the prompt uses the open source model requirement "inspired by nano banana"
    base_prompt = "Cyberpunk noir style, inspired by nano banana, high contrast, vibrant neon lighting, dark shadows, decaying urban environment, intricate details, masterpiece."
    full_prompt = f"{base_prompt} Featuring characters: {personagens.replace('ignore', '[REDACTED]')}. Context: {texto.replace('ignore', '[REDACTED]')}"

    payload = {
        "inputs": full_prompt,
        "parameters": {
            "num_inference_steps": 30,
            "guidance_scale": 7.5,
            "negative_prompt": "ugly, blurry, deformed, low quality, bright daylight, cheerful, text, watermark"
        }
    }

    print(f"Gerando imagem para: {filename}")
    print(f"Prompt: {full_prompt}")

    image_bytes = query(payload)

    if image_bytes:
        with open(out_path, 'wb') as f:
            f.write(image_bytes)
        print(f"Imagem salva com sucesso em: {out_path}")
    else:
        print("Falha ao gerar a imagem.")
        sys.exit(1)

if __name__ == "__main__":
    main()
