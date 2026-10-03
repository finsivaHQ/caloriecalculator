import json

batch5_foods = [
  {"name": "Cheese Pizza", "slug": "cheese-pizza", "category": "Fast Food", "calories": 266, "protein": 11, "carbs": 33, "fats": 10, "description": "A popular fast food staple consisting of dough, tomato sauce, and melted cheese."},
  {"name": "Hamburger", "slug": "hamburger", "category": "Fast Food", "calories": 254, "protein": 13, "carbs": 24, "fats": 11, "description": "A classic sandwich consisting of a cooked ground beef patty in a sliced bun."},
  {"name": "Cheeseburger", "slug": "cheeseburger", "category": "Fast Food", "calories": 303, "protein": 15, "carbs": 24, "fats": 16, "description": "A hamburger with a slice of melted cheese, increasing its fat and caloric content."},
  {"name": "French Fries", "slug": "french-fries", "category": "Fast Food", "calories": 312, "protein": 3.4, "carbs": 41, "fats": 15, "description": "Deep-fried potato strips that are highly calorically dense and hyperpalatable."},
  {"name": "Onion Rings", "slug": "onion-rings", "category": "Fast Food", "calories": 411, "protein": 4.1, "carbs": 44, "fats": 24, "description": "Deep-fried, battered onion slices loaded with trans or saturated fats."},
  {"name": "Chicken Nuggets", "slug": "chicken-nuggets", "category": "Fast Food", "calories": 296, "protein": 14, "carbs": 15, "fats": 20, "description": "Battered and deep-fried chicken pieces popular in fast food chains."},
  {"name": "Fried Chicken", "slug": "fried-chicken", "category": "Fast Food", "calories": 320, "protein": 16, "carbs": 11, "fats": 23, "description": "Chicken pieces coated in seasoned batter and deep-fried to a crisp."},
  {"name": "Taco", "slug": "taco", "category": "Fast Food", "calories": 226, "protein": 11, "carbs": 20, "fats": 12, "description": "A traditional Mexican dish consisting of a folded tortilla filled with meat and toppings."},
  {"name": "Firm Tofu", "slug": "firm-tofu", "category": "Soy/Protein", "calories": 144, "protein": 17, "carbs": 2.8, "fats": 8.7, "description": "A denser soy-based protein excellent for stir-fries and vegan diets."},
  {"name": "Seitan", "slug": "seitan", "category": "Vegan Protein", "calories": 370, "protein": 75, "carbs": 14, "fats": 1.9, "description": "A highly concentrated wheat gluten protein used as a vegan meat substitute."},
  {"name": "Tempeh", "slug": "tempeh", "category": "Soy/Protein", "calories": 192, "protein": 20, "carbs": 7.6, "fats": 11, "description": "Fermented soybeans pressed into a cake, offering probiotics and robust protein."},
  {"name": "Edamame", "slug": "edamame", "category": "Soy/Protein", "calories": 121, "protein": 12, "carbs": 8.9, "fats": 5.2, "description": "Immature soybeans still in the pod, often served steamed with salt."},
  {"name": "Canned Kidney Beans", "slug": "canned-kidney-beans", "category": "Legumes", "calories": 85, "protein": 5.5, "carbs": 15, "fats": 0.2, "description": "Pre-cooked beans offering a quick source of fiber and plant-based protein."},
  {"name": "Canned Black Beans", "slug": "canned-black-beans", "category": "Legumes", "calories": 91, "protein": 6, "carbs": 16, "fats": 0.4, "description": "Ready-to-eat legumes packed with antioxidants and soluble fiber."},
  {"name": "Navy Beans", "slug": "navy-beans", "category": "Legumes", "calories": 140, "protein": 8.2, "carbs": 26, "fats": 0.6, "description": "Small white beans famously used in baked bean recipes."},
  {"name": "Pinto Beans", "slug": "pinto-beans", "category": "Legumes", "calories": 143, "protein": 9, "carbs": 26, "fats": 0.7, "description": "The most popular bean in the US, widely used in Mexican cuisine."},
  {"name": "Black Olives", "slug": "black-olives", "category": "Fats/Condiments", "calories": 116, "protein": 0.8, "carbs": 6, "fats": 11, "description": "Ripe olives cured in brine, providing healthy monounsaturated fats."},
  {"name": "Green Olives", "slug": "green-olives", "category": "Fats/Condiments", "calories": 145, "protein": 1, "carbs": 3.8, "fats": 15, "description": "Unripe, tangy olives offering robust flavor and healthy oils."},
  {"name": "Dill Pickle", "slug": "dill-pickle", "category": "Vegetables", "calories": 11, "protein": 0.3, "carbs": 2.3, "fats": 0.2, "description": "Cucumbers fermented in brine, nearly zero calories but extremely high in sodium."},
  {"name": "Jalapeno", "slug": "jalapeno", "category": "Vegetables", "calories": 29, "protein": 0.9, "carbs": 6.5, "fats": 0.4, "description": "A medium-spicy chili pepper rich in metabolism-boosting capsaicin."},
  {"name": "Artichoke", "slug": "artichoke", "category": "Vegetables", "calories": 47, "protein": 3.3, "carbs": 11, "fats": 0.2, "description": "A fibrous thistle offering massive amounts of prebiotics and antioxidants."},
  {"name": "Okra", "slug": "okra", "category": "Vegetables", "calories": 33, "protein": 1.9, "carbs": 7.5, "fats": 0.2, "description": "A green seed pod vegetable famous for its mucilaginous (slimy) texture when cooked."},
  {"name": "Leek", "slug": "leek", "category": "Vegetables", "calories": 61, "protein": 1.5, "carbs": 14, "fats": 0.3, "description": "A milder, sweeter member of the onion family used primarily in soups."},
  {"name": "Cooked Spinach", "slug": "cooked-spinach", "category": "Vegetables", "calories": 23, "protein": 3, "carbs": 3.8, "fats": 0.3, "description": "A dark leafy green whose nutrients become highly bioavailable when heated."},
  {"name": "Papaya", "slug": "papaya", "category": "Fruit", "calories": 43, "protein": 0.5, "carbs": 11, "fats": 0.3, "description": "A tropical fruit containing the digestive enzyme papain."},
  {"name": "Fig", "slug": "fig", "category": "Fruit", "calories": 74, "protein": 0.8, "carbs": 19, "fats": 0.3, "description": "A unique, sweet fruit known for its soft, chewy texture and seeds."},
  {"name": "Medjool Date", "slug": "medjool-date", "category": "Fruit", "calories": 277, "protein": 1.8, "carbs": 75, "fats": 0.2, "description": "A massive, sweet stone fruit often used as a natural sugar substitute."},
  {"name": "Prune", "slug": "prune", "category": "Fruit", "calories": 240, "protein": 2.2, "carbs": 64, "fats": 0.4, "description": "Dried plums renowned for their high sorbitol and fiber content."},
  {"name": "Raisins", "slug": "raisins", "category": "Fruit", "calories": 299, "protein": 3.1, "carbs": 79, "fats": 0.5, "description": "Dried grapes offering a very dense source of quick-digesting carbohydrates."},
  {"name": "Grapefruit", "slug": "grapefruit", "category": "Fruit", "calories": 42, "protein": 0.8, "carbs": 11, "fats": 0.1, "description": "A tart citrus fruit historically associated with weight loss diets."},
  {"name": "Cantaloupe", "slug": "cantaloupe", "category": "Fruit", "calories": 34, "protein": 0.8, "carbs": 8.2, "fats": 0.2, "description": "A sweet orange melon that is highly hydrating and low calorie."},
  {"name": "Honeydew", "slug": "honeydew", "category": "Fruit", "calories": 36, "protein": 0.5, "carbs": 9.1, "fats": 0.1, "description": "A light green, subtly sweet melon packed with water and Vitamin C."},
  {"name": "Gluten-Free Pasta", "slug": "gluten-free-pasta", "category": "Grains", "calories": 357, "protein": 7.5, "carbs": 76, "fats": 2, "description": "Pasta made from alternative flours like rice or corn for those with Celiac disease."},
  {"name": "Wild Rice", "slug": "wild-rice", "category": "Grains", "calories": 101, "protein": 4, "carbs": 21, "fats": 0.3, "description": "A nutrient-dense aquatic grass seed with fewer carbs than white rice."},
  {"name": "Oat Milk", "slug": "oat-milk", "category": "Dairy/Alternatives", "calories": 48, "protein": 1, "carbs": 7, "fats": 1.5, "description": "A creamy, slightly sweet plant milk naturally higher in carbohydrates."},
  {"name": "Canned Coconut Milk", "slug": "canned-coconut-milk", "category": "Dairy/Alternatives", "calories": 197, "protein": 2, "carbs": 2.8, "fats": 21, "description": "A highly calorically dense, fat-rich milk used extensively in curries."},
  {"name": "Macaroni and Cheese", "slug": "macaroni-and-cheese", "category": "Meals", "calories": 164, "protein": 5.4, "carbs": 21, "fats": 6.3, "description": "A beloved comfort food offering a high amount of simple carbs and fats."},
  {"name": "Pancake", "slug": "pancake", "category": "Breakfast", "calories": 227, "protein": 6.4, "carbs": 28, "fats": 9.7, "description": "A flat cake made from starch-based batter, typically covered in syrup."},
  {"name": "Waffle", "slug": "waffle", "category": "Breakfast", "calories": 291, "protein": 7, "carbs": 33, "fats": 14, "description": "A leavened batter cooked between hot plates, higher in fat than pancakes."},
  {"name": "Hash Browns", "slug": "hash-browns", "category": "Breakfast", "calories": 326, "protein": 3.8, "carbs": 30, "fats": 22, "description": "Pan-fried shredded potatoes, extremely high in oil and calories."}
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
for idx, item in enumerate(batch5_foods):
    comma = ',' if idx < len(batch5_foods) - 1 else ''
    s = f'  {{ name: "{item["name"]}", slug: "{item["slug"]}", category: "{item["category"]}", calories: {item["calories"]}, protein: {item["protein"]}, carbs: {item["carbs"]}, fats: {item["fats"]}, description: "{item["description"]}" }}{comma}\n'
    new_strs.append(s)

lines.insert(insert_idx, "".join(new_strs))

with open('src/data/foods.ts', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Added Batch 5 foods")
