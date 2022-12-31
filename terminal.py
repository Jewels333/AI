import pandas as pd

encryptionkey = pd.read_csv(r"<YourPathTo.csv>",
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

def split(message):
    return [char for char in message]

message = 'It is a beautiful day to code something new. In fact, a day like any other,' \ 
' with new projects and ideas. Maybe also new challenges and nerve-racking bugs. Time will tell.'

message_split = split(message)

print('Welcome to the terminal.')
AccessInput = input('Enter Access Key\n')
