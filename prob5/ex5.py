# start list of n's
ns = [1]
for i in range(25):
    new = ns[i]*10
    ns.append(new)


e_old = '%.14g' % (1,)
print("-----------------------------")
print("it |    n    |       e   ")
print("-----------------------------")

for i,n in enumerate(ns):
    e = ( 1 + 1/n)**n        # Calculate limit
    e = str('%.14f' % (e,))  # leave 14 digits to make sure it's not rounding at 12
    e = e[:14]               # get only 12 decimal digits (first digit and decimal point count 2)
    if e_old == e:           # if agrees at 12 decimal (no rounding) with old value, stop
        print("%02d | %.2E| %.12f --> converged!"%(i+1, n, float(e)))
        break
    else: print("%02d | %.2E| %.12f"%(i+1, n, float(e)))
    e_old = str(e)
print("-----------------------------")
