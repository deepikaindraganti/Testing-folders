wt=float(input("Weight: "))
kl=input("(K)g or (L)bs: ")
if (kl.upper()!='K' and kl.upper()!='L'):
    kl=input("Re-enter a valid metric type! (K or L): ")
if kl=='k' or kl=='K':
    fnew=wt*2.20462
    print("Weight in (L)bs: ", fnew)
else:
    fnew=wt/(2.20462)
    print("Weight in (K)g: ", fnew)
