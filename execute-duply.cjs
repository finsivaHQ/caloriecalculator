const fs = require('fs');
const path = require('path');

const deletesAndRedirects = [
  // English - Weight Loss / Deficit
  { file: 'src/pages/guides/calorie-deficit-guide.astro', redirectFrom: '/guides/calorie-deficit-guide/', redirectTo: '/calorie-deficit-calculator/' },
  { file: 'src/pages/guides/calorie-calculator-to-lose-weight.astro', redirectFrom: '/guides/calorie-calculator-to-lose-weight/', redirectTo: '/' },
  { file: 'src/pages/guides/how-many-calories-should-i-eat.astro', redirectFrom: '/guides/how-many-calories-should-i-eat/', redirectTo: '/' },
  { file: 'src/pages/guides/how-to-calculate-calorie-intake.astro', redirectFrom: '/guides/how-to-calculate-calorie-intake/', redirectTo: '/' },
  { file: 'src/pages/guides/weight-loss-guide.astro', redirectFrom: '/guides/weight-loss-guide/', redirectTo: '/calorie-deficit-calculator/' },

  // English - Weight Gain / Surplus
  { file: 'src/pages/guides/weight-gain-guide.astro', redirectFrom: '/guides/weight-gain-guide/', redirectTo: '/guides/calorie-surplus-guide/' },
  { file: 'src/pages/guides/bulking-calorie-calculator.astro', redirectFrom: '/guides/bulking-calorie-calculator/', redirectTo: '/guides/calorie-surplus-guide/' },

  // English - BMR Equations
  { file: 'src/pages/guides/bmr-equations.astro', redirectFrom: '/guides/bmr-equations/', redirectTo: '/guides/what-is-bmr/' },
  { file: 'src/pages/guides/bmr-tdee-formulas-mifflin-harris-benedict.astro', redirectFrom: '/guides/bmr-tdee-formulas-mifflin-harris-benedict/', redirectTo: '/guides/what-is-bmr/' },
  { file: 'src/pages/guides/mifflin-st-jeor-equation.astro', redirectFrom: '/guides/mifflin-st-jeor-equation/', redirectTo: '/guides/what-is-bmr/' },
  { file: 'src/pages/guides/mifflin-st-jeor-women.astro', redirectFrom: '/guides/mifflin-st-jeor-women/', redirectTo: '/guides/what-is-bmr/' },
  { file: 'src/pages/guides/mifflin-st-jeor-stress-factors.astro', redirectFrom: '/guides/mifflin-st-jeor-stress-factors/', redirectTo: '/guides/what-is-bmr/' },
  { file: 'src/pages/guides/katch-mcardle-equation.astro', redirectFrom: '/guides/katch-mcardle-equation/', redirectTo: '/guides/what-is-bmr/' },

  // English - TDEE
  { file: 'src/pages/guides/whats-my-tdee.astro', redirectFrom: '/guides/whats-my-tdee/', redirectTo: '/tdee-calculator/' },
  { file: 'src/pages/guides/calories-burned-in-a-day.astro', redirectFrom: '/guides/calories-burned-in-a-day/', redirectTo: '/tdee-calculator/' },

  // English - Protein
  { file: 'src/pages/guides/protein-guide.astro', redirectFrom: '/guides/protein-guide/', redirectTo: '/protein-calculator/' },

  // Spanish - Weight Loss / Deficit
  { file: 'src/pages/country/spain/calorias-para-perder-peso.astro', redirectFrom: '/country/spain/calorias-para-perder-peso/', redirectTo: '/country/spain/calculadora-de-calorias/' },
  { file: 'src/pages/country/spain/como-calcular-mis-calorias-diarias.astro', redirectFrom: '/country/spain/como-calcular-mis-calorias-diarias/', redirectTo: '/country/spain/calculadora-de-calorias/' },
  { file: 'src/pages/country/spain/cuantas-calorias-debo-consumir-al-dia.astro', redirectFrom: '/country/spain/cuantas-calorias-debo-consumir-al-dia/', redirectTo: '/country/spain/calculadora-de-calorias/' },
  { file: 'src/pages/country/spain/que-es-el-deficit-calorico.astro', redirectFrom: '/country/spain/que-es-el-deficit-calorico/', redirectTo: '/country/spain/calculadora-de-calorias/' },

  // Spanish - Weight Gain
  { file: 'src/pages/country/spain/calorias-para-ganar-peso.astro', redirectFrom: '/country/spain/calorias-para-ganar-peso/', redirectTo: '/country/spain/que-es-el-superavit-calorico/' },

  // Spanish - BMR
  { file: 'src/pages/country/spain/calculadora-harris-benedict.astro', redirectFrom: '/country/spain/calculadora-harris-benedict/', redirectTo: '/country/spain/que-es-el-metabolismo-basal/' },
];

let redirectsContent = '';
if (fs.existsSync('public/_redirects')) {
  redirectsContent = fs.readFileSync('public/_redirects', 'utf8');
}

for (const item of deletesAndRedirects) {
  if (fs.existsSync(item.file)) {
    fs.unlinkSync(item.file);
    console.log(`Deleted: ${item.file}`);
  } else {
    console.log(`Not found: ${item.file}`);
  }

  const redirectRule = `${item.redirectFrom} ${item.redirectTo} 301`;
  if (!redirectsContent.includes(redirectRule)) {
    redirectsContent += `\n${redirectRule}`;
  }
}

fs.writeFileSync('public/_redirects', redirectsContent.trim() + '\n', 'utf8');
console.log('Updated public/_redirects');

