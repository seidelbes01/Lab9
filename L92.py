#The author's name is Sydney Eidelbes

def CountFreq(dictionary):
  freq = {}
  for items in dictionary.values():
    freq[items] = freq.get(items,0)+1
  print(freq)
  
classnames={"lopez":"abigail","aguirre":"anastacia","lombardo":"emma","macrowski":"allison","eidelbes":"sydney","burns":"therese","guo":"mandy","patin":"samantha","antimo":"viviana","newton":"abigail","ward":"elise","bradley":"leena"}

CountFreq(classnames)
    
            
            
