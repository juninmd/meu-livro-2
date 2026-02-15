import os
import sys
import requests
import argparse

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HF_TOKEN = os.environ.get("HF_TOKEN")

def query(payload):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def generate_prompt(content):
    # Simple extraction: Title + first paragraph
    lines = content.split('\n')
    title = "Cyberpunk Scene"
    paragraph = ""
    for line in lines:
        if line.startswith("# "):
            title = line.replace("# ", "").strip()
        elif line.strip() and not line.startswith("#") and not line.startswith("<"):
            paragraph = line.strip()
            break

    # Construct prompt with specific style instructions
    prompt = f"cyberpunk noir style, {title}, {paragraph[:200]}, inspired by nano banana, cinematic lighting, highly detailed, 8k, dystopian atmosphere"
    return prompt

def main():
    parser = argparse.ArgumentParser(description='Generate chapter image.')
    parser.add_argument('file_path', type=str, help='Path to the chapter markdown file')
    args = parser.parse_args()

    if not HF_TOKEN:
        print("HF_TOKEN environment variable not set. Skipping image generation.")
        return

    file_path = args.file_path
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        sys.exit(1)

    with open(file_path, 'r') as f:
        content = f.read()

    prompt = generate_prompt(content)
    print(f"Generating image for {file_path} with prompt: {prompt}")

    try:
        image_bytes = query({"inputs": prompt})

        # Check if response is JSON (error) or bytes (image)
        if image_bytes.startswith(b'{') and b'error' in image_bytes:
            print(f"Error from API: {image_bytes}")
            sys.exit(1)

        # Determine output path
        filename = os.path.basename(file_path).replace('.md', '.jpg')
        output_dir = os.path.join('docs', 'public', 'midia')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, filename)

        with open(output_path, 'wb') as f:
            f.write(image_bytes)

        print(f"Image saved to {output_path}")

    except Exception as e:
        print(f"Failed to generate image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
