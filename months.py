which_one = int(input("What Months (1-12)?"))

months = ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October', 'November' , 'December']
if 1 <= which_one <= 12:
    print("Months " , months[which_one - 1])