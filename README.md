# About the Project

Summoners war is mainly a stat based game that is best played by equipting the best gear (runes) on your ally monsters. Of course, not all runes that the player earns are not equal in their stat efficiency, which raises the question for the player as to what runes would bring out the best in their builds. 

This project aims at helping players evaluate their rune quality by giving them a percentage based score on the following parameters:

1. Base Efficiency: Efficiency of a rune within its rarity.
2. Absolute Efficiency: Efficiency of a rune as compared to a legendary (best) rune.

`The parameters above don't account for an extra innate stat that the rune can start out with.`

3. Innate Efficiency: Efficiency of the innate stat (If any)
4. Overall Efficiency: Efficiency of a rune that takes into account both absolute and innate efficiency. This is the best paramter.

# Files

1. Rune_stats.txt: This file contains the maximum roll value table for each stat. This is read as an input file in the python source code.

2. eff_calculator.py: This is the main python source code. This computes the efficiency of the rune and prints out the statistics in percentage format.
