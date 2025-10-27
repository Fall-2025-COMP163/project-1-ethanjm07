"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Ethan Mitchell
Date: 10/20/25

AI Usage: Microsoft Copilet helped with logic issues in create character function.
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """

    if character_class !=
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    char = {'name' : name,
            'class': character_class,
            'level': level,
            'strength':strength,
            'magic':magic,
            'health':health,
            'gold': 50}
    return char
    
    """  
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    
    
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass
level = 1
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
    stats = (strength,magic,health,)
    return stats
    """"
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    """
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    """
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
    with open(filename,'r') as file:
        
    # TODO: Implement this function
    # Remember to handle file not found errors
    return 

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    """""
    """""    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    person = create_character('Ethan','Warrior')
    print(person)
    save_character(person,"ethan.txt")
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
