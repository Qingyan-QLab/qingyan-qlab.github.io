(() => {
  'use strict';
  const languageButton = document.getElementById('language');
  const titles = {zh:'Q-lab · 理解世界，与人共生',en:'Q-lab · Understand the world. Live alongside us.'};
  const descriptions = {zh:'Q-lab 聚焦 AI 基础研究，探索几何、物理世界、具身智能、永续学习与心智模型，走向无缝融入人类社会的机器人。',en:'Q-lab pursues fundamental AI research in geometry, physics, embodiment, continual learning, and mental models, toward robots that integrate seamlessly into human society.'};
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
    document.title = titles[language];
    document.querySelector('meta[name="description"]').content = descriptions[language];
    document.querySelector('meta[property="og:title"]').content = titles[language];
    document.querySelector('meta[property="og:description"]').content = descriptions[language];
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

  const tabs = [...document.querySelectorAll('[role="tab"]')];
  function selectTab(tab, focus = false) {
    tabs.forEach(candidate => {
      const selected = candidate === tab;
      candidate.setAttribute('aria-selected', String(selected));
      candidate.tabIndex = selected ? 0 : -1;
      document.getElementById(candidate.getAttribute('aria-controls')).hidden = !selected;
      document.querySelector(`[data-diagram="${candidate.dataset.topic}"]`).classList.toggle('active', selected);
    });
    if (focus) tab.focus();
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectTab(tab));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) { event.preventDefault(); selectTab(tabs[next], true); }
    });
  });
})();
