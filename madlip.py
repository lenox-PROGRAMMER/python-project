def get_inputs():
    print("Welcome to Madlibs Generator!")
    animal = input("Enter the animal's name: ")
    profession = input("Enter profession: ")
    cloth = input("Enter cloth: ")
    thing = input("Enter a thing: ")
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb : ")
    food = input("Enter a food: ")
    return animal, profession, cloth, thing, name, place, verb, food

def generate_madlib(animal, profession, cloth, thing, name, place, verb, food):
    madlib = (f"Once upon a time, there was a(n) {animal} who wanted to be a {profession}. "
              f"It wore {cloth} and carried a {thing}. One day, {name} went to {place} "
              f"to {verb} while eating {food}.")
    return madlib

def main():
    # Get user inputs
    inputs = get_inputs()
    # Generate and display the madlib story
    story = generate_madlib(*inputs)
    print("\nHere is your madlib story:")
    print(story)

# Run the program
if __name__ == "__main__":
    main()
