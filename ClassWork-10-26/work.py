#%%
def funName(name: str, birthYear: int):
    """generates a fun name of

    Args:
        name (str): your name
        birthYear (int): [description]

    Returns:
        [type]: [description]
    """
    names=['cow', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep', 'monkey', 'rooster', 'doggo', 'pig', 'rat']
    return name+' the '+names[-((2021-birthYear)%12)]
# %%
def decode(message):
    decoded=''
    for i in message:
        decoded+=chr(int(i))
    return decoded

#%%
def encode(message):
    encoding=''
    for char in message:
        encoding+= str(ord(char)) + ','
    return encoding.split(',')[:-1]

#%%