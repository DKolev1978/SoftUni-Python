import re
text = input()

tx1 = re.findall("fish", text, flags=re.IGNORECASE)
tx2 = re.findall("sun", text, flags=re.IGNORECASE)
tx3 = re.findall("water", text, flags=re.IGNORECASE)
tx4 = re.findall("sand", text, flags=re.IGNORECASE)
tx = tx1 + tx2 + tx3 + tx4

if not tx:
    print(0)
else:
    print(len(tx))