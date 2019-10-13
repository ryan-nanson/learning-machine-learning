# -*- coding: utf-8 -*-
"""
Ryan Nanson

Generate Harry Potter Spells.
"""
from textgenrnn import textgenrnn
import csv
# Read Spells.csv and create lists
with open('Spells.csv') as csvfile:
    spells = []
    effects = []
    spellsreader = csv.reader(csvfile, delimiter=';')
    next(spellsreader, None)  # skip the headers
    for row in spellsreader:
        if not (row[1] == 'Unknown' or row[1] == ''):
            print(row[1])
            spells.append(row[1])
            effects.append(row[3])

# Write to single line text files ready for input to textgenrnn
with open("spells.txt", "w") as output:
    output.write('\n'.join(spells))
    
with open("effects.txt", "w") as output:
    output.write('\n'.join(effects))

# Generate Spells
spellgen = textgenrnn()
spellgen.train_from_file('spells.txt', num_epochs=1)
generated_spells = spellgen.generate(5, return_as_list=True)

# Generate Spell Effects
effectgen = textgenrnn()
effectgen.train_from_file('effects.txt', num_epochs=1)
generated_effects = effectgen.generate(5, return_as_list=True)
