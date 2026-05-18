// Simple JS - just for theme toggle
// Saves choice in localStorage so it stays after refresh

document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('themeBtn');

  // Load saved theme
  if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark');
    if (btn) btn.textContent = '☀️';
  }

  if (btn) {
    btn.addEventListener('click', function () {
      document.body.classList.toggle('dark');
      const isDark = document.body.classList.contains('dark');
      btn.textContent = isDark ? '☀️' : '🌙';
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
  }
});
