import pandas as pd

# Adding Katakana words to the dictionary
data_with_katakana = {
    "Word (Kanji/Katakana)": [
        "遺跡", "都", "奈良", "京都", "大阪", "古墳", "居住地跡", "石器", "氷河期", "三鷹市", "武蔵野台地",
        "関東ローム層", "火山", "堆積", "層", "下末吉ローム", "旧石器時代", "岩宿遺跡", "群馬県", "多摩ニュータウン遺跡",
        "多摩川", "境川", "大栗川", "乞田川", "三沢川", "水源", "ナウマンゾウ", "オオツノジカ", "縄文時代", "海進",
        "弥生時代", "稲作", "荒川", "中川", "微高地", "柴又八幡神社古墳", "石室", "復元", "見学"
    ],
    "Hiragana/Katakana": [
        "いせき", "みやこ", "なら", "きょうと", "おおさか", "こふん", "きょじゅうちあと", "せっき", "ひょうがき", "みたかし", "むさしのだいち",
        "かんとうろーむそう", "かざん", "たいせき", "そう", "しもすえよしろーむ", "きゅうせっきじだい", "いわじゅくいせき", "ぐんまけん", "たまにゅーたうんいせき",
        "たまがわ", "さかいがわ", "おおぐりがわ", "こったがわ", "みさわがわ", "すいげん", "ナウマンゾウ", "オオツノジカ", "じょうもんじだい", "かいしん",
        "やよいじだい", "いなさく", "あらかわ", "なかがわ", "びこうち", "しばまたはちまんじんじゃこふん", "せきしつ", "ふくげん", "けんがく"
    ],
    "Meaning/Grammar": [
        "ruins", "capital city", "Nara (place name)", "Kyoto (place name)", "Osaka (place name)", "ancient tomb", "residential site", "stone tools", "ice age", "Mitaka City", "Musashino Plateau",
        "Kanto Loam Layer", "volcano", "sediment", "layer", "Shimosueyoshi Loam", "Paleolithic era", "Iwajuku Ruins", "Gunma Prefecture", "Tama New Town ruins",
        "Tama River", "Sakai River", "Oguri River", "Kotta River", "Misawa River", "water source", "Naumann Elephant", "Great Antlered Deer", "Jomon period", "transgression (marine)",
        "Yayoi period", "rice cultivation", "Arakawa River", "Nakagawa River", "elevated land", "Shibamata Hachiman Shrine Tumulus", "stone chamber", "restoration", "observation/study"
    ]
}

# Create the DataFrame with Katakana
df_with_katakana = pd.DataFrame(data_with_katakana)

# Save the DataFrame to Excel
excel_file = "C:/Users/wowp1/Desktop/git/ufc/language/Japanese/Books/１日１ページ意外と知らない東京すべて365/1_歴史_東京の遺跡_単語_excel.xlsx";
df_with_katakana.to_excel(excel_file, index=False)


# Load the current Excel file that has Kanji, Katakana, Hiragana, and Grammar information
df = pd.read_excel(excel_file)
print(df)
# Add a new row for Grammar words from the Japanese text
grammar_terms = [
    {'Japanese': '～たり～たりする', 'Kana': '～たり～たりする', 'Meaning/Grammar': 'Used to list examples of actions. Equivalent to "doing things like..." in English.'},
    {'Japanese': '～がちだ', 'Kana': '～がちだ', 'Meaning/Grammar': 'Indicates a tendency to do something. Equivalent to "tend to..." in English.'},
    {'Japanese': '～から', 'Kana': '～から', 'Meaning/Grammar': 'Indicates a reason or cause. Equivalent to "because" in English.'},
    {'Japanese': '～ので', 'Kana': '～ので', 'Meaning/Grammar': 'Indicates a reason or cause in a softer tone. Equivalent to "because" or "since" in English.'},
    {'Japanese': '～ようだ', 'Kana': '～ようだ', 'Meaning/Grammar': 'Used to express conjecture based on appearance. Equivalent to "it seems..." or "it looks like..." in English.'},
    {'Japanese': '～ながら', 'Kana': '～ながら', 'Meaning/Grammar': 'Indicates doing two actions simultaneously. Equivalent to "while..." in English.'},
    {'Japanese': '～にとって', 'Kana': '～にとって', 'Meaning/Grammar': 'Indicates a perspective or point of view. Equivalent to "for (someone)" in English.'},
    {'Japanese': '～とは限らない', 'Kana': '～とはかぎらない', 'Meaning/Grammar': 'Indicates that something is not necessarily true. Equivalent to "not always" or "not necessarily" in English.'},
    {'Japanese': '～ことがある', 'Kana': '～ことがある', 'Meaning/Grammar': 'Indicates that something happens occasionally. Equivalent to "there are times when..." in English.'},
    {'Japanese': '～ばかり', 'Kana': '～ばかり', 'Meaning/Grammar': 'Indicates an abundance of something, often used with negative connotations. Equivalent to "nothing but..." in English.'}
]

# Append grammar terms to the DataFrame
for term in grammar_terms:
    df = df.append(term, ignore_index=True)

# Save the updated DataFrame back to a new Excel file
df.to_excel(excel_file, index=False)
