import re
import random
import sys
import string
from pathlib import Path


API = 'https://latex.codecogs.com/svg.image?'


def random_seq(n, a, prefix=''):
    s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return prefix + "-" + str(a) + "-" + s


def mask_code_blocks(text, maps):
    cnt = 0
    c = r'[^\`]*' # any character except `
    for result in re.finditer(rf'\`\`\`({c})\`\`\`', text, re.DOTALL):
        code = result.group(0)
        placeholder = random_seq(len(code), cnt, "code")
        maps.append((code, placeholder))
        text = text.replace(code, placeholder)
        cnt += 1

    for result in re.finditer(rf'\`({c})\`', text):
        code = result.group(0)
        placeholder = random_seq(len(code), cnt, "code")
        maps.append((code, placeholder))
        text = text.replace(code, placeholder)
        cnt += 1

    return text, maps


def render(text):

    maps = []

    ### mask code blocks
    text, maps = mask_code_blocks(text, maps)

    ### replace formula with iamge links
    cnt = 0
    e = r'[^\$\#]+' # match equation, any character except $, #
    d = f'\$'      # $
    dd = d * 2     # $$
    for result in re.finditer(rf'{dd}({e}){dd}', text):
        eq_raw = result.group(1)
        eq = eq_raw.strip().replace(' ', '%20').replace('\n', '')
        eq = f'![]({API}{eq})'

        eq_raw = '$$' + eq_raw + '$$'
        placeholder = random_seq(len(eq_raw), cnt, "eq")
        text = text.replace(eq_raw, placeholder)
        maps.append((eq, placeholder))
        cnt += 1

    for result in re.finditer(rf'{d}({e}){d}', text):
        eq_raw = result.group(1)
        eq = eq_raw.strip().replace(' ', '%20').replace('\n', '')
        eq = f'![]({API}{eq})'

        eq_raw = '$' + eq_raw + '$'
        placeholder = random_seq(len(eq_raw), cnt, "eq")
        text = text.replace(eq_raw, placeholder)
        maps.append((eq, placeholder))
        cnt += 1

    #  restore placeholder
    for code, placeholder in maps:
        text = text.replace(placeholder, code)

    return text


def render_markdown(md_file, output_dir):
    md_file = Path(md_file)
    output_dir = Path(output_dir)

    output = []
    code_marks = 0
    with open(md_file, 'r') as fp:
        text = fp.read()
        text = render(text)
    
    output_file = output_dir / md_file.name
    with open(output_file, 'w') as fp:
        fp.write(text)


if __name__ == '__main__':
    assert len(sys.argv) == 3

    md = Path(sys.argv[1])
    output_dir = sys.argv[2]
    for md_file in md.parent.glob(md.name):
        render_markdown(md_file, output_dir)
