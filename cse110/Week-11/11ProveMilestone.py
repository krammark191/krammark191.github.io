with open("cse110/Week-11/life-expectancy.csv") as file:
    
    lowest_value = 100.0
    highest_value = 0.0
    average = 0.0
    count = 0
    sum = 0.0
    highest_country = ""
    highest_year = 0
    lowest_country = ""
    lowest_year = 0
    highest_country_in_year = ""
    lowest_country_in_year = ""
    highest_by_year = 0.0
    lowest_by_year = 100.0
    year_in = int(input("\nEnter the year of interest: "))

    # With open file, read line by line.
    for line in file:
        line = line.strip()
        info_piece = line.split(",")

        # Set up variables for each line.
        entity = info_piece[0]
        code = info_piece[1]
        try:
            year = int(info_piece[2])
        except:
            year = -1
        try:
            life_expectancy = float(info_piece[3])
        except:
            life_expectancy = -1

        # Find the lowest value for life expectancy.
        if lowest_value > life_expectancy and year != -1:
            lowest_value = life_expectancy
            lowest_country = entity
            lowest_year = year
        
        # Find the highest value for life expectancy.
        if highest_value < life_expectancy and year != -1:
            highest_value = life_expectancy
            highest_country = entity
            highest_year = year
        
        if year == year_in:

            # Find year average.
            sum += life_expectancy
            count += 1

            # Find lowest local value for life expectancy.
            if lowest_by_year > life_expectancy:
                lowest_by_year = life_expectancy
                lowest_country_in_year = entity
            
            # Find highest local value for life expectancy.
            if highest_by_year < life_expectancy:
                highest_by_year = life_expectancy
                highest_country_in_year = entity

    average = sum / count
        
    print(f"\nThe overall max life expectancy is: {highest_value:.2f} from {highest_country} in {highest_year}")
    print(f"The overall max life expectancy is: {lowest_value:.2f} from {lowest_country} in {lowest_year}")

    
    print(f"\nFrom the year {year_in}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {highest_country_in_year} with {highest_by_year:.2f}")
    print(f"The min life expectancy was in {lowest_country_in_year} with {lowest_by_year:.2f}\n")