export interface FoodData {
  name: string;
  slug: string;
  category: string;
  calories: number;
  protein: number;
  carbs: number;
  fats: number;
  description: string;
}

export const foods: FoodData[] = [
  { name: "Chicken Breast", slug: "chicken-breast", category: "Meat", calories: 165, protein: 31, carbs: 0, fats: 3.6, description: "A lean source of protein, excellent for muscle building and weight loss." },
  { name: "Apple", slug: "apple", category: "Fruit", calories: 52, protein: 0.3, carbs: 14, fats: 0.2, description: "A crisp, refreshing fruit high in fiber and vitamin C." },
  { name: "Almonds", slug: "almonds", category: "Nuts", calories: 579, protein: 21, carbs: 22, fats: 50, description: "Nutrient-dense tree nuts packed with healthy fats, protein, and fiber." },
  { name: "White Rice", slug: "white-rice", category: "Grains", calories: 130, protein: 2.7, carbs: 28, fats: 0.3, description: "A staple grain that provides quick-digesting carbohydrates for energy." },
  { name: "Brown Rice", slug: "brown-rice", category: "Grains", calories: 111, protein: 2.6, carbs: 23, fats: 0.9, description: "A whole grain with a chewy texture, rich in fiber and essential minerals." },
  { name: "Broccoli", slug: "broccoli", category: "Vegetables", calories: 34, protein: 2.8, carbs: 6.6, fats: 0.4, description: "A cruciferous vegetable packed with vitamins, fiber, and antioxidants." },
  { name: "Salmon", slug: "salmon", category: "Fish", calories: 208, protein: 20, carbs: 0, fats: 13, description: "A fatty fish renowned for its high omega-3 fatty acids and high-quality protein." },
  { name: "Eggs", slug: "eggs", category: "Dairy/Protein", calories: 155, protein: 13, carbs: 1.1, fats: 11, description: "A nutritional powerhouse containing all nine essential amino acids." },
  { name: "Oats", slug: "oats", category: "Grains", calories: 389, protein: 16.9, carbs: 66, fats: 6.9, description: "A complex carbohydrate rich in beta-glucan fiber, great for heart health." },
  { name: "Banana", slug: "banana", category: "Fruit", calories: 89, protein: 1.1, carbs: 23, fats: 0.3, description: "A potassium-rich fruit providing an excellent source of quick energy." },
  { name: "Sweet Potato", slug: "sweet-potato", category: "Vegetables", calories: 86, protein: 1.6, carbs: 20, fats: 0.1, description: "A root vegetable loaded with complex carbs, fiber, and vitamin A." },
  { name: "Peanut Butter", slug: "peanut-butter", category: "Nuts/Spreads", calories: 588, protein: 25, carbs: 20, fats: 50, description: "A dense source of healthy fats and protein, perfect for bulking or snacking." },
  { name: "Greek Yogurt", slug: "greek-yogurt", category: "Dairy", calories: 59, protein: 10, carbs: 3.6, fats: 0.4, description: "A strained yogurt high in protein and probiotics for gut health." },
  { name: "Avocado", slug: "avocado", category: "Fruit/Fats", calories: 160, protein: 2, carbs: 8.5, fats: 15, description: "A unique fruit predominantly composed of heart-healthy monounsaturated fats." },
  { name: "Spinach", slug: "spinach", category: "Vegetables", calories: 23, protein: 2.9, carbs: 3.6, fats: 0.4, description: "A leafy green loaded with iron, calcium, and essential vitamins." },
  { name: "Quinoa", slug: "quinoa", category: "Grains", calories: 120, protein: 4.4, carbs: 21, fats: 1.9, description: "A complete protein pseudo-cereal, providing sustained energy and fiber." },
  { name: "Lentils", slug: "lentils", category: "Legumes", calories: 116, protein: 9, carbs: 20, fats: 0.4, description: "A plant-based protein powerhouse packed with slow-digesting carbs and fiber." },
  { name: "Walnuts", slug: "walnuts", category: "Nuts", calories: 654, protein: 15, carbs: 14, fats: 65, description: "A brain-boosting nut exceptionally high in ALA omega-3 fatty acids." },
  { name: "Cottage Cheese", slug: "cottage-cheese", category: "Dairy", calories: 98, protein: 11, carbs: 3.4, fats: 4.3, description: "A slow-digesting casein protein source favored by bodybuilders." },
  { name: "Tofu", slug: "tofu", category: "Soy/Protein", calories: 144, protein: 16, carbs: 2.8, fats: 8.7, description: "A versatile plant-based protein derived from soybeans, rich in calcium." },
  { name: "Blueberries", slug: "blueberries", category: "Fruit", calories: 57, protein: 0.7, carbs: 14, fats: 0.3, description: "An antioxidant-rich berry that supports brain and cardiovascular health." },
  { name: "Olive Oil", slug: "olive-oil", category: "Fats", calories: 884, protein: 0, carbs: 0, fats: 100, description: "A pure fat source, foundational to the Mediterranean diet and heart health." },
  { name: "Black Beans", slug: "black-beans", category: "Legumes", calories: 132, protein: 8.9, carbs: 24, fats: 0.5, description: "A highly satiating legume offering a great mix of protein and dietary fiber." },
  { name: "Potato", slug: "potato", category: "Vegetables", calories: 77, protein: 2, carbs: 17, fats: 0.1, description: "One of the most satiating foods on the planet when boiled or baked." },
  { name: "Pork Chops", slug: "pork-chops", category: "Meat", calories: 231, protein: 24, carbs: 0, fats: 14, description: "A dense source of protein and B-vitamins for maintaining lean mass." }
];
