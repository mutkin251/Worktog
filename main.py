print(" Додаткове завдання")
achievements = {
    'Mine to die': {"locked": "Die by digging down"},
    'MINE to mine': {"locked": "Craft a pickaxe"},
    'It HURT!': {"locked": "Die by falling down"}
}
def display_achievments(achievments):
    print(achievments)

def add_achievment(achievments, name, description):
    achievments[name] = description
    print(achievments)
def unlock_achievment(achievements, name, description):
    achievements.pop(name)
    achievements[name]={"unlocked", description}
    print(achievements)
choice=int(input("What do you want to do? 1-display achievments; 2-unlock achievments; 3-add achievment; 4-exit; "))
gip = True
while gip==True:
    if choice ==1:
        display_achievments(achievements)
    elif choice == 2:
        unlock_achievment(achievements,input(f"Want to open an achievement? Which one? Print IT! "), input("New description of this achievments(It can be he same): "))
    elif choice == 3:
        add_achievment(achievements, input("Name a new achievement: "), input("Description of this new achievments: "))
    elif choice == 4:
        gip=False
        break