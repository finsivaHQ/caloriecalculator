const fs = require('fs');
const path = require('path');

// Re-read _redirects up to the auto-generated section to reset
let existingRedirectsRaw = fs.readFileSync('public/_redirects', 'utf8');
if (existingRedirectsRaw.includes('# Auto-generated redirects')) {
  existingRedirectsRaw = existingRedirectsRaw.split('# Auto-generated redirects')[0];
  fs.writeFileSync('public/_redirects', existingRedirectsRaw);
}

const existingRedirectsList = existingRedirectsRaw.split('\n').filter(line => line.trim() && !line.startsWith('#')).map(line => line.split(' ')[0]);

// Same deletedPages array as before
const deletedPages = [
  '/guides/best-exercises-to-burn-calories/',
  '/guides/calories-burned-swimming/',
  '/guides/daily-energy-requirements-explained/',
  '/guides/exercise-calories-burned-walking-running/',
  '/guides/how-to-gain-weight/',
  '/guides/intermittent-fasting-for-beginners/',
  '/guides/accurate-tdee-calculator-men-women/',
  '/guides/are-calorie-calculators-accurate/',
  '/guides/best-calorie-counter-macro-tracking-apps/',
  '/guides/best-free-calorie-calculator/',
  '/guides/bike-calorie-calculator/',
  '/guides/fast-food-restaurant-calorie-calculator/',
  '/guides/online-calorie-calculator/',
  '/guides/protein-calculator-guide/',
  '/guides/protein-calorie-calculator/',
  '/guides/protein-calories/',
  '/guides/tdee-calculation/',
  '/guides/tdee-calculator-guide/',
  '/guides/tdee-calculator-weight-loss-guide/',
  '/guides/uk-nhs-tdee-guidelines/',
  '/low-calorie/alcohol/',
  '/low-calorie/drinks/',
  '/low-calorie/dunkin/',
  '/low-calorie/foods/',
  '/low-calorie/',
  '/low-calorie/starbucks/',
  '/low-calorie/sweet-treats/',
  '/alcohol-calories-calculator/',
  '/guides/alcohol-calorie-counter/',
  '/resources/calorie-deficit-guide/',
  '/resources/calorie-surplus-guide/',
  '/resources/what-is-tdee/',
  '/army-body-fat-calculator/',
  '/bmi-calculator/',
  '/body-fat-calculator/',
  '/guides/metabolism-calculator/',
  '/healthy-weight-calculator/',
  '/lean-body-mass-calculator/',
  '/resources/army-tape-test/',
  '/resources/bmi-calculator/',
  '/resources/body-fat-percentage/',
  '/resources/lean-body-mass/',
  '/weight-gain-calculator/',
  '/bmr-calculator/',
  '/guides/bmr-calculator/',
  '/guides/calculate-bmr/',
  '/guides/harris-benedict-calculator/',
  '/guides/harris-benedict-revised/',
  '/guides/how-many-calories-to-lose-weight-calculator/',
  '/guides/maintenance-calorie-calculator/',
  '/guides/weight-loss-calorie-calculator/',
  '/ideal-weight-calculator/',
  '/intermittent-fasting-calculator/',
  '/macro-calculator/',
  '/maintenance-calories-calculator/',
  '/resources/harris-benedict-equation/',
  '/resources/ideal-body-weight/',
  '/resources/macro-calculator/',
  '/resources/maintenance-calorie-calculator/',
  '/resources/water-intake-calculator/',
  '/resources/weight-loss-calculator/',
  '/tdee-calculator-for-weight-loss/',
  '/water-intake-calculator/',
  '/weight-loss-calculator/',
  '/guides/epley-formula/',
  '/one-rep-max-calculator/',
  '/pace-calculator/',
  '/target-heart-rate-calculator/',
  '/workouts/all-in-one-exercise/10-exercises/',
  '/workouts/all-in-one-exercise/7-exercises/',
  '/workouts/all-in-one-exercise/best-beginners/',
  '/workouts/all-in-one-exercise/best-machine/',
  '/workouts/all-in-one-exercise/equipment/',
  '/workouts/all-in-one-exercise/full-body-workout/',
  '/workouts/all-in-one-exercise/',
  '/workouts/all-in-one-exercise/workout-at-home/',
  '/workouts/back-workouts/',
  '/workouts/chest-workouts/',
  '/workouts/home-workouts/',
  '/workouts/',
  '/workouts/leg-curl-machine/',
  '/workouts/leg-curl-machine/alternatives/',
  '/workouts/leg-curl-machine/benefits/',
  '/workouts/leg-curl-machine/best-leg-curl-machines/',
  '/workouts/leg-curl-machine/common-mistakes/',
  '/workouts/leg-curl-machine/evolve-stehende-beinbeuger-maschine-evolve-fitness-ul-140-grosse/',
  '/workouts/leg-curl-machine/for-hamstrings/',
  '/workouts/leg-curl-machine/hamstring-leg-curl-machine/',
  '/workouts/leg-curl-machine/how-to-use-a-leg-curl-machine/',
  '/workouts/leg-curl-machine/leg-curl-extension-machine/',
  '/workouts/leg-curl-machine/leg-extension-machine/',
  '/workouts/leg-curl-machine/lying-hamstring-curl/',
  '/workouts/leg-curl-machine/muscles-worked/',
  '/workouts/leg-curl-machine/prone-leg-curl/',
  '/workouts/leg-curl-machine/seated-vs-lying-leg-curl/',
  '/workouts/leg-curl-machine/single-leg-curl-machine-guide/',
  '/workouts/leg-curl-machine/standing-leg-curl-guide/',
  '/workouts/leg-workouts/',
  '/workouts/lying-leg-raises/',
  '/workouts/shoulder-workouts/',
  '/guides/protein-to-kcal/',
  '/resources/protein-to-calories/',
  '/guides/estimate-delivery-date/',
  '/age-calculator/',
  '/due-date-calculator/',
  '/mortgage-calculator/',
  '/pregnancy-calculator/',
  '/pregnancy-conception-calculator/',
  '/guides/calorie-calculator-accuracy/',
  '/guides/calorie-calculator-by-age/',
  '/guides/calorie-calculator-for-men/',
  '/guides/calorie-calculator-for-women/'
];

function mapToAlive(url) {
  if (url.includes('protein')) return '/protein-calculator/';
  if (url.includes('tdee')) return '/tdee-calculator/';
  if (url.includes('bmr') || url.includes('harris-benedict') || url.includes('metabolism')) return '/guides/what-is-bmr/';
  if (url.includes('lose-weight') || url.includes('weight-loss') || url.includes('deficit')) return '/guides/calorie-deficit-guide/';
  if (url.includes('gain') || url.includes('surplus')) return '/guides/bulking-calorie-calculator/';
  if (url.includes('maintenance')) return '/guides/maintenance-calories/';
  if (url.includes('swimming')) return '/swimming-calories-calculator/';
  if (url.includes('bike') || url.includes('cycling')) return '/cycling-calories-calculator/';
  if (url.includes('walk') || url.includes('run') || url.includes('pace') || url.includes('step')) return '/running-calorie-calculator/';
  if (url.includes('workout') || url.includes('exercise') || url.includes('leg-curl') || url.includes('target-heart')) return '/calories-burned-calculator/';
  if (url.includes('low-calorie') || url.includes('foods')) return '/foods/';
  if (url.includes('mortgage') || url.includes('pregnancy') || url.includes('age') || url.includes('due-date') || url.includes('delivery')) return '/';
  if (url.includes('bmi') || url.includes('body-fat') || url.includes('lean-body') || url.includes('tape-test')) return '/';
  if (url.includes('fasting')) return '/';
  if (url.includes('water')) return '/';
  if (url.includes('alcohol')) return '/guides/how-many-calories-in-a-gram-guide/';
  if (url.includes('macro')) return '/guides/macro-guide/';
  if (url.includes('calorie-calculator')) return '/';
  return '/';
}

function pageExists(urlPath) {
  // Try mapping URL path to physical .astro file
  // e.g. /guides/calorie-calculator-accuracy/ -> src/pages/guides/calorie-calculator-accuracy.astro
  // e.g. /workouts/ -> src/pages/workouts/index.astro OR src/pages/workouts.astro
  
  const cleanPath = urlPath.replace(/^\//, '').replace(/\/$/, '');
  
  if (cleanPath === '') return true; // root exists
  
  const exactFile = path.join('src/pages', cleanPath + '.astro');
  const indexFile = path.join('src/pages', cleanPath, 'index.astro');
  
  return fs.existsSync(exactFile) || fs.existsSync(indexFile);
}

let newRedirects = '\n# Auto-generated redirects for historically deleted pages\n';
let addedCount = 0;

for (const oldUrl of deletedPages) {
  if (!existingRedirectsList.includes(oldUrl)) {
    if (!pageExists(oldUrl)) {
      const newUrl = mapToAlive(oldUrl);
      newRedirects += `${oldUrl} ${newUrl} 301\n`;
      addedCount++;
    } else {
      console.log(`Skipping ${oldUrl} because the page actually exists!`);
    }
  }
}

if (addedCount > 0) {
  fs.appendFileSync('public/_redirects', newRedirects);
  console.log(`Added ${addedCount} new redirects to public/_redirects`);
} else {
  console.log('No new redirects needed.');
}
