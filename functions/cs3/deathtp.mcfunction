tpj @e[type=Player,score_DED_min=1] 0
spreadplayers 0 0 5 1000 false @e[type=Player,score_DED_min=1]
scoreboard players set @e[type=Player,score_DED_min=1] DED 0
tpj @e[type=Player,score_inVoid=0] 0
spreadplayers 0 0 5 70 false @e[type=Player,score_inVoid=0]
scoreboard players set @e[type=Player,score_inVoid=0] inVoid 1
scoreboard players set @a[tag=!one] inVoid 1
scoreboard players tag @a[tag=!one] add one
