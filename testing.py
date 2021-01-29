from mcpi.minecraft import Minecraft
mc=Minecraft.create()
def clear_space():
        global mc
	input()#this is going to be for getting it right you will see it soon
	p = mc.player.getTilePos()
	input()
	s = mc.player.getTilePos()
	input()
	mc.setBlocks(p.x, p.y, p.z, s.x, s.y, s.z, 0)

clear_space()
#soon in mcpizero! as seen in the video!
