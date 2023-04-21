import os
def toCSV(filename,A):
  x=""
  for C in A:
    i=0
    for B in C:
      if i!=0 :
        x+=";"
      x+=B
      i+=1
    x+="\n"
  f=open(filename,"w+")
  f.write(x)
  f.close
    
def save():
  folder=input("Masukkan nama folder:")
  if os.path.exists('save'):
    if os.path.exists(f"save/{folder}"):
      pass
    else:
      os.makedirs(f"save/{folder}")
  else:
    os.makedirs('save')
    
  toCSV(f"save/{folder}/users.csv",namamatriks)
  toCSV(f"save/{folder}/bahan_bangunan.csv",)
  toCSV(f"save/{folder}/candi.csv",)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


