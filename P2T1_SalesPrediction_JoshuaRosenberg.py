# Get Sales
 # 26Sep2018
 # CTI-110 P2T1 - Sales Prediction
 # Joshua Rosenberg
 #


#Get the predicted total sales

total_sales= float(input('Enter the projected sales: '))

#calculate the profit as 23 percent of total sales
profit = total_sales * 0.23

#Display the profit
print("the profit is $" ,  format(profit, ",.2f"))
