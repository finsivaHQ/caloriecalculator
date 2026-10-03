import json

batch4_foods = [
  {"name": "Beef Sirloin", "slug": "beef-sirloin", "category": "Meat", "calories": 244, "protein": 27, "carbs": 0, "fats": 14, "description": "A popular, relatively lean cut of steak packed with iron and protein."},
  {"name": "Lamb Chops", "slug": "lamb-chops", "category": "Meat", "calories": 294, "protein": 25, "carbs": 0, "fats": 21, "description": "Tender, flavorful meat often consumed in Mediterranean diets."},
  {"name": "Duck Breast", "slug": "duck-breast", "category": "Meat", "calories": 135, "protein": 25, "carbs": 0, "fats": 4, "description": "Rich poultry with a high fat content in the skin but lean meat underneath."},
  {"name": "Hot Dog (Beef)", "slug": "beef-hot-dog", "category": "Meat", "calories": 290, "protein": 11, "carbs": 4, "fats": 26, "description": "A highly processed sausage, popular at barbecues and sporting events."},
  {"name": "Cod", "slug": "cod", "category": "Fish", "calories": 82, "protein": 18, "carbs": 0, "fats": 0.7, "description": "A very lean, mild-tasting white fish commonly used in fish and chips."},
  {"name": "Halibut", "slug": "halibut", "category": "Fish", "calories": 91, "protein": 19, "carbs": 0, "fats": 1.3, "description": "A firm, meaty flatfish that is extremely low in fat and calories."},
  {"name": "Scallops", "slug": "scallops", "category": "Seafood", "calories": 69, "protein": 12, "carbs": 3.2, "fats": 0.5, "description": "Sweet, buttery bivalves that offer a very lean protein source."},
  {"name": "Lobster", "slug": "lobster", "category": "Seafood", "calories": 77, "protein": 16, "carbs": 0, "fats": 0.7, "description": "A premium crustacean offering incredibly lean protein, often paired with butter."},
  {"name": "Crab Meat", "slug": "crab-meat", "category": "Seafood", "calories": 84, "protein": 18, "carbs": 0, "fats": 0.7, "description": "Sweet and delicate seafood rich in zinc, copper, and selenium."},
  {"name": "Oysters", "slug": "oysters", "category": "Seafood", "calories": 68, "protein": 7, "carbs": 3.9, "fats": 2.5, "description": "Nutrient-dense bivalves famous for their exceptionally high zinc content."},
  {"name": "Sweet Corn", "slug": "sweet-corn", "category": "Vegetables", "calories": 86, "protein": 3.2, "carbs": 19, "fats": 1.2, "description": "A starchy vegetable providing sweet flavor, fiber, and complex carbs."},
  {"name": "Green Beans", "slug": "green-beans", "category": "Vegetables", "calories": 31, "protein": 1.8, "carbs": 7, "fats": 0.2, "description": "A fibrous, low-calorie vegetable staple in many global cuisines."},
  {"name": "Beetroot", "slug": "beetroot", "category": "Vegetables", "calories": 43, "protein": 1.6, "carbs": 10, "fats": 0.2, "description": "An earthy root vegetable known to improve blood flow and exercise endurance."},
  {"name": "Butternut Squash", "slug": "butternut-squash", "category": "Vegetables", "calories": 45, "protein": 1, "carbs": 12, "fats": 0.1, "description": "A sweet, starchy winter squash loaded with Vitamin A and fiber."},
  {"name": "Pumpkin", "slug": "pumpkin", "category": "Vegetables", "calories": 26, "protein": 1, "carbs": 6.5, "fats": 0.1, "description": "A highly voluminous, low-calorie gourd used in both savory and sweet dishes."},
  {"name": "Rye Bread", "slug": "rye-bread", "category": "Grains", "calories": 259, "protein": 8.5, "carbs": 48, "fats": 3.3, "description": "A dense, hearty bread with a lower glycemic index than white bread."},
  {"name": "Sourdough Bread", "slug": "sourdough-bread", "category": "Grains", "calories": 289, "protein": 12, "carbs": 56, "fats": 1.8, "description": "A fermented bread that is often easier to digest than standard wheat bread."},
  {"name": "Pita Bread", "slug": "pita-bread", "category": "Grains", "calories": 275, "protein": 9, "carbs": 56, "fats": 1.2, "description": "A flatbread widely used in Middle Eastern and Mediterranean cuisine."},
  {"name": "Bagel (Plain)", "slug": "plain-bagel", "category": "Grains", "calories": 250, "protein": 10, "carbs": 49, "fats": 1.5, "description": "A dense, chewy, ring-shaped bread product, highly calorically dense."},
  {"name": "Croissant", "slug": "croissant", "category": "Grains", "calories": 406, "protein": 8.2, "carbs": 46, "fats": 21, "description": "A flaky, buttery French pastry containing very high amounts of fat."},
  {"name": "Parmesan Cheese", "slug": "parmesan-cheese", "category": "Dairy", "calories": 431, "protein": 38, "carbs": 4.1, "fats": 29, "description": "A hard, aged cheese packing an immense amount of protein and umami flavor."},
  {"name": "Swiss Cheese", "slug": "swiss-cheese", "category": "Dairy", "calories": 380, "protein": 27, "carbs": 5.4, "fats": 28, "description": "A firm cheese with distinctive holes, rich in calcium and protein."},
  {"name": "Cream Cheese", "slug": "cream-cheese", "category": "Dairy", "calories": 342, "protein": 6, "carbs": 4.1, "fats": 34, "description": "A soft, highly palatable spreadable cheese predominantly composed of fat."},
  {"name": "Ricotta Cheese", "slug": "ricotta-cheese", "category": "Dairy", "calories": 174, "protein": 11, "carbs": 3, "fats": 13, "description": "A whey-based cheese often used in Italian dishes like lasagna and cannolis."},
  {"name": "Rice Noodles", "slug": "rice-noodles", "category": "Grains", "calories": 109, "protein": 0.9, "carbs": 24, "fats": 0.2, "description": "A gluten-free noodle alternative staple in many Asian dishes."},
  {"name": "Cola (Regular)", "slug": "cola", "category": "Beverages", "calories": 41, "protein": 0, "carbs": 11, "fats": 0, "description": "A heavily sweetened carbonated soft drink containing zero nutrients."},
  {"name": "Orange Juice", "slug": "orange-juice", "category": "Beverages", "calories": 45, "protein": 0.7, "carbs": 10, "fats": 0.2, "description": "A popular fruit juice packed with Vitamin C but also natural sugars."},
  {"name": "Apple Juice", "slug": "apple-juice", "category": "Beverages", "calories": 46, "protein": 0.1, "carbs": 11, "fats": 0.1, "description": "A sweet, clear juice that is primarily composed of fast-digesting carbohydrates."},
  {"name": "Red Wine", "slug": "red-wine", "category": "Beverages", "calories": 85, "protein": 0.1, "carbs": 2.6, "fats": 0, "description": "An alcoholic beverage rich in antioxidants like resveratrol."},
  {"name": "Beer (Regular)", "slug": "beer", "category": "Beverages", "calories": 43, "protein": 0.5, "carbs": 3.6, "fats": 0, "description": "A fermented alcoholic drink often referred to as 'liquid bread'."},
  {"name": "Ketchup", "slug": "ketchup", "category": "Condiments", "calories": 112, "protein": 1, "carbs": 27, "fats": 0.1, "description": "A popular, sweet tomato-based condiment containing added sugars."},
  {"name": "Mayonnaise", "slug": "mayonnaise", "category": "Condiments", "calories": 680, "protein": 1, "carbs": 0.6, "fats": 75, "description": "An emulsion of oil and egg yolks, making it incredibly calorically dense."},
  {"name": "Mustard (Yellow)", "slug": "mustard", "category": "Condiments", "calories": 60, "protein": 4, "carbs": 5, "fats": 3, "description": "A low-calorie, tangy condiment providing immense flavor for almost zero macros."},
  {"name": "Soy Sauce", "slug": "soy-sauce", "category": "Condiments", "calories": 53, "protein": 8, "carbs": 4.9, "fats": 0.6, "description": "A high-sodium, umami-rich liquid condiment staple in Asian cuisines."},
  {"name": "Hummus", "slug": "hummus", "category": "Snacks/Spreads", "calories": 166, "protein": 7.9, "carbs": 14, "fats": 9.6, "description": "A creamy Middle Eastern dip made from blended chickpeas, tahini, and oil."},
  {"name": "Guacamole", "slug": "guacamole", "category": "Snacks/Spreads", "calories": 157, "protein": 2, "carbs": 8.5, "fats": 14.7, "description": "A smashed avocado dip rich in monounsaturated fats and flavor."},
  {"name": "Salsa", "slug": "salsa", "category": "Condiments", "calories": 36, "protein": 1.5, "carbs": 7, "fats": 0.2, "description": "A very low-calorie tomato and pepper dip, perfect for weight loss diets."},
  {"name": "Potato Chips", "slug": "potato-chips", "category": "Snacks", "calories": 536, "protein": 7, "carbs": 53, "fats": 35, "description": "Deep-fried, heavily salted slices of potato that are highly hyperpalatable."},
  {"name": "Pretzels", "slug": "pretzels", "category": "Snacks", "calories": 380, "protein": 10, "carbs": 80, "fats": 3, "description": "A baked bread snack coated in salt, offering mostly pure carbohydrates."},
  {"name": "Gummy Bears", "slug": "gummy-bears", "category": "Snacks", "calories": 315, "protein": 5, "carbs": 74, "fats": 0.2, "description": "A gelatin-based candy providing high sugar and zero satiety."}
]

with open('src/data/foods.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the last closing bracket of the array
insert_idx = -1
for i in range(len(lines)-1, -1, -1):
    if '];' in lines[i]:
        insert_idx = i
        break

if insert_idx == -1:
    print("Could not find end of array")
    exit(1)
    
# Add comma to the last item if it doesn't have one
for i in range(insert_idx - 1, -1, -1):
    line = lines[i].strip()
    if line.startswith('{'):
        if not line.endswith(','):
            lines[i] = lines[i].rstrip() + ',\n'
        break

# Format new items
new_strs = []
for idx, item in enumerate(batch4_foods):
    comma = ',' if idx < len(batch4_foods) - 1 else ''
    s = f'  {{ name: "{item["name"]}", slug: "{item["slug"]}", category: "{item["category"]}", calories: {item["calories"]}, protein: {item["protein"]}, carbs: {item["carbs"]}, fats: {item["fats"]}, description: "{item["description"]}" }}{comma}\n'
    new_strs.append(s)

lines.insert(insert_idx, "".join(new_strs))

with open('src/data/foods.ts', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Added Batch 4 foods")
