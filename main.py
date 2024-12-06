from blockblast import Blockblast

bb = Blockblast()

block = bb.generate_block()

print("block")
print(block)

bb.place_block(block, 0, 0)