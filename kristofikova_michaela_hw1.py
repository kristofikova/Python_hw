import json

with open("alice.txt", mode="r", encoding="utf-8") as hw01_output:
    text = hw01_output.read()

cleaned_text = text.replace(' ','').replace('\n','')

text_characters = cleaned_text.lower()

character_frequency = {}

for character in text_characters:
    if character in character_frequency:
        character_frequency[character] += 1
    else:
        character_frequency[character] = 1

output_data = character_frequency

with open("hw1_output.json", mode="w", encoding="utf-8") as json_file:
    json.dump(output_data, json_file, ensure_ascii=False, indent=4, sort_keys=True)
