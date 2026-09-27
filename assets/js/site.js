document.addEventListener('DOMContentLoaded', () => {
  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  const nav = document.querySelector('#mainNavigation');
  if (nav && window.bootstrap) {
    nav.querySelectorAll('a.nav-link').forEach((link) => {
      link.addEventListener('click', () => {
        const instance = bootstrap.Collapse.getInstance(nav);
        if (instance && nav.classList.contains('show')) instance.hide();
      });
    });
  }

  const form = document.querySelector('[data-email-form]');
  if (form) {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;

      const destination = form.dataset.destination;
      const data = new FormData(form);
      const subject = `GRAIN website enquiry: ${data.get('topic')}`;
      const body = [
        `Name: ${data.get('name')}`,
        `Organization: ${data.get('organization') || 'Not provided'}`,
        `Reply email: ${data.get('email')}`,
        `Enquiry: ${data.get('topic')}`,
        '',
        String(data.get('message') || ''),
      ].join('\n');

      const feedback = document.querySelector('[data-form-feedback]');
      if (feedback) {
        feedback.textContent = 'Your email app should open with a prepared message. Please review it and press Send there to deliver your enquiry.';
        feedback.classList.add('show');
        feedback.setAttribute('role', 'status');
      }

      window.location.href = `mailto:${destination}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });
  }
});
