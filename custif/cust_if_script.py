
#!/usr/bin/env python3

message = 'You have scored an, '       

print()
print('What was your Test score?')
print()

testscore = float(input())

if testscore >= 90:
    message = message + 'A.'
elif testscore >= 80:
    message = message + 'B.'
elif testscore >= 70:
    message = message + 'C.'
elif testscore >= 60:
    message = message + 'D.'
else:
    message = message + 'F.'
print()
print(message)
print()
