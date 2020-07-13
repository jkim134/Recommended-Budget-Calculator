def main():
    print()
    print('Basic Recommended Budget From Chime.com' ) 

    budget_program = 'Recommendation Budget'
    your_budget = recommendation_budget
    while budget_program == 'Recommendation Budget':
        print()
        print('YOUR RECOMMENDED BUDGET CATEGORY PERCENTAGES!')        
        print('Housing is 25%:\n $', your_budget *.25)
        print('Insurance is 15%:\n $', your_budget *.15)
        print('Food is 10%:\n $', your_budget *.10)
        print('Transportation is 5%:\n $', your_budget *.05)
        print('Utilities is 5%:\n $'), your_budget *.05)
        print('Savings is 15%:\n $'), your_budget *.15)
        print('Entertainment is 10%:\n $', your_budget *.10)
        print('Giving is 10%:\n $', your_budget *.10)
        print('Personal is 5%:\n $', your_budget *.05)
        print()
        print('Menu:')
        print('1 to Add your income: ')
        print('Q to Quit')
        choice = input('Select 1 or Q: ')
        if choice == '1':
            your_budget = addincome(your_budget)
        elif choice == 'q':
            print('Goodbye!')
            break
        elif choice == 'Q':
            print('Thank You!')
            break
        else:
            print('Invalid selection, please select 1 or Q')

main()
