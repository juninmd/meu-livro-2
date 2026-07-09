with open('REVISÃO.md', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith("**Análise"):
        print(f"Found analysis: {line.strip()}")
