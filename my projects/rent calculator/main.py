# inputs required
# 1.room rent
# 2.food bill
# 3.electricity bill
# 4.total numbers of roommates
# 5.additional expences

# output
# bill per person

bills_dict={
    'room_rent':int(input("enter the amount room rent per month: ")),
    'food_bill':int(input("enter the food bill of this month: ")),
    'electricity_bill':int(input("enter the electricity bill of this month: ")),
    'no_of_roommates':int(input("enter how many roommates are there: ")),
    'extra_expences':int(input("enter the amount of additional amount of expences: "))
}

total_bill=0

for bill_type,amount in bills_dict.items():
    if bill_type!='no_of_roommates':
        total_bill+=amount

bill_per_person=total_bill//bills_dict['no_of_roommates']

print(f"\nthe total amount of the bill per person of this month is: ",bill_per_person)

