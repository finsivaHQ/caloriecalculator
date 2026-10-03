import re

file_path = r"d:\TOOLS WEB TOOLS\kiro calorie\src\pages\index.astro"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_prose = """
      <h2>The Ultimate Guide to Understanding Your Calorie Needs</h2>
      <p>
        Welcome to the most comprehensive and free calorie calculator available. Whether your goal is to shed stubborn body fat, build lean muscle mass, or simply maintain a healthy weight, understanding your daily energy expenditure is the most critical first step. This guide will walk you through exactly how to use this tool, the science behind the calculations, and how to apply these numbers to your daily life to achieve sustainable, long-term results.
      </p>

      <h2>How to Use This Calorie Calculator (Step-by-Step Guide)</h2>
      <p>
        Our calculator is designed to be as intuitive as possible while providing highly accurate, science-backed results. To get the most accurate estimate, follow these steps:
      </p>
      
      <h3>Step 1: Input Your Basic Biometrics</h3>
      <p>
        Start by entering your <strong>Age</strong>, <strong>Gender</strong>, <strong>Height</strong>, and <strong>Weight</strong>. These four variables are the foundation of the basal metabolic rate equation. Age plays a role because our metabolism naturally slows down as we get older, primarily due to a gradual loss of lean muscle mass. Gender is included because biological males typically have a higher ratio of muscle to fat compared to females of the same weight, leading to a higher resting energy expenditure. Be as honest and accurate as possible with your current weight and height to ensure the baseline calculation is precise.
      </p>

      <h3>Step 2: Determine Your Activity Level Correctly</h3>
      <p>
        This is where most people make a critical error. It is incredibly common to overestimate how active you are. Here is a breakdown of what each activity level actually means in a practical context:
      </p>
      <ul>
        <li><strong>Sedentary (x1.2):</strong> You work a desk job, commute in a car, and do little to no structured exercise. Your daily step count is likely below 5,000 steps.</li>
        <li><strong>Lightly Active (x1.375):</strong> You have a desk job but you perform light exercise (like walking or gentle yoga) 1 to 3 days a week, or you are on your feet somewhat during the day but not doing hard labor.</li>
        <li><strong>Moderately Active (x1.55):</strong> You engage in moderate exercise (like brisk walking, cycling, or weightlifting) 3 to 5 days a week. Alternatively, you have a job that keeps you moving all day, like a teacher or retail worker, combined with some exercise.</li>
        <li><strong>Very Active (x1.725):</strong> You perform intense exercise or sports 6 to 7 days a week. Think of a dedicated athlete training hard every single day.</li>
        <li><strong>Extra Active (x1.9):</strong> You have a highly physically demanding job (like construction, roofing, or farming) AND you train hard daily, or you are a professional athlete training multiple times a day.</li>
      </ul>
      <p>
        If you are unsure, it is generally safer to select a slightly lower activity level and adjust later based on your real-world progress.
      </p>

      <h3>Step 3: Choose Your Primary Goal</h3>
      <p>
        Once the calculator has determined your maintenance calories, you can select your goal: weight loss, maintenance, or weight gain. The calculator will automatically apply the appropriate caloric deficit or surplus and generate a daily target for you.
      </p>

      <h2>The Science Behind the Math: Demystifying Metabolism</h2>
      <p>
        To truly master your nutrition, it helps to understand what the numbers actually mean. Your body burns energy in several different ways, which cumulatively make up your Total Daily Energy Expenditure (TDEE). Our calculator uses the highly regarded <strong>Mifflin-St Jeor equation</strong>, which numerous clinical studies have shown to be the most accurate predictive equation for the general population.
      </p>
      
      <h3>Basal Metabolic Rate (BMR)</h3>
      <p>
        Your BMR represents the absolute minimum amount of energy your body requires simply to stay alive and function while at complete rest. Imagine you were lying in a dark room all day doing absolutely nothing—your body still needs calories to keep your heart beating, your lungs breathing, your brain functioning, and your body temperature regulated. For most people, BMR accounts for roughly 60% to 70% of their total daily calorie expenditure. 
      </p>

      <h3>Non-Exercise Activity Thermogenesis (NEAT)</h3>
      <p>
        NEAT includes all the calories you burn from movements that are not structured exercise. This includes walking to the kitchen, fidgeting at your desk, doing household chores, or carrying groceries. NEAT varies wildly from person to person and is one of the biggest reasons why two people of the same size might have vastly different calorie needs. 
      </p>

      <h3>Thermic Effect of Food (TEF)</h3>
      <p>
        Did you know you burn calories just by digesting food? The process of chewing, digesting, absorbing, and storing the nutrients you consume takes energy. This is known as the Thermic Effect of Food (TEF). Protein has the highest thermic effect (about 20-30% of protein calories are burned during digestion), followed by carbohydrates (5-10%), and fats (0-3%).
      </p>

      <h3>Exercise Activity Thermogenesis (EAT)</h3>
      <p>
        This refers to the calories burned during intentional, structured exercise, such as going for a run, lifting weights, or swimming. While it's what most people focus on for weight loss, it often makes up a surprisingly small percentage of total daily energy expenditure for the average person.
      </p>

      <h2>Calories for Weight Loss: Mastering the Caloric Deficit</h2>
      <p>
        The fundamental rule of weight loss is thermodynamics: you must consume fewer calories than your body expends. This state is known as a <strong>calorie deficit</strong>. When your body doesn't get enough energy from food, it is forced to tap into its stored energy reserves (body fat) to make up the difference.
      </p>
      <p>
        A widely cited rule of thumb states that one pound of body fat contains approximately 3,500 calories. Therefore, creating a daily deficit of 500 calories (500 x 7 days = 3,500) should mathematically result in one pound of fat loss per week. While the human body is more complex than simple math and metabolic adaptations do occur, this remains an excellent starting guideline.
      </p>
      <p>
        <strong>Why Extreme Deficits Backfire:</strong> It can be tempting to slash your calories drastically to lose weight as fast as possible. However, extreme diets often lead to a loss of lean muscle mass, intense hunger, lethargy, and a slowing down of your metabolism as your body tries to conserve energy. A moderate deficit of 300 to 500 calories is much more sustainable, preserves muscle tissue, and leads to better long-term adherence.
      </p>

      <h2>Calories for Weight Gain: Building Muscle Efficiently</h2>
      <p>
        If your goal is to build muscle, you need to provide your body with the building blocks and energy to synthesize new tissue. This requires a <strong>calorie surplus</strong>—eating more calories than your TDEE.
      </p>
      <p>
        <strong>Lean Bulking vs. Dirty Bulking:</strong> A "dirty bulk" involves eating everything in sight to drive the scale up as fast as possible. The problem with this approach is that the body can only synthesize a limited amount of muscle tissue at a time; any excess calories beyond that limit will simply be stored as fat. A "lean bulk" is much smarter. By eating in a small surplus of 200 to 400 calories above maintenance, you provide enough energy to maximize muscle growth while minimizing unnecessary fat gain.
      </p>

      <h2>Maintenance Calories: Finding Your Balance</h2>
      <p>
        Maintenance calories (your exact TDEE) are the sweet spot where you are neither gaining nor losing weight. Eating at maintenance is ideal if you are happy with your current physique, if you are an athlete looking to fuel performance without changing weight, or if you are aiming for <strong>body recomposition</strong>. Recomposition is the process of losing fat and building muscle simultaneously, which is highly possible for beginners, those returning from a layoff, or individuals with higher body fat percentages who eat at or very slightly below maintenance calories while strength training.
      </p>

      <h2>Macronutrients Explained: Beyond Just Calories</h2>
      <p>
        While total calories determine <em>whether</em> you gain or lose weight, your macronutrient split (macros) strongly influences <em>what kind</em> of weight you gain or lose.
      </p>
      <ul>
        <li><strong>Protein (4 calories per gram):</strong> The building block of muscle. A high protein intake is essential during weight loss to preserve lean mass and keep you feeling full, and crucial during weight gain to fuel muscle protein synthesis.</li>
        <li><strong>Carbohydrates (4 calories per gram):</strong> Your body's preferred source of energy. Carbs fuel high-intensity workouts, support recovery, and support healthy thyroid function.</li>
        <li><strong>Fats (9 calories per gram):</strong> Essential for hormone production, joint health, and the absorption of fat-soluble vitamins (A, D, E, and K). Because fats are more than twice as calorie-dense as carbs and protein, portion control is important.</li>
      </ul>

      <h2>Exhaustive Calorie & Dieting FAQs</h2>
      
      <h3>Why am I not losing weight on a calorie deficit?</h3>
      <p>
        If you have been in a consistent deficit for several weeks and the scale hasn't moved, the reality is that you are not in a deficit. This usually happens for three reasons: underestimating portion sizes (use a food scale!), forgetting to log liquid calories or cooking oils, or overestimating calories burned from exercise. It is also possible that water retention (from sodium, stress, or carbohydrate intake) is masking fat loss on the scale. Be patient and meticulously track everything for a few days to identify discrepancies.
      </p>

      <h3>Do I need to count calories forever?</h3>
      <p>
        Absolutely not. Calorie counting is simply a tool for education. By tracking your intake for a few weeks or months, you will develop an incredible awareness of portion sizes, the caloric density of different foods, and your own hunger cues. Many people transition to intuitive eating or portion estimation once they have calibrated their understanding of food through a period of tracking.
      </p>

      <h3>Should I eat back the calories I burn from exercise?</h3>
      <p>
        Generally, no. If you used our calculator and selected an activity level like "Lightly Active" or "Moderately Active," your exercise calories are <em>already factored into</em> your Total Daily Energy Expenditure. Eating them back would result in double-counting and likely erase your caloric deficit.
      </p>

      <h3>How does age affect my calorie needs?</h3>
      <p>
        As we age, our resting metabolic rate naturally decreases, largely due to a gradual loss of muscle mass (sarcopenia) and decreased spontaneous physical activity. This is why you cannot eat the same way at 50 as you did at 20 without gaining weight. The best way to combat this age-related metabolic slowdown is to engage in regular resistance training to build and preserve muscle tissue.
      </p>

      <h3>Can I build muscle in a calorie deficit?</h3>
      <p>
        Yes, but it is difficult and highly context-dependent. This is easiest for beginners (newbie gains), individuals with a significant amount of excess body fat to use as fuel, or people returning to training after a long break. Advanced trainees with low body fat will find it almost impossible to build new muscle while losing fat and should focus on distinct bulking and cutting phases.
      </p>

      <h3>Does meal timing matter?</h3>
      <p>
        For general health and weight management, total daily caloric intake and hitting your macronutrient targets are exponentially more important than when you eat. Whether you eat three large meals, six small meals, or practice intermittent fasting, the results will be largely the same if the total calories are equal. Choose an eating schedule that fits your lifestyle, keeps hunger at bay, and allows you to adhere to your diet consistently.
      </p>

      <h2>Important Limitations & Safety Warnings</h2>
      <p>
        While calculating your macros and calories is a powerful way to take control of your health, it is not a perfect science. Please keep the following limitations in mind:
      </p>
      <ul>
        <li><strong>Minimum Safe Intake:</strong> Most health organizations advise against dropping below 1,200 calories per day for women and 1,500 calories per day for men unless under direct medical supervision. Doing so can lead to nutritional deficiencies, gallstones, and muscle wasting.</li>
        <li><strong>Medical Conditions:</strong> If you suffer from metabolic disorders, polycystic ovary syndrome (PCOS), thyroid issues (hypothyroidism), or take certain medications, standard formulas may over- or under-estimate your needs. Always consult with a physician or registered dietitian.</li>
        <li><strong>Mental Health:</strong> Calorie counting can trigger obsessive behaviors or exacerbate eating disorders in susceptible individuals. If you have a history of disordered eating, please avoid rigid tracking and seek guidance from a qualified professional.</li>
        <li><strong>The Human Element:</strong> Remember that equations are based on population averages. Your unique genetics, daily stress levels, sleep quality, and gut microbiome all play subtle but significant roles in how your body processes energy. Use the calculator as a starting point, monitor your results, and adjust accordingly.</li>
      </ul>

      <Sources sources={[
        { label: "Dietary Guidelines for Americans — Calorie Needs", href: "https://www.dietaryguidelines.gov/" },
        { label: "Mifflin-St Jeor equation for resting energy expenditure — NIH", href: "https://pubmed.ncbi.nlm.nih.gov/2305711/" },
      ]} />
"""

# Now replace the content in the file using regex or string splitting
# Find <div class="prose-content mx-auto max-w-3xl"> and </div>\n  </Section>
start_marker = '<div class="prose-content mx-auto max-w-3xl">'
end_marker = '    </div>\\n  </Section>'

start_idx = content.find(start_marker)

# We want to replace everything after the start_marker up to the </div> tag before </Section>
# Let's find </Section> and go backwards to find the </div>.
end_section_idx = content.find('</Section>', start_idx)
end_div_idx = content.rfind('</div>', start_idx, end_section_idx)

if start_idx != -1 and end_div_idx != -1:
    # include start_marker in replacement
    new_content = content[:start_idx + len(start_marker)] + "\\n" + new_prose + "\\n    " + content[end_div_idx:]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Content replaced successfully.")
else:
    print("Markers not found.")
    print("Start:", start_idx)
    print("End Div:", end_div_idx)
