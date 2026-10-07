const fs = require('fs');
const path = require('path');

const dirsToSearch = ['src/pages', 'src/components'];

const replacements = {
    // Text colors
    '\\btext-(?:gray|slate)-(?:800|900)\\b': 'text-ink',
    '\\btext-black\\b': 'text-ink',
    '\\btext-(?:gray|slate)-700\\b': 'text-body',
    '\\btext-(?:gray|slate)-(?:300|400|500|600)\\b': 'text-mute',
    // Backgrounds
    '\\bbg-white\\b': 'bg-surface',
    '\\bbg-white\\/(\\d+)\\b': 'bg-surface/$1',
    '\\bbg-(?:gray|slate)-(?:50|100)\\b': 'bg-canvas-soft',
    '\\bbg-(?:gray|slate)-(?:200|300)\\b': 'bg-surface',
    '\\bbg-(?:gray|slate)-(?:700|800|900)\\b': 'bg-surface-elevated',
    '\\bbg-black\\b': 'bg-surface-elevated',
    // Borders
    '\\bborder-(?:gray|slate)-(?:100|200|300|400|500|600|700|800|900)\\b': 'border-hairline',
    // Remove manual dark mode classes
    '\\bdark:(?:bg|text|border)-[a-zA-Z0-9-]+\\b': ''
};

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let original = content;

    // Special case for buttons or images that might legitimately need text-white on a dark background or bg-white
    // But since this is standard content, let's blindly apply semantic tokens first
    for (const [pattern, replacement] of Object.entries(replacements)) {
        const regex = new RegExp(pattern, 'g');
        content = content.replace(regex, replacement);
    }
    
    // Clean up multiple spaces that might result from removing dark: classes
    content = content.replace(/class="([^"]*?)\s{2,}([^"]*?)"/g, 'class="$1 $2"');
    content = content.replace(/class="\s+/g, 'class="');
    content = content.replace(/\s+"/g, '"');

    if (content !== original) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Updated: ${filePath}`);
    }
}

function walk(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const p = path.join(dir, file);
        if (fs.statSync(p).isDirectory()) {
            walk(p);
        } else if (p.endsWith('.astro')) {
            processFile(p);
        }
    }
}

dirsToSearch.forEach(walk);
