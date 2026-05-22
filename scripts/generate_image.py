import os
import sys
import argparse
import requests
import time

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {os.environ.get('HF_TOKEN')}"}

def generate_image(prompt, output_path):
    if not os.environ.get('HF_TOKEN'):
        print("HF_TOKEN environment variable not set. Skipping image generation.")
        return

    # Enhanced payload with negative prompt and parameters
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
            print(f"Attempt {attempt+1} to generate image...")
            response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
            response.raise_for_status()

            # Check if the response is actually an image (bytes)
            content_type = response.headers.get('content-type', '')
            if 'application/json' in content_type:
                 error_json = response.json()
                 # If model is loading, wait and retry
                 if 'error' in error_json and 'loading' in error_json.get('error', '').lower():
                     estimated_time = error_json.get('estimated_time', 20)
                     print(f"Model is loading. Waiting {estimated_time} seconds...")
                     time.sleep(estimated_time)
                     continue

                 print(f"Error: Received JSON response instead of image: {error_json}")
                 # Don't exit, just return (fail gracefully for this image)
                 return

            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"Image saved to {output_path}")
            return

        except requests.exceptions.RequestException as e:
            print(f"Error querying API: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
            else:
                print("Max retries reached. Skipping image generation.")
                pass

def main():
    parser = argparse.ArgumentParser(description="Generate image for a chapter.")
    parser.add_argument("filepath", help="Path to the chapter markdown file.")
    args = parser.parse_args()

    filepath = args.filepath
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)

    # Read content to generate prompt
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Simple prompt extraction: Take first 500 characters, remove markdown headers
    lines = content.split('\n')
    text_content = []
    in_metadata = False
    personagens = ""
    for line in lines:
        if line.strip() == '---':
            if in_metadata:
                in_metadata = False
            else:
                in_metadata = True
            continue
        if in_metadata:
            if line.startswith("personagens:"):
                personagens = line.replace("personagens:", "").strip()
        if not in_metadata and line.strip() and not line.startswith('#'):
            text_content.append(line.strip())

    raw_text = " ".join(text_content)[:500]

    # Enhanced Style Prompt
    style_prompt = "Cyberpunk Noir style, Nano Banana aesthetic, vibrant neon, high contrast, surreal, tech-heavy, intricate details, 8k resolution, cinematic lighting."
    personagens_prompt = f" Featuring characters: {personagens}." if personagens else ""
    full_prompt = f"{style_prompt}{personagens_prompt} based on scene: {raw_text}"

    # Determine output path
    filename = os.path.basename(filepath).replace(".md", ".png")
    output_dir = "docs/public/midia"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    print(f"Generating image for {filename}...")
    generate_image(full_prompt, output_path)

if __name__ == "__main__":
    main()
