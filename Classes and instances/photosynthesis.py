from atom import Atom
from molecule import Molecule
from chloroplast import Chloroplast

hydrogen = Atom('H', 1, 0)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
demo = Chloroplast()
els = [water, co2]

while True:
    print('\nWhat molecule would you like to add?')
    print('[1] Water')
    print('[2] carbondioxyde')
    choice = input('Please enter your choice: ')

    if choice == '1':
        molecule_to_add = "water"
    elif choice == '2':
        molecule_to_add = "co2"
    else:
        print('\n=== That is not a valid choice.')
        continue

    try:
        res = demo.add_molecule(molecule_to_add)
        if len(res) == 0:
            print(demo)
        else:
            print('\n=== Photosynthesis!')
            print(res)
            print(demo)

    except Exception as e:
        print(f'\n=== An error occurred: {e}')