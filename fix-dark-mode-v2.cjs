const fs = require('fs');
const path = require('path');

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        if (isDirectory) {
            walkDir(dirPath, callback);
        } else {
            callback(path.join(dir, f));
        }
    });
}

function processFile(filePath) {
    if (!filePath.endsWith('.astro') && !filePath.endsWith('.tsx')) return;

    let content = fs.readFileSync(filePath, 'utf8');
    let original = content;

    // Backgrounds
    content = content.replace(/\bbg-blue-50\b/g, 'bg-canvas-soft');
    content = content.replace(/\bbg-indigo-50\b/g, 'bg-canvas-soft');
    content = content.replace(/\bbg-slate-50\b/g, 'bg-canvas-soft');
    content = content.replace(/\bbg-gray-50\b/g, 'bg-canvas-soft');
    
    content = content.replace(/\bbg-blue-100\b/g, 'bg-surface');
    content = content.replace(/\bbg-indigo-100\b/g, 'bg-surface');
    content = content.replace(/\bbg-slate-100\b/g, 'bg-surface');
    content = content.replace(/\bbg-gray-100\b/g, 'bg-surface');

    // Borders
    content = content.replace(/\bborder-blue-100\b/g, 'border-hairline');
    content = content.replace(/\bborder-indigo-100\b/g, 'border-hairline');
    content = content.replace(/\bborder-blue-200\b/g, 'border-hairline');
    content = content.replace(/\bborder-indigo-200\b/g, 'border-hairline');
    content = content.replace(/\bborder-slate-200\b/g, 'border-hairline');
    content = content.replace(/\bborder-slate-100\b/g, 'border-hairline');
    content = content.replace(/\bborder-gray-200\b/g, 'border-hairline');
    content = content.replace(/\bborder-gray-100\b/g, 'border-hairline');

    // Gradients
    content = content.replace(/\bfrom-blue-50\b/g, 'from-surface');
    content = content.replace(/\bfrom-indigo-50\b/g, 'from-surface');
    content = content.replace(/\bfrom-slate-50\b/g, 'from-surface');
    content = content.replace(/\bfrom-gray-50\b/g, 'from-surface');
    
    content = content.replace(/\bto-blue-50\b/g, 'to-canvas-soft');
    content = content.replace(/\bto-indigo-50\b/g, 'to-canvas-soft');
    content = content.replace(/\bto-slate-50\b/g, 'to-canvas-soft');
    content = content.replace(/\bto-gray-50\b/g, 'to-canvas-soft');
    content = content.replace(/\bto-blue-100\b/g, 'to-canvas-soft');
    content = content.replace(/\bto-indigo-100\b/g, 'to-canvas-soft');

    // Text (Dark colors meant for light backgrounds)
    content = content.replace(/\btext-indigo-900\b/g, 'text-ink');
    content = content.replace(/\btext-indigo-800\b/g, 'text-ink');
    content = content.replace(/\btext-blue-900\b/g, 'text-ink');
    content = content.replace(/\btext-blue-800\b/g, 'text-ink');
    content = content.replace(/\btext-slate-900\b/g, 'text-ink');
    content = content.replace(/\btext-slate-800\b/g, 'text-ink');
    content = content.replace(/\btext-gray-900\b/g, 'text-ink');
    content = content.replace(/\btext-gray-800\b/g, 'text-ink');
    
    content = content.replace(/\btext-indigo-700\b/g, 'text-body');
    content = content.replace(/\btext-blue-700\b/g, 'text-body');
    content = content.replace(/\btext-slate-700\b/g, 'text-body');
    content = content.replace(/\btext-gray-700\b/g, 'text-body');
    
    content = content.replace(/\btext-slate-600\b/g, 'text-mute');
    content = content.replace(/\btext-gray-600\b/g, 'text-mute');
    content = content.replace(/\btext-slate-500\b/g, 'text-mute');
    content = content.replace(/\btext-gray-500\b/g, 'text-mute');

    // Handle the specific Expert tip background gradient/overlay
    content = content.replace(/\bbg-indigo-100\b/g, 'bg-surface/50'); // for absolute pseudo elements

    if (content !== original) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Updated: ${filePath}`);
    }
}

walkDir('src', processFile);
console.log('Dark mode class replacement complete.');
