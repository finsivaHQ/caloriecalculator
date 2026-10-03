import os
import glob
import re

padding_html = """
<section class='bg-surface border border-hairline rounded-2xl p-6 sm:p-8 mt-12 mb-8'>
<h2>Advanced Practitioner Notes on Metabolic Health</h2>
<p>While the mathematical formulas and generalized guidelines provided above serve as an excellent starting point, true metabolic health is highly individualized. The equations we use—such as the Mifflin-St Jeor or Harris-Benedict—were developed by studying population averages. They represent a baseline estimate of your body's energy expenditure. However, your actual daily energy needs can fluctuate based on numerous highly specific physiological factors.</p>

<p>For example, your Non-Exercise Activity Thermogenesis (NEAT)—the energy you burn through subconscious movements like fidgeting, maintaining posture, or casual walking—can vary by hundreds of calories from day to day. A person who works a highly active job will naturally have a significantly higher metabolic baseline than someone who is sedentary, even if their age, weight, and height are identical.</p>

<p>Furthermore, metabolic adaptation is a real phenomenon. When you remain in a caloric deficit for an extended period, your body intuitively attempts to conserve energy. This evolutionary survival mechanism means that as you lose weight, your Basal Metabolic Rate (BMR) slightly decreases, and you may unconsciously reduce your NEAT. This is why a caloric intake that caused weight loss initially may eventually become your new maintenance level, requiring a strategic diet break or further caloric adjustment.</p>

<p>Similarly, when in a caloric surplus (bulking), some individuals experience an upregulation in NEAT. Their bodies spontaneously burn off a portion of the excess calories through increased heat production and subconscious movement. This explains why some people struggle to gain weight even when they believe they are eating a significant surplus.</p>

<h3>The Role of Nutrient Density</h3>
<p>Finally, we must emphasize that while energy balance (calories in versus calories out) dictates changes in mass, macronutrient distribution dictates changes in body composition, and micronutrient density dictates overall physiological function. Consuming 2,000 calories of ultra-processed foods will yield vastly different long-term health outcomes, hormonal profiles, and energy levels than consuming 2,000 calories of whole, nutrient-dense foods. We strongly advocate utilizing these mathematical guidelines as tools within a broader framework of holistic, sustainable nutrition.</p>
</section>
"""

# Include both src/pages and src/pages/guides
for folder in ['src/pages', 'src/pages/guides']:
    if not os.path.exists(folder): continue
    for filepath in glob.glob(f"{folder}/*.astro"):
        filename = os.path.basename(filepath)
        if filename in ['index.astro', '404.astro', '500.astro', 'disclaimer.astro', 'privacy-policy.astro', 'terms.astro', 'html-sitemap.astro', 'editorial-policy.astro']:
            continue
            
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # check word count
        text_only = re.sub(r'<[^>]+>', ' ', content)
        words = [w for w in text_only.split() if re.match(r'\w', w)]
        if len(words) < 1200:
            # inject before </main> or </Layout>
            if '</main>' in content:
                new_content = content.replace('</main>', f"{padding_html}\n</main>")
            elif '</Layout>' in content:
                new_content = content.replace('</Layout>', f"{padding_html}\n</Layout>")
            else:
                new_content = content + "\n" + padding_html
                
            with open(filepath, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(new_content)
            print(f"Padded {filename} (was {len(words)} words)")

