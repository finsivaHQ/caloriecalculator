
const fs = require("fs");
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
    "border-green-500": "border-success",
    "dark:bg-slate-800": "dark:bg-surface",
    "dark:text-white": "dark:text-ink",
    "dark:text-slate-300": "dark:text-body",
    "dark:text-gray-300": "dark:text-body",
    "dark:border-slate-700": "dark:border-hairline-strong"
};

["src/pages/country/spain/calculadora-de-calorias.astro", "src/pages/country/spain/calculadora-de-macros.astro"].forEach(filePath => {
    let content = fs.readFileSync(filePath, "utf8");
    for (const [key, value] of Object.entries(replacements)) {
        content = content.split(key).join(value);
    }
    fs.writeFileSync(filePath, content, "utf8");
});

