
from mcpi.minecraft import Minecraft
from mcpi import block
import random
import math
import time
import thread
import city_functions
mc = Minecraft.create()


def full_flatten():
    #mc.postToChat("Full Flatten in Process")
    mc.setBlocks(-128,-64,-128,128,128,128,block.AIR,0)
    #mc.postToChat("Full Flatten Complete")

def up_flatten():
    #mc.postToChat("Up Flatten in Process")
    mc.setBlocks(-128,0,-128,128,128,128,block.AIR,0)
    #mc.postToChat("Up Flatten in Complete")

def foundations():
    #mc.postToChat("Foundation Building in Process")
    mc.setBlocks(-128,-1,-128,128,0,128,block.STONE,0)
    #mc.postToChat("Foundation Building Complete")

def skyscraper(x,y,z,size,floors):
    #mc.postToChat("Skyscraper Building in Process")
    blocks = [ block.STONE, block.BRICK_BLOCK, block.OBSIDIAN, block.SANDSTONE, block.STONE_BRICK]
    b = blocks[random.randint(0,len(blocks)-1)]
    a = block.AIR
    g = block.GLASS_PANE
    mc.setBlocks(x,y,z,x+size,(floors*3)+y,z+size,b)

    #hollow out floors
    #mc.postToChat("Hollow out floors")
    
    mc.setBlocks(x,y,z,x+size,(floors*3)+y,z+size,a)

    #adding glass
        #mc.postToChat("Adding Glass")
    for f in range(0,floors):
        mc.setBlocks(x+size,(f*3)+y,z,x+size,(f*3)+y+1,z+size,g)
    for f in range(0,floors):
        mc.setBlocks(x+size,(f*3)+y,z,x+size,(f*3)+y+1,z+size,g)
        mc.setBlocks(x,(f*3)+y,z,x,(f*3)+y+1,z+size,g)
        mc.setBlocks(x,(f*3)+y,z,x+size,(f*3)+y+1,z,g)
        mc.setBlocks(x,(f*3)+y,z+size,x+size-3,(f*3)+y+1,z+size,g)
        mc.setBlocks(x,(f*3)+y,z,x,(f*3)+y+1,z,b)
        mc.setBlocks(x+size,(f*3)+y,z,x+size,(f*3)+y+1,z,b)
        mc.setBlocks(x,(f*3)+y,z+size,x,(f*3)+y+1,z+size,b)
        mc.setBlocks(x+size,(f*3)+y,z+size,x+size,(f*3)+y+1,z+size,b)

    #mc.postToChat("Skyscraper Building Complete")


xshard = 0
zshard = 0
bFound = False
grid_coords = []
grid_size = 9

#make an array for the grid system co-ordinates
counter = 0
for x in range(-128,128):
    for z in range(-128,128):
        if(x % grid_size == 0 and z % grid_size == 0):
            grid_coords.append([x,z])

#mc.setBlocks(-128,-64,-128,128,128,128,block.AIR,0)

#whaere the shard will be
grid_start = random.randint(0,len(grid_coords)-1)
xshard = grid_coords[grid_start][0]
zshard = grid_coords[grid_start][1]


def roads():
    #mc.postToChat("Road laying in Process")
    for x in range(-128,128):
        if(x % grid_size == 0):
            mc.setBlocks(x,0,-128,x+1,0,128,block.DIAMOND_BLOCK)
    for z in range(-128,128):
        if(z % grid_size == 0):
            mc.setBlocks(-128,0,z,128,0,z+1,block.DIAMOND_BLOCK)
    #mc.postToChat("Road laying complete")



def skyscrapers():
    num = 0
    for x in range(-128,128):
         for z in range(-128,128):
             if(x % grid_size == 0 and z % grid_size == 0):
                 floors = random.randint(3,12)
                 skyscraper(x+2,1,z+2,grid_size-3,floors)
                 num+=1
                 mc.postToChat("Skyscraper  number " + str(num) + " complete")


def garden():
    xsize = random.randint(1,6)
    zsize = random.randint(1,6)

    #start at a random grid
    grid_start = random.randint(0,len(grid_coords)-1)
    xcoord = grid_coords[grid_start][0]
    zcoord = grid_coords[grid_start][1]



    #mc.postToChat("Garden Created at x: " + str(xcoord) + " z: " + str(zcoord))
    #remove the buildings
    mc.setBlocks(xcoord,0,zcoord,xcoord + xsize*(grid_size) +1,128,zcoord + zsize*(grid_size) +1,block.AIR,0)

    #lay the grass
    mc.setBlocks(xcoord,0,zcoord,xcoord + xsize*(grid_size) +1,0,zcoord + zsize*(grid_size) +1,block.GRASS)
    mc.player.setPos(xcoord, 3, zcoord)

def shard():

    #clear ground for the shard
    mc.setBlocks(xshard,1,zshard,xshard +(grid_size) +1,128,zshard + (grid_size) +1,block.AIR,0)

    mc.setBlocks(xshard+1,1,zshard+2,xshard+grid_size-1,10,zshard+grid_size-1,block.DIAMOND_BLOCK)
    mc.setBlocks(xshard+2,11,zshard+2,xshard+grid_size-1,20,zshard+grid_size-1,block.DIAMOND_BLOCK)
    mc.setBlocks(xshard+3,21,zshard+2,xshard+grid_size-1,30,zshard+grid_size-1,block.DIAMOND_BLOCK)
    mc.setBlocks(xshard+4,31,zshard+2,xshard+grid_size-1,40,zshard+grid_size-1,block.DIAMOND_BLOCK)
    mc.setBlocks(xshard+5,41,zshard+2,xshard+grid_size-1,50,zshard+grid_size-1,block.DIAMOND_BLOCK)
    #mc.postToChat("Shard Created at x: " + str(xcoord) + " z: " + str(zcoord))
    #mc.player.setPos(xshard, 3, zshard)

def distance():
    global bFound
    while not bFound:
        time.sleep(5)
        ppos = mc.player.getPos()
        xdist = ppos.x - xshard
        zdist = ppos.z - zshard

        distance = int( math.sqrt( (xdist * xdist) + (zdist * zdist)))

        if(distance < 15):
            bFound = True
            mc.postToChat("Shard Found!! You can fly now!")
        else:
             mc.postToChat("Distance from shard: " + str(distance))

def noFlying():
    global bFound
    while not bFound:
        ppos = mc.player.getPos()
        if(ppos.y > 3):
            mc.player.setPos(ppos.x,1,ppos.z);
            mc.postToChat("No flying!!!")

full_flatten
up_flatten()
foundations()
roads()

skyscrapers()
garden()
shard()
thread.start_new_thread(distance,())
thread.start_new_thread(noFlying,())

mc.postToChat("Find the shard to be able to fly around the city")
#skyscraper(2,2)
