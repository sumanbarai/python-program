d={}
# print(type(d))
d2={"harry":"burger", "yogesh":"noodles","subhsm":"magic","L":"maggie"}
# print(d2["subhsm"])

d3={"harry":"burger", "yogesh":"noodles","subhsm":"magic","L":"maggie",2:{"suman":"barai","dsb":"gfr"}}

for i in d2:
    print(i,"=",d2[i])

for i in d3:
    if type(d3[i]) is dict:
        for k in d3[i]:
            print(k,'=',d3[i][k])
    else:
        print(i,"=",d3[i])
                    