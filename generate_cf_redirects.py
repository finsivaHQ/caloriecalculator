import re
import os

try:
    with open('astro.config.mjs', 'r', encoding='utf-8') as f:
        content = f.read()

    redirects_match = re.search(r'redirects:\s*\{([^}]+)\}', content)
    if redirects_match:
        lines = redirects_match.group(1).splitlines()
        os.makedirs('public', exist_ok=True)
        with open('public/_redirects', 'a', encoding='utf-8') as f:
            f.write('\n# Extracted from astro.config.mjs\n')
            for line in lines:
                if ':' in line and 'destination' in line:
                    source = line.split(':')[0].strip().strip("'")
                    dest_match = re.search(r"destination:\s*'([^']+)'", line)
                    if dest_match:
                        dest = dest_match.group(1)
                        f.write(f'{source} {dest} 301\n')
                elif ':' in line:
                    source = line.split(':')[0].strip().strip("'")
                    dest = line.split(':')[1].strip().strip(",").strip("'")
                    f.write(f'{source} {dest} 301\n')
        print('Successfully generated public/_redirects.')
    else:
        print('No redirects block found.')
except Exception as e:
    print(f"Error: {e}")
