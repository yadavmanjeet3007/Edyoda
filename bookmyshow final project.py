#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Bookmyshow:
    def __init__(self):
         
            print("Welcome to book my show!")
            self.row = int(input("Enter the no of rows : "))
            self.seats = int(input("Enter the no seats in row : "))
            self.matrix = []
            self.seat_count = 0
            self.current_income = 0
            self.total_no_seats = self.row*self.seats
            self.current_income = 0
            self.total_income = 0
            self.info = {}
            self.price = 0
            for i in range(self.row):
                a = []
                for j in range(self.seats):
                    a.append('S')
                self.matrix.append(a)
            self.options()
    def options(self):
        
        print("Select option number to proceed :")
        print("1.Show seats")
        print("2.Buy ticket")
        print("3.Statistics")
        print("4.User info")
        print("0.Exit")
        x = int(input())
        
        if x == 1:
            self.show_seats()
        elif x == 2:
            self.buy_ticket()
        elif x == 3:
            self.statistics()
        elif x == 4:
            self.user_info()
        elif x == 0:
            self.exit()
        else:
            print("Choose correct option as given above.")
            self.options()

    def show_seats(self): 
        print('\nCinema:')
        print(end='  ')
        for j in range(1,self.seats+1):
            print(j,end=" ")
        print()
        a = 0
        for i in self.matrix:
            a+=1
            print(a,end=' ')
            print(' '.join(i),sep=",") 
    
    def buy_ticket(self):
        a = int(input("Enter no. of row you want to book :"))
        b = int(input("Enter no. of seat you want to book :"))
        
        if self.total_no_seats < 60:
            self.price = 10
            self.total_income = self.total_no_seats * 10
            
            print("Price of ticket is :",self.price)
        elif self.total_no_seats > 60:
            if a < self.row//2:
                self.price = 10
            else:
                self.price = 8
            first_half_income = (self.row//2)*self.seats*10
            second_half_income = (self.row - self.row//2)*self.seats*8
            self.total_income= first_half_income+second_half_income 
            
            print("Price of ticket is : ",self.price)

        confirm = input('Type y for booking and n for stop booking :')
        
        if confirm == 'y' or 'Y':
            u_dict = {}
            print("Enter your name :")
            name = input()
            print("Enter your age :")
            age = input()
            print("Enter your gender M for male or F for female :")
            gender = input()
            print("Enter your mobile no. :")
            mobile_no = input()
            self.matrix[a-1][b-1] = 'B'
            self.seat_count +=1
            self.current_income += self.price
            u_dict[(a,b)] = [name,age,gender,mobile_no]
            self.info.update(u_dict)
            print("Booked successfully!")
        else:
            print('This seat is not booked!')
            
        self.options()   
        
    def statistics(self):
       
        print('No.of purchased ticket: ',self.seat_count)
        self.percentage = (self.seat_count/self.total_no_seats)*100
        print('Percentage of ticket booked','{:.2f}'.format(self.percentage))
        print('Current income: ',self.current_income)
        print('Total income: ',self.total_income)
        
        
        self.options() 
        
    def user_info(self):
        
        check_a = int(input('Enter the row you booked\n'))
        check_b = int(input('Enter the seat you booked\n'))
        
        if self.matrix[check_a-1][check_b-1] == 'B':
            user = self.info[(check_a,check_b)]
            print(user)
        else:
            print('This seat is not booked yet')
        self.options()    
            
    def exit(self):
        print('you successfully exit')
        self.options()
        
x = Bookmyshow()
x.options()


# In[ ]:




