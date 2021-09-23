print('Please enter the following information:\n')

#The following collects data from the user.

first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_num = input('Phone number: ')
job_title = input('Job title: ')
id_num = input('ID number: ')
hair_clr = input('Hair color: ')
eye_clr = input('Eye color: ')
month_strt = input('Month started: ')
training = input('Training received? ')

#The following prints the data into an ID Card format.

print('\nThe ID Card is:')
print('----------------------------------------')
print(f'{last_name.upper()}, {first_name.title()}')
print(job_title.title())
print(f'ID: {id_num}\n')
print(email_address.lower())
print(phone_num, "\n")
print("Hair: {0:20} Eyes: {1}".format(hair_clr.title(),eye_clr.title()))
print("Month: {0:19} Training: {1}".format(month_strt.title(),training.title()))
print('----------------------------------------')