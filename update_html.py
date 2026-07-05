import re
import sys

file_path = r'd:\WORK\TokuteiViet\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fonts
content = re.sub(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Be\+Vietnam\+Pro:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">',
    content
)

# 2. Canvas & LS
content = re.sub(
    r'<div id="ls">.*?</canvas>',
    '',
    content,
    flags=re.DOTALL
)

# 3. JS Blocks
content = re.sub(
    r'// ---- Loading screen ----.*?// ---- Data ----',
    '// ---- Data ----',
    content,
    flags=re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced simple text")
