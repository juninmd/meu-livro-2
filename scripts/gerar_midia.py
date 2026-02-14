#!/usr/bin/env python3
"""Gera imagens, trailer e narração para o capítulo usando Ollama."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT_DIR = DOCS / "public" / "midia"
CHAPTER = DOCS / "capitulo-1.md"
CHARACTERS = DOCS / "personagens.md"

SCENES = [
    ("capa-capitulo-1", "Capa cinematográfica da distopia A Última Frequência"),
    ("cena-kael-no-topo", "Kael no topo do prédio durante chuva ácida, drone silenciador ao fundo"),
    ("cena-maestro-ministerio", "Maestro no Ministério da Harmonia diante de painéis de vigilância"),
]


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=check, capture_output=True, text=True)


def has(binary: str) -> bool:
    return shutil.which(binary) is not None


def ask_ollama(prompt: str, model: str = "llama3.1") -> str:
    payload = {"model": model, "prompt": prompt, "stream": False, "options": {"temperature": 0.6}}
    result = run(["curl", "-s", "http://127.0.0.1:11434/api/generate", "-d", json.dumps(payload)])
    data = json.loads(result.stdout or "{}")
    return data.get("response", "")


def sanitize_svg(svg: str) -> str:
    match = re.search(r"<svg[\s\S]*</svg>", svg)
    if match:
        return match.group(0)
    return """<svg xmlns='http://www.w3.org/2000/svg' width='1280' height='720'><rect width='1280' height='720' fill='#100a2a'/><text x='80' y='350' fill='#f5f3ff' font-size='58' font-family='Arial'>A Última Frequência</text><text x='80' y='410' fill='#c4b5fd' font-size='28' font-family='Arial'>Fallback automático</text></svg>"""


def generate_images() -> list[Path]:
    chapter = CHAPTER.read_text(encoding="utf-8")
    chars = CHARACTERS.read_text(encoding="utf-8")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pngs: list[Path] = []

    for name, objective in SCENES:
        prompt = f"""
Você é um diretor de arte cyberpunk.
Gere SOMENTE um SVG válido (1280x720), sem markdown.
Objetivo visual: {objective}

Universo:
{chars[:2600]}

Trecho do capítulo:
{chapter[:3200]}
""".strip()
        svg = sanitize_svg(ask_ollama(prompt))
        svg_path = OUT_DIR / f"{name}.svg"
        svg_path.write_text(svg, encoding="utf-8")

        png_path = OUT_DIR / f"{name}.png"
        if has("rsvg-convert"):
            run(["rsvg-convert", "-w", "1280", "-h", "720", str(svg_path), "-o", str(png_path)])
            pngs.append(png_path)

    return pngs


def generate_narration() -> Path | None:
    chapter = CHAPTER.read_text(encoding="utf-8")
    narration = ask_ollama(
        "Resuma o capítulo abaixo em até 140 palavras para narração impactante em português brasileiro.\n"
        "Sem título, sem markdown.\n\n" + chapter[:6000]
    ).strip()
    txt = OUT_DIR / "capitulo-1-narracao.txt"
    txt.write_text(narration, encoding="utf-8")

    if not has("espeak-ng"):
        print("[warn] espeak-ng não encontrado; arquivo de áudio não será gerado.")
        return None

    wav = OUT_DIR / "capitulo-1-narracao.wav"
    run(["espeak-ng", "-v", "pt-br", "-s", "150", "-f", str(txt), "-w", str(wav)])
    return wav


def generate_video(images: list[Path], audio: Path | None) -> None:
    if not images or not has("ffmpeg"):
        print("[warn] ffmpeg indisponível ou sem imagens PNG; vídeo não será gerado.")
        return

    concat = OUT_DIR / "slides.txt"
    temp = OUT_DIR / "capitulo-1-trailer-sem-audio.mp4"
    video = OUT_DIR / "capitulo-1-trailer.mp4"

    lines = []
    for img in images:
        lines += [f"file '{img.as_posix()}'", "duration 3"]
    lines.append(f"file '{images[-1].as_posix()}'")
    concat.write_text("\n".join(lines), encoding="utf-8")

    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", str(temp)])

    if audio and audio.exists():
        run(["ffmpeg", "-y", "-i", str(temp), "-i", str(audio), "-c:v", "copy", "-c:a", "aac", "-shortest", str(video)])
    else:
        temp.rename(video)


def main() -> None:
    images = generate_images()
    audio = generate_narration()
    generate_video(images, audio)
    print("Mídia gerada em", OUT_DIR)


if __name__ == "__main__":
    main()
