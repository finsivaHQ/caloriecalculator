import json

batch3_foods = [
  {"name": "Jasmine Rice", "slug": "jasmine-rice", "category": "Grains", "calories": 130, "protein": 2.7, "carbs": 29, "fats": 0.2, "description": "A fragrant long-grain rice commonly used in Southeast Asian cuisine."},
  {"name": "Whole Wheat Pasta", "slug": "whole-wheat-pasta", "category": "Grains", "calories": 124, "protein": 5.3, "carbs": 26, "fats": 0.5, "description": "A high-fiber pasta alternative offering complex carbohydrates and sustained energy."},
  {"name": "Chicken Thigh", "slug": "chicken-thigh", "category": "Meat", "calories": 209, "protein": 26, "carbs": 0, "fats": 10.9, "description": "A juicy, flavorful dark meat chicken cut, higher in fat than the breast."},
  {"name": "Turkey Bacon", "slug": "turkey-bacon", "category": "Meat", "calories": 368, "protein": 30, "carbs": 3.1, "fats": 26, "description": "A lower-fat alternative to traditional pork bacon with a smoky flavor."},
  {"name": "Smoked Salmon", "slug": "smoked-salmon", "category": "Fish", "calories": 117, "protein": 18, "carbs": 0, "fats": 4.3, "description": "Cured and smoked salmon, packed with sodium, protein, and omega-3s."},
  {"name": "Ham", "slug": "ham", "category": "Meat", "calories": 145, "protein": 21, "carbs": 1.5, "fats": 5.5, "description": "A lean, processed pork product typically used in sandwiches."},
  {"name": "Salami", "slug": "salami", "category": "Meat", "calories": 336, "protein": 22, "carbs": 1.2, "fats": 26, "description": "A highly processed, cured sausage rich in fats and savory flavor."},
  {"name": "Beef Jerky", "slug": "beef-jerky", "category": "Snacks/Meat", "calories": 410, "protein": 33, "carbs": 11, "fats": 26, "description": "A dehydrated, high-protein meat snack perfect for on-the-go energy."},
  {"name": "Pork Tenderloin", "slug": "pork-tenderloin", "category": "Meat", "calories": 143, "protein": 26, "carbs": 0, "fats": 3.5, "description": "One of the leanest cuts of pork, comparable in macros to chicken breast."},
  {"name": "Cauliflower", "slug": "cauliflower", "category": "Vegetables", "calories": 25, "protein": 1.9, "carbs": 4.9, "fats": 0.3, "description": "A versatile cruciferous vegetable often used as a low-carb substitute for rice."},
  {"name": "Brussels Sprouts", "slug": "brussels-sprouts", "category": "Vegetables", "calories": 43, "protein": 3.4, "carbs": 8.9, "fats": 0.3, "description": "Miniature cabbage-like vegetables rich in Vitamin K and antioxidants."},
  {"name": "Zucchini", "slug": "zucchini", "category": "Vegetables", "calories": 17, "protein": 1.2, "carbs": 3.1, "fats": 0.3, "description": "A very low-calorie summer squash widely used as a noodle alternative (zoodles)."},
  {"name": "Asparagus", "slug": "asparagus", "category": "Vegetables", "calories": 20, "protein": 2.2, "carbs": 3.9, "fats": 0.1, "description": "A natural diuretic vegetable packed with folate and vitamins."},
  {"name": "Cabbage", "slug": "cabbage", "category": "Vegetables", "calories": 25, "protein": 1.3, "carbs": 5.8, "fats": 0.1, "description": "A leafy green or purple biennial plant, highly satiating and low in calories."},
  {"name": "Celery", "slug": "celery", "category": "Vegetables", "calories": 14, "protein": 0.7, "carbs": 3, "fats": 0.2, "description": "A crunchy, fibrous vegetable that is almost entirely composed of water."},
  {"name": "Mushrooms", "slug": "mushrooms", "category": "Vegetables", "calories": 22, "protein": 3.1, "carbs": 3.3, "fats": 0.3, "description": "An earthy fungi offering unique antioxidants and a meaty texture."},
  {"name": "Eggplant", "slug": "eggplant", "category": "Vegetables", "calories": 25, "protein": 1, "carbs": 6, "fats": 0.2, "description": "A spongy, absorbent nightshade vegetable heavily used in Mediterranean cooking."},
  {"name": "Red Onion", "slug": "red-onion", "category": "Vegetables", "calories": 40, "protein": 1.1, "carbs": 9.3, "fats": 0.1, "description": "A sharp, aromatic vegetable providing color and flavor to salads and dishes."},
  {"name": "Radish", "slug": "radish", "category": "Vegetables", "calories": 16, "protein": 0.7, "carbs": 3.4, "fats": 0.1, "description": "A peppery, crunchy root vegetable exceptionally low in calories."},
  {"name": "Mango", "slug": "mango", "category": "Fruit", "calories": 60, "protein": 0.8, "carbs": 15, "fats": 0.4, "description": "A sweet, tropical stone fruit containing high amounts of Vitamin C and A."},
  {"name": "Kiwi", "slug": "kiwi", "category": "Fruit", "calories": 61, "protein": 1.1, "carbs": 15, "fats": 0.5, "description": "A fuzzy fruit with bright green flesh, containing more Vitamin C than oranges."},
  {"name": "Peach", "slug": "peach", "category": "Fruit", "calories": 39, "protein": 0.9, "carbs": 9.5, "fats": 0.3, "description": "A juicy summer fruit with fuzzy skin and a sweet, delicate flavor."},
  {"name": "Plum", "slug": "plum", "category": "Fruit", "calories": 46, "protein": 0.7, "carbs": 11, "fats": 0.3, "description": "A sweet and tart stone fruit that helps promote digestive health."},
  {"name": "Pomegranate", "slug": "pomegranate", "category": "Fruit", "calories": 83, "protein": 1.7, "carbs": 19, "fats": 1.2, "description": "A jewel-like fruit whose arils are packed with powerful antioxidants."},
  {"name": "Raspberries", "slug": "raspberries", "category": "Fruit", "calories": 52, "protein": 1.2, "carbs": 12, "fats": 0.7, "description": "Incredibly high-fiber berries offering major satiety for very few calories."},
  {"name": "Blackberries", "slug": "blackberries", "category": "Fruit", "calories": 43, "protein": 1.4, "carbs": 10, "fats": 0.5, "description": "Dark, tart berries loaded with Vitamin C, fiber, and manganese."},
  {"name": "Cranberries", "slug": "cranberries", "category": "Fruit", "calories": 46, "protein": 0.4, "carbs": 12, "fats": 0.1, "description": "Tart, red berries famous for supporting urinary tract health."},
  {"name": "Cherries", "slug": "cherries", "category": "Fruit", "calories": 63, "protein": 1.1, "carbs": 16, "fats": 0.2, "description": "Sweet, dark red fruits containing melatonin, which can aid in sleep."},
  {"name": "Pear", "slug": "pear", "category": "Fruit", "calories": 57, "protein": 0.4, "carbs": 15, "fats": 0.1, "description": "A sweet, fibrous fruit that helps promote a healthy gut."},
  {"name": "Pistachios", "slug": "pistachios", "category": "Nuts", "calories": 562, "protein": 20, "carbs": 28, "fats": 45, "description": "Lower-calorie nuts compared to others, rich in lutein and zeaxanthin."},
  {"name": "Pecans", "slug": "pecans", "category": "Nuts", "calories": 691, "protein": 9.2, "carbs": 14, "fats": 72, "description": "A highly calorically dense, fat-rich nut commonly used in baking."},
  {"name": "Macadamia Nuts", "slug": "macadamia-nuts", "category": "Nuts", "calories": 718, "protein": 7.9, "carbs": 14, "fats": 76, "description": "The highest-fat nut available, packed with heart-healthy monounsaturated fats."},
  {"name": "Brazil Nuts", "slug": "brazil-nuts", "category": "Nuts", "calories": 659, "protein": 14, "carbs": 12, "fats": 67, "description": "Large nuts that are the richest known dietary source of selenium."},
  {"name": "Sunflower Seeds", "slug": "sunflower-seeds", "category": "Seeds", "calories": 584, "protein": 21, "carbs": 20, "fats": 51, "description": "A crunchy, salty snack packed with Vitamin E and healthy fats."},
  {"name": "Sesame Seeds", "slug": "sesame-seeds", "category": "Seeds", "calories": 573, "protein": 18, "carbs": 23, "fats": 50, "description": "Tiny seeds often used as garnishes, high in calcium and healthy oils."},
  {"name": "Nutella", "slug": "nutella", "category": "Snacks", "calories": 539, "protein": 6, "carbs": 57, "fats": 31, "description": "A highly palatable hazelnut cocoa spread, extremely dense in sugar and fats."},
  {"name": "Almond Butter", "slug": "almond-butter", "category": "Nuts/Spreads", "calories": 614, "protein": 21, "carbs": 19, "fats": 56, "description": "A slightly healthier, higher-fiber alternative to traditional peanut butter."},
  {"name": "Soy Milk", "slug": "soy-milk", "category": "Dairy/Alternatives", "calories": 33, "protein": 2.9, "carbs": 1.8, "fats": 1.6, "description": "A plant-based milk alternative providing macros very similar to cow's milk."},
  {"name": "Almond Milk (Unsweetened)", "slug": "almond-milk-unsweetened", "category": "Dairy/Alternatives", "calories": 15, "protein": 0.6, "carbs": 0.3, "fats": 1.2, "description": "An incredibly low-calorie dairy alternative, mostly used for mixing or cereals."}
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
for idx, item in enumerate(batch3_foods):
    comma = ',' if idx < len(batch3_foods) - 1 else ''
    s = f'  {{ name: "{item["name"]}", slug: "{item["slug"]}", category: "{item["category"]}", calories: {item["calories"]}, protein: {item["protein"]}, carbs: {item["carbs"]}, fats: {item["fats"]}, description: "{item["description"]}" }}{comma}\n'
    new_strs.append(s)

lines.insert(insert_idx, "".join(new_strs))

with open('src/data/foods.ts', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Added Batch 3 foods")
