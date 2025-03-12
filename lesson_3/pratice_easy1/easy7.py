flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# #solution 1 
flintstones.append('Dino')
print(flintstones)

#solution 2
flintstones.extend(['Dino'])
print(flintstones)

#solution 3
flintstones.insert(len(flintstones), 'Dino')  
print(flintstones)