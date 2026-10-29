(() => {
  'use strict';
  const languageButton = document.getElementById('language');
  let language = 'zh';
  function setLanguage(next, updateURL = false) {
    language = next === 'en' ? 'en' : 'zh';
    document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('[data-zh][data-en]').forEach(element => {
      element.textContent = element.dataset[language].replace(/\\n/g, '\n');
    });
    document.querySelectorAll('[data-zh-aria]').forEach(element => element.setAttribute('aria-label', element.getAttribute(`data-${language}-aria`)));
    document.querySelectorAll('[data-zh-alt]').forEach(element => element.alt = element.getAttribute(`data-${language}-alt`));
    const languageLabels = languageButton.querySelectorAll('span');
    languageLabels[0].classList.toggle('language-active', language === 'zh');
    languageLabels[2].classList.toggle('language-active', language === 'en');
    languageButton.setAttribute('aria-label', language === 'zh' ? 'Switch to English' : '切换至中文');
    document.title = document.body.getAttribute(`data-title-${language}`);
    document.querySelector('meta[name="description"]').content = document.body.getAttribute(`data-description-${language}`);
    document.querySelector('meta[property="og:title"]').content = document.body.getAttribute(`data-title-${language}`);
    document.querySelector('meta[property="og:description"]').content = document.body.getAttribute(`data-description-${language}`);
    try { localStorage.setItem('qlab-language', language); } catch { /* Storage is optional. */ }
    if (updateURL) {
      const url = new URL(window.location.href);
      url.searchParams.set('lang', language);
      history.replaceState(null, '', url);
    }
  }
  const requestedLanguage = new URLSearchParams(location.search).get('lang');
  let savedLanguage;
  try { savedLanguage = localStorage.getItem('qlab-language'); } catch { /* Default to Chinese. */ }
  setLanguage(requestedLanguage || savedLanguage || 'zh');
  languageButton.addEventListener('click', () => setLanguage(language === 'zh' ? 'en' : 'zh', true));

})();
