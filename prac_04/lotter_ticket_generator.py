import random
def main():
    number_of_picks = int(input("How many quick picks? "))

    for pick in range(1, number_of_picks + 1):
        lottery_tickets = create_lottery_ticket()
        print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(lottery_tickets[0],lottery_tickets[1],lottery_tickets[2],lottery_tickets[3],lottery_tickets[4],lottery_tickets[5]))


def create_lottery_ticket():
    numbers = []
    """
    for i in range(1,46):
        numbers.append(i)
    """
    for i in range(0,6):
        random_number = random.randint(1, 45)
        numbers.append(random_number)
    numbers = sorted(numbers)
    index = 0
    for number in numbers:
        number = str(number)
        numbers[index] = number
        index += 1
    return numbers
main()