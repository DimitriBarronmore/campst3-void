scoreboard players set * inVoid 0
scoreboard players set @a inVoid 0
execute @e[type=armor_stand,name=beanCounter] ~ ~ ~ /scoreboard players set @e[type=Player,rm=1] inVoid 1
tpj @e[type=Player,score_inVoid=0] 0
spreadplayers 0 0 5 70 false @e[type=Player,score_inVoid=0]
scoreboard players set @e[type=Player,score_inVoid=0] inVoid 1
function cs3:reset
