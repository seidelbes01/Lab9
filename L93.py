#The author's name is Sydney Eidelbes

classnames=["abigail","lopez","anastacia","aguirre","emma","lombardo","allison","macrowski","sydney","eidelbes","therese","burns","mandy","guo","samantha","patin","viviana","antimo","abigail","newton","elise","ward","leena","bradley"]

def first_letters(li):
    freq = {}
    for items in li[1::2]:
        items=items[0]
        freq[items] = freq.get(items,0)+1
    print(freq)

first_letters(classnames)
