---
layout: page
title: "Contact"
permalink: /contact/
---

If you'd like to get in touch with me for research-related inquiries, feel free to reach out via email. I'm open to discussing topics related to my work, collaborations, or any relevant questions you might have.

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

<script>
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contact-form");
  form.addEventListener("submit", async function (event) {
    event.preventDefault();
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
          "X-API-Key": "sjk_1a071de23f934b12bfc91b790bc9d7c0"
        },
        body: JSON.stringify(jsonObject)
      });

      const result = await response.json();

      if (response.ok) {
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
    JavaScript is disabled in your browser. Please enable JavaScript to use the contact form.
  </p>
</noscript>
