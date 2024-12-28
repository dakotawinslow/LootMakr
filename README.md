# LootMakr
### A device to take the difficulty out of giving RPG players great loot

There are lots of great loot generators out there for creating hordes of treasure to give to DnD players, but they all have 2 fatal flaws: 
- they might give out loot that no one wants
- they are slow to use on the fly

These two issues stem from the same essential issue; namely, loot generators don't know where you are, who you just killed, and who is getting the loot. LootMakr wants to change that. The goal if this project is to design a system that generates good, context-aware treasure caches through an interface that is fast and easy wenough to use in real time at the table.

## Archetecture

LootMaker is, at it's core, a random generator program. It will have a simple text-based interface:

`loot [options]`

Invoking `loot` on it's own should generate a small treasure horde, the kind you might find on the first or second floor of a level-appropriate dungeon. How does it know level-appropriateness? A config file! The config stores party data, including the names, levels, classes, and primary weapons of the player charaacters. This takes most of the work out of loot generation - just set the config once per level-up and you are good to go!

## Loot Generation Algorithm
Party size and level determines a base treasure quota, which is then multiplied by the horde quality (scraps up to Dragon Horde) to determine the overall value of the horde. From there, items are generated one-at-a-time. Hordes of middling size and better are guarnateed to have at least one class-appropriate magic item per player. After each item is generated, its value is deducted from the overall quota until the target for overall value is reached.