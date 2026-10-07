
const fs = require("fs");
const path = require("path");

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walkDir(dirPath, callback) : callback(path.join(dir, f));
    });
}

const replacements = {
    "text-slate-900": "text-ink",
    "text-slate-800": "text-ink",
    "text-gray-900": "text-ink",
    "text-gray-800": "text-ink",
    "text-slate-700": "text-body",
    "text-slate-600": "text-body",
    "text-gray-700": "text-body",
    "text-gray-600": "text-body",
    "text-slate-500": "text-mute",
    "text-gray-500": "text-mute",
    "bg-slate-50": "bg-canvas-soft",
    "bg-slate-100": "bg-canvas-soft-2",
    "bg-gray-50": "bg-canvas-soft",
    "bg-gray-100": "bg-canvas-soft-2",
    "bg-white": "bg-surface",
    "border-slate-200": "border-hairline",
    "border-slate-300": "border-hairline-strong",
    "border-gray-200": "border-hairline",
    "border-gray-300": "border-hairline-strong",
    "bg-blue-50": "bg-brand-soft",
    "bg-indigo-50": "bg-brand-soft",
    "bg-blue-100": "bg-brand-soft",
    "bg-blue-500": "bg-brand",
    "bg-blue-600": "bg-brand",
    "bg-blue-700": "bg-brand-hover",
    "bg-indigo-600": "bg-brand",
    "bg-indigo-700": "bg-brand-hover",
    "text-blue-500": "text-brand",
    "text-blue-600": "text-brand",
    "text-blue-700": "text-brand-hover",
    "text-blue-800": "text-ink",
    "text-blue-900": "text-ink",
    "text-indigo-600": "text-brand",
    "text-indigo-700": "text-brand-hover",
    "border-blue-500": "border-brand",
    "border-blue-600": "border-brand",
    "border-indigo-500": "border-brand",
    "text-green-800": "text-ink",
    "bg-green-50": "bg-success",
    "border-green-500": "border-success"
};

walkDir("./src/pages", (filePath) => {
    if (filePath.endsWith(".astro")) {
        let content = fs.readFileSync(filePath, "utf8");
        let originalContent = content;
        
        for (const [key, value] of Object.entries(replacements)) {
            const regex = new RegExp("\\b" + key + "\\b", "g");
            content = content.replace(regex, value);
        }
        
        if (content !== originalContent) {
            fs.writeFileSync(filePath, content, "utf8");
            console.log(`Updated: ${filePath}`);
        }
    }
});

