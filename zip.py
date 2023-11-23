name = ["Manish", "Kavita", "Avani", "Rahul","Priti"]
age = [24, 52, 85, 20, 28]
gender = ['Male', 'Female', 'Female', 'Male', 'Female']
all_details = list(zip(name, age, gender))
for n, a, g in all_details:
    print("Name",n)
    print("age",a)
    print("gender",g)
    