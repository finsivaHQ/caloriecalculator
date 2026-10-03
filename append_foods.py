import json

new_foods = [
  {"name": "Ground Beef (80% Lean)", "slug": "ground-beef-80", "category": "Meat", "calories": 254, "protein": 17, "carbs": 0, "fats": 20, "description": "A rich, flavorful meat often used in burgers and tacos, containing high fats."},
  {"name": "Turkey Breast", "slug": "turkey-breast", "category": "Meat", "calories": 135, "protein": 30, "carbs": 0, "fats": 1, "description": "Extremely lean poultry, perfect for high-protein diets."},
  {"name": "Tuna (Canned in Water)", "slug": "canned-tuna", "category": "Fish", "calories": 86, "protein": 19, "carbs": 0, "fats": 1, "description": "A budget-friendly, high-protein seafood staple."},
  {"name": "Tilapia", "slug": "tilapia", "category": "Fish", "calories": 96, "protein": 20, "carbs": 0, "fats": 1.7, "description": "A mild-flavored, lean white fish."},
  {"name": "Shrimp", "slug": "shrimp", "category": "Seafood", "calories": 99, "protein": 24, "carbs": 0.2, "fats": 0.3, "description": "A low-calorie, high-protein crustacean rich in iodine."},
  {"name": "Whole Milk", "slug": "whole-milk", "category": "Dairy", "calories": 61, "protein": 3.2, "carbs": 4.8, "fats": 3.3, "description": "Nutrient-rich liquid dairy containing a balance of macros."},
  {"name": "Skim Milk", "slug": "skim-milk", "category": "Dairy", "calories": 34, "protein": 3.4, "carbs": 5, "fats": 0.1, "description": "Fat-free milk offering protein and calcium for fewer calories."},
  {"name": "Cheddar Cheese", "slug": "cheddar-cheese", "category": "Dairy", "calories": 403, "protein": 25, "carbs": 1.3, "fats": 33, "description": "A hard, flavorful cheese high in protein, fat, and calcium."},
  {"name": "Mozzarella Cheese", "slug": "mozzarella-cheese", "category": "Dairy", "calories": 300, "protein": 22, "carbs": 2.2, "fats": 22, "description": "A semi-soft cheese popular in Italian dishes and pizzas."},
  {"name": "Orange", "slug": "orange", "category": "Fruit", "calories": 47, "protein": 0.9, "carbs": 12, "fats": 0.1, "description": "A citrus fruit renowned for its high Vitamin C content."},
  {"name": "Strawberries", "slug": "strawberries", "category": "Fruit", "calories": 32, "protein": 0.7, "carbs": 7.7, "fats": 0.3, "description": "Sweet, low-calorie berries packed with antioxidants."},
  {"name": "Grapes", "slug": "grapes", "category": "Fruit", "calories": 69, "protein": 0.7, "carbs": 18, "fats": 0.2, "description": "Bite-sized fruits providing quick, natural sugars for energy."},
  {"name": "Watermelon", "slug": "watermelon", "category": "Fruit", "calories": 30, "protein": 0.6, "carbs": 7.6, "fats": 0.2, "description": "A highly hydrating fruit that is mostly water and very low calorie."},
  {"name": "Pineapple", "slug": "pineapple", "category": "Fruit", "calories": 50, "protein": 0.5, "carbs": 13, "fats": 0.1, "description": "A tropical fruit containing bromelain, a digestive enzyme."},
  {"name": "Carrots", "slug": "carrots", "category": "Vegetables", "calories": 41, "protein": 0.9, "carbs": 10, "fats": 0.2, "description": "A crunchy root vegetable rich in beta-carotene."},
  {"name": "Tomato", "slug": "tomato", "category": "Vegetables", "calories": 18, "protein": 0.9, "carbs": 3.9, "fats": 0.2, "description": "A versatile botanical fruit used as a vegetable, high in lycopene."},
  {"name": "Cucumber", "slug": "cucumber", "category": "Vegetables", "calories": 15, "protein": 0.7, "carbs": 3.6, "fats": 0.1, "description": "An incredibly low-calorie, hydrating vegetable perfect for salads."},
  {"name": "Bell Pepper", "slug": "bell-pepper", "category": "Vegetables", "calories": 20, "protein": 0.9, "carbs": 4.6, "fats": 0.2, "description": "A sweet, crunchy vegetable packed with more Vitamin C than oranges."},
  {"name": "Onion", "slug": "onion", "category": "Vegetables", "calories": 40, "protein": 1.1, "carbs": 9.3, "fats": 0.1, "description": "A foundational aromatic vegetable used worldwide for flavor."},
  {"name": "Garlic", "slug": "garlic", "category": "Vegetables", "calories": 149, "protein": 6.4, "carbs": 33, "fats": 0.5, "description": "A pungent allium known for its powerful flavor and health benefits."},
  {"name": "Cashews", "slug": "cashews", "category": "Nuts", "calories": 553, "protein": 18, "carbs": 30, "fats": 44, "description": "Creamy tree nuts that are slightly higher in carbs than others."},
  {"name": "Peanuts", "slug": "peanuts", "category": "Legumes", "calories": 567, "protein": 26, "carbs": 16, "fats": 49, "description": "Technically legumes, these are a cheap, high-protein snack."},
  {"name": "Chia Seeds", "slug": "chia-seeds", "category": "Seeds", "calories": 486, "protein": 17, "carbs": 42, "fats": 31, "description": "Tiny seeds packed with omega-3s and massive amounts of fiber."},
  {"name": "Flaxseeds", "slug": "flaxseeds", "category": "Seeds", "calories": 534, "protein": 18, "carbs": 29, "fats": 42, "description": "Ground flax provides excellent dietary fiber and healthy fats."},
  {"name": "Pumpkin Seeds", "slug": "pumpkin-seeds", "category": "Seeds", "calories": 559, "protein": 30, "carbs": 11, "fats": 49, "description": "A crunchy seed very high in magnesium and plant protein."},
  {"name": "Chickpeas", "slug": "chickpeas", "category": "Legumes", "calories": 164, "protein": 8.9, "carbs": 27, "fats": 2.6, "description": "A versatile legume used for hummus, salads, and curries."},
  {"name": "Kidney Beans", "slug": "kidney-beans", "category": "Legumes", "calories": 127, "protein": 8.7, "carbs": 23, "fats": 0.5, "description": "Hearty beans that provide robust fiber and complex carbs."},
  {"name": "Green Peas", "slug": "green-peas", "category": "Legumes", "calories": 81, "protein": 5.4, "carbs": 14, "fats": 0.4, "description": "Sweet legumes that offer a surprising amount of protein per serving."},
  {"name": "Pasta (Cooked)", "slug": "cooked-pasta", "category": "Grains", "calories": 131, "protein": 5, "carbs": 25, "fats": 1.1, "description": "A popular wheat-based carbohydrate source for sustained energy."},
  {"name": "Bread (Whole Wheat)", "slug": "whole-wheat-bread", "category": "Grains", "calories": 247, "protein": 13, "carbs": 41, "fats": 3.4, "description": "A fiber-rich bread offering complex carbohydrates."},
  {"name": "Bread (White)", "slug": "white-bread", "category": "Grains", "calories": 266, "protein": 8.9, "carbs": 50, "fats": 3.2, "description": "A soft, quick-digesting carb often fortified with vitamins."},
  {"name": "Butter", "slug": "butter", "category": "Fats", "calories": 717, "protein": 0.9, "carbs": 0.1, "fats": 81, "description": "A dairy fat used for cooking, baking, and spreading."},
  {"name": "Coconut Oil", "slug": "coconut-oil", "category": "Fats", "calories": 862, "protein": 0, "carbs": 0, "fats": 100, "description": "A plant-based oil high in medium-chain triglycerides (MCTs)."},
  {"name": "Bacon (Cooked)", "slug": "bacon", "category": "Meat", "calories": 541, "protein": 37, "carbs": 1.4, "fats": 42, "description": "A highly palatable, salty cured meat rich in fats and protein."},
  {"name": "Sausage (Pork)", "slug": "pork-sausage", "category": "Meat", "calories": 346, "protein": 14, "carbs": 1.5, "fats": 31, "description": "A processed meat providing high calories and dietary fat."},
  {"name": "Dark Chocolate (70%)", "slug": "dark-chocolate-70", "category": "Snacks", "calories": 598, "protein": 7.8, "carbs": 46, "fats": 43, "description": "A rich dessert packed with antioxidants and healthy fats."},
  {"name": "Honey", "slug": "honey", "category": "Sugars", "calories": 304, "protein": 0.3, "carbs": 82, "fats": 0, "description": "A natural sweetener providing instant carbohydrate energy."},
  {"name": "Maple Syrup", "slug": "maple-syrup", "category": "Sugars", "calories": 260, "protein": 0, "carbs": 67, "fats": 0, "description": "A flavorful natural syrup often used on pancakes and waffles."},
  {"name": "Ice Cream (Vanilla)", "slug": "vanilla-ice-cream", "category": "Snacks", "calories": 207, "protein": 3.5, "carbs": 24, "fats": 11, "description": "A sweet frozen dairy dessert high in sugar and fats."},
  {"name": "Popcorn (Air Popped)", "slug": "air-popped-popcorn", "category": "Snacks", "calories": 387, "protein": 13, "carbs": 78, "fats": 4.5, "description": "A high-volume, fiber-rich whole grain snack."}
]

with open('src/data/foods.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the last closing bracket of the array
out_lines = []
for i in range(len(lines)-1, -1, -1):
    if '];' in lines[i]:
        # Insert here
        insert_idx = i
        break

# Format new items
new_strs = []
for item in new_foods:
    s = f'  {{ name: "{item["name"]}", slug: "{item["slug"]}", category: "{item["category"]}", calories: {item["calories"]}, protein: {item["protein"]}, carbs: {item["carbs"]}, fats: {item["fats"]}, description: "{item["description"]}" }},\n'
    new_strs.append(s)

lines.insert(insert_idx, "".join(new_strs))

with open('src/data/foods.ts', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Added 40 foods")
