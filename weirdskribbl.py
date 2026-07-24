import time
import random
# import kagglehub


f = open("Text/filler.txt").read().splitlines()

res = []
for l in f:
    print(l)
    res.append(l)
print(",".join(res))

time.sleep(100)

# str = "AngryCave,Blaze,BlazeHappy,Cave,CaveFaceInTheFace,DisappointedCave,EvilCave,PharaohCave,RealisticCave,SadCave,Thomas,UpsideDownCave,Weathered_Copper_BlocK,Weathered_Copper_BlocK2,Yahya,abduction,advancement,advancement2,aerial_assault_drone,aol,aostralia,assassin,australia,barry,blaze,blueenderman,bruh,cake,camel,camel2,captain_kelrig,captaincoldbeard,cave_spider,celestipede_body,celestipede_head,celestipede_tail,command_block,creeper,chicken,darkhelmet,dennis,diamond_hoe,distortedzombie,dk,drone,ghast,frog,farewell,evoker,enderman,enderghast,enderdragon,elder_guardian,dwarf,gnome,greenenderman,guardian,happy_ghast,happy_ghastling,henry,herobrine,hyso,iron_golem,jeb_nooooo,kneel,laser_blaster,laser_blaster2,lemon_camel,lucas,magmacube,mariowaah,master,mcmovie_sheep,montyshocked,narelle,no,pharaoh,pig,polarbear,pumpkin,rick_astley,sandmonster,sanic,sherifffirearm,skeleton,slime,spider,startrekkin,steve,steve_in_love,supersanic,theworldisending,thinkos,utgy,villager,vindicator,warden,wither,wither_skeleton,yellowenderman,yes,yoda,zombie,zombie_pigman"
# str = str.replace("_", " ")
# print(str)
# print(len(str.split(",")))

letters = [c for c in "abcdefghijklmnopqrstuvwxyz"]

words = []
for i in letters:
    for j in letters:
        for k in letters:
            for l in letters + [" "]:
                words.append(f"{i}{j}{k}{l}")
            
candidates = ",".join(words)

f = open("Text/words.txt", "r+").read().splitlines()
res = set()

for w in f:
    if len(w) == 4 or len(w) == 3:
        res.add(w)

while len(",".join(res)) < 20000:
    print(len(",".join(res)))
    candidate = candidates.split(",").pop(random.randrange(0, len(candidates.split(","))))
    res.add(candidate)

res = list(res)
print(",".join(res))
print(len(res))
