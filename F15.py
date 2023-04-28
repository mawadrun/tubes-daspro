import os
def Savefile(filename,A):
  x = ""
  for C in A:
    i = 0
    for B in C:
      if i != 0 :
        x += ";"
      x += B
      i += 1
    x += "\n"
  f = open(filename,"w+")
  f.write(x)
  f.close()
    
def save():
  folder = input("Masukkan nama folder:")
  if os.path.exists('save'):
    if os.path.exists(f"save/{folder}"):
      pass
    else:
      os.makedirs(f"save/{folder}")
  else:
    os.makedirs('save')
    
  Savefile(f"save/{folder}/users.csv",namamatriks)
  Savefile(f"save/{folder}/bahan_bangunan.csv",)
  Savefile(f"save/{folder}/candi.csv",)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


