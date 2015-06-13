import random
import math
import time
import thread


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
