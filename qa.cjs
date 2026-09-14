const url = 'https://caloriecalculatorfree.com/country/spain/calculadora-harris-benedict/';
fetch(url).then(async r => {
  console.log('HTTP:', r.status);
  const text = await r.text();
  console.log('Encoding OK (¿):', text.includes('¿'));
  console.log('Encoding OK (á):', text.includes('á'));
  console.log('Encoding OK (ñ):', text.includes('ñ'));
  console.log('Replacement Char:', text.includes('\uFFFD'));
  console.log('Lang es:', text.includes('lang="es"'));
  console.log('H1:', text.match(/<h1[^>]*>(.*?)<\/h1>/s)?.[1]);
  console.log('Title:', text.match(/<title>(.*?)<\/title>/is)?.[1]);
  console.log('Canonical:', text.match(/<link rel="canonical" href="(.*?)"/)?.[1]);
  console.log('Noindex:', text.includes('noindex'));
  console.log('Math check 1:', text.includes('66.4730'));
  console.log('JSON-LD:', text.includes('"@type":"FAQPage"'));
  
  // Links check
  console.log('Calculator Link:', text.includes('href="/country/spain/calculadora-de-calorias/"'));
  console.log('Article 1 Link:', text.includes('href="/country/spain/cuantas-calorias-debo-consumir-al-dia/"'));
  console.log('Article 2 Link:', text.includes('href="/country/spain/como-calcular-mis-calorias-diarias/"'));
})
