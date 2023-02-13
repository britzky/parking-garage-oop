# Your parking gargage class should have the following methods:
# - takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1
# - payForParking
#    - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
#    - If the ticket has been paid, display a message of "Thank You, have a nice day"
#    - If the ticket has not been paid, display an input prompt for payment
#       - Once paid, display message "Thank you, have a nice day!"
#    - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#    - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# Your parking gargage class should have the following methods:
# - takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1
# - payForParking
#    - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
#    - If the ticket has been paid, display a message of "Thank You, have a nice day"
#    - If the ticket has not been paid, display an input prompt for payment
#       - Once paid, display message "Thank you, have a nice day!"
#    - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#    - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

class ParkingGarage():
    def __init__(self, tickets_left, parking_left):
        self.tickets = []
        self.parking_spaces = []
        self.current_ticket = {}
        self.tickets_left = tickets_left
        self.parking_left = parking_left
   
    def takeTicket(self):
        '''
        Counting method to make sure there are spaces available 
        '''
        self.tickets_left -= 1
        self.parking_left -=1
     
    def payForParking(self):
        '''
        While loop to make sure if they want to park they at least pay 1
        dollar 
        '''
        while True:
            paid = int(input('Enter the amount your paying '))
            if paid > 0:
                self.current_ticket[paid] = True
                print('Thank you, have a nice day!')
                break
            else:
                print('You have to pay at least $1')
    def leaveGarage(self):
        '''
        While loop to make sure that everyone who even thinks about 
        parking in this lot pays at least 1 dollar 
        '''
        while self.current_ticket:
            if self.current_ticket:
                print('Thank you, have a nice day! ')
                break
        else:
            pay = int(input('Please enter the amount you\'re paying now '))
            if pay <= 0:
                print('You have to pay at least 1 dollar') 
            elif pay > 0:
                self.current_ticket[pay] = True 
                print('Thank you, have a nice day!')               
        self.tickets_left += 1
        self.parking_left +=1
    
    def lotCount(self):
        '''
        print the amount of tickets and parking spaces left
        '''
        print(f'There are {self.tickets_left} tickets left and {self.parking_left} parking spots left in this lot')


    def runner(self):
        '''
        runner method to let the driver know if there are available 
        spots and ask if they want to park
        '''
        while self.tickets_left and self.parking_left > 0:
                parking.lotCount()
                park = input('Would you like to park? (enter "y" for yes and "n" for no) ').lower()
                if park == 'y':
                    parking.takeTicket()
                    parking.payForParking()
                    continue
                elif park == 'n':
                    parking.leaveGarage()
                    break
                else: 
                    print('Not a valid option, please try again.')
        else:
            print('Lot full, try later')
parking = ParkingGarage(5, 5)
parking.runner()