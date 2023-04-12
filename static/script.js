target = document.querySelector('.center .result');
url = document.getElementById('short_url');
copy_alert = document.querySelector('.result .copied');
target.addEventListener('click', function myFunction() {
  result = navigator.clipboard.writeText(url.innerText);
  result.then(() => {
    copy_alert.classList.add('show')
    setTimeout(() => {
      copy_alert.classList.remove('show')
    }, 1000);
  });
});
