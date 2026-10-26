/**
 * gsc-miner.js
 * Automated GSC Query Mining & Opportunity Detection Script
 *
 * Usage:
 *   node scripts/gsc-miner.js [path/to/Queries.csv or gsc.json]
 *   node scripts/gsc-miner.js --demo
 */

import fs from 'fs';

// Active calculator & guide route mapping for automatic clustering
const ROUTE_RULES = [
  { match: /(protein|macro|amino|whey)/i, target: '/protein-calculator/', name: 'Protein Calculator' },
  { match: /(tdee|bmr|mifflin|harris|metabolic rate)/i, target: '/tdee-calculator/', name: 'TDEE Calculator' },
  { match: /(deficit|lose weight|fat loss|cutting)/i, target: '/calorie-deficit-calculator/', name: 'Calorie Deficit Calculator' },
  { match: /(bulk|surplus|gain weight|mass)/i, target: '/guides/calorie-surplus-guide/', name: 'Calorie Surplus Guide' },
  { match: /(recipe|ingredients)/i, target: '/recipe-calorie-calculator/', name: 'Recipe Calorie Calculator' },
  { match: /(meal|breakfast|lunch|dinner)/i, target: '/meal-calorie-calculator/', name: 'Meal Calorie Calculator' },
  { match: /(walking|steps|walk)/i, target: '/walking-calorie-calculator/', name: 'Walking Calorie Calculator' },
  { match: /(running|jogging|run)/i, target: '/running-calorie-calculator/', name: 'Running Calorie Calculator' },
  { match: /(cycling|bike|biking)/i, target: '/cycling-calories-calculator/', name: 'Cycling Calorie Calculator' },
  { match: /(swimming|swim|laps)/i, target: '/swimming-calories-calculator/', name: 'Swimming Calorie Calculator' },
  { match: /(treadmill|incline)/i, target: '/treadmill-calorie-calculator/', name: 'Treadmill Calorie Calculator' },
  { match: /(burned|burn|exercise|workout)/i, target: '/calories-burned-calculator/', name: 'Calories Burned Calculator' },
  { match: /(how many calories in|calories in|kcal in)/i, target: '/foods/', name: 'Food Database' },
  { match: /.*/, target: '/', name: 'Main Calorie Calculator' }
];

function mapQueryToPage(query) {
  for (const rule of ROUTE_RULES) {
    if (rule.match.test(query)) {
      return { url: rule.target, name: rule.name };
    }
  }
  return { url: '/', name: 'Main Calorie Calculator' };
}

// Built-in verified historical baseline dataset for demo/immediate execution
const DEMO_QUERIES = [
  { query: 'how to calculate your calories and protein for fat loss', clicks: 2, impressions: 38, ctr: 0.0526, position: 7.75 },
  { query: 'how many calori', clicks: 4, impressions: 120, ctr: 0.0333, position: 8.92 },
  { query: 'calories to eat per day calculator', clicks: 12, impressions: 450, ctr: 0.0267, position: 9.75 },
  { query: 'how many calories are in a gram of fat', clicks: 8, impressions: 210, ctr: 0.0381, position: 10.0 },
  { query: 'fat grams to kcal', clicks: 5, impressions: 160, ctr: 0.0312, position: 10.33 },
  { query: 'how much protein per day to lose weight', clicks: 7, impressions: 195, ctr: 0.0359, position: 10.76 },
  { query: 'calorie calculator bulk', clicks: 3, impressions: 85, ctr: 0.0353, position: 11.0 },
  { query: 'calories to lose weight women calculator', clicks: 6, impressions: 140, ctr: 0.0428, position: 11.0 },
  { query: 'how many grams of protein should i eat per meal', clicks: 4, impressions: 90, ctr: 0.0444, position: 12.0 },
  { query: 'how many grams of protein should i eat a day', clicks: 9, impressions: 240, ctr: 0.0375, position: 13.08 },
  { query: 'mifflin-st jeor equation calculator', clicks: 2, impressions: 110, ctr: 0.0182, position: 16.5 },
  { query: 'accurate maintenance calorie calculator', clicks: 3, impressions: 75, ctr: 0.0400, position: 17.0 },
  { query: 'calories burned walking 10000 steps', clicks: 1, impressions: 65, ctr: 0.0154, position: 18.2 },
  { query: 'calories in 1 banana', clicks: 5, impressions: 310, ctr: 0.0161, position: 14.2 },
  { query: 'calories in 1 boiled egg', clicks: 8, impressions: 420, ctr: 0.0190, position: 12.8 }
];

function parseCSV(content) {
  const lines = content.split('\n').filter(l => l.trim().length > 0);
  const headers = lines[0].split(',').map(h => h.trim().toLowerCase().replace(/"/g, ''));
  const qIdx = headers.findIndex(h => h.includes('top queries') || h.includes('query'));
  const cIdx = headers.findIndex(h => h.includes('clicks'));
  const iIdx = headers.findIndex(h => h.includes('impressions'));
  const ctrIdx = headers.findIndex(h => h.includes('ctr'));
  const pIdx = headers.findIndex(h => h.includes('position'));

  if (qIdx === -1) {
    throw new Error('CSV missing Query column header');
  }

  const rows = [];
  for (let i = 1; i < lines.length; i++) {
    const cols = lines[i].split(',').map(c => c.trim().replace(/"/g, ''));
    if (cols.length < headers.length) continue;
    rows.push({
      query: cols[qIdx],
      clicks: parseInt(cols[cIdx]) || 0,
      impressions: parseInt(cols[iIdx]) || 0,
      ctr: parseFloat(cols[ctrIdx]) || 0,
      position: parseFloat(cols[pIdx]) || 99
    });
  }
  return rows;
}

function analyzeQueries(queries) {
  console.log(`\nAnalyzing ${queries.length} queries against active site architecture...\n`);

  const strikingDistance = queries
    .filter(q => q.position >= 5.0 && q.position <= 20.0)
    .sort((a, b) => b.impressions - a.impressions);

  const lowCTR = queries
    .filter(q => q.impressions >= 100 && q.ctr < 0.025)
    .sort((a, b) => b.impressions - a.impressions);

  console.log('=====================================================');
  console.log('🎯 STRIKING DISTANCE OPPORTUNITIES (Positions 5 - 20)');
  console.log('=====================================================');
  strikingDistance.forEach((item, idx) => {
    const mapping = mapQueryToPage(item.query);
    console.log(`${idx + 1}. [Pos ${item.position.toFixed(1)}] "${item.query}"`);
    console.log(`   -> Target: ${mapping.name} (${mapping.url}) | Impressions: ${item.impressions} | Clicks: ${item.clicks}`);
  });

  console.log('\n=====================================================');
  console.log('⚠️ LOW CTR ALERTS (High Impressions, CTR < 2.5%)');
  console.log('=====================================================');
  lowCTR.forEach((item, idx) => {
    const mapping = mapQueryToPage(item.query);
    console.log(`${idx + 1}. "${item.query}" | Impr: ${item.impressions} | CTR: ${(item.ctr * 100).toFixed(2)}% | Pos: ${item.position.toFixed(1)}`);
    console.log(`   -> Action: Polish Title Tag & Meta Description on ${mapping.name} (${mapping.url})`);
  });

  return { strikingDistance, lowCTR };
}

// Main execution
const args = process.argv.slice(2);
let dataset = DEMO_QUERIES;

if (args.length > 0 && args[0] !== '--demo') {
  const filePath = args[0];
  if (fs.existsSync(filePath)) {
    const raw = fs.readFileSync(filePath, 'utf8');
    if (filePath.endsWith('.json')) {
      dataset = JSON.parse(raw);
    } else {
      dataset = parseCSV(raw);
    }
  } else {
    console.error(`File not found: ${filePath}. Running with built-in baseline dataset.`);
  }
} else {
  console.log('Running GSC Miner in baseline demo mode.');
  console.log('To run on fresh GSC export: node scripts/gsc-miner.js <path-to-export.csv>');
}

analyzeQueries(dataset);
