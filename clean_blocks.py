import os
import re

# Block 1 targets
block1_files = [
    "src/pages/guides/how-many-calories-in-a-gram-guide.astro",
    "src/pages/guides/calorie-calculator-accuracy.astro",
    "src/pages/guides/macro-guide.astro",
    "src/pages/guides/what-is-bmr.astro",
    "src/pages/guides/maintenance-calories.astro"
]

block1_start = r"<p>Furthermore, metabolic adaptation is a real phenomenon\."
block1_end = r"broader framework of holistic, sustainable nutrition\.</p>"

for fpath in block1_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex substitution
        pattern = re.compile(block1_start + r".*?" + block1_end, re.DOTALL)
        replacement = "<p><em>For a deep dive into how your body adjusts to calorie deficits and nutrient density, read our complete guide to <a href='/guides/starvation-mode-metabolic-adaptation/'>Metabolic Adaptation & Health</a>.</em></p>"
        
        new_content, count = pattern.subn(replacement, content)
        if count > 0:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed Block 1 in {fpath}")

# Block 2 targets
block2_files = [
    "src/pages/calories-burned-calculator.astro",
    "src/pages/recipe-calorie-calculator.astro",
    "src/pages/meal-calorie-calculator.astro",
    "src/pages/cycling-calories-calculator.astro"
]

block2_start = r"<h3>How to Use This Calculator Effectively</h3>"
# Looking at the previous output, the repeating text starts around the "How to Use" or "Gather Accurate Data"
block2_start_alt = r"<strong>Gather Accurate Data:</strong>"
block2_end = r"let the data guide your path\.</p>"

for fpath in block2_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex substitution for Block 2
        # Many times it's repeated multiple times at the end of the file. We can match from "Advanced Strategies" to the end.
        pattern_adv = re.compile(r"<h2>Advanced Strategies for.*?let the data guide your path\.</p>(\s*<p>We highly recommend bookmarking.*?let the data guide your path\.</p>)*", re.DOTALL)
        
        new_content, count_adv = pattern_adv.subn("<p><em>Explore our <a href='/guides/'>Comprehensive Health Guides</a> to master advanced tracking strategies.</em></p>", content)
        
        # also match "Gather Accurate Data" paragraph blocks
        pattern_gather = re.compile(r"<p><strong>Gather Accurate Data:.*?Implement and Monitor:.*?results.</p>", re.DOTALL)
        new_content, count_gather = pattern_gather.subn("<p><em>Ensure you input accurate measurements. Read our guide on <a href='/guides/calorie-calculator-accuracy/'>Tracking Accuracy</a> for best results.</em></p>", new_content)
        
        if count_adv > 0 or count_gather > 0:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed Block 2 in {fpath}")
