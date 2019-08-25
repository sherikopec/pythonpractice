def split (creditcardnumber):
    return list(creditcardnumber)
creditcardnumber = input('Please input your credit card number: ')

my_sum = 0
my_sum2 = 0
totalone = 0
totaltwo = 0
totalthree = 0

def calculate_credit_card_number_check_digit():
    for counter, number in enumerate(creditcardnumber,1):
        number = int(number)
        if counter % 2 == 0:
            my_sum = (number * 2)
            if my_sum > 9:
                my_sum2 = my_sum - 9
                totalone += my_sum2
            else: 
                totaltwo += my_sum
        else:
            totalthree += number

    total = (totalone + totaltwo + totalthree)

calculate_credit_card_number_check_digit()