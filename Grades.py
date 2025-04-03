score = int(input("Score: "))
if score >= 99:
    print("A+")
elif score >= 92 and score <= 98:
 print("A")
elif score >= 90 and score < 92:
    print("A-")
elif score >= 87 and score < 89:
    print("B+")
elif score >= 82 and score < 87:
    print("B")
elif score >= 80 and score < 82:
    print("B-")
elif score >= 77 and score < 80:
    print("C+")
elif score >= 72 and score < 77:
    print("C")
elif score >= 70 and score < 72:
    print("C-")
elif score >= 68 and score < 70:
    print("D+")
elif score >= 63 and score < 68:
    print("D")
elif score >= 60 and score < 63:
    print("D-")
else:
    print("F")