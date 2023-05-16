# these variables cannot change
gravityconstant = 10
maxplayers = 2 
carconstant = 7 
lifespan = 9
selfcount = 1

#franklincodevariable
ef = gravityconstant * gravityconstant + maxplayers
print(ef) # 102
ar = gravityconstant + maxplayers + ef
print(ar) # 114
ey = gravityconstant * lifespan + carconstant
print(ey) # 97
en = gravityconstant * gravityconstant + gravityconstant
print(en) # 110
key = ef - maxplayers + (ey - (gravityconstant * lifespan))
print(key) # 107
el = key + selfcount
print(el) # 108
ay = key - maxplayers
print(ay) #105
enlast = en
print(enlast) #en

buildingheight = ef + ar + ey + en + key + el + ay + en
print("building height" + " " + str(buildingheight)) 
# Building height must be always 853

print("code:" + " " + str(chr (ef)) + str(chr (ar)) + str(chr (ey)) + str(chr (en)) + str(chr (key)) + str(chr (el)) + str(chr (ay)) + str(chr (enlast)))

roomsize = buildingheight - (el + ey)
print("roomsize" + " " + str(roomsize)) 

# therefore, Changing one value will change everything because each nodes are dependent to each other's node. secured but hard to modify. Even if you change the values of the franklincodevariable to constant integers, the output will still be franklin.
