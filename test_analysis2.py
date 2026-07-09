with open('REVISÃO.md', 'r') as f:
    text = f.read()

for i in range(1, 76):
    import re
    pattern = rf"(?i)\*\*Análise d(o|os) Capítulos?.*?\b{i}\b.*?\*\*"
    if not re.search(pattern, text):
        print(f"Missing analysis header for chapter {i}")
