from time import sleep
print(" Додаткове завдання")
achievements = {
    'Mine to die': {
        'status': "locked",
        'description': "Die by digging down"
    },
    'Mine to mine': {
        'status': "locked",
        'description': "Craft a pickaxe"
    },
    'It HURT!': {
        'status': "locked",
        'description': "Die by falling down"
    }
}
print(achievements.keys())
def display_achievements(achievements):
    print(achievements)

def add_achievement(achievements, name, description, status):
    achievements[name] = [status, description]
    print(achievements)
def unlock_achievement(achievements, name,status):
    if achievements[name].get('status')=="locked":
        achievements[name].update({'status': "unlocked"})
    else:
        print("That achievement is unlocked; ")
    print(achievements)
def delete_achievement(achievements,name):
    achievements.pop(name)
    print(achievements)
while 1>0:
    sleep(4)
    print("===="*100)
    choice = int(input("What do you want to do? 1-display achievments(full_info); 2-unlock achievments; 3-add achievment; 4-delete achievment; 5-exit; "))
    if choice ==1:
        display_achievements(achievements)
    elif choice == 2:
        name = input(f"Want to open an achievement? Which one? Print IT! ")
        unlock_achievement(achievements,name,achievements[name].get('status'))
    elif choice == 3:
        add_achievement(achievements, input("Name a new achievement: "), input("Description of this new achievments: "), input("Status of the achievment(locked,unlocked): "))
    elif choice == 4:
        delete_achievement(achievements, input("Enter the name of the achievement that you want to delete: "))
    elif choice == 5:
        break