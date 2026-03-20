import os
import sys
import argparse
import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {os.environ.get('HF_TOKEN')}"}

def generate_image(prompt, output_path):
    if not os.environ.get('HF_TOKEN'):
        print("HF_TOKEN environment variable not set. Skipping image generation.")
        return

    payload = {
        "inputs": prompt,
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()

        # Check if the response is actually an image (bytes)
        if response.headers.get('content-type') == 'application/json':
             print(f"Error: Received JSON response instead of image: {response.json()}. Skipping generation.")
             return

        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Image saved to {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error querying API: {e}")
        # Don't fail the build if image gen fails, just log it.
        # Unless it's critical, but usually for docs it's better to proceed.
        # But for this task, let's just print error.
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
    # A better approach would be to ask an LLM to summarize, but we don't have that access here easily without another API key.
    # So we'll use the text directly.
    # remove metadata header if present (between ---)
    lines = content.split('\n')
    text_content = []
    in_metadata = False
    for line in lines:
        if line.strip() == '---':
            if in_metadata:
                in_metadata = False
            else:
                in_metadata = True
            continue
        if not in_metadata and line.strip():
            text_content.append(line.strip())

    raw_text = " ".join(text_content)[:500]

    style_prompt = "Cyberpunk Noir style, Nano Banana aesthetic, vibrant neon, high contrast, surreal, tech-heavy, intricate details, 8k resolution. "
    full_prompt = f"{style_prompt} based on: {raw_text}"

    # Determine output path
    filename = os.path.basename(filepath).replace(".md", ".png")
    output_dir = "docs/public/midia"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    print(f"Generating image for {filename}...")
    generate_image(full_prompt, output_path)

if __name__ == "__main__":
    main()
