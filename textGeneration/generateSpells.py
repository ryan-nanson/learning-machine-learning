# -*- coding: utf-8 -*-
"""
Ryan Nanson
Generate Harry Potter Spells.
https://github.com/ryan-nanson/learning-machine-learning/tree/master/textGeneration
"""
from textgenrnn import textgenrnn
import csv
# Read Spells.csv and create lists
with open('Spells.csv') as csvfile:
    spells = []
    spellsreader = csv.reader(csvfile, delimiter=';')
    next(spellsreader, None)  # skip the headers
    for row in spellsreader:
        if not (row[1] == 'Unknown' or row[1] == ''):
            spell = "%s: %s" % (row[1],row[3])
            print(spell)
            spells.append(spell)

# Write to single line text files ready for input to textgenrnn
with open("spells.txt", "w") as output:
    output.write('\n'.join(spells))

# Generate Spells and Effects
spellgen = textgenrnn()
spellgen.train_from_file('spells.txt', num_epochs=1)
generated_spells = spellgen.generate(50, temperature=0.35, return_as_list=True)
