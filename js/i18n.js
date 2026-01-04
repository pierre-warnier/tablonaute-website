// Tablonaute i18n - Language detection and translation
(function() {
  const SUPPORTED_LANGS = ['en', 'fr', 'es', 'de', 'it', 'nl', 'pt', 'ru', 'uk', 'pl', 'ja', 'zh', 'ko', 'ar', 'hi'];
  const RTL_LANGS = ['ar'];
  let translations = {};
  let currentLang = 'en';

  // Get language - defaults to English unless user selected another
  function detectLanguage() {
    const stored = localStorage.getItem('tablonaute-lang');
    if (stored && SUPPORTED_LANGS.includes(stored)) {
      return stored;
    }
    return 'en';
  }

  // Load translations
  async function loadTranslations() {
    try {
      const response = await fetch('/lang/translations.json');
      translations = await response.json();
      return true;
    } catch (e) {
      console.error('Failed to load translations:', e);
      return false;
    }
  }

  // Get translation
  function t(key) {
    if (translations[currentLang] && translations[currentLang][key]) {
      return translations[currentLang][key];
    }
    if (translations['en'] && translations['en'][key]) {
      return translations['en'][key];
    }
    return key;
  }

  // Apply translations to page
  function applyTranslations() {
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      el.textContent = t(key);
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      el.placeholder = t(key);
    });

    document.querySelectorAll('[data-i18n-title]').forEach(el => {
      const key = el.getAttribute('data-i18n-title');
      el.title = t(key);
    });

    // Update HTML lang and dir attributes
    document.documentElement.lang = currentLang;
    if (RTL_LANGS.includes(currentLang)) {
      document.documentElement.dir = 'rtl';
      document.body.classList.add('rtl');
    } else {
      document.documentElement.dir = 'ltr';
      document.body.classList.remove('rtl');
    }

    // Update page title
    const pageTitle = document.querySelector('title');
    if (pageTitle) {
      const pageName = pageTitle.getAttribute('data-page');
      if (pageName && translations[currentLang]) {
        const titleKey = pageName + '_title';
        if (translations[currentLang][titleKey]) {
          pageTitle.textContent = t(titleKey) + ' - Tablonaute';
        }
      }
    }
  }

  // Set language
  function setLanguage(lang) {
    if (SUPPORTED_LANGS.includes(lang)) {
      currentLang = lang;
      localStorage.setItem('tablonaute-lang', lang);
      applyTranslations();
      updateLanguageSelector();
    }
  }

  // Create language selector
  function createLanguageSelector() {
    const selector = document.getElementById('language-selector');
    if (!selector) return;

    selector.innerHTML = '';

    SUPPORTED_LANGS.forEach(lang => {
      const option = document.createElement('option');
      option.value = lang;
      option.textContent = translations[lang]?.lang_name || lang.toUpperCase();
      if (lang === currentLang) {
        option.selected = true;
      }
      selector.appendChild(option);
    });

    selector.addEventListener('change', (e) => {
      setLanguage(e.target.value);
    });
  }

  function updateLanguageSelector() {
    const selector = document.getElementById('language-selector');
    if (selector) {
      selector.value = currentLang;
    }
  }

  // Initialize
  async function init() {
    await loadTranslations();
    currentLang = detectLanguage();
    applyTranslations();
    createLanguageSelector();
  }

  // Export for global access
  window.i18n = {
    init,
    t,
    setLanguage,
    getCurrentLang: () => currentLang
  };

  // Auto-init when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
