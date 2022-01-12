# print("Week" + 1)     # no, fails to compile
print("Week", 1)        # yes
print("Week" "1")       # no, outputs Week1
print("Week" + str(1))  # no, outputs Week1
print('Week 1')         # yes
print(f"Week {'1'}")    # yes
print("Week 1")         # yes
print("Week", "1")      # yes
print(f"Week {1}")      # yes
print("Week" + "1")     # no, outputs Week1

