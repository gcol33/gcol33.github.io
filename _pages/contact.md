---
layout: default
title: "Contact"
permalink: /contact/
breadcrumb:
  - name: "Home"
    url: "/"
  - name: "Contact"
---

<div class="bloc l-bloc" id="bloc-6">
  <div class="container bloc-sm">
    <div class="row">
      <div class="text-start col-12">
        {% include breadcrumb.html items=page.breadcrumb %}
      </div>
    </div>
  </div>
</div>

<div class="bloc l-bloc background-blocs" id="bloc-7">
  <div class="container bloc-sm bloc-md-md bloc-md-lg">
    <div class="row">
      <div class="text-start col-lg-8 col-md-10">
        <h1 class="mb-4">Contact</h1>
        <p class="mb-4">If you'd like to get in touch with me for research-related inquiries, feel free to reach out via email. I'm open to discussing topics related to my work, collaborations, or any relevant questions you might have.</p>

        <form id="contact-form" action="https://api.submitjson.com/v1/submit/FnybrlFC2" method="POST">
          <div class="form-group mb-3">
            <label class="form-label" for="name">Name</label>
            <input id="name" class="form-control" required name="name">
          </div>
          <div class="form-group mb-3">
            <label class="form-label" for="email">Email</label>
            <input id="email" class="form-control" type="email" required name="email">
          </div>
          <div class="form-group mb-3">
            <label class="form-label" for="message">Message</label>
            <textarea id="message" class="form-control" rows="4" required name="message"></textarea>
          </div>
          <div class="form-check mb-3">
            <input class="form-check-input" type="checkbox" id="optin" required name="optin">
            <label class="form-check-label" for="optin">I'm not a robot.</label>
          </div>
          <button class="btn btn-lg btn-d button-01" type="submit">Submit</button>
        </form>
      </div>
    </div>
  </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contact-form");
  const RATE_LIMIT_KEY = "contact_submissions";
  const MAX_SUBMISSIONS = 10;
  const WINDOW_MS = 60 * 60 * 1000; // 1 hour

  function getSubmissions() {
    try {
      const data = JSON.parse(localStorage.getItem(RATE_LIMIT_KEY) || "[]");
      const now = Date.now();
      return data.filter(t => now - t < WINDOW_MS);
    } catch { return []; }
  }

  function recordSubmission() {
    const submissions = getSubmissions();
    submissions.push(Date.now());
    localStorage.setItem(RATE_LIMIT_KEY, JSON.stringify(submissions));
  }

  function isRateLimited() {
    return getSubmissions().length >= MAX_SUBMISSIONS;
  }

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    if (isRateLimited()) {
      alert("Too many submissions. Please try again later.");
      return;
    }

    const formData = new FormData(this);
    const fields = ['name', 'email', 'message'];

    for (let field of fields) {
      if (!formData.get(field)) {
        alert(`Please fill out the ${field} field.`);
        return;
      }
    }

    const jsonObject = { data: Object.fromEntries(formData.entries()) };

    try {
      const response = await fetch("https://api.submitjson.com/v1/submit/FnybrlFC2", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-API-Key": "{{ site.submitjson_api_key }}"
        },
        body: JSON.stringify(jsonObject)
      });

      const result = await response.json();

      if (response.ok) {
        recordSubmission();
        alert("Form submitted successfully!");
        form.reset();
      } else {
        alert("Submission failed: " + JSON.stringify(result));
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Error submitting form: " + error.message);
    }
  });
});
</script>

<noscript>
  <p style="color:red;">
    JavaScript is disabled in your browser. Please enable JavaScript to use the contact form, or email me directly at <a href="mailto:gilles.colling@univie.ac.at">gilles.colling@univie.ac.at</a>.
  </p>
</noscript>
