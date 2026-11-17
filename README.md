# Daily Adhkar & Duas — JSON Dataset

A clean, ready-to-use JSON dataset of **29 adhkar (أذكار)** and **114 authentic duas (دعائیں) in 19 topics**, each in **Arabic, English and Urdu** with transliteration and a **hadith or Quran reference**.

> "Remember Me, and I will remember you." — *Surah Al-Baqarah, 2:152*
>
> "Call upon Me; I will respond to you." — *Surah Ghafir, 40:60*

## Used in the Fajr App

This dataset powers the Dhikr and Dua sections of **[Fajr: Prayer Alarm & Adhan](https://play.google.com/store/apps/details?id=com.alifanalytics.fajr_app)**, an Android app by [Alif Analytics](https://play.google.com/store/apps/details?id=com.alifanalytics.fajr_app).

<a href="https://play.google.com/store/apps/details?id=com.alifanalytics.fajr_app">
  <img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" height="60">
</a>

**Companion datasets:**
- [99 Names of Allah (Asma ul Husna) JSON Dataset](https://github.com/anno143/99-Names-of-Allah-Asma-ul-Husna-JSON-Dataset)
- [99 Names of Prophet Muhammad ﷺ JSON Dataset](https://github.com/anno143/99-Names-of-Prophet-Muhammad-JSON-Dataset)

## Features

- **29 adhkar**: tasbih, tahmid, takbir, istighfar, salawat, after-prayer and morning & evening adhkar
- **114 duas** in **19 topics**: sleep, travel, food, prayer, distress, family, health, weather, Quranic duas and more
- Fully vocalized Arabic (with harakat)
- Transliteration for easy reading
- English and **Urdu (اردو)** translations
- When to recite, with recommended counts for adhkar
- Hadith or Quran reference for every entry
- One file per dua topic, plus a combined file with everything
- Plain UTF-8 JSON: Arabic and Urdu text is stored as readable characters

## Files

```
Adhkar.json               # all 29 adhkar
Duas.json                 # all 114 duas + topic index (source of truth)
duas/
  sleep.json              # one file per topic
  travel.json
  ...
scripts/
  split_duas.py           # regenerates duas/*.json from Duas.json
```

## Adhkar

### Data Structure

`Adhkar.json` is a JSON array:

```json
[
  {
    "id": 1,
    "dhikr": "Tasbih",
    "arabic": "سُبْحَانَ اللَّهِ",
    "transliteration": "SubhanAllah",
    "translation_english": "Glory be to Allah",
    "translation_urdu": "اللہ پاک ہے",
    "recommended_count": "33x after prayer / anytime",
    "category": "after_prayer",
    "reference": "Sahih Muslim 597"
  }
]
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Unique ID |
| `dhikr` | string | Common name of the dhikr |
| `arabic` | string | Arabic text, vocalized |
| `transliteration` | string | Latin transliteration |
| `translation_english` | string | English translation |
| `translation_urdu` | string | Urdu translation |
| `recommended_count` | string | How many times and when to recite, with its virtue where reported |
| `category` | string | One of the categories below |
| `reference` | string | Quran or hadith source |

### Categories

| `category` | Meaning | Count |
|---|---|---|
| `general` | Anytime dhikr | 9 |
| `after_prayer` | After the obligatory prayers | 6 |
| `morning_evening` | Morning & evening adhkar | 6 |
| `forgiveness` | Istighfar | 5 |
| `salawat` | Blessings on the Prophet ﷺ | 2 |
| `distress` | In times of worry | 1 |

### Full List

| # | Dhikr | Category |
|---|---|---|
| 1 | Tasbih | `after_prayer` |
| 2 | Tahmid | `after_prayer` |
| 3 | Takbir | `after_prayer` |
| 4 | Tahlil | `general` |
| 5 | Istighfar | `forgiveness` |
| 6 | Hawqalah | `general` |
| 7 | Tasbih wa Bihamdihi | `general` |
| 8 | Hasbunallah | `distress` |
| 9 | Salawat (Short) | `salawat` |
| 10 | Salawat Ibrahimiyyah | `salawat` |
| 11 | Third Kalima (Tamjeed) | `general` |
| 12 | Tahlil (Long/Complete) | `general` |
| 13 | Sayyidul Istighfar (Master Prayer for Forgiveness) | `forgiveness` |
| 14 | Ta'awwudh | `general` |
| 15 | Basmalah | `general` |
| 16 | Kalima Tayyibah (First Kalima) | `general` |
| 17 | Tasbih wa Bihamdihi (Short) | `general` |
| 18 | Tasbih of Juwayriyah | `morning_evening` |
| 19 | Istighfar with Tawbah | `forgiveness` |
| 20 | Istighfar (Complete) | `forgiveness` |
| 21 | Rabbighfir li wa tub 'alayya | `forgiveness` |
| 22 | Hasbiyallahu | `morning_evening` |
| 23 | Raditu Billahi Rabban | `morning_evening` |
| 24 | Bismillahilladhi La Yadurru | `morning_evening` |
| 25 | A'udhu bi Kalimatillah | `morning_evening` |
| 26 | Dua for Well-being | `morning_evening` |
| 27 | Allahumma Antas-Salam | `after_prayer` |
| 28 | Allahumma A'inni | `after_prayer` |
| 29 | Ayat al-Kursi | `after_prayer` |

## Duas

### Topics

| `topic` | English | اردو | Duas | File |
|---|---|---|---|---|
| `sleep` | Sleeping & Waking | سونا اور جاگنا | 5 | [`duas/sleep.json`](duas/sleep.json) |
| `home` | Home | گھر | 3 | [`duas/home.json`](duas/home.json) |
| `toilet` | Toilet | بیت الخلاء | 2 | [`duas/toilet.json`](duas/toilet.json) |
| `wudu` | Wudu (Ablution) | وضو | 3 | [`duas/wudu.json`](duas/wudu.json) |
| `mosque_prayer` | Mosque & Prayer | مسجد اور نماز | 11 | [`duas/mosque_prayer.json`](duas/mosque_prayer.json) |
| `food_drink` | Food & Drink | کھانا پینا | 6 | [`duas/food_drink.json`](duas/food_drink.json) |
| `clothing` | Clothing | لباس | 2 | [`duas/clothing.json`](duas/clothing.json) |
| `travel` | Travel | سفر | 5 | [`duas/travel.json`](duas/travel.json) |
| `distress` | Distress, Anxiety & Debt | پریشانی، غم اور قرض | 10 | [`duas/distress.json`](duas/distress.json) |
| `forgiveness` | Forgiveness | مغفرت | 5 | [`duas/forgiveness.json`](duas/forgiveness.json) |
| `guidance_knowledge` | Guidance, Knowledge & Decisions | ہدایت، علم اور فیصلے | 10 | [`duas/guidance_knowledge.json`](duas/guidance_knowledge.json) |
| `family` | Parents, Family & Children | والدین، اہل و عیال اور اولاد | 8 | [`duas/family.json`](duas/family.json) |
| `health` | Sickness & Health | بیماری اور صحت | 6 | [`duas/health.json`](duas/health.json) |
| `weather` | Rain, Wind & Nature | بارش، ہوا اور موسم | 6 | [`duas/weather.json`](duas/weather.json) |
| `fasting` | Fasting & Ramadan | روزہ اور رمضان | 3 | [`duas/fasting.json`](duas/fasting.json) |
| `protection` | Protection | حفاظت | 5 | [`duas/protection.json`](duas/protection.json) |
| `social` | Social Etiquette | معاشرتی آداب | 9 | [`duas/social.json`](duas/social.json) |
| `death` | Death, Funeral & Graves | موت، جنازہ اور قبرستان | 3 | [`duas/death.json`](duas/death.json) |
| `quranic` | Quranic Duas (Rabbana) | قرآنی دعائیں (ربنا) | 12 | [`duas/quranic.json`](duas/quranic.json) |

### Data Structure

Each file in `duas/` holds one topic:

```json
{
  "topic": "travel",
  "title_en": "Travel",
  "title_ur": "سفر",
  "count": 5,
  "duas": [
    {
      "id": 33,
      "topic": "travel",
      "title": "Riding a Vehicle",
      "arabic": "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَٰذَا ...",
      "transliteration": "Subhanal-ladhi sakhkhara lana hadha ...",
      "translation_english": "Glory be to the One who has subjected this to us ...",
      "translation_urdu": "پاک ہے وہ ذات جس نے اسے ہمارے قابو میں کر دیا ...",
      "when": "When riding a car, plane or any vehicle",
      "reference": "Quran 43:13-14; Sunan Abi Dawud 2602"
    }
  ]
}
```

`Duas.json` contains every dua in one `duas` array, plus a `topics` index (`topic`, `title_en`, `title_ur`, `file`, `count`) for building menus.

| Field | Type | Description |
|---|---|---|
| `id` | int | Unique ID across all topics |
| `topic` | string | Topic key (matches the file name) |
| `title` | string | Short English title of the dua |
| `arabic` | string | Arabic text, vocalized |
| `transliteration` | string | Latin transliteration |
| `translation_english` | string | English translation |
| `translation_urdu` | string | Urdu translation |
| `when` | string | When or how to recite it |
| `reference` | string | Quran or hadith source |

## Usage

Direct links to the raw files:

```
https://raw.githubusercontent.com/anno143/Daily-Dhikr-Adhkar-JSON-Dataset/main/Adhkar.json
https://raw.githubusercontent.com/anno143/Daily-Dhikr-Adhkar-JSON-Dataset/main/Duas.json
https://raw.githubusercontent.com/anno143/Daily-Dhikr-Adhkar-JSON-Dataset/main/duas/travel.json
```

**JavaScript**

```js
const base = "https://raw.githubusercontent.com/anno143/Daily-Dhikr-Adhkar-JSON-Dataset/main";

// All adhkar for after prayer
const adhkar = await (await fetch(`${base}/Adhkar.json`)).json();
const afterPrayer = adhkar.filter(d => d.category === "after_prayer");

// One dua topic
const travel = await (await fetch(`${base}/duas/travel.json`)).json();
console.log(travel.title_ur, travel.duas[0].arabic);
```

**Python**

```python
import json

with open("Duas.json", encoding="utf-8") as f:
    data = json.load(f)

for t in data["topics"]:
    print(t["title_en"], "-", t["title_ur"], f"({t['count']})")

sleep = [d for d in data["duas"] if d["topic"] == "sleep"]
print(sleep[0]["translation_urdu"])
```

**Dart / Flutter**

```dart
final jsonStr = await rootBundle.loadString('assets/duas/food_drink.json');
final topic = json.decode(jsonStr);
print(topic['title_ur']);
for (final d in topic['duas']) {
  print(d['arabic']);
}
```

> Tip: Urdu and Arabic are right-to-left. Render them with RTL text direction and a font that supports Arabic script (e.g. Noto Nastaliq Urdu, Noto Naskh Arabic, Amiri). Quranic duas include pause marks (ۚ ۖ ۗ), so use a font that supports them.

## About the References

References use the common numbering on [sunnah.com](https://sunnah.com) for hadith and surah:ayah for the Quran. The virtues mentioned in `recommended_count` and `when` are short summaries of what the referenced hadith reports. Some narrations (e.g. in Abu Dawud, Tirmidhi and Ibn Majah) are graded differently by different scholars; check the reference if you need the grading.

## Contributing

Corrections and additions are welcome. Please open an issue or a pull request with the `id`, the field, and a source for the change.

To add or edit a dua, change `Duas.json` only, then run:

```bash
python scripts/split_duas.py
```

This regenerates every file in `duas/` so the per-topic files always match `Duas.json`.

## Credits

Compiled by [Alif Analytics](https://play.google.com/store/apps/details?id=com.alifanalytics.fajr_app).

## License

Free to use in personal and commercial projects. Please keep a link back to this repository.
