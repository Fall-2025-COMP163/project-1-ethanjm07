"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Ethan Mitchell
Date: 10/20/25

AI Usage: Microsoft Copilet helped with logic issues in create character function. In\
save_character function, AI helped with bad directory logic issue
Example: AI helped with file I/O error handling logic in save_character function
"""
import os

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    character = {'name' : name,
            'class': character_class,
            'level': level,
            'strength':strength,
            'magic':magic,
            'health':health,
            'gold': 50}
    return character
    
   
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    base_strength = 5
    base_magic = 5
    base_health = 10
    
    if character_class == "Warrior":
        strength = (base_strength * 5)*level
        magic = (base_magic * 1)*level
        health = (base_health * 5)*level
    elif character_class == "Mage":
        strength = (base_strength * 1) * level
        magic = (base_magic * 5) * level
        health = (base_health * 3) * level
    elif character_class == "Rogue":
        strength = (base_strength * 3) * level
        magic = (base_magic * 3) * level
        health = (base_health * 1) * level
    elif character_class == "Cleric":
        strength = (base_strength * 3) * level
        magic = (base_magic * 3) * level
        health = (base_health * 1) * level
    else:
        strength = base_strength
        magic = base_magic
        health = base_health
    stats = (strength,magic,health,)
    return stats
   
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    """
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        # Directory does not exist
        return False
    with open(filename, 'w') as file:
            file.write(f"Character Name:{character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level:{character['level']}\n")
            file.write(f"Strength:{character['strength']}\n")
            file.write(f"Magic:{character['magic']}\n")
            file.write(f"Health:{character['health']}\n")
            file.write(f"Gold:{character['gold']}")
    return True
    
 
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    if not os.path.exists(filename):
        print("Error: File not found.")
        return None

    with open(filename, 'r') as file:
        character = {}
        for line in file:
            if ':' in line:
                key, value = line.strip().split(":", 1)
                key = key.strip()
                value = value.strip()

                # Map the file keys to dictionary keys
                if key == "Character Name":
                    character["name"] = value
                elif key == "Class":
                    character["class"] = value
                elif key == "Level":
                    character["level"] = int(value)
                elif key == "Strength":
                    character["strength"] = int(value)
                elif key == "Magic":
                    character["magic"] = int(value)
                elif key == "Health":
                    character["health"] = int(value)
                elif key == "Gold":
                    character["gold"] = int(value)

    return character
        
    # TODO: Implement this function
    # Remember to handle file not found errors
    

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    """""
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

    # TODO: Implement this function
    

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character['level'] += 1
    
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health
    
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    person = create_character('Ethan','Warrior')
    save_character(person,"ethan.txt")
    loaded = load_character('ethan.txt')
    display_character(person)
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
