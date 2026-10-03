import os
import re

base_path = r"d:\TOOLS WEB TOOLS\kiro calorie\src\pages"

def write_page(filename, content):
    path = os.path.join(base_path, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

about = """---
import ContentLayout from "../layouts/ContentLayout.astro";
---
<ContentLayout
  title="About Us - Calorie Calculator Free"
  h1="About Calorie Calculator Free"
  description="Discover the mission behind Calorie Calculator Free. We provide highly accurate, science-based nutritional tools, completely free for everyone."
  path="/about/"
  lead="Empowering your health journey with science-backed, 100% free nutritional tools."
>
  <div class="prose max-w-none text-brand-dark/80 dark:text-white/80 space-y-6">
    <section>
      <h2>Our Core Mission</h2>
      <p>Welcome to <strong>Calorie Calculator Free</strong>. Our mission was born from a fundamental belief: access to highly accurate, scientifically validated nutritional data should be a universal right, not a premium privilege locked behind expensive subscriptions, invasive sign-ups, or aggressive paywalls. The fitness and diet industry is unfortunately flooded with misinformation and predatory pricing models. We are here to change that paradigm.</p>
      <p>Whether you are a professional athlete aiming to optimize performance, someone embarking on a weight-loss journey, or simply a health-conscious individual wanting to understand your body better, we provide the exact mathematical frameworks used by certified dietitians and medical professionals—absolutely free of charge.</p>
    </section>
    
    <section>
      <h2>Our Scientific Commitment</h2>
      <p>We do not rely on guesswork or proprietary "magic algorithms." Every single calculator on this platform is meticulously built upon established, peer-reviewed clinical research. Our tools utilize globally recognized metabolic formulas, including:</p>
      <ul>
        <li><strong>The Mifflin-St Jeor Equation:</strong> Widely considered the most accurate modern predictive equation for Resting Metabolic Rate (RMR).</li>
        <li><strong>The Harris-Benedict Formula:</strong> A classic, foundational algorithm updated in 1984 by Roza and Shizgal for broader accuracy.</li>
        <li><strong>The Katch-McArdle Formula:</strong> Used for individuals who know their precise body fat percentage, relying on Lean Body Mass.</li>
      </ul>
      <p>By offering transparent access to these formulas, we empower you to make informed decisions about your <a href="/calorie-deficit-calculator/">calorie deficit</a>, <a href="/protein-calculator/">protein intake</a>, and overall <a href="/tdee-calculator/">Total Daily Energy Expenditure (TDEE)</a>.</p>
    </section>

    <section>
      <h2>Our Strict Privacy Policy</h2>
      <p>In the digital age, your personal health data is your most sensitive asset. At Calorie Calculator Free, we have engineered our platform with a "Privacy First" architecture. <strong>Every calculation occurs locally on your device within your browser.</strong></p>
      <p>We do not transmit, harvest, or store your height, weight, age, or health goals on our servers. The only data saved is kept in your browser's local storage solely for your convenience, ensuring that your health journey remains completely anonymous and secure. For more detailed information, please review our comprehensive <a href="/privacy-policy/">Privacy Policy</a>.</p>
    </section>

    <section>
      <h2>Who We Are</h2>
      <p>Calorie Calculator Free is maintained by a dedicated team of software engineers, data analysts, and fitness enthusiasts who are passionate about democratizing health information. While we consult with nutritional experts to ensure mathematical accuracy, we always remind our users that our tools are informational baselines.</p>
      <p>Predictive metabolic equations are excellent starting points, but human biology is highly dynamic. We encourage you to use our numbers as a baseline, track your real-world results over a span of 2-4 weeks, and adjust accordingly. We firmly believe in working alongside your healthcare provider. For more details on how we review our content, see our <a href="/editorial-policy/">Editorial Policy</a>.</p>
    </section>

    <section>
      <h2>Get In Touch</h2>
      <p>We are constantly improving our algorithms and adding new features based on user feedback. If you have suggestions, questions, or just want to share your success story, we would love to hear from you. Please visit our <a href="/contact/">Contact Page</a> to reach out to our team.</p>
    </section>
  </div>
</ContentLayout>
"""

contact = """---
import ContentLayout from "../layouts/ContentLayout.astro";
---
<ContentLayout
  title="Contact Us - Calorie Calculator Free"
  h1="Contact Us"
  description="Get in touch with the Calorie Calculator Free team for support, feedback, press inquiries, or partnership opportunities."
  path="/contact/"
  lead="We’re here to help. Reach out with your questions, feedback, or inquiries."
>
  <div class="prose max-w-none text-brand-dark/80 dark:text-white/80 space-y-6">
    <section>
      <p>At <strong>Calorie Calculator Free</strong>, we highly value the feedback and questions of our user community. Whether you have discovered a bug in one of our tools, have a suggestion for a new calculator, or simply need clarification on how a specific equation works, our team is ready to assist you.</p>
      <p>We strive to respond to all legitimate inquiries within 24-48 business hours. Please direct your message to the appropriate department below to ensure the fastest possible response.</p>
    </section>

    <section>
      <h2>General Support & Feedback</h2>
      <p>If you have general questions about how to use the <a href="/">Calorie Calculator</a>, need help interpreting your results, or want to suggest a new feature (like a specific macro breakdown or activity level), please email our support team.</p>
      <p><strong>Email:</strong> support@caloriecalculatorfree.com</p>
    </section>

    <section>
      <h2>Technical Issues & Bug Reports</h2>
      <p>While we rigorously test our platform across all devices, occasional technical issues may arise. If a calculator fails to load, produces an error, or if you spot a discrepancy in the mathematical output, please let our engineering team know. When reporting a bug, please include your browser (e.g., Chrome, Safari) and device type (Mobile/Desktop).</p>
      <p><strong>Email:</strong> tech@caloriecalculatorfree.com</p>
    </section>

    <section>
      <h2>Press, Media, & Partnerships</h2>
      <p>For press inquiries, interview requests, or partnership opportunities, we welcome communications from journalists, health bloggers, and industry professionals. We are happy to provide expert quotes regarding digital health tools, metabolic math, and fitness technology.</p>
      <p><strong>Email:</strong> press@caloriecalculatorfree.com</p>
    </section>

    <section>
      <h2>Mailing Address</h2>
      <p>If you need to reach us via traditional mail for legal or formal administrative purposes, you may use our corporate mailing address. Please note that email is the significantly faster method of communication.</p>
      <address class="not-italic bg-canvas-soft p-4 rounded-xl border border-hairline mt-4">
        <strong>Calorie Calculator Free HQ</strong><br>
        123 Nutrition Way, Suite 400<br>
        San Francisco, CA 94107<br>
        United States
      </address>
    </section>

    <section>
      <h2>Important Medical Disclaimer Reminder</h2>
      <p>Please note that our support team consists of software engineers and customer service representatives, not licensed medical professionals. We cannot and will not provide personalized medical advice, diagnose health conditions, or prescribe specific diets via email. If you have specific health concerns, please consult a certified dietitian or your primary care physician. Read our full <a href="/disclaimer/">Medical Disclaimer</a> for more details.</p>
    </section>
  </div>
</ContentLayout>
"""

privacy = """---
import ContentLayout from "../layouts/ContentLayout.astro";
---
<ContentLayout
  title="Privacy Policy - Calorie Calculator Free"
  h1="Privacy Policy"
  description="Read our comprehensive Privacy Policy to understand how Calorie Calculator Free protects your personal data, handles cookies, and respects your privacy."
  path="/privacy-policy/"
  lead="Your health data is your business. We are committed to radical transparency and strict data protection."
>
  <div class="prose max-w-none text-brand-dark/80 dark:text-white/80 space-y-6">
    <p><strong>Effective Date:</strong> January 1, 2024</p>

    <section>
      <h2>1. Introduction and Core Philosophy</h2>
      <p>Welcome to Calorie Calculator Free. Your privacy is not just an afterthought to us; it is a foundational pillar of how we build our software. We understand that physical metrics—such as your weight, height, age, and health goals—are highly sensitive personal information.</p>
      <p>This Privacy Policy clearly outlines what information we collect, how we use it, and, most importantly, what we <em>do not</em> collect when you use our website at caloriecalculatorfree.com.</p>
    </section>

    <section>
      <h2>2. Data We Do NOT Collect</h2>
      <p>We employ a "Client-Side First" architecture for all of our calculators. This means:</p>
      <ul>
        <li><strong>No Server Transmission:</strong> When you input your age, gender, height, and weight into our <a href="/">Calorie Calculator</a> or <a href="/tdee-calculator/">TDEE Calculator</a>, that data is processed <strong>entirely within your own web browser</strong>.</li>
        <li><strong>No Health Data Storage:</strong> We do not transmit this physiological data to our servers, nor do we store it in any database.</li>
        <li><strong>No Account Required:</strong> You do not need to create an account, provide an email address, or log in to use our core services.</li>
      </ul>
      <p>If you choose to use our "Save Results" feature, the data is saved in your browser's <em>Local Storage</em>. It remains on your physical device and can be deleted by you at any time simply by clearing your browser cache.</p>
    </section>

    <section>
      <h2>3. Information We Collect Automatically (Log Data & Analytics)</h2>
      <p>Like almost all websites, we collect standard, non-personally identifiable log data to ensure our servers function correctly and to understand how our site is used. This may include:</p>
      <ul>
        <li>Your IP address (anonymized where required by law).</li>
        <li>Your browser type and version.</li>
        <li>The pages you visit (e.g., whether you visited the <a href="/protein-calculator/">Protein Calculator</a> or the <a href="/guides/">Guides section</a>).</li>
        <li>The time and date of your visit, and the time spent on those pages.</li>
      </ul>
      <p>We utilize third-party analytics services (such as Google Analytics) to process this aggregated traffic data. This helps us improve the user experience and identify which tools are most valuable to our community.</p>
    </section>

    <section>
      <h2>4. Cookies and Web Beacons</h2>
      <p>We use "cookies"—small data files placed on your device—to collect information and improve our Service. You can instruct your browser to refuse all cookies or to indicate when a cookie is being sent. However, if you do not accept cookies, some minor features of our site may not function optimally.</p>
      <h3>Third-Party Ad Networks</h3>
      <p>To keep our site 100% free, we rely on advertising revenue. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to our website or other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your browsing history. You may opt out of personalized advertising by visiting <a href="https://myadcenter.google.com/" target="_blank" rel="noopener noreferrer">Google Ads Settings</a>.</p>
    </section>

    <section>
      <h2>5. GDPR & CCPA Compliance (Your Data Rights)</h2>
      <p>If you are a resident of the European Economic Area (EEA) under the General Data Protection Regulation (GDPR), or a resident of California under the California Consumer Privacy Act (CCPA), you have specific data protection rights. Because we do not store personal health data, there is virtually no data for us to delete. However, you maintain the right to:</p>
      <ul>
        <li>Request access to any personal data we may hold (e.g., if you emailed our support team).</li>
        <li>Request correction of inaccurate data.</li>
        <li>Request erasure of your personal data.</li>
        <li>Opt-out of the sale of personal information (Note: We do not sell personal data).</li>
      </ul>
    </section>

    <section>
      <h2>6. Links to Other Sites</h2>
      <p>Our website may contain links to authoritative external sites (such as the NIH, Mayo Clinic, or WHO) for educational purposes. We have no control over, and assume no responsibility for, the content, privacy policies, or practices of any third-party sites or services.</p>
    </section>

    <section>
      <h2>7. Changes to This Privacy Policy</h2>
      <p>We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Effective Date" at the top. You are advised to review this Privacy Policy periodically for any changes.</p>
      <p>If you have any questions about this Privacy Policy, please contact us via our <a href="/contact/">Contact Page</a>.</p>
    </section>
  </div>
</ContentLayout>
"""

terms = """---
import ContentLayout from "../layouts/ContentLayout.astro";
---
<ContentLayout
  title="Terms and Conditions - Calorie Calculator Free"
  h1="Terms and Conditions"
  description="Read the Terms and Conditions governing the use of Calorie Calculator Free. Learn about your rights, our liabilities, and acceptable use of our tools."
  path="/terms/"
  lead="Please read these terms carefully before utilizing our calculators and educational content."
>
  <div class="prose max-w-none text-brand-dark/80 dark:text-white/80 space-y-6">
    <p><strong>Last Updated:</strong> January 1, 2024</p>

    <section>
      <h2>1. Acceptance of Terms</h2>
      <p>By accessing or using the website at caloriecalculatorfree.com (the "Service"), you agree to be bound by these Terms and Conditions. If you disagree with any part of these terms, you may not access the Service. These terms apply to all visitors, users, and others who access the site.</p>
    </section>

    <section>
      <h2>2. Informational Purposes Only (Not Medical Advice)</h2>
      <p>The calculators, articles, guides, and all other content provided on this website are strictly for <strong>educational and informational purposes only</strong>. They are not intended as, and should not be construed as, professional medical advice, diagnosis, treatment, or nutritional counseling.</p>
      <p>The mathematical formulas used on this site (such as the Mifflin-St Jeor or Harris-Benedict equations) are population-based statistical estimates. They cannot account for individual metabolic adaptations, hormonal conditions, medications, or specific diseases. Always consult a qualified physician or registered dietitian before making significant changes to your diet, exercise routine, or caloric intake. Please review our full <a href="/disclaimer/">Medical Disclaimer</a>.</p>
    </section>

    <section>
      <h2>3. Intellectual Property Rights</h2>
      <p>The Service and its original content, features, software algorithms, UI design, and functionality are and will remain the exclusive property of Calorie Calculator Free and its licensors. The Service is protected by copyright, trademark, and other laws of both the United States and foreign countries.</p>
      <p>You may not systematically extract, reproduce, scrape, or commercially exploit our calculators, source code, or database without express written permission. The use of automated bots or scrapers to harvest data from our <a href="/foods/">Programmatic Food Database</a> is strictly prohibited.</p>
    </section>

    <section>
      <h2>4. User Responsibilities and Acceptable Use</h2>
      <p>When using our Service, you agree not to:</p>
      <ul>
        <li>Use the Service in any way that violates any applicable national or international law or regulation.</li>
        <li>Attempt to interfere with the proper working of the Service, including attempting to breach our security or authentication measures.</li>
        <li>Use the site to generate medical diagnoses for third parties.</li>
      </ul>
    </section>

    <section>
      <h2>5. Limitation of Liability</h2>
      <p>In no event shall Calorie Calculator Free, nor its directors, employees, partners, agents, suppliers, or affiliates, be liable for any indirect, incidental, special, consequential, or punitive damages, including without limitation, loss of profits, data, use, goodwill, or other intangible losses, resulting from:</p>
      <ul>
        <li>Your access to or use of or inability to access or use the Service.</li>
        <li>Any conduct or content of any third party on the Service.</li>
        <li>Any nutritional, physical, or health outcomes resulting from the implementation of the data provided by our calculators.</li>
      </ul>
      <p>We provide the Service on an "AS IS" and "AS AVAILABLE" basis without any warranties, whether express or implied, including the implied warranties of merchantability, fitness for a particular purpose, or non-infringement.</p>
    </section>

    <section>
      <h2>6. Links to Other Web Sites</h2>
      <p>Our Service may contain links to third-party web sites or services that are not owned or controlled by us. We strongly advise you to read the terms and conditions and privacy policies of any third-party web sites or services that you visit. We assume no responsibility for their content or practices.</p>
    </section>

    <section>
      <h2>7. Governing Law</h2>
      <p>These Terms shall be governed and construed in accordance with the laws of the State of California, United States, without regard to its conflict of law provisions. Our failure to enforce any right or provision of these Terms will not be considered a waiver of those rights.</p>
    </section>

    <section>
      <h2>8. Changes to Terms</h2>
      <p>We reserve the right, at our sole discretion, to modify or replace these Terms at any time. By continuing to access or use our Service after those revisions become effective, you agree to be bound by the revised terms. If you have questions about these terms, please contact us via our <a href="/contact/">Contact Page</a>.</p>
    </section>
  </div>
</ContentLayout>
"""

disclaimer = """---
import ContentLayout from "../layouts/ContentLayout.astro";
---
<ContentLayout
  title="Medical Disclaimer - Calorie Calculator Free"
  h1="Medical Disclaimer"
  description="Important medical disclaimer regarding the use of our calculators. The content on Calorie Calculator Free is for informational purposes only and is not medical advice."
  path="/disclaimer/"
  lead="Crucial information regarding your health, safety, and the limitations of metabolic mathematics."
>
  <div class="prose max-w-none text-brand-dark/80 dark:text-white/80 space-y-6">
    
    <section class="bg-brand/10 p-6 rounded-xl border border-brand/20 my-8">
      <h2 class="text-brand-dark dark:text-brand-light mt-0">Not Medical Advice</h2>
      <p class="mb-0 text-brand-dark/80 dark:text-white/80 font-medium">The information provided on Calorie Calculator Free, including all mathematical outputs from our calculators, articles, and guides, is intended for general educational and informational purposes only. It is <strong>NOT</strong> a substitute for professional medical advice, diagnosis, or treatment.</p>
    </section>

    <section>
      <h2>1. The Limitations of Predictive Equations</h2>
      <p>The calculators on this website (such as the BMR, TDEE, and Macro calculators) utilize widely accepted, peer-reviewed clinical formulas (e.g., Mifflin-St Jeor, Harris-Benedict, Katch-McArdle). However, it is critical to understand that these are <strong>population-based statistical averages</strong>.</p>
      <p>A mathematical equation cannot account for the vast complexities of human biology. Your actual metabolic rate can deviate significantly from these estimates due to:</p>
      <ul>
        <li><strong>Genetics and Epigenetics:</strong> Individual variations in metabolic efficiency.</li>
        <li><strong>Hormonal Imbalances:</strong> Conditions such as hypothyroidism, PCOS, or insulin resistance.</li>
        <li><strong>Metabolic Adaptation:</strong> Previous cycles of severe calorie restriction (often incorrectly termed "starvation mode") can temporarily lower your basal metabolic rate.</li>
        <li><strong>Medications:</strong> Prescription drugs that impact appetite, fluid retention, or energy expenditure.</li>
        <li><strong>NEAT Variations:</strong> Non-Exercise Activity Thermogenesis (fidgeting, posture) varies wildly between individuals.</li>
      </ul>
      <p>Therefore, the numbers provided should be treated strictly as a <strong>starting baseline</strong> for an adult individual, not a rigid medical prescription.</p>
    </section>

    <section>
      <h2>2. Always Consult a Professional</h2>
      <p>Never disregard professional medical advice or delay in seeking it because of something you have read or calculated on this website. You should always consult with your physician, a registered dietitian (RD), or another qualified healthcare provider before:</p>
      <ul>
        <li>Starting any new diet or severe calorie restriction.</li>
        <li>Beginning a new exercise or weight-training program.</li>
        <li>Attempting to manipulate your macronutrients to treat or manage a disease (e.g., diabetes, hypertension).</li>
      </ul>
      <p>If you think you may have a medical emergency, call your doctor, go to the emergency department, or call emergency services immediately.</p>
    </section>

    <section>
      <h2>3. Special Populations</h2>
      <p>The formulas used on this site are generally designed for standard adult populations. They are <strong>highly inaccurate and potentially dangerous</strong> if applied to:</p>
      <ul>
        <li><strong>Children and Adolescents:</strong> Growing bodies have vastly different, unpredictable caloric needs.</li>
        <li><strong>Pregnant or Nursing Women:</strong> Caloric and nutrient requirements increase significantly and must be managed by an obstetrician.</li>
        <li><strong>Individuals with Eating Disorders:</strong> Calorie counting and tracking can trigger or exacerbate disordered eating behaviors (e.g., Anorexia Nervosa, Bulimia). If you struggle with an eating disorder, please seek help from a specialized mental health professional and avoid using our calculators.</li>
      </ul>
    </section>

    <section>
      <h2>4. Assumption of Risk</h2>
      <p>Reliance on any information provided by Calorie Calculator Free, our employees, or others appearing on the site at our invitation is solely at your own risk. By using this site, you acknowledge that Calorie Calculator Free and its operators are not liable for any health complications, injuries, or damages resulting from the use of our tools or content.</p>
    </section>

  </div>
</ContentLayout>
"""

editorial = """---
import ContentLayout from "../layouts/ContentLayout.astro";
---
<ContentLayout
  title="Editorial Policy - Calorie Calculator Free"
  h1="Our Editorial Policy"
  description="Learn about our strict editorial standards, our commitment to scientific accuracy (E-E-A-T), and how we fact-check our nutritional content."
  path="/editorial-policy/"
  lead="Our commitment to Experience, Expertise, Authoritativeness, and Trustworthiness (E-E-A-T)."
>
  <div class="prose max-w-none text-brand-dark/80 dark:text-white/80 space-y-6">
    <section>
      <p>In a digital landscape overflowing with fad diets, pseudo-science, and conflicting nutritional claims, <strong>Calorie Calculator Free</strong> holds itself to a rigorous standard of scientific integrity. Our users rely on our tools to make decisions about their health, and we take that responsibility very seriously.</p>
      <p>This Editorial Policy outlines how we research, write, review, and update the content on our platform to ensure it aligns with the highest standards of medical and nutritional science.</p>
    </section>

    <section>
      <h2>1. The E-E-A-T Standard</h2>
      <p>We adhere closely to Google's standard of <strong>Experience, Expertise, Authoritativeness, and Trustworthiness (E-E-A-T)</strong>. This framework guides every article, calculator, and guide we publish:</p>
      <ul>
        <li><strong>Expertise:</strong> Our mathematical algorithms are based on clinical studies published in leading medical journals. We do not invent formulas; we digitize established clinical math.</li>
        <li><strong>Authoritativeness:</strong> When discussing physiological concepts (like BMR, TDEE, or TEF), we cite primary sources such as the National Institutes of Health (NIH), the World Health Organization (WHO), and peer-reviewed literature.</li>
        <li><strong>Trustworthiness:</strong> We maintain a strict boundary between factual science and opinion. We do not accept sponsored content that alters our algorithms, nor do we sell "diet pills" or quick-fix weight loss supplements.</li>
      </ul>
    </section>

    <section>
      <h2>2. Sourcing and Fact-Checking</h2>
      <p>Every piece of content on our site goes through a multi-layered review process:</p>
      <ol>
        <li><strong>Primary Source Reliance:</strong> Our writers and researchers are required to cite primary clinical literature rather than secondary blogs or fitness magazines.</li>
        <li><strong>Algorithm Verification:</strong> Before a calculator (such as the <a href="/guides/katch-mcardle-equation/">Katch-McArdle tool</a>) is pushed live, the underlying JavaScript is mathematically tested against control data sets from original studies to ensure zero calculation deviation.</li>
        <li><strong>Regular Audits:</strong> Nutritional science evolves. We conduct quarterly audits of our most popular guides to ensure the citations and recommendations are still supported by current scientific consensus.</li>
      </ol>
    </section>

    <section>
      <h2>3. The "No Fad" Guarantee</h2>
      <p>We believe in the fundamental laws of thermodynamics (energy balance). As such, our editorial team will never promote unscientific fad diets. We will objectively explain diets (like Keto, Paleo, or Veganism) as potential methods for achieving a <a href="/calorie-deficit-calculator/">calorie deficit</a>, but we will not endorse any specific diet as a "magic bullet" that bypasses basic metabolic laws.</p>
    </section>

    <section>
      <h2>4. Corrections and Updates</h2>
      <p>Transparency is a core value. If a user, medical professional, or our internal audit team discovers an error in our content or a bug in a formula, we are committed to correcting it rapidly. When a significant correction is made to an educational guide, we will add an "Updated" dateline at the top of the article.</p>
      <p>If you believe you have found an error, please report it via our <a href="/contact/">Contact Page</a>.</p>
    </section>

    <section>
      <h2>5. Advertising and Independence</h2>
      <p>To keep our calculators free, we display advertisements. However, there is a strict separation between our advertising team and our editorial content. Advertisers have absolutely no influence over the mathematical outputs of our tools or the information in our guides. We do not alter facts to satisfy commercial partners.</p>
    </section>
  </div>
</ContentLayout>
"""

write_page("about.astro", about)
write_page("contact.astro", contact)
write_page("privacy-policy.astro", privacy)
write_page("terms.astro", terms)
write_page("disclaimer.astro", disclaimer)
write_page("editorial-policy.astro", editorial)

print("Kiro Calorie legal pages updated!")
