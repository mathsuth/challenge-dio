def hero_ranking(power):
    if power <= 1000:
        return "Iron"
    elif power >= 1001 and power <= 2000:
        return "Bronze"
    elif power >= 2001 and power <= 5000:
        return "Silver"
    elif power >= 5001 and power <= 7000:  
        return "Gold"
    elif power >= 7001 and power <= 8000:
        return "Platinum"
    elif power >= 8001 and power <= 9000:
        return "Ascendant"
    elif power >= 9001 and power <= 10000:
        return "Immortal"
    elif power > 10000:
        return "Radiant"

while True:
    hero = input("Enter the hero's name: ")
    power = int(input("Enter the hero's XP: "))
    print("The hero", hero, "has the level", hero_ranking(power))
    proceed = input("Do you want to add another hero? (y/n): ")
    if proceed != 'y':
        break
