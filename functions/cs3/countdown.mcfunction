scoreboard players add @e[type=armor_stand,name=beanCounter] inVoid 1
execute @e[type=armor_stand,name=beanCounter,score_inVoid_min=2,score_inVoid=2] ~ ~ ~ /title @a title "Reset in 3 Minutes"
execute @e[type=armor_stand,name=beanCounter,score_inVoid_min=3,score_inVoid=3] ~ ~ ~ /title @a title "Reset in 2 Minutes"
execute @e[type=armor_stand,name=beanCounter,score_inVoid_min=4,score_inVoid=4] ~ ~ ~ /title @a title "Reset in 1 Minute"
execute @e[type=armor_stand,name=beanCounter,score_inVoid_min=5] ~ ~ ~ /title @a title "RESETTING"
function cs3:tpvoid if @e[type=armor_stand,name=beanCounter,score_inVoid_min=5]
