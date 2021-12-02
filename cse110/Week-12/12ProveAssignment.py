import time

with open("cse110/Week-11/life-expectancy.csv") as file:
    
    # Variables for highest and lowest general statistics.
    lowest_value = 100.0
    highest_value = 0.0
    highest_country = ""
    highest_year = 0
    lowest_country = ""
    lowest_year = 0
    universal_line_count = 1

    # Variables for average calculation.
    count = 0
    sum = 0.0
    
    # Variables for highest and lowest countries in a given year.
    highest_country_in_year = ""
    lowest_country_in_year = ""
    highest_by_year = 0.0
    lowest_by_year = 100.0
    year_in = int(input("\nEnter the year of interest: "))

    # Variables for the largest drop.
    drop_country = ""
    drop_year = 0
    gap_size = 0.0
    life_expectancy_last = 0.0
    code_last = ""

    # Variables for min, max, and average of a given country.
    country_in = input("Enter the country of interest: ")
    local_min = 100.0
    local_max = 0.0
    local_count = 0
    local_sum = 0.0
    lowest_local_year = 0
    highest_local_year = 0

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
        
        # Find year specific stats.
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
        
        # Find the largest drop from one year to the next.
        if universal_line_count != 1:
            if gap_size < life_expectancy_last - life_expectancy and life_expectancy_last != 0.0 and code_last == code:
                gap_size = life_expectancy_last - life_expectancy
                drop_year = year
                drop_country = entity
            life_expectancy_last = life_expectancy
            code_last = code

        # Find the minimum, maximum, and average life expectancy of a given country.
        if entity.lower() == country_in.lower():

            # Find your local average.
            local_sum += life_expectancy
            local_count += 1

            # Find lowest national value for life expectancy.
            if local_min > life_expectancy:
                local_min = life_expectancy
                lowest_local_year = year
            
            # Find highest national value for life expectancy.
            if local_max < life_expectancy:
                local_max = life_expectancy
                highest_local_year = year
        
        universal_line_count += 1


    average = sum / count
    local_average = local_sum / local_count
    
    time.sleep(1)
    print(f"\nThe overall max life expectancy is: {highest_value:.2f} from {highest_country} in {highest_year}")
    print(f"The overall max life expectancy is: {lowest_value:.2f} from {lowest_country} in {lowest_year}")
    print(f"The largest drop in life expectancy from one year to the next was in {drop_country} from {drop_year - 1} to {drop_year}.")
    print(f"The life expectancy dropped by {gap_size:.2f} years.")

    time.sleep(1)
    print(f"\nFrom the year {year_in}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {highest_country_in_year} with {highest_by_year:.2f}")
    print(f"The min life expectancy was in {lowest_country_in_year} with {lowest_by_year:.2f}")

    time.sleep(1)
    print(f"\nFrom the country {country_in}:")
    print(f"The average life expectancy across all years was {local_average:.2f}")
    print(f"The max life expectancy was in {highest_local_year} with {local_max:.2f}")
    print(f"The min life expectancy was in {lowest_local_year} with {local_min:.2f}\n")