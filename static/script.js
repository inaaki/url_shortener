target = document.querySelector('.center .result');
url = document.getElementById('short_url');
target.addEventListener('click', function myFunction() {
  navigator.clipboard.writeText(url.innerText);
  alert('url copied');
});
console.log(target, url)