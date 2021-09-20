#%%

#here's a function to print the values of a geometric sequence
def geoSeq(n, start, ratio):

    #print greeting
    print('Hi!  This is a greeting.')

    #assign starting value to variable
    a_n = start

    #loop through n times, one for each number
    for _ in range(n):
        #print out cur value
        print(a_n, end=' ')

        #calculate next term
        a_n*=ratio

# %%
geoSeq(5,2,2)