const fs = require('fs');
const path = require('path');

const files = [
  'src/pages/calorie-deficit-calculator.astro',
  'src/pages/calories-burned-calculator.astro',
  'src/pages/cycling-calories-calculator.astro',
  'src/pages/food-calories-search.astro',
  'src/pages/index.astro',
  'src/pages/meal-calorie-calculator.astro',
  'src/pages/protein-calculator.astro',
  'src/pages/recipe-calorie-calculator.astro',
  'src/pages/running-calorie-calculator.astro',
  'src/pages/swimming-calories-calculator.astro',
  'src/pages/tdee-calculator.astro',
  'src/pages/treadmill-calorie-calculator.astro',
  'src/pages/walking-calorie-calculator.astro',
  'src/pages/country/spain/calculadora-de-calorias.astro',
  'src/pages/calorie-basics/what-is-a-calorie.astro',
  'src/pages/guides/bmr-equations.astro',
  'src/pages/guides/bmr-tdee-formulas-mifflin-harris-benedict.astro',
  'src/pages/guides/body-recomposition-guide.astro',
  'src/pages/guides/calorie-calculator-accuracy.astro',
  'src/pages/guides/calorie-deficit-guide.astro',
  'src/pages/guides/calorie-surplus-guide.astro',
  'src/pages/guides/calories-burned-in-a-day.astro',
  'src/pages/guides/healthy-weight-range.astro',
  'src/pages/guides/how-many-calories-in-a-gram-guide.astro',
  'src/pages/guides/how-many-calories-should-i-eat.astro',
  'src/pages/guides/macro-guide.astro',
  'src/pages/guides/maintenance-calories.astro',
  'src/pages/guides/mifflin-st-jeor-equation.astro',
  'src/pages/guides/mifflin-st-jeor-stress-factors.astro',
  'src/pages/guides/mifflin-st-jeor-women.astro',
  'src/pages/guides/protein-guide.astro',
  'src/pages/guides/weight-gain-guide.astro',
  'src/pages/guides/weight-loss-guide.astro',
  'src/pages/guides/what-is-bmr.astro',
  'src/pages/guides/whats-my-tdee.astro',
  'src/pages/country/spain/calculadora-harris-benedict.astro',
  'src/pages/country/spain/calorias-para-ganar-peso.astro',
  'src/pages/country/spain/calorias-para-perder-peso.astro',
  'src/pages/country/spain/como-calcular-mis-calorias-diarias.astro',
  'src/pages/country/spain/cuantas-calorias-debo-consumir-al-dia.astro',
  'src/pages/404.astro',
  'src/pages/500.astro',
  'src/pages/about.astro',
  'src/pages/contact.astro',
  'src/pages/disclaimer.astro',
  'src/pages/editorial-policy.astro',
  'src/pages/html-sitemap.astro',
  'src/pages/privacy-policy.astro',
  'src/pages/terms.astro',
  'src/pages/guides/index.astro',
  'src/pages/resources/index.astro'
];

files.forEach(f => {
  const content = fs.readFileSync(path.join(process.cwd(), f), 'utf8');
  let match = content.match(/title\s*=\s*["']([^"']+)["']/i);
  if (!match) match = content.match(/title\s*:\s*["']([^"']+)["']/i);
  if (!match) match = content.match(/<title>([^<]+)<\/title>/i);
  let title = match ? match[1] : 'No Title Found';
  console.log(`${f.replace('src/pages/', '')} : ${title}`);
});
