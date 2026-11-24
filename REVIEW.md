# Content Review: Translations, Arabic Text and References

A full pass over all 29 adhkar and 114 duas: Arabic text, transliteration, English and Urdu translations, recitation notes and references. Hadith numbers follow sunnah.com; Quran references use surah:ayah.

## Fixed

### Arabic text

| Entry | Problem | Fix |
|---|---|---|
| Adhkar 13 (Sayyid al-Istighfar) | Missing `لَكَ` in the second phrase. Bukhari 6306 reads `وَأَبُوءُ لَكَ بِذَنْبِي` | Added `لَكَ` to the Arabic and transliteration |
| Adhkar 11 (Third Kalima) | Different vocalization from the rest of the file (`اللهِ`, `للهِ`, `إِلَهَ`) | Standardised to `اللَّهِ`, `لِلَّهِ`, `إِلَٰهَ` |
| Dua 28 (After eating) | `حَمْدًا` is not in Bukhari 5458, which reads `الْحَمْدُ لِلَّهِ كَثِيرًا طَيِّبًا…` | Removed it |
| Dua 8 (Entering the home) | The opening of the narration, `اللَّهُمَّ إِنِّي أَسْأَلُكَ خَيْرَ الْمَوْلِجِ وَخَيْرَ الْمَخْرَجِ`, was missing | Added in all four text fields |
| Dua 97 (Mirror) | The wording didn't match the cited source. Ahmad 3823 reads `اللَّهُمَّ أَحْسَنْتَ خَلْقِي فَأَحْسِنْ خُلُقِي` | Changed to match the source |
| Duas 52, 53, 63, 89, 111 | Began with `رَّبِّ` / `رَّبَّنَا`. The shadda only exists in the Mushaf because of the word before it (e.g. `وَقُل رَّبِّ`). A dua read on its own starts with `رَبِّ` | Removed the leading shadda |

### English

| Entry | Problem | Fix |
|---|---|---|
| Dua 76 | Diseases mistranslated: *baras* (برص) is vitiligo/leucoderma, not leprosy, and *judham* (جذام) is leprosy, not elephantiasis | "vitiligo (baras), madness, leprosy (judham)…" |
| Adhkar 13 | "my covenant and my promise to You". The Arabic `عَهْدِكَ وَوَعْدِكَ` means **Your** covenant and promise | "I abide by Your covenant and Your promise" |
| Dua 28 | "which cannot be sufficed, nor bid farewell to" didn't make sense in English | Rewritten |

### Urdu

| Entry | Problem | Fix |
|---|---|---|
| Dua 41 | `عاجزی` means humility (a virtue) in Urdu, but `العجز` here means helplessness/incapacity | `بے بسی` |
| Dua 88 | `ہم تجھے ان کے مقابلے میں کرتے ہیں` is not a complete Urdu sentence | `ہم تجھے ان کے مقابلے میں (ڈھال) بناتے ہیں` |
| Dua 45 | `مجھے… کافی ہو جا` is awkward Urdu | `…بچا کر کفایت فرما` |
| Adhkar 7 | Word order was awkward: `اللہ عظمت والا پاک ہے` | `پاک ہے اللہ اپنی تعریف کے ساتھ، پاک ہے اللہ عظمت والا` |
| Dua 34 | `بے شک` (for `إِنَّا`) was missing, though Dua 33 (same verse) has it | Added |
| Dua 47 | `میں ہی` adds an emphasis that isn't in the Arabic | Removed `ہی` |
| Dua 65 | `بیویوں` narrows `أَزْوَاجِنَا` (spouses) to "wives". The English says "spouses" | `جیون ساتھیوں` |
| Dua 72 | `تجھے` is used to address Allah, but this line is said **to a sick person** | `تمہیں` |

### Recitation notes and virtues

| Entry | Problem | Fix |
|---|---|---|
| Adhkar 4 (Tahlil) | "100x daily" isn't in Tirmidhi 3383. The 100x virtue belongs to the long tahlil (Adhkar 12) | "Anytime (the best dhikr)" |
| Adhkar 13 | "Guarantees Paradise" overstated the hadith | Now says what the hadith says: whoever says it with conviction and dies that day or night is among the people of Paradise |
| Adhkar 20 | "3x" isn't in Abu Dawud 1517 or Tirmidhi 3577 | Replaced with the reported virtue |
| Dua 97 | The mirror context comes only from a weaker narration (Ahmad 3823 has no mirror) | Noted in `when` |
| Dua 101 | `فَلْتَصْبِرْ وَلْتَحْتَسِبْ` is third person ("let her be patient"), because it was a message to the Prophet's ﷺ daughter | Noted in `when` how to say it directly |

## References added

| Entry | Added |
|---|---|
| Adhkar 3 | Sahih Muslim 596 (the 34x takbir after prayer, which 597 doesn't cover) |
| Adhkar 9 | Sunan Abi Dawud 1047 (Friday); at-Tabarani for 10x morning/evening (grading disputed) |
| Adhkar 11 | Sunan Abi Dawud 832 (all five phrases together) |
| Adhkar 21 | Note that Tirmidhi's wording ends *at-Tawwabul-Ghafur* |
| Dua 8 | Grading note: weak chain (al-Albani) |
| Dua 14 | Sahih al-Bukhari 426 (preferring the right) |
| Dua 17 | Sahih Muslim 399 |
| Duas 18, 20 | Sunan Abi Dawud 886, Jami' at-Tirmidhi 261 (source of "3x") |
| Dua 90 | Sunan Ibn Majah 3509 (invoking blessing against the evil eye; the title mentions it but only a Quran verse was cited) |
| Dua 97 | Sahih Ibn Hibban 959 |
| Dua 101 | Sahih Muslim 923 |

All other references were checked and match their entries.

## Not changed (owner's decision)

1. **Transliteration is inconsistent for ظ.** Sometimes it's `dh` (*'Adheem*, *hifdhuhuma*), which is also the spelling for ذ (*dhikr*, *dhanbi*). Elsewhere it's `z` (*zalamtu*, *zalimin*, *manzar*). Choose one scheme, for example `z` or `ẓ` for ظ, and apply it everywhere.
2. **Counts inside the text fields.** Dua 74 has `(ثَلَاثًا)` / `(سَبْعًا)` in the Arabic field, and Dua 34 has `(3 بار)` / `(3x)` in its translations. Apps that show the Arabic as recitable text would display these notes. Consider moving them to `when`.
3. **Dua 75** starts with `أَنِّي`, which is the Quran's wording after `إِذْ نَادَىٰ رَبَّهُ`. As a standalone dua it is usually said as `رَبِّ أَنِّي مَسَّنِيَ الضُّرُّ…` or kept as a quotation.
4. **Weak or disputed narrations** (Abu Dawud 5096, the at-Tabarani salawat count, the mirror context) are kept but labelled. Remove them if the app should list only sahih/hasan material.
