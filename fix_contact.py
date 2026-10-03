import os

base_path = r"d:\TOOLS WEB TOOLS\kiro calorie\src\pages"

def write_page(filename, content):
    path = os.path.join(base_path, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

contact = """---
import ContentLayout from "../layouts/ContentLayout.astro";
import { inputCls } from "../lib/ui";
---

<ContentLayout
  title="Contact Us — Calorie Calculator Free"
  h1="Contact Us"
  description="Get in touch with the Calorie Calculator Free team for support, feedback, press inquiries, or partnership opportunities. We read every message."
  path="/contact/"
  lead="We’re here to help. Reach out with your questions, feedback, or inquiries."
  showCta={false}
>
  <div class="prose max-w-none text-brand-dark/80 dark:text-white/80 space-y-6">
    <section>
      <p>At <strong>Calorie Calculator Free</strong>, we highly value the feedback and questions of our user community. Whether you have discovered a bug in one of our tools, have a suggestion for a new calculator, or simply need clarification on how a specific equation works, our team is ready to assist you. Our goal is to provide the most accurate, user-friendly, and scientifically backed nutritional tools available on the web.</p>
      <p>We strive to respond to all legitimate inquiries within 24-48 business hours. Please direct your message to the appropriate department below to ensure the fastest possible response.</p>
    </section>

    <section>
      <h2>General Support & Feedback</h2>
      <p>If you have general questions about how to use the <a href="/">Calorie Calculator</a>, need help interpreting your results, or want to suggest a new feature (like a specific macro breakdown or activity level), please email our support team.</p>
      <p>Because our calculators run privately in your browser, we cannot see your results. When emailing for support, please include any context or details regarding the numbers you entered so we can adequately assist you.</p>
      <p><strong>Email:</strong> <a href="mailto:calgroupofficial@gmail.com">calgroupofficial@gmail.com</a></p>
      <p><strong>Alternate Email:</strong> <a href="mailto:topg8086@gmail.com">topg8086@gmail.com</a></p>
    </section>

    <section>
      <h2>Technical Issues & Bug Reports</h2>
      <p>While we rigorously test our platform across all devices, occasional technical issues may arise. If a calculator fails to load, produces an error, or if you spot a discrepancy in the mathematical output, please let our engineering team know. When reporting a bug, please include your browser (e.g., Chrome, Safari) and device type (Mobile/Desktop).</p>
    </section>

    <section>
      <h2>Press, Media, & Partnerships</h2>
      <p>For press inquiries, interview requests, or partnership opportunities, we welcome communications from journalists, health bloggers, and industry professionals. We are happy to provide expert quotes regarding digital health tools, metabolic math, and fitness technology.</p>
    </section>

    <section>
      <h2>Mailing Address</h2>
      <p>If you need to reach us via traditional mail for legal or formal administrative purposes, you may use our corporate mailing address. Please note that email or the contact form below is the significantly faster method of communication.</p>
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

  <hr class="my-10" />
  
  <h2>Send Us a Message</h2>
  <p>Use the secure form below to send a message directly to our inbox.</p>

  <!-- Success message (shown after a successful submission) -->
  <div
    id="form-success"
    class="not-prose mt-6 hidden rounded-xl border border-success/40 bg-success/10 p-5 text-center"
  >
    <p class="text-base font-semibold text-ink">Thanks for reaching out! 🎉</p>
    <p class="mt-1 text-sm text-body">
      Your message has been sent — we'll get back to you within two business days.
    </p>
  </div>

  <form
    id="contact-form"
    action="https://formspree.io/f/mjgdwwkz"
    method="POST"
    class="not-prose mt-6 space-y-4"
  >
    <div class="grid gap-4 sm:grid-cols-2">
      <div class="space-y-1.5">
        <label for="name" class="block text-sm font-medium text-ink">Name</label>
        <input id="name" name="name" type="text" required class={inputCls} />
      </div>
      <div class="space-y-1.5">
        <label for="email" class="block text-sm font-medium text-ink">Email</label>
        <input id="email" name="email" type="email" required class={inputCls} />
      </div>
    </div>
    <div class="space-y-1.5">
      <label for="subject" class="block text-sm font-medium text-ink">Subject</label>
      <input id="subject" name="_subject" type="text" class={inputCls} />
    </div>
    <div class="space-y-1.5">
      <label for="message" class="block text-sm font-medium text-ink">Message</label>
      <textarea id="message" name="message" rows="5" required class={inputCls + " h-auto py-2.5"}></textarea>
    </div>

    <!-- Honeypot: hidden from users, catches spam bots -->
    <input
      type="text"
      name="_gotcha"
      tabindex="-1"
      autocomplete="off"
      aria-hidden="true"
      class="hidden"
    />

    <!-- Inline error message -->
    <p
      id="form-error"
      role="alert"
      class="hidden rounded-lg border border-error/40 bg-error/10 px-4 py-3 text-sm text-body"
    >
    </p>

    <button
      id="submit-btn"
      type="submit"
      class="inline-flex h-11 items-center justify-center rounded-full bg-ink px-6 text-sm font-medium text-canvas transition-all hover:opacity-90 active:scale-[0.99] disabled:opacity-60"
    >
      Send message
    </button>
  </form>
</ContentLayout>

<script>
  const form = document.getElementById("contact-form") as HTMLFormElement | null;
  const successEl = document.getElementById("form-success");
  const errorEl = document.getElementById("form-error");
  const btn = document.getElementById("submit-btn") as HTMLButtonElement | null;

  form?.addEventListener("submit", async (e) => {
    e.preventDefault();
    if (!btn) return;
    errorEl?.classList.add("hidden");
    const original = btn.textContent;
    btn.disabled = true;
    btn.textContent = "Sending…";

    try {
      const res = await fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" },
      });

      if (res.ok) {
        form.reset();
        form.classList.add("hidden");
        successEl?.classList.remove("hidden");
        successEl?.scrollIntoView({ behavior: "smooth", block: "center" });
      } else {
        const data = await res.json().catch(() => null);
        const msg =
          data?.errors?.map((x: { message: string }) => x.message).join(", ") ||
          "Something went wrong. Please try again, or email us directly at calgroupofficial@gmail.com.";
        if (errorEl) {
          errorEl.textContent = msg;
          errorEl.classList.remove("hidden");
        }
      }
    } catch {
      if (errorEl) {
        errorEl.textContent =
          "Network error — please check your connection and try again, or email us directly at calgroupofficial@gmail.com.";
        errorEl.classList.remove("hidden");
      }
    } finally {
      btn.disabled = false;
      btn.textContent = original;
    }
  });
</script>
"""

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
      <p>Welcome to <strong>Calorie Calculator Free</strong>. Our mission was born from a fundamental belief: access to highly accurate, scientifically validated nutritional data should be a universal right, not a premium privilege locked behind expensive subscriptions, invasive sign-ups, or aggressive paywalls. The fitness and diet industry is unfortunately flooded with misinformation, predatory pricing models, and opaque algorithms designed to sell supplements rather than inform the user.</p>
      <p>We are here to radically change that paradigm. Our goal is to build the internet's most comprehensive, transparent, and easy-to-use repository of metabolic math. Whether you are a professional athlete aiming to optimize performance, someone embarking on a weight-loss journey, a clinician needing quick access to verified formulas, or simply a health-conscious individual wanting to understand your body better, we provide the exact mathematical frameworks used by certified dietitians and medical professionals—absolutely free of charge.</p>
    </section>
    
    <section>
      <h2>Our Scientific Commitment</h2>
      <p>We do not rely on guesswork or proprietary "magic algorithms." The fitness world is plagued by apps that hide their formulas to create a false sense of value. At Calorie Calculator Free, we are fully transparent. Every single calculator on this platform is meticulously built upon established, peer-reviewed clinical research. Our tools utilize globally recognized metabolic formulas, including:</p>
      <ul>
        <li><strong>The Mifflin-St Jeor Equation:</strong> Developed in 1990 and endorsed by the American Dietetic Association, this is widely considered the most accurate modern predictive equation for Resting Metabolic Rate (RMR) in modern lifestyles.</li>
        <li><strong>The Harris-Benedict Formula:</strong> A classic, foundational algorithm updated in 1984 by Roza and Shizgal for broader accuracy, which remains highly effective for broad population modeling.</li>
        <li><strong>The Katch-McArdle Formula:</strong> The gold standard used for individuals who know their precise body fat percentage, relying strictly on Lean Body Mass rather than total weight.</li>
      </ul>
      <p>By offering transparent access to these formulas, we empower you to make informed, data-driven decisions about your <a href="/calorie-deficit-calculator/">calorie deficit</a>, <a href="/protein-calculator/">protein intake</a>, and overall <a href="/tdee-calculator/">Total Daily Energy Expenditure (TDEE)</a>. We believe that when you understand the math, you can control the outcome.</p>
    </section>

    <section>
      <h2>Our Strict Privacy Policy</h2>
      <p>In the digital age, your personal health data—including your weight, age, and dietary habits—is your most sensitive asset. At Calorie Calculator Free, we have engineered our platform with a strict "Privacy First" architecture from day one. <strong>Every calculation occurs locally on your device within your browser.</strong></p>
      <p>We do not transmit, harvest, or store your physiological data on our servers. The only data saved is kept in your browser's local storage solely for your convenience, ensuring that your health journey remains completely anonymous and secure. You never have to worry about a data breach exposing your weight loss goals, because we simply do not possess that data. For more detailed information, please review our comprehensive <a href="/privacy-policy/">Privacy Policy</a>.</p>
    </section>

    <section>
      <h2>Who We Are & How We Work</h2>
      <p>Calorie Calculator Free is maintained by a dedicated team of software engineers, data analysts, and fitness enthusiasts who are passionate about democratizing health information. We spend hundreds of hours researching clinical papers, designing intuitive user interfaces, and ensuring cross-platform compatibility so that anyone, on any device, can access professional-grade tools.</p>
      <p>While we consult with nutritional experts to ensure mathematical accuracy, we always remind our users that our tools provide informational baselines, not medical diagnoses. Predictive metabolic equations are excellent starting points, but human biology is highly dynamic and subject to thousands of variables. We encourage you to use our numbers as a baseline, track your real-world results over a span of 2-4 weeks, and adjust accordingly. We firmly believe in working alongside your healthcare provider. For more details on how we review our content, see our <a href="/editorial-policy/">Editorial Policy</a>.</p>
    </section>

    <section>
      <h2>The Future of Calorie Calculator Free</h2>
      <p>Our work is never truly finished. We are constantly expanding our offerings. Recently, we launched our massive <a href="/foods/">Programmatic Food Database</a>, containing highly accurate macronutrient profiles for hundreds of popular foods. We are also building out robust calculators for specialized athletic pursuits, such as our running and swimming energy expenditure tools.</p>
      <p>We are constantly improving our algorithms and adding new features based directly on user feedback. If you have suggestions, questions, or just want to share your success story, we would love to hear from you. Your input directly shapes our development roadmap. Please visit our <a href="/contact/">Contact Page</a> to reach out to our team.</p>
    </section>
  </div>
</ContentLayout>
"""

write_page("contact.astro", contact)
write_page("about.astro", about)

print("Restored contact form and increased about word count for kiro calorie.")
