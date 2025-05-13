lst=eval(input("enter elements of your list at once: "))
    #eval lets user enter any element at once cuz eval makes it a 
    #a string to be entered at once
sum_obs=sum(lst)
no_obs=len(lst)
mean=sum_obs/no_obs
print("your list: ",lst, "\nmean is: ",mean)