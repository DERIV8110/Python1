i=1
tot_charity=0
tot_donation=0

while i<=3:
    char_sales=float(input(f"charity sales amount on day {i}: "))
    don=float(input(f"donation amount on day {i}: "))
    tot_charity+=char_sales
    tot_donation+=don
    i+=1

target=tot_charity+tot_donation #you can't use 200000-something as variable,
                                #it will always print 200000

if tot_charity+tot_donation<200000:
        print("we are short of Rs.",200000-target,"from the the intended amount of Rs 2Lakh")
else:
        print("charity camp successfully raised more than Rs. 2 Lakh")