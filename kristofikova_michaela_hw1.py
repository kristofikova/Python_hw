import json

with open("alice.txt", mode="r", encoding="utf-8") as hw01_output:
    text = hw01_output.read()

znaky_v_textu = ''.join(znak.lower()
                        for znak in text if znak not in (' ', ('\n')))

serazene_data = sorted(znaky_v_textu)

cetnost_znaku = {}

for znak in serazene_data:
    if znak in cetnost_znaku:
        cetnost_znaku[znak] += 1
    else:
        cetnost_znaku[znak] = 1


vystup_data = {"data": cetnost_znaku}
with open("hw1_output.json", mode="w", encoding="utf-8") as json_file:
    json.dump(vystup_data, json_file, ensure_ascii=False, indent=4)
