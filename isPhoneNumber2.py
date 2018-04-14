import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumbers = phoneNumRegex.findall(message)
print(phoneNumbers)

re.compile( r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

