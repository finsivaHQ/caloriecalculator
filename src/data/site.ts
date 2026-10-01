/** site.ts - global site constants & navigation structure. */

export const SITE = {
  name: "Calorie Calculator Free",
  shortName: "CalorieCalculatorFree",
  domain: "caloriecalculatorfree.com",
  url: "https://caloriecalculatorfree.com",
  tagline: "Free Calorie Calculator for Accurate Daily Calorie Needs",
  description:
    "Free, science-based calorie calculator. Find your BMR, TDEE, and daily calorie needs for weight loss, gain, or maintenance — plus macros and 10+ health calculators.",
  locale: "en_US",
  twitter: "@caloriecalcfree",
  themeColor: "#0a0a0a",
} as const;

export interface NavLink {
  label: string;
  href: string;
  desc?: string;
  lang?: 'en' | 'es';
}

export const ALL_CALCULATORS: NavLink[] = [
  { label: "Calorie Calculator", href: "/", desc: "Daily calories for your goal", lang: 'en' },
  { label: "TDEE Calculator", href: "/tdee-calculator/", desc: "Total daily energy expenditure", lang: 'en' },
  { label: "Protein Calculator", href: "/protein-calculator/", desc: "Daily protein target", lang: 'en' },
  { label: "Calorie Deficit Calculator", href: "/calorie-deficit-calculator/", desc: "Daily deficit target", lang: 'en' },
  { label: "Calories Burned", href: "/calories-burned-calculator/", desc: "Exercise calorie burn", lang: 'en' },
  { label: "Running Calorie Calculator", href: "/running-calorie-calculator/", desc: "Calories burned running", lang: 'en' },
  { label: "Walking Calorie Calculator", href: "/walking-calorie-calculator/", desc: "Calories burned walking", lang: 'en' },
  { label: "Treadmill Calorie Calculator", href: "/treadmill-calorie-calculator/", desc: "Treadmill calorie burn", lang: 'en' },
  { label: "Cycling Calories Calculator", href: "/cycling-calories-calculator/", desc: "Calories burned cycling", lang: 'en' },
  { label: "Swimming Calories Calculator", href: "/swimming-calories-calculator/", desc: "Calories burned swimming", lang: 'en' },
  { label: "Recipe Calorie Calculator", href: "/recipe-calorie-calculator/", desc: "Total & per-serving recipe calories", lang: 'en' },
  { label: "Meal Calorie Calculator", href: "/meal-calorie-calculator/", desc: "Split daily calories across meals", lang: 'en' },

  { label: "Calculadora de Calorías", href: "/country/spain/calculadora-de-calorias/", desc: "Calculadora de calorías diaria", lang: 'es' },
];

/** Header dropdown groups. */
export const NAV: { label: string; href?: string; children?: NavLink[] }[] = [
  { label: "Home", href: "/" },
  { label: "Food Database", href: "/foods/" },
  { label: "Guides", href: "/guides/" },
  { label: "Resources", href: "/resources/" },
];

/** Footer link groups. */
export const FOOTER: { title: string; links: NavLink[] }[] = [
  {
    title: "Company",
    links: [
      { label: "About", href: "/about/" },
      { label: "Editorial Policy", href: "/editorial-policy/" },
      { label: "Contact", href: "/contact/" },
      { label: "Privacy Policy", href: "/privacy-policy/" },
      { label: "Terms", href: "/terms/" },
      { label: "Disclaimer", href: "/disclaimer/" },
      { label: "HTML Sitemap", href: "/html-sitemap/" },
    ],
  },
];
