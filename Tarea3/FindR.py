R1 , R2, R3, R4 = 0, 0, 0, 0

def check(R1, R2, R3, R4):
    # print("R1:"+str(R1)+"\nR2:"+str(R2)+"\nR3:"+str(R3)+"\nR4:"+str(R4))
    # print(int(120*R4*((R3-1)/(R3+R4)) + 120*R2*((R1+1)/(R1+R2))))
    return int(120*R4*((R3-1)/(R3+R4)) + 120*R2*((R1+1)/(R1+R2))) == 51



to = 10
low = 1200
for i in range(0, to, 1):
    R1 = i
    for j in range(i, to, 1):
        R2 = j
        for z in range(j, to, 1):
            R3 = z
            for t in range(z, to, 1):
                R4 = z
                if int(120*R4*((R3-1)/(R3+R4)) + 120*R2*((R1+1)/(R1+R2))) < low:
                    low = int(120*R4*((R3-1)/(R3+R4)) + 120*R2*((R1+1)/(R1+R2)))
                # if check(R1, R2, R3, R4):
                #     print("R1:"+str(R1)+"\nR2:"+str(R2)+"\nR3:"+str(R3)+"\nR4:"+str(R4))
print(low)
#
# to = 100
# for i in range(1, to, 1):
#     R1 = i
#     for j in range(i, to, 1):
#         R2 = j
#         for z in range(j, to, 1):
#             R3 = z
#             for t in range(z, to, 1):
#                 R4 = z
#                 if check(R1, R2, R3, R4):
#                     print("R1:"+str(R1)+"\nR2:"+str(R2)+"\nR3:"+str(R3)+"\nR4:"+str(R4))
#
# to = 11
# for i in range(10, to, 1):
#     R1 = i
#     for j in range(i, to, 1):
#         R2 = j
#         for z in range(j, to, 1):
#             R3 = z
#             for t in range(z, to, 1):
#                 R4 = z
#                 if check(R1, R2, R3, R4):
#                     print("R1:"+str(R1)+"\nR2:"+str(R2)+"\nR3:"+str(R3)+"\nR4:"+str(R4))
# #
# for i in range(100, 1000, 10):
#     R1 = i
#     for j in range(i, 1000, 10):
#         R2 = j
#         for z in range(j, 1000, 10):
#             R3 = z
#             for t in range(z, 1000, 10):
#                 R4 = z
#                 if check(R1, R2, R3, R4):
#                     print("R1:"+str(R1)+"\nR2:"+str(R2)+"\nR3:"+str(R3)+"\nR4:"+str(R4))
#
# for i in range(1000, 10000, 100):
#     R1 = i
#     for j in range(i, 10000, 100):
#         R2 = j
#         for z in range(j, 10000, 100):
#             R3 = z
#             for t in range(z, 10000, 100):
#                 R4 = z
#                 if check(R1, R2, R3, R4):
#                     print("R1:"+str(R1)+"\nR2:"+str(R2)+"\nR3:"+str(R3)+"\nR4:"+str(R4))
