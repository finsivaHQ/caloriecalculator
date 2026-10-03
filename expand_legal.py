import os

base_path = r"d:\TOOLS WEB TOOLS\kiro calorie\src\pages"

def write_page(filename, content):
    path = os.path.join(base_path, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

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
    <p><strong>Effective Date:</strong> January 1, 2024 (Last Reviewed: October 2026)</p>

    <section>
      <h2>1. Introduction and Core Philosophy</h2>
      <p>Welcome to Calorie Calculator Free. Your privacy is not just an afterthought to us; it is a foundational pillar of how we build our software. We understand that physical metrics—such as your weight, height, age, and health goals—are highly sensitive personal information. In an era where data brokering and unauthorized data sharing are common, we take a different path.</p>
      <p>This Privacy Policy clearly outlines what information we collect, how we use it, and, most importantly, what we <em>do not</em> collect when you use our website at caloriecalculatorfree.com. By using our tools, you agree to the terms outlined in this document.</p>
    </section>

    <section>
      <h2>2. Data We Do NOT Collect (The Client-Side Promise)</h2>
      <p>The vast majority of health and fitness applications require you to create an account and upload your body metrics to a remote database. We employ a strict "Client-Side First" architecture for all of our calculators. This means:</p>
      <ul>
        <li><strong>No Server Transmission:</strong> When you input your age, gender, height, and weight into our <a href="/">Calorie Calculator</a>, <a href="/tdee-calculator/">TDEE Calculator</a>, or any other tool on this site, that data is processed <strong>entirely within your own web browser</strong> using local JavaScript.</li>
        <li><strong>No Health Data Storage:</strong> Because the math happens on your phone or computer, we do not transmit this physiological data to our servers, nor do we store it in any database. We literally cannot see what you type into the calculator fields.</li>
        <li><strong>No Account Required:</strong> You do not need to create an account, provide an email address, or log in to use our core services. We do not want your email address unless you specifically contact us for support.</li>
      </ul>
      <p>If you choose to use our "Save Results" feature, the data is saved in your browser's <em>Local Storage</em>. It remains on your physical device and can be deleted by you at any time simply by clearing your browser cache. This ensures maximum privacy for your health journey.</p>
    </section>

    <section>
      <h2>3. Information We Collect Automatically (Log Data & Analytics)</h2>
      <p>While we do not collect personal health data, like almost all modern websites, we collect standard, non-personally identifiable log data to ensure our servers function correctly and to understand how our site is used. This data is critical for defending against cyber attacks and optimizing our page load speeds. This may include:</p>
      <ul>
        <li>Your IP address (which is anonymized and truncated where required by law).</li>
        <li>Your browser type, operating system, and device type (Mobile vs. Desktop).</li>
        <li>The specific pages you visit (e.g., whether you visited the <a href="/protein-calculator/">Protein Calculator</a> or the <a href="/guides/">Guides section</a>).</li>
        <li>The time and date of your visit, the time spent on those pages, and referring/exit pages.</li>
      </ul>
      <p>We utilize third-party analytics services (such as Google Analytics and Cloudflare Web Analytics) to process this aggregated traffic data. This helps us improve the user experience, identify which tools are most valuable to our community, and determine where we should focus our engineering efforts next.</p>
    </section>

    <section>
      <h2>4. Form Submissions and Email Communications</h2>
      <p>If you choose to contact us via the form on our <a href="/contact/">Contact Page</a> or by emailing us directly, you will be voluntarily providing us with your email address, name, and the contents of your message. We use this information <strong>solely</strong> to respond to your inquiry, troubleshoot your technical issue, or address your feedback.</p>
      <p>We use Formspree to securely route contact form submissions to our inbox. We will never sell your email address to marketing agencies, nor will we subscribe you to any promotional newsletters without your explicit, double-opt-in consent. Once a support ticket is resolved, the communication is securely archived.</p>
    </section>

    <section>
      <h2>5. Cookies and Web Beacons</h2>
      <p>We use "cookies"—small data files placed on your device—to collect information, maintain site preferences (like Dark/Light mode), and improve our Service. You can instruct your browser to refuse all cookies or to indicate when a cookie is being sent. However, if you do not accept cookies, some minor features of our site may not function optimally (for example, your theme preference might reset on your next visit).</p>
      
      <h3>Third-Party Ad Networks</h3>
      <p>To keep our site 100% free for everyone, we rely on advertising revenue. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to our website or other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your browsing history. You may opt out of personalized advertising by visiting <a href="https://myadcenter.google.com/" target="_blank" rel="noopener noreferrer">Google Ads Settings</a>.</p>
    </section>

    <section>
      <h2>6. GDPR, CCPA, and Global Privacy Rights</h2>
      <p>We respect international privacy frameworks. If you are a resident of the European Economic Area (EEA) under the General Data Protection Regulation (GDPR), a resident of California under the California Consumer Privacy Act (CCPA), or reside in a jurisdiction with similar privacy laws, you have specific data protection rights.</p>
      <p>Because we <strong>do not store personal health data or user accounts</strong>, the scope of personal data we hold is extremely limited. However, regarding any data we do hold (such as an email you sent to support), you maintain the right to:</p>
      <ul>
        <li><strong>Right to Access:</strong> Request a copy of any personal data we may hold about you.</li>
        <li><strong>Right to Rectification:</strong> Request correction of inaccurate data.</li>
        <li><strong>Right to Erasure (Right to be Forgotten):</strong> Request deletion of your personal communications with us.</li>
        <li><strong>Right to Opt-Out:</strong> Opt-out of the sale of personal information (Note: We categorically do not sell personal data to data brokers).</li>
      </ul>
      <p>To exercise any of these rights, please reach out via our Contact Page. We will respond to your request within the legally mandated timeframe (typically 30 days).</p>
    </section>

    <section>
      <h2>7. Children's Privacy</h2>
      <p>Calorie Calculator Free is not intended for use by children under the age of 13. Furthermore, nutritional calculations for growing adolescents are vastly different than those for adults and require pediatric supervision. We do not knowingly collect personally identifiable information from anyone under the age of 13. If you are a parent or guardian and you are aware that your child has provided us with personal data (such as via an email inquiry), please contact us so that we will take the necessary actions to remove that information from our servers.</p>
    </section>

    <section>
      <h2>8. Links to Other Sites</h2>
      <p>Our website often contains links to authoritative external sites (such as the NIH, Mayo Clinic, PubMed, or WHO) for educational citation purposes. We have no control over, and assume no responsibility for, the content, privacy policies, or practices of any third-party sites or services. We strongly advise you to read the privacy policy of every site you visit.</p>
    </section>

    <section>
      <h2>9. Changes to This Privacy Policy</h2>
      <p>We may update our Privacy Policy from time to time to reflect changes in legal requirements, technical infrastructure, or business practices. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Effective Date" at the top.</p>
      <p>You are advised to review this Privacy Policy periodically for any changes. Changes to this Privacy Policy are effective when they are posted on this page.</p>
      <p>If you have any questions, concerns, or require further clarification about this Privacy Policy, please do not hesitate to contact us via our <a href="/contact/">Contact Page</a>.</p>
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
    <p><strong>Last Updated:</strong> January 1, 2024 (Last Reviewed: October 2026)</p>

    <section>
      <h2>1. Acceptance of Terms</h2>
      <p>By accessing or using the website at caloriecalculatorfree.com (the "Service"), you agree to be bound by these Terms and Conditions. If you disagree with any part of these terms, you may not access the Service. These terms apply to all visitors, users, automated systems, and others who access the site.</p>
      <p>Your access to and use of the Service is also conditioned on your acceptance of and compliance with our <a href="/privacy-policy/">Privacy Policy</a>, which details our data handling practices.</p>
    </section>

    <section>
      <h2>2. Informational Purposes Only (Not Medical Advice)</h2>
      <p>The calculators, articles, guides, food databases, and all other content provided on this website are strictly for <strong>educational and informational purposes only</strong>. They are not intended as, and should not be construed as, professional medical advice, diagnosis, treatment, or specialized nutritional counseling.</p>
      <p>The mathematical formulas used on this site (such as the Mifflin-St Jeor, Harris-Benedict, or Katch-McArdle equations) are population-based statistical estimates. They cannot account for individual metabolic adaptations, hormonal conditions, medications, or specific diseases. Always consult a qualified physician or registered dietitian before making significant changes to your diet, exercise routine, or caloric intake. By using this site, you explicitly acknowledge these limitations. Please review our full, detailed <a href="/disclaimer/">Medical Disclaimer</a>.</p>
    </section>

    <section>
      <h2>3. Intellectual Property Rights</h2>
      <p>The Service and its original content, features, software algorithms, UI design, text, graphics, and functionality are and will remain the exclusive property of Calorie Calculator Free and its licensors. The Service is protected by copyright, trademark, and other intellectual property laws of both the United States and foreign countries.</p>
      <p><strong>Prohibited Actions:</strong> You may not systematically extract, reproduce, scrape, reverse-engineer, or commercially exploit our calculators, source code, or database without express written permission. Specifically, the use of automated bots, spiders, or scrapers to harvest data from our <a href="/foods/">Programmatic Food Database</a> or calculators for use in a competing application is strictly prohibited and will result in IP blocking and potential legal action.</p>
    </section>

    <section>
      <h2>4. User Responsibilities and Acceptable Use</h2>
      <p>When using our Service, you agree to do so only for lawful purposes. You agree not to:</p>
      <ul>
        <li>Use the Service in any way that violates any applicable national or international law or regulation.</li>
        <li>Attempt to interfere with the proper working of the Service, including attempting to breach our security, overload our infrastructure (e.g., via DDoS attacks), or manipulate our hosting environment.</li>
        <li>Use the site to generate medical diagnoses for third parties or present our estimates as medical fact to clients if you are a fitness professional.</li>
        <li>Inject malicious scripts, spam links, or attempt cross-site scripting via any of our contact forms or potential future commenting systems.</li>
      </ul>
    </section>

    <section>
      <h2>5. Accuracy of Information</h2>
      <p>While we strive to ensure that all equations and nutritional data on our site are accurate and up-to-date, we do not warrant the completeness, reliability, or absolute accuracy of this information. Nutritional science is constantly evolving. The data provided in our <a href="/foods/">Food Database</a> is aggregated from public agricultural and nutritional databases and may contain slight variations compared to specific branded products.</p>
      <p>Any reliance you place on such information is strictly at your own risk. We reserve the right to modify the contents of this site at any time without obligation to update historical data.</p>
    </section>

    <section>
      <h2>6. Limitation of Liability</h2>
      <p>To the maximum extent permitted by applicable law, in no event shall Calorie Calculator Free, nor its directors, employees, partners, agents, suppliers, or affiliates, be liable for any indirect, incidental, special, consequential, or punitive damages, including without limitation, loss of profits, data, use, goodwill, or other intangible losses, resulting from:</p>
      <ul>
        <li>Your access to or use of or inability to access or use the Service.</li>
        <li>Any conduct or content of any third party on the Service.</li>
        <li>Any nutritional, physical, or health outcomes (including weight gain, weight loss, injury, or metabolic issues) resulting from the implementation of the mathematical data provided by our calculators.</li>
        <li>Errors, mistakes, or inaccuracies in the mathematical output.</li>
      </ul>
      <p>We provide the Service on an "AS IS" and "AS AVAILABLE" basis without any warranties, whether express or implied, including the implied warranties of merchantability, fitness for a particular purpose, or non-infringement.</p>
    </section>

    <section>
      <h2>7. Links to Third-Party Web Sites</h2>
      <p>Our Service may contain links to third-party web sites or services that are not owned or controlled by us. We strongly advise you to read the terms and conditions and privacy policies of any third-party web sites or services that you visit. We assume no responsibility for the content, privacy policies, or practices of any third-party sites or services.</p>
    </section>

    <section>
      <h2>8. Governing Law and Dispute Resolution</h2>
      <p>These Terms shall be governed and construed in accordance with the laws of the State of California, United States, without regard to its conflict of law provisions.</p>
      <p>Our failure to enforce any right or provision of these Terms will not be considered a waiver of those rights. If any provision of these Terms is held to be invalid or unenforceable by a court, the remaining provisions of these Terms will remain in effect. These Terms constitute the entire agreement between us regarding our Service, and supersede and replace any prior agreements we might have had between us regarding the Service.</p>
    </section>

    <section>
      <h2>9. Changes to Terms</h2>
      <p>We reserve the right, at our sole discretion, to modify or replace these Terms at any time. If a revision is material, we will try to provide at least 30 days' notice prior to any new terms taking effect. What constitutes a material change will be determined at our sole discretion. By continuing to access or use our Service after those revisions become effective, you agree to be bound by the revised terms.</p>
      <p>If you have questions about these terms, please contact us via our <a href="/contact/">Contact Page</a>.</p>
    </section>
  </div>
</ContentLayout>
"""

write_page("privacy-policy.astro", privacy)
write_page("terms.astro", terms)
print("Expanded kiro calorie terms and privacy")
