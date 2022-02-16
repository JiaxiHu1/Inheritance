import a_PlantClass as pc

#there is a plant and the color is assigned to it 
primrose = pc.Plant("Green")
#another plant and assigned color to it 
#but because it's also have another attribute - petals 
#we need to assign petals to sunflowers too 
sunflower = pc.Flower("Yellow",12)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())

#this will give us error too 
#because plant is only in the super class 
#get_petals method is not in the sub class 
'''
print(primrose.get_petals())
'''
