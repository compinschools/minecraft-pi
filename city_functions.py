from mcpi.minecraft import Minecraft
from mcpi import block
import random
import math
import time
import thread

mc = Minecraft.create()

def full_flatten():
    
    #mc.postToChat("Full Flatten in Process")
    mc.setBlocks(-128,-64,-128,128,64,128,block.AIR,0)
    #mc.postToChat("Full Flatten Complete")

def up_flatten():
    
    #mc.postToChat("Up Flatten in Process")
    mc.setBlocks(-128,1,-128,128,128,128,block.AIR,0)
    #mc.postToChat("Up Flatten in Complete")

def foundations():
    #mc.postToChat("Foundation Building in Process")
    mc.setBlocks(-128,0,-128,128,0,128,block.STONE,0)
    #mc.postToChat("Foundation Building Complete")

def skyscraper(x,y,z,size,floors):
    #mc.postToChat("Skyscraper Building in Process")
    blocks = [ block.STONE, block.BRICK_BLOCK, block.OBSIDIAN, block.SANDSTONE, block.STONE_BRICK]
    b = blocks[random.randint(0,len(blocks)-1)]
    a = block.AIR
    g = block.GLASS_PANE
    mc.setBlocks(x,y,z,x+size,(floors*3)+y,z+size,b)

    
    #mc.postToChat("Hollow out floors")
    


    #adding glass
        #mc.postToChat("Adding Glass")
    for f in range(0,floors):
        mc.setBlocks(x+1,y+(f*3),z+1,x+size-1,y+(f*3)+1,z+size-1,a)#hollow out floors
        mc.setBlocks(x,(f*3)+y,z,x,(f*3)+y+1,z+size,g)
        mc.setBlocks(x+size,(f*3)+y,z,x+size,(f*3)+y+1,z+size,g)
        mc.setBlocks(x,(f*3)+y,z,x+size,(f*3)+y+1,z,g)
        mc.setBlocks(x,(f*3)+y,z+size,x+size,(f*3)+y+1,z+size,g)
        mc.setBlocks(x,(f*3)+y,z,x,(f*3)+y+1,z,b)
        mc.setBlocks(x+size,(f*3)+y,z,x+size,(f*3)+y+1,z,b)
        mc.setBlocks(x,(f*3)+y,z+size,x,(f*3)+y+1,z+size,b)
        mc.setBlocks(x+size,(f*3)+y,z+size,x+size,(f*3)+y+1,z+size,b)

    return b
    #mc.postToChat("Skyscraper Building Complete")

def spire(x,y,z,size,blk):
    current_size = size
    current_y = y
    current_x = x
    current_z = z
    while (current_size > 0):
        #print("current_x: " + str(current_x))
        #print("current_z: " + str(current_z))
        #print("current_y: " + str(current_y))
        #print("current_size: " + str(current_size))
        mc.setBlocks(current_x, current_y, current_z,
                     current_x+current_size, current_y, current_z+current_size,
                     blk)
        current_x = current_x + 1
        current_z = current_z + 1
        current_y = current_y + 1
        current_size = current_size - 2
        
    
    
def skyscraperWithSpire(x,y,z,size,floors):
    b = skyscraper(x,y,z,size,floors)
    spire(x,(floors*3)+y+1,z,size,b)

