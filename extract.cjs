const fs = require('fs');
const path = require('path');

const dirs = ['src/pages/guides', 'src/pages/calorie-basics'];
const posts = [];

for (const dir of dirs) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        if (!file.endsWith('.astro') || file === 'index.astro') continue;
        const filePath = path.join(dir, file);
        const content = fs.readFileSync(filePath, 'utf8');
        
        let title = '';
        let description = '';
        let urlPath = '/' + dir.split('/').pop() + '/' + file.replace('.astro', '/');
        
        const titleMatch = content.match(/title=["']([^"']+)["']/);
        const constTitleMatch = content.match(/const title\s*=\s*["']([^"']+)["']/);
        if (constTitleMatch) title = constTitleMatch[1];
        else if (titleMatch) title = titleMatch[1];
        
        const descMatch = content.match(/description=["']([^"']+)["']/);
        const constDescMatch = content.match(/const description\s*=\s*["']([^"']+)["']/);
        if (constDescMatch) description = constDescMatch[1];
        else if (descMatch) description = descMatch[1];
        
        const pathMatch = content.match(/path=["']([^"']+)["']/);
        const constPathMatch = content.match(/const path\s*=\s*["']([^"']+)["']/);
        if (constPathMatch) urlPath = constPathMatch[1];
        else if (pathMatch) urlPath = pathMatch[1];

        if (title) {
            posts.push({ title, description, href: urlPath });
        }
    }
}

fs.writeFileSync('posts.json', JSON.stringify(posts, null, 2), 'utf8');
