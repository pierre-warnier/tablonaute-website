#!/usr/bin/env python3
"""Update FAQ in translations.json with corrections and new entries."""

import json
from pathlib import Path

translations_path = Path(__file__).parent / "lang" / "translations.json"
updates_path = Path(__file__).parent / "faq_updates.json"

# Load existing translations
with open(translations_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load updates
with open(updates_path, 'r', encoding='utf-8') as f:
    updates = json.load(f)

# Apply updates for en and fr (the two we have full translations for)
for lang in ['en', 'fr']:
    if lang in updates and lang in data:
        data[lang].update(updates[lang])
        print(f"Updated {lang} with {len(updates[lang])} keys")

# For other languages, just fix the critical errors (14->15 languages, Settings->Home Screen)
other_langs = ['es', 'de', 'it', 'nl', 'pt', 'ru', 'uk', 'pl', 'ja', 'zh', 'ko', 'ar', 'hi']

language_fixes = {
    'es': ('15 idiomas', 'Soporte completo para inglés, francés, español, alemán, italiano, holandés, portugués, ruso, ucraniano, polaco, japonés, chino, coreano, árabe e hindi.'),
    'de': ('15 Sprachen', 'Volle Unterstützung für Englisch, Französisch, Spanisch, Deutsch, Italienisch, Niederländisch, Portugiesisch, Russisch, Ukrainisch, Polnisch, Japanisch, Chinesisch, Koreanisch, Arabisch und Hindi.'),
    'it': ('15 lingue', 'Supporto completo per inglese, francese, spagnolo, tedesco, italiano, olandese, portoghese, russo, ucraino, polacco, giapponese, cinese, coreano, arabo e hindi.'),
    'nl': ('15 talen', 'Volledige ondersteuning voor Engels, Frans, Spaans, Duits, Italiaans, Nederlands, Portugees, Russisch, Oekraïens, Pools, Japans, Chinees, Koreaans, Arabisch en Hindi.'),
    'pt': ('15 idiomas', 'Suporte completo para inglês, francês, espanhol, alemão, italiano, holandês, português, russo, ucraniano, polonês, japonês, chinês, coreano, árabe e hindi.'),
    'ru': ('15 языков', 'Полная поддержка английского, французского, испанского, немецкого, итальянского, нидерландского, португальского, русского, украинского, польского, японского, китайского, корейского, арабского и хинди.'),
    'uk': ('15 мов', 'Повна підтримка англійської, французької, іспанської, німецької, італійської, нідерландської, португальської, російської, української, польської, японської, китайської, корейської, арабської та гінді.'),
    'pl': ('15 języków', 'Pełne wsparcie dla angielskiego, francuskiego, hiszpańskiego, niemieckiego, włoskiego, niderlandzkiego, portugalskiego, rosyjskiego, ukraińskiego, polskiego, japońskiego, chińskiego, koreańskiego, arabskiego i hindi.'),
    'ja': ('15言語', '英語、フランス語、スペイン語、ドイツ語、イタリア語、オランダ語、ポルトガル語、ロシア語、ウクライナ語、ポーランド語、日本語、中国語、韓国語、アラビア語、ヒンディー語に完全対応。'),
    'zh': ('15种语言', '全面支持英语、法语、西班牙语、德语、意大利语、荷兰语、葡萄牙语、俄语、乌克兰语、波兰语、日语、中文、韩语、阿拉伯语和印地语。'),
    'ko': ('15개 언어', '영어, 프랑스어, 스페인어, 독일어, 이탈리아어, 네덜란드어, 포르투갈어, 러시아어, 우크라이나어, 폴란드어, 일본어, 중국어, 한국어, 아랍어, 힌디어 완벽 지원.'),
    'ar': ('15 لغة', 'دعم كامل للإنجليزية والفرنسية والإسبانية والألمانية والإيطالية والهولندية والبرتغالية والروسية والأوكرانية والبولندية واليابانية والصينية والكورية والعربية والهندية.'),
    'hi': ('15 भाषाएं', 'अंग्रेज़ी, फ़्रेंच, स्पेनिश, जर्मन, इतालवी, डच, पुर्तगाली, रूसी, यूक्रेनी, पोलिश, जापानी, चीनी, कोरियाई, अरबी और हिंदी के लिए पूर्ण समर्थन।'),
}

for lang in other_langs:
    if lang in data and lang in language_fixes:
        data[lang]['languages'] = language_fixes[lang][0]
        data[lang]['languages_desc'] = language_fixes[lang][1]
        print(f"Fixed language count for {lang}")

# Save updated translations
with open(translations_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nSaved to {translations_path}")
