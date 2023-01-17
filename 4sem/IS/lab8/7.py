replace_table = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
    "б": "b", "ю": "ju", "ё": "jo"
}

with open("cyrillic.txt", "r", encoding="utf8") as in_file:
    lines = in_file.readlines()

new_lines = []

for line in lines:
    new_line = ""
    for letter in line:
        if letter.lower() in replace_table:
            if letter.isupper():
                table_letter = replace_table[letter.lower()][0].upper(
                ) + replace_table[letter.lower()][1:]
                new_line += table_letter
            else:
                new_line += replace_table[letter.lower()]
        else:
            new_line += letter
    new_lines.append(new_line)

with open("transliteration.txt", "w", encoding="utf8") as out_file:
    out_file.writelines(line for line in new_lines)
