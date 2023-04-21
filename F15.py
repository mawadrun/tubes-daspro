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
    

