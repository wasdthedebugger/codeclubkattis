def main():
    identified_animals: dict[dict] = {
        
    }
    
    animals: list[list[str]] = []
    
    while True:
        current_animals: list[str] = []
        number: int = int(input())
        if number == 0:
            break
        for i in range(number):
            current_animals.append(str(input()).lower())
        
        animals.append(current_animals)
        
    for animal in animals:
        animal_dict: dict[str, int] = {}
        for single_animal in animal:
            single_animal_name = single_animal.split(" ")[-1]
            if single_animal_name not in animal_dict:
                animal_dict[single_animal_name] = 1
            else:
                animal_dict[single_animal_name] += 1
                
        identified_animals[len(identified_animals) + 1] = animal_dict
            

    for key, value in identified_animals.items():
        print(f"List {key}:")
        for animal, count in value.items():
            print(f"{animal} | {count}")
    
if __name__ == "__main__":
    main()