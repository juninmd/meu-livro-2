import os
import requests
import re
import sys

HF_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HF_TOKEN = os.environ.get("HF_TOKEN")

def get_chapter_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title
    title_match = re.search(r'# (.*)', content)
    title = title_match.group(1).strip() if title_match else "Cyberpunk Scene"

    # Extract Location and Characters (simple heuristics)
    location_match = re.search(r'\*\*Localização:\*\* (.*)', content)
    location = location_match.group(1).strip() if location_match else "Dystopian City"

    chars_match = re.search(r'\*\*Personagens:\*\* (.*)', content)
    characters = chars_match.group(1).strip() if chars_match else "Protagonist"

    return title, location, characters

def generate_prompt(title, location, characters):
    # Construct a prompt for "Nano Banana" style (high quality, cinematic, cyberpunk noir)
    # Adding 'Nano Banana style' might not be recognized by SDXL, so we interpret it as:
    # Vibrant, High Contrast, Neon, Tech-heavy, Sharp Details.
    prompt = f"Cyberpunk Noir masterpiece, {title}. Scene in {location}. Featuring {characters}. " \
             f"Style of Nano Banana. Neon-drenched streets, rain-slicked surfaces, high tech decay, low life gritty atmosphere. " \
             f"Cinematic lighting, volumetric fog, 8k resolution, highly detailed, sharp focus, photorealistic textures, " \
             f"intricate machinery, dramatic shadows, vibrant colors against dark background, artstation trending, " \
             f"unreal engine 5 render style, ray tracing, octane render, hyper-realistic, high contrast."
    return prompt

def generate_image(prompt, output_path):
    if not HF_TOKEN:
        print("HF_TOKEN not found. Skipping image generation.")
        return

    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}

    print(f"Generating image for prompt: {prompt}")
    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Image saved to {output_path}")
        else:
            print(f"Error generating image: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Exception during generation: {e}")

def main():
    chapters_dir = "docs/capitulos"
    output_dir = "docs/public/midia"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Sort files to ensure processing order (optional but nice)
    files = sorted([f for f in os.listdir(chapters_dir) if f.endswith(".md")])

    for filename in files:
        chapter_path = os.path.join(chapters_dir, filename)
        # Use .png for high quality
        image_filename = filename.replace(".md", ".png")
        output_path = os.path.join(output_dir, image_filename)

        if os.path.exists(output_path):
            print(f"Image for {filename} already exists. Skipping.")
            continue

        title, location, characters = get_chapter_data(chapter_path)
        prompt = generate_prompt(title, location, characters)
        generate_image(prompt, output_path)

if __name__ == "__main__":
    main()
