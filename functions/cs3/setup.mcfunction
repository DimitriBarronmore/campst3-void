summon armor_stand 0 0 0 {CustomName:beanCounter,Invisible:1,Invulnerable:1,NoGravity:1}
scoreboard objectives add DED deathCount
scoreboard objectives add inVoid dummy
setworldspawn 0 64 0
gamerule gameLoopFunction cs3:deathtp
