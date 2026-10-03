import json

batch6_foods = [
  {"name": "Black Coffee", "slug": "black-coffee", "category": "Beverages", "calories": 2, "protein": 0.3, "carbs": 0, "fats": 0, "description": "A highly consumed zero-calorie stimulant packed with antioxidants."},
  {"name": "Espresso", "slug": "espresso", "category": "Beverages", "calories": 9, "protein": 0.1, "carbs": 1.7, "fats": 0.2, "description": "A highly concentrated shot of coffee, providing a rapid caffeine boost."},
  {"name": "Caffe Latte", "slug": "latte", "category": "Beverages", "calories": 42, "protein": 2.8, "carbs": 4.7, "fats": 1.3, "description": "Espresso mixed with steamed milk, adding significant dairy calories."},
  {"name": "Cappuccino", "slug": "cappuccino", "category": "Beverages", "calories": 31, "protein": 1.8, "carbs": 3.8, "fats": 1, "description": "Espresso mixed with a large amount of milk foam, making it lighter than a latte."},
  {"name": "Green Tea", "slug": "green-tea", "category": "Beverages", "calories": 1, "protein": 0.2, "carbs": 0, "fats": 0, "description": "A traditional unoxidized tea famous for its EGCG antioxidant content."},
  {"name": "Matcha", "slug": "matcha", "category": "Beverages", "calories": 3, "protein": 0.3, "carbs": 0.4, "fats": 0.1, "description": "Finely ground green tea leaves consumed whole for maximum nutrient intake."},
  {"name": "Ribeye Steak", "slug": "ribeye-steak", "category": "Meat", "calories": 291, "protein": 24, "carbs": 0, "fats": 22, "description": "An incredibly flavorful, well-marbled cut of beef heavily consumed by meat lovers."},
  {"name": "Filet Mignon", "slug": "filet-mignon", "category": "Meat", "calories": 267, "protein": 26, "carbs": 0, "fats": 17, "description": "The most tender cut of beef, very lean and highly sought after."},
  {"name": "Pork Belly", "slug": "pork-belly", "category": "Meat", "calories": 518, "protein": 9, "carbs": 0, "fats": 53, "description": "An exceptionally fatty cut of pork used to make bacon and popular in Asian cuisine."},
  {"name": "Regular Yogurt", "slug": "regular-yogurt", "category": "Dairy", "calories": 61, "protein": 3.5, "carbs": 4.7, "fats": 3.3, "description": "A fermented milk product rich in probiotics and calcium."},
  {"name": "Sour Cream", "slug": "sour-cream", "category": "Dairy", "calories": 193, "protein": 2.1, "carbs": 2.9, "fats": 19, "description": "A high-fat dairy condiment used to garnish soups and baked potatoes."},
  {"name": "Kefir", "slug": "kefir", "category": "Dairy", "calories": 60, "protein": 3.3, "carbs": 4.5, "fats": 3.3, "description": "A fermented milk drink containing up to three times more probiotics than yogurt."},
  {"name": "California Roll", "slug": "california-roll", "category": "Meals/Sushi", "calories": 130, "protein": 3.4, "carbs": 28, "fats": 0.8, "description": "A popular Western-style sushi roll filled with imitation crab, avocado, and cucumber."},
  {"name": "Salmon Sushi", "slug": "salmon-sushi", "category": "Meals/Sushi", "calories": 146, "protein": 5.9, "carbs": 27, "fats": 1.1, "description": "Nigiri or maki featuring raw salmon and sticky vinegared rice."},
  {"name": "Ramen (Instant)", "slug": "instant-ramen", "category": "Meals", "calories": 436, "protein": 9.4, "carbs": 60, "fats": 17, "description": "A highly processed, dehydrated noodle brick extremely dense in sodium and carbs."},
  {"name": "Pad Thai", "slug": "pad-thai", "category": "Meals", "calories": 219, "protein": 6.8, "carbs": 33, "fats": 6.7, "description": "A staple Thai street food consisting of stir-fried rice noodles in a sweet and savory sauce."},
  {"name": "Yam", "slug": "yam", "category": "Vegetables", "calories": 118, "protein": 1.5, "carbs": 28, "fats": 0.2, "description": "A starchy, dry root vegetable very high in complex carbohydrates."},
  {"name": "Plantain", "slug": "plantain", "category": "Fruit/Starch", "calories": 122, "protein": 1.3, "carbs": 32, "fats": 0.4, "description": "A starchy, savory cousin to the banana, typically cooked before eating."},
  {"name": "Cassava", "slug": "cassava", "category": "Vegetables", "calories": 160, "protein": 1.4, "carbs": 38, "fats": 0.3, "description": "A starchy tuberous root that is a major staple food in the developing world."},
  {"name": "Spaghetti Squash", "slug": "spaghetti-squash", "category": "Vegetables", "calories": 31, "protein": 0.6, "carbs": 7, "fats": 0.6, "description": "A unique winter squash that naturally shreds into low-calorie, noodle-like strands."},
  {"name": "Granola", "slug": "granola", "category": "Breakfast", "calories": 471, "protein": 10, "carbs": 64, "fats": 20, "description": "A highly dense mixture of rolled oats, nuts, and honey often mistaken as low-calorie."},
  {"name": "Corn Flakes", "slug": "corn-flakes", "category": "Breakfast", "calories": 357, "protein": 7.5, "carbs": 84, "fats": 0.4, "description": "A classic, heavily processed cold cereal offering simple, fast-digesting carbohydrates."},
  {"name": "White Sugar", "slug": "white-sugar", "category": "Sugars", "calories": 387, "protein": 0, "carbs": 100, "fats": 0, "description": "Pure crystalline sucrose, offering completely empty calories with zero micronutrients."},
  {"name": "Brown Sugar", "slug": "brown-sugar", "category": "Sugars", "calories": 380, "protein": 0.1, "carbs": 98, "fats": 0, "description": "White sugar combined with molasses, giving it a distinctive color and flavor."},
  {"name": "Agave Nectar", "slug": "agave-nectar", "category": "Sugars", "calories": 310, "protein": 0, "carbs": 76, "fats": 0.5, "description": "A plant-based liquid sweetener extremely high in fructose."},
  {"name": "Ranch Dressing", "slug": "ranch-dressing", "category": "Condiments", "calories": 432, "protein": 1.2, "carbs": 5.9, "fats": 45, "description": "A highly calorically dense, buttermilk and oil-based salad dressing."},
  {"name": "Caesar Dressing", "slug": "caesar-dressing", "category": "Condiments", "calories": 429, "protein": 2.1, "carbs": 4.3, "fats": 45, "description": "A savory, umami-rich salad dressing made with olive oil, egg yolks, and anchovies."},
  {"name": "Vinaigrette", "slug": "vinaigrette", "category": "Condiments", "calories": 272, "protein": 0, "carbs": 8.3, "fats": 27, "description": "An oil and vinegar emulsion, generally lower in calories than creamy dressings."},
  {"name": "Chocolate Cake", "slug": "chocolate-cake", "category": "Sweets", "calories": 371, "protein": 5.3, "carbs": 53, "fats": 16, "description": "A highly palatable baked dessert loaded with refined sugar and fats."},
  {"name": "Brownie", "slug": "brownie", "category": "Sweets", "calories": 466, "protein": 5.9, "carbs": 51, "fats": 28, "description": "A dense, rich chocolate baked confection offering very high calories."},
  {"name": "Doughnut", "slug": "doughnut", "category": "Sweets", "calories": 452, "protein": 4.9, "carbs": 51, "fats": 25, "description": "Deep-fried, sugar-glazed dough packed with saturated fats and simple carbs."},
  {"name": "Blueberry Muffin", "slug": "blueberry-muffin", "category": "Sweets", "calories": 377, "protein": 5.2, "carbs": 53, "fats": 16, "description": "A sweet baked good often mimicking cake, heavily loaded with sugar and oil."},
  {"name": "Passion Fruit", "slug": "passion-fruit", "category": "Fruit", "calories": 97, "protein": 2.2, "carbs": 23, "fats": 0.7, "description": "A tangy, aromatic tropical fruit loaded with dietary fiber and Vitamin C."},
  {"name": "Dragon Fruit", "slug": "dragon-fruit", "category": "Fruit", "calories": 60, "protein": 1.2, "carbs": 13, "fats": 0, "description": "A visually striking cactus fruit with a mild, subtly sweet flavor."},
  {"name": "Lychee", "slug": "lychee", "category": "Fruit", "calories": 66, "protein": 0.8, "carbs": 17, "fats": 0.4, "description": "A sweet, translucent tropical fruit popular in Southeast Asian desserts."},
  {"name": "Guava", "slug": "guava", "category": "Fruit", "calories": 68, "protein": 2.6, "carbs": 14, "fats": 1, "description": "A robust tropical fruit containing an enormous amount of Vitamin C."},
  {"name": "Gelatin", "slug": "gelatin", "category": "Sweets", "calories": 62, "protein": 1.2, "carbs": 14, "fats": 0, "description": "A translucent, fruit-flavored dessert offering low calories and zero fats."},
  {"name": "Graham Crackers", "slug": "graham-crackers", "category": "Snacks", "calories": 428, "protein": 7.1, "carbs": 74, "fats": 11, "description": "Sweetened whole wheat crackers commonly used as a base for pies or s'mores."},
  {"name": "Marshmallow", "slug": "marshmallow", "category": "Sweets", "calories": 318, "protein": 1.8, "carbs": 81, "fats": 0.2, "description": "A spongy confection made of sugar, water, and gelatin, whipped to a solid consistency."},
  {"name": "Protein Powder (Whey)", "slug": "whey-protein", "category": "Supplements", "calories": 352, "protein": 78, "carbs": 5, "fats": 1.5, "description": "The most widely consumed fitness supplement, delivering massive, bioavailable protein."}
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
for idx, item in enumerate(batch6_foods):
    comma = ',' if idx < len(batch6_foods) - 1 else ''
    s = f'  {{ name: "{item["name"]}", slug: "{item["slug"]}", category: "{item["category"]}", calories: {item["calories"]}, protein: {item["protein"]}, carbs: {item["carbs"]}, fats: {item["fats"]}, description: "{item["description"]}" }}{comma}\n'
    new_strs.append(s)

lines.insert(insert_idx, "".join(new_strs))

with open('src/data/foods.ts', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Added Batch 6 foods")
