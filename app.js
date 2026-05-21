const btn = document.getElementById('btnSubmit');
if (btn) btn.addEventListener('click', e => { e.preventDefault(); document.querySelector('form')?.submit(); });