import pandas as pd

# Data to include in the Excel file
kanji_data = {
    "Kanji": ["遺跡", "古墳", "居住地", "石器", "痕跡", "氷河期", "台地", "周辺", "存在", "火山灰", "太平洋戦争", "発見", "証明", "集中", "安定", "採取", "段丘", "流れ", "石器", "出土"],
    "Hiragana": ["いせき", "こふん", "きょじゅうち", "せっき", "こんせき", "ひょうがき", "だいち", "しゅうへん", "そんざい", "かざんばい", "たいへいようせんそう", "はっけん", "しょうめい", "しゅうちゅう", "あんてい", "さいしゅ", "だんきゅう", "ながれ", "せっき", "しゅつど"]
}

katakana_data = {
    "Katakana": ["ナウマンゾウ", "オオツノジカ", "ニューヨーク", "トウキョウ"],
    "Reading": ["Naumanzou", "Ootsunojika", "Nyuuyooku", "Toukyou"]
}

grammar_data = {
    "Grammar Point": ["がち", "だけが〜ではない", "ば〜ほど", "によって", "〜につれて", "たびに", "ほど", "ように", "さえ", "とともに"],
    "Explanation": [
        "tends to; prone to",
        "not only ~",
        "the more ~, the more ~",
        "depending on; according to",
        "as ~ happens",
        "every time ~ happens",
        "degree to which ~",
        "like; as if",
        "even; so much as",
        "together with; along with"
    ]
}

# Create pandas dataframes
kanji_df = pd.DataFrame(kanji_data)
katakana_df = pd.DataFrame(katakana_data)
grammar_df = pd.DataFrame(grammar_data)

# Write data to Excel file with separate sheets
excel_path = "C:/Users/wowp1/Desktop/git/ufc/language/Japanese/Books/１日１ページ意外と知らない東京すべて365/1_歴史_東京の遺跡/japanese_words_and_grammar_extended.xlsx"
with pd.ExcelWriter(excel_path) as writer:
    kanji_df.to_excel(writer, sheet_name="Kanji & Hiragana", index=False)
    katakana_df.to_excel(writer, sheet_name="Katakana", index=False)
    grammar_df.to_excel(writer, sheet_name="Grammar Points", index=False)

