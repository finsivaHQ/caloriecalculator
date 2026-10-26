/**
 * calculations.ts
 * -------------------------------------------------------------------------
 * Pure, framework-agnostic health & fitness math used by every calculator.
 * All functions are unit-explicit: heights in cm, weights in kg, unless a
 * function name says otherwise. Use the converters in `units.ts` at the UI
 * boundary so the math here stays in metric.
 *
 * Formula references:
 *  - BMR: Mifflin-St Jeor (1990) — highly reliable for the general population.
 *  - TDEE: BMR x activity multiplier.
 *  - Body fat: U.S. Navy circumference method.
 *  - Lean mass: Boer (1984).
 *  - Ideal weight: Robinson, Miller, Devine, Hamwi.
 * -------------------------------------------------------------------------
 */

export type Sex = "male" | "female";
export type Sexo = Sex;

/** Activity levels with their TDEE multipliers and human labels. */
export const ACTIVITY_LEVELS = {
  sedentary: { multiplier: 1.2, label: "Sedentary", hint: "Little or no exercise" },
  light: { multiplier: 1.375, label: "Lightly active", hint: "Exercise 1–3 days/week" },
  moderate: { multiplier: 1.55, label: "Moderately active", hint: "Exercise 3–5 days/week" },
  active: { multiplier: 1.725, label: "Very active", hint: "Exercise 6–7 days/week" },
  athlete: { multiplier: 1.9, label: "Extra active", hint: "Hard exercise + physical job" },
} as const;

export type ActivityKey = keyof typeof ACTIVITY_LEVELS;

/**
 * Goal definitions. `delta` is the daily calorie adjustment applied to TDEE.
 * 1 lb of fat ≈ 3500 kcal, so 500 kcal/day ≈ 1 lb/week.
 */
export const GOALS = {
  maintain: { label: "Maintain weight", delta: 0, rate: "0 lb/week" },
  mildLoss: { label: "Mild weight loss", delta: -250, rate: "0.5 lb/week" },
  loss: { label: "Weight loss", delta: -500, rate: "1 lb/week" },
  extremeLoss: { label: "Extreme weight loss", delta: -1000, rate: "2 lb/week" },
  mildGain: { label: "Mild weight gain", delta: 250, rate: "0.5 lb/week" },
  gain: { label: "Weight gain", delta: 500, rate: "1 lb/week" },
  extremeGain: { label: "Extreme weight gain", delta: 1000, rate: "2 lb/week" },
} as const;

export type GoalKey = keyof typeof GOALS;
export type ObjetivoKey = GoalKey;

/**
 * Basal Metabolic Rate — Mifflin-St Jeor equation.
 * @param sex     biological sex
 * @param age     years
 * @param heightCm height in centimetres
 * @param weightKg weight in kilograms
 * @returns BMR in kcal/day
 */
export function bmrMifflinStJeor(
  sex: Sex,
  age: number,
  heightCm: number,
  weightKg: number
): number {
  const base = 10 * weightKg + 6.25 * heightCm - 5 * age;
  return sex === "male" ? base + 5 : base - 161;
}

/** Total Daily Energy Expenditure = BMR x activity multiplier. */
export function tdee(bmr: number, activity: ActivityKey): number {
  return bmr * ACTIVITY_LEVELS[activity].multiplier;
}

/** Apply a goal's calorie delta to a TDEE, with a sensible safety floor. */
export function goalCalories(tdeeValue: number, goal: GoalKey, sex: Sex): number {
  const target = tdeeValue + GOALS[goal].delta;
  // Health floor: never recommend below 1500 (men) / 1200 (women) kcal.
  const floor = sex === "male" ? 1500 : 1200;
  return Math.max(target, floor);
}

export interface Macros {
  proteinG: number;
  carbsG: number;
  fatG: number;
  proteinKcal: number;
  carbsKcal: number;
  fatKcal: number;
}

/**
 * Macro split from a calorie target.
 * Defaults to a balanced 30P / 40C / 30F split (by calories).
 * Protein = 4 kcal/g, Carbs = 4 kcal/g, Fat = 9 kcal/g.
 */
export function macrosFromCalories(
  calories: number,
  split: { protein: number; carbs: number; fat: number } = { protein: 0.3, carbs: 0.4, fat: 0.3 }
): Macros {
  const proteinKcal = calories * split.protein;
  const carbsKcal = calories * split.carbs;
  const fatKcal = calories * split.fat;
  return {
    proteinKcal,
    carbsKcal,
    fatKcal,
    proteinG: Math.round(proteinKcal / 4),
    carbsG: Math.round(carbsKcal / 4),
    fatG: Math.round(fatKcal / 9),
  };
}

/** Body Mass Index = kg / m^2. */
export function bmi(weightKg: number, heightCm: number): number {
  const m = heightCm / 100;
  return weightKg / (m * m);
}

export type BmiCategory = "Underweight" | "Normal" | "Overweight" | "Obese";

export function bmiCategory(value: number): BmiCategory {
  if (value < 18.5) return "Underweight";
  if (value < 25) return "Normal";
  if (value < 30) return "Overweight";
  return "Obese";
}

/**
 * Body fat % — U.S. Navy circumference method. Measurements in cm.
 * Women require a hip measurement; men do not.
 */
export function bodyFatNavy(
  sex: Sex,
  heightCm: number,
  neckCm: number,
  waistCm: number,
  hipCm?: number
): number {
  if (sex === "male") {
    return (
      495 /
        (1.0324 - 0.19077 * Math.log10(waistCm - neckCm) + 0.15456 * Math.log10(heightCm)) -
      450
    );
  }
  const hip = hipCm ?? 0;
  return (
    495 /
      (1.29579 - 0.35004 * Math.log10(waistCm + hip - neckCm) + 0.221 * Math.log10(heightCm)) -
    450
  );
}

/** Lean Body Mass — Boer formula. Returns kg. */
export function leanBodyMassBoer(sex: Sex, heightCm: number, weightKg: number): number {
  return sex === "male"
    ? 0.407 * weightKg + 0.267 * heightCm - 19.2
    : 0.252 * weightKg + 0.473 * heightCm - 48.3;
}

/**
 * Ideal body weight (kg) across four classic formulas.
 * Each uses inches over 5 ft (60 in).
 */
export function idealWeights(sex: Sex, heightCm: number) {
  const inchesOver5ft = Math.max(0, heightCm / 2.54 - 60);
  const male = sex === "male";
  return {
    robinson: (male ? 52 : 49) + (male ? 1.9 : 1.7) * inchesOver5ft,
    miller: (male ? 56.2 : 53.1) + (male ? 1.41 : 1.36) * inchesOver5ft,
    devine: (male ? 50 : 45.5) + 2.3 * inchesOver5ft,
    hamwi: (male ? 48 : 45.5) + (male ? 2.7 : 2.2) * inchesOver5ft,
  };
}

/**
 * Daily water intake estimate (litres).
 * Baseline ≈ 35 ml/kg, plus ~12 ml/kg per hour of exercise.
 */
export function waterIntakeLitres(weightKg: number, exerciseMinutes = 0): number {
  const baseline = weightKg * 0.035;
  const exercise = (exerciseMinutes / 60) * weightKg * 0.012;
  return baseline + exercise;
}

/** Daily protein target range (g) from body weight & activity. */
export function proteinTargetG(weightKg: number, activity: ActivityKey) {
  const perKg = activity === "sedentary" ? [0.8, 1.0] : activity === "athlete" ? [1.6, 2.2] : [1.2, 1.6];
  return { min: Math.round(weightKg * perKg[0]), max: Math.round(weightKg * perKg[1]) };
}

/**
 * Estimate weeks to reach a target weight given a daily calorie deficit/surplus.
 * Returns null when the direction makes the goal unreachable.
 */
export function weeksToGoal(
  currentKg: number,
  targetKg: number,
  dailyDelta: number
): number | null {
  const diffKg = targetKg - currentKg;
  if (dailyDelta === 0 || Math.sign(diffKg) !== Math.sign(dailyDelta)) {
    if (diffKg === 0) return 0;
    return null;
  }
  // 7700 kcal ≈ 1 kg of body mass.
  const kcalNeeded = Math.abs(diffKg) * 7700;
  const days = kcalNeeded / Math.abs(dailyDelta);
  return days / 7;
}

export function round(n: number, dp = 0): number {
  const f = 10 ** dp;
  return Math.round(n * f) / f;
}

/**
 * Calories burned during exercise using the MET (Metabolic Equivalent) method.
 *   kcal = MET × 3.5 × weightKg / 200 × minutes
 * MET values come from the Compendium of Physical Activities.
 * @param met       activity intensity in METs
 * @param weightKg  body weight in kilograms
 * @param minutes   duration in minutes
 */
export function caloriesBurned(met: number, weightKg: number, minutes: number): number {
  return (met * 3.5 * weightKg) / 200 * minutes;
}

export function healthyWeightRange(heightCm: number, minBmi = 18.5, maxBmi = 24.9) {
  const m = heightCm / 100;
  return { minKg: minBmi * m * m, maxKg: maxBmi * m * m };
}

export function mealCalories(totalCalories: number, meals: number) {
  if (meals <= 0) return 0;
  return Math.round(totalCalories / meals);
}

export interface Ingredient {
  name: string;
  calories: number;
}

export interface RecipeResult {
  total: number;
  perServing: number;
}

export function recipeCalories(ingredients: Ingredient[], servings: number): RecipeResult {
  const total = ingredients.reduce((s, i) => s + i.calories, 0);
  return { total, perServing: servings > 0 ? Math.round(total / servings) : total };
}

export interface FastingPlan {
  name: string;
  fastHours: number;
  eatHours: number;
  description: string;
}

export const FASTING_PLANS: FastingPlan[] = [
  { name: "12:12", fastHours: 12, eatHours: 12, description: "12-hour fast, 12-hour eating window" },
  { name: "14:10", fastHours: 14, eatHours: 10, description: "14-hour fast, 10-hour eating window" },
  { name: "16:8", fastHours: 16, eatHours: 8, description: "16-hour fast, 8-hour eating window (Leangains)" },
  { name: "18:6", fastHours: 18, eatHours: 6, description: "18-hour fast, 6-hour eating window" },
  { name: "20:4", fastHours: 20, eatHours: 4, description: "20-hour fast, 4-hour eating window (Warrior Diet)" },
  { name: "OMAD", fastHours: 23, eatHours: 1, description: "One Meal A Day, 23-hour fast" },
];

/**
 * One Rep Max (1RM) — Epley formula.
 * 1RM = weight × (1 + reps / 30)
 * @param weightKg  lifted weight in kg
 * @param reps      reps completed at that weight
 */
export function oneRepMaxEpley(weightKg: number, reps: number): number {
  if (reps <= 0 || weightKg <= 0) return 0;
  if (reps === 1) return weightKg;
  return weightKg * (1 + reps / 30);
}

/**
 * Target Heart Rate — Karvonen method.
 * @param restingBpm  resting heart rate
 * @param maxBpm      maximum heart rate
 * @param intensity   fraction 0–1
 */
export function targetHeartRateKarvonen(restingBpm: number, maxBpm: number, intensity: number): number {
  if (intensity <= 0) return restingBpm;
  return Math.round(restingBpm + (maxBpm - restingBpm) * Math.min(intensity, 1));
}

/**
 * Maximum heart rate estimation — simple age-based formula.
 */
export function maxHeartRate(age: number): number {
  return 220 - age;
}

/**
 * U.S. Army body fat percentage — circumference method.
 * Male: requires age, height, neck, waist.
 * Female: requires age, height, neck, waist, hip.
 * All measurements in cm.
 */
export function armyBodyFat(
  sex: Sex,
  age: number,
  heightCm: number,
  waistCm: number,
  neckCm: number,
  hipCm?: number
): number {
  if (sex === "male") {
    // % body fat = (86.010 × log10(waist - neck) - 70.041 × log10(height) + 36.76
    const logWaistNeck = Math.log10(waistCm - neckCm);
    const logHeight = Math.log10(heightCm);
    return Math.max(0, 86.01 * logWaistNeck - 70.041 * logHeight + 36.76);
  }
  const hip = hipCm ?? 0;
  // % body fat = (163.205 × log10(waist + hip - neck) - 97.684 × log10(height) - 78.387
  const logWaistHipNeck = Math.log10(waistCm + hip - neckCm);
  const logHeight = Math.log10(heightCm);
  return Math.max(0, 163.205 * logWaistHipNeck - 97.684 * logHeight - 78.387);
}

/**
 * Alcohol calories from volume, ABV, and drink type.
 * Alcohol provides 7 kcal/g. Ethanol density ≈ 0.789 g/mL.
 * @param volumeMl      liquid volume in millilitres
 * @param abvPercent    alcohol by volume as a percentage (e.g. 5 for 5%)
 * @returns calories from alcohol
 */
export function alcoholCalories(volumeMl: number, abvPercent: number): number {
  const ethanolMl = volumeMl * (abvPercent / 100);
  const ethanolG = ethanolMl * 0.789;
  return Math.round(ethanolG * 7);
}
