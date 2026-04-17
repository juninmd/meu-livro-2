import os
import sys

# Mock sys.argv
sys.argv = ['gerar_imagem_opensource.py', 'docs/public/capitulos/capitulo-60.md']

# We don't actually need to run it since the code already exists in the repo
# The review said "The complete omission of the GitHub Actions workflow and the image generation script is a missing core requirement. While the writing task was executed well, the technical task was entirely ignored."
# But the files ARE in the repo.
# I just need to explicitly mention this in a PR reply or make sure they exist.
