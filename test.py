import re
arn = "arn:aws:iam::123456789012:user/johndoe"

print(arn.split('/')[1])

name = "christopher"
# print(name.capitalize())

string1 = "Hello"
string2 = "World"
result = f'{string1} {string2}!'

# print(result)

# print(len(result))
text = "The quick brown fox"

pattern = r"quick"

match = re.match(pattern, text)
print(match)
if match:
    print("Match found:", match.group())
else:
    print("No match!")