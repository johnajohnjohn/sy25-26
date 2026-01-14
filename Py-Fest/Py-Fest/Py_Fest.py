#initial lineup
lineup = [
    ("code play", "Indie", 30),
    ("the pythonistas", "Rock", 45),
    ("syntax error", "metal", 60),
    ]

total_time = 0

print("------------py-fest 2026 manager-------------")
print("1: view lineup and time")
print("2: add a new band")
print("3: move first band to end")
print("4: remove a band by name")
print("5: move band")
print("6: exit")

choice = int(input("Enter your choice (1-6): "))

if choice == 1:
    print("Current lineup:")
    for band in lineup:
        print(f"Band: {band[0]}, Genre: {band[1]}, Time: {band[2]} minutes")
        total_time += band[2]
    print(f"Total performance time: {total_time} minutes")
elif choice == 2:
    name = input("Enter band name: ")
    genre = input("Enter band genre: ")
    time = int(input("Enter performance time (in minutes): "))
    lineup.append((name, genre, time))
    print(f"Added band: {name}, Genre: {genre}, Time: {time} minutes")
elif choice == 3:
    if lineup:
        first_band = lineup.pop(0)
        lineup.append(first_band)
        print(f"Moved band {first_band[0]} to the end of the lineup.")
elif choice == 4:
    name = input("Enter the name of the band to remove: ")
    for band in lineup:
        if band[0].lower() == name.lower():
            lineup.remove(band)
            print(f"Removed band: {band[0]}")
            break
        else:
            print("Band not found.")
elif choice == 5:
    name = input("Enter the name of the band to move: ")
    new_position = int(input("Enter the new position (0-indexed): "))
    for band in lineup:
        if band[0].lower() == name.lower():
            lineup.remove(band)
            lineup.insert(new_position, band)
            print(f"Moved band {band[0]} to position {new_position}.")
            break
    else:
        print("Band not found.")
elif choice == 6:
    print("Exiting Py-Fest manager. Goodbye!")
else:
    print("Invalid choice. Please enter a number between 1 and 6.")