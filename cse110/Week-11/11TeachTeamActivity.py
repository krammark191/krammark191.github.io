with open("cse110/Week-11/hr_system.txt") as file:
    
    # With open file, read line by line.
    for line in file:
        line = line.strip()
        info_piece = line.split(" ")

        # Set up variables for each line.
        name = info_piece[0]
        id_num = info_piece[1]
        title = info_piece[2]
        salary = float(info_piece[3])

        # Calculate bimonthly pay with bonus for engineer.
        paycheck = salary / 24
        if title.lower() == "engineer":
            paycheck += 1000
        
        # Print info with formatting.
        print(f"{name} (ID: {id_num}), {title} - ${paycheck:.2f}")