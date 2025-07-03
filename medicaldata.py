import os
import pickle
o="-"*145
def ascend():
   f=open("med.dat", "rb")
   global reclst
   global x
   reclst=[]
   while True:
         try:
             rec=pickle.load(f)
             reclst.append(rec)
         except EOFError:
                break
   if reclst==[]:
         print("\t\t\tEMPTY FILE")
   f.close()
   x=[]
   if reclst!=[]:
        for i in reclst:
              x.append(i["Name"])
   x.sort()
def insertrec():
  print("\t\t\t\t\tEnter salesman details")
  id=input("\n\t\t\t\t\tId                                 : ")
  name=input("\t\t\t\t\tName                               : ")
  co=int(input("\n\t\t\t\t\tDIVISIONS\n\t\t\t\t\t1...Oreon\n\
\t\t\t\t\t2...Vista\n\t\t\t\t\t3...Prima\n\t\t\t\t\tChoose Division             : "))
  if co==1:
      comp="Oreon"
      s=int(input("\n\t\t\t\t\t\tSPECIALITIES\n\t\t\t\t\t1...Dermatology\n\t\t\
\t\t\t2...Orthopaedic\n\t\t\t\t\tChoose Speciality           :"))
      if s==1:
               spec="Dermatology"
      else:
              spec="Orthopaedic"
  elif co==2:
         comp="Vista"
         g=int(input("\n\t\t\t\t\t1...Pediatrics\n\t\t\t\t\t2...Gynaecology\
\n\t\t\t\t\tChoose Speciality      : "))
         if g==1:
              spec="Pediatrics"
         else:
              spec="Gynaecology"
  else:
         comp="Prima"
         h=int(input("\n\t\t\t\t\t1...Gastrology\n\t\t\t\t\t2...Cardiology\n\t\
\t\t\t\tChoose Speciality       : "))
         if h==1:
              spec="Gastrology"
         else:
              spec="Cardiology"
  area=input("\t\t\t\t\tArea                                  : ")
  salary=float(input("\t\t\t\t\tSalary                               : Rs"))
  tar=salary*5
  tart=float(input("\t\t\t\t\tEnter total achievement              : "))
  inc=0
  if tart>tar:
         tara="Target Achieved"
         if tart>=1.01*tar and tart<=1.25*tar:
              inc+=0.05*(tart-tar)
         elif tart>=1.26*tar and tart<=1.5*tar:
              inc+=0.05*(0.25*tar)+0.1*(tart-1.25*tar)
         elif tart>=1.51*tar and tart<=1.75*tar:
              inc+=0.05*(0.25*tar)+0.1*(0.25*tar)+0.15*(tart-1.5*tar)
         elif tart>=1.76*tar and tart<=2.0*tar:
              inc+=0.05*(0.25*tar)+0.1*(0.25*tar)+0.15*(0.25*tar)+0.2*(tart-1.75*tar)
         elif tart>2.0*tar:
              inc+=0.05*(0.25*tar)+0.1*(0.25*tar)+0.15*(0.25*tar)+0.2*(0.25*tar)+0.25*(tart-2.0*tar)
  else:
         tara="Target Not Achieved"
  rec={"Id":id,"Name":name,"Company":comp,"Speciality":spec,"Area":area,"Salary":salary,"\
Target":tar,"Ach":tart,"Incentive":inc}
  f=open("med.dat", "ab")
  pickle.dump(rec, f)
  f.close()
def readrec():
    ascend()
    flag=0
    for j in x:
         for i in reclst:
              if flag==0:
                     print("\n\t\t\t\t\tCURRENT DATA \n")
                     print(o)
                     print("    ID\t     NAME         DIVISION\tSPECIALITY           AREA        SALARY(in Rs)\tTARGET*     \
    ACHIEVEMENT     INCENTIVE")
                     flag=1
              if i["Name"]==j:
                            print(o," "*20,"   ",i["Id"],"   ",i["Name"],"\t  ",i["Company"],"\t",i["Speciality"],"\t   ",i["Area"],"\t",i["Salary"],"\t\
",i["Target"],"\t  ",i["Ach"],"\t",i["Incentive"])  
    print(o)                                      
def repsarea(a):
    h=" "*6+"-"*145

    ascend()
    flag=0
    n=1
    for j in x:
         for i in reclst:
               if i["Area"]==a:
                   n=0
                   if flag==0:
                       print("\n\t\t\t\t\t SALES REPS OF ",a.upper(),"\n")
                       print(h)
                       print("         ID\t      NAME\t\tDIVISION\tSPECIALITY       SALARY     TARGET*         ACHIEVEMENT     \
INCENTIVE")
                       flag=1
                   if i["Name"]==j:
                            print(h)
                            print("       ",i["Id"],"    ",i["Name"],"\t\t",i["Company"],"\t     ",i["Speciality"],"\t",i["Salary"],"  \
",i["Target"],"\t    ",i["Ach"],"\t  ",i["Incentive"])  
    if n==1:
         print("\n\t\t\t\t\tRECORD NOT FOUND")
    elif n==0:
         print(h)
def repscomp(c):
    h=" "*6+"-"*168
    ascend()
    flag=0
    n=1
    for j in x:
         for i in reclst:
               if i["Company"]==c:
                   n=0
                   if flag==0:
                       print("\n\t\t\t\t\tSALES REPS OF ",c.upper(),"\n")
                       print(h)
                       print("        ID\t     NAME\t\tSPECIALITY           AREA                     SALARY     TARGET*     ACHIEVEMENT  \
INCENTIVE")
                       flag=1
                   if i["Name"]==j:
                            print(h)
                            print(" ",i["Id"],"    ",i["Name"],"\t",i["Speciality"],"\t",i["Area"],"\t\t",i["Salary"],"\t    ",i["Target"],"\t \
",i["Ach"],"\t",i["Incentive"])  
    
    if n==1:
         print("\n\t\t\t\t\tRECORD NOT FOUND")
    elif n==0:
         print(h)
def displaydiv(d):
    g="\t"+" "*5+"-"*151
    ascend()
    flag=0
    n=1
    for j in x:
         for i in reclst:
               if i["Speciality"]==d:
                   n=0
                   if flag==0:
                       print("\n\t\t\t\t\tSALES REPS OF ",d.upper())
                       print(g)
                       print("                      ID\t   NAME\t\t  AREA              SALARY        \tTARGET*    \t ACHIEVEMENT     \
INCENTIVE")
                       flag=1
                   if i["Name"]==j:
                            print(g)
                            print("                    ",i["Id"],"    ",i["Name"],"\t",i["Area"],"\t\t",i["Salary"],"\t\t",i["Target"],"\t  ",i["Ach"],"\t\
",i["Incentive"])  
    if n==1:
         print("\n\t\t\t\t\tRECORD NOT FOUND")
    elif n==0:
         print(g)
def searchrec(r):
    f=open("med.dat", "rb")
    flag=False
    while True:
        try:
            rec=pickle.load(f)
            if rec["Id"]==r:
                print("\n","\t"*5,"-"*44)
                print("\t\t\t\t\tId              :  ",rec["Id"])
                print("\t\t\t\t\tName            :  ",rec["Name"])
                print("\t\t\t\t\tDivision        :  ",rec["Company"])
                print("\t\t\t\t\tSpeciality      : ",rec["Speciality"])
                print("\t\t\t\t\tArea            :  ",rec["Area"])
                print("\t\t\t\t\tSalary          :  ",rec["Salary"])
                print("\t\t\t\t\tTarget          :  ",rec["Target"])
                print("\t\t\t\t\tAchievement     :  ",rec["Ach"])
                print("\t\t\t\t\tIncentive       :  ",rec["Incentive"])
                print("\t"*5,"-"*44,"\n")
                flag=True
        except EOFError:
                break
    if flag==False:
        print("\n\t\t\t\t\tRECORD NOT FOUND")
    f.close()
def updatesalary(r):
    f=open("med.dat", "rb")
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
                break
    f.close()
    f=0
    for i in range(len(reclst)):
        if reclst[i]["Id"]==r:
            print("\t\t\t\t\tCurrent Salary      : Rs",reclst[i]["Salary"])
            m=float(input("\t\t\t\t\tEnter New Salary : Rs"))
            reclst[i]["Salary"]=m
            reclst[i]["Target"]=m*5
            f=1
    if f==0:
        print("\n\t\t\t\t\tINVALID ID\n")
    else:
        print("\n\t\t\t\t\tDATA SUCCESSFULLY UPDATED!!!\n")
    f=open("med.dat", "wb")
    for x in reclst:
        pickle.dump(x,f)
    f.close()
def updatearea(r):
    f=open("med.dat", "rb")
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
                break
    f.close()
    z=0
    for i in range(len(reclst)):
        if reclst[i]["Id"]==r:
            print("\t\t\t\t\tCurrent Area              :  ",reclst[i]["Area"])
            a=input("\t\t\t\t\tEnter new area          : ")
            reclst[i]["Area"]=a
            z=1
    if z==0:
        print("\n\t\t\t\t\tINVALID ID")
    f=open("med.dat", "wb") 
    for x in reclst:
        pickle.dump(x,f)
    f.close()
def deleterec(r):
    f=open("med.dat", "rb")
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
                break
            
    f.close()
    f=open("med.dat", "wb")
    fl=0
    for x in reclst:
        if x["Id"]==r:
           fl=1
           continue
        else:
           pickle.dump(x, f)
    if fl==0:
        print("\n\t\t\t\t\tINVALID ID\n")
    else:
        print("\n\t\t\t\t\tDATA SUCCESSFULLY DELETED!!!\n") 
    f.close()
def updatesp(r):
    f=open("med.dat", "rb")
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
                break
    f.close()
    f=0
    for i in range(len(reclst)):
        if reclst[i]["Id"]==r:
            p={"Oreon":["Dermatology","Orthopaedic"],"Vista":["Pediatrics","Gynaecology"],"Prima":["Gastrology","Cardiology"]}
            print("\t\t\t\t\tCurrent Speciality              :  ",reclst[i]["Speciality"])
            a=input("\t\t\t\t\tEnter New Speciality          : ")
            reclst[i]["Speciality"]=a
            for k in p:
                 if a in p[k]:
                      reclst[i]["Company"]=k
            f=1
    if f==0:
        print("\n\t\t\t\t\tINVALID ID")
    f=open("med.dat", "wb") 
    for x in reclst:
        pickle.dump(x,f)
    f.close()
def tac():
    ascend()
    flag=0
    n=1
    for j in x:
         for i in reclst:
               if i["Incentive"]!=0:
                   n=0
                   if flag==0:
                       print("\n\t\t\t\tSALES REPS WHO ACHIEVED THEIR TARGET\n")
                       print(o)
                       print("    ID\t   NAME\t\tDIVISION\tSPECIALITY           AREA                     SALARY     TARGET*     \
ACHIEVEMENT     INCENTIVE")
                       flag=1
                   if i["Name"]==j:
                            print(o)
                            print("   ",i["Id"],"    ",i["Name"],"\t",i["Company"],"\t\t",i["Speciality"],"\t",i["Area"],"\t\t",i["Salary"],"\t   \
",i["Target"],"\t  ",i["Ach"],"\t",i["Incentive"])
    if n==0:
         print(o)
    if n==1:
         print("\n\t\t\t\t\tRECORD NOT FOUND")
def tnc():
    ascend()
    flag=0
    q=1
    for j in x:
         for i in reclst:
               if i["Incentive"]==0:
                   if flag==0:
                       q=0
                       print("\n\t\t\t\tSALES REPS WHO HAVEN'T ACHIEVED THEIR TARGET\n")
                       print(o)
                       print("    ID\t   NAME\t\tDIVISION\tSPECIALITY           AREA                     SALARY     TARGET*     \
ACHIEVEMENT     INCENTIVE")
                       flag=1
                   if i["Name"]==j:
                            print(o)
                            print("   ",i["Id"],"    ",i["Name"],"\t",i["Company"],"\t\t",i["Speciality"],"\t",i["Area"],"\t\t",i["Salary"],"\t    \
",i["Target"],"\t  ",i["Ach"],"\t",i["Incentive"])  
    if q==0:
         print(o)
    else:
         print("\n\t\t\t\t\tRECORD NOT FOUND")
def slab():
     print("\n\t\t\t\t\tINCENTIVE SLAB\n")
     w="\t\t\t\t\t+------------------------------+-----------------------+"
     print(w)
     print("\t\t\t\t\t| Achievement of Target (in %) |    Incentives*         |")
     print(w) 
     print("\t\t\t\t\t| 101-125                      |      5%                |")
     print(w)
     print("\t\t\t\t\t| 126-150                      |    10%                 |")
     print(w) 
     print("\t\t\t\t\t| 151-175                      |    15%                 |")
     print(w)
     print("\t\t\t\t\t| 176-200                      |    20%                 |")
     print(w)
     print("\t\t\t\t\t|  >200                        |    25%                 |")
     print(w)
print("\t\t\t\t\tBIO MEDICA PHARMACEUTICALS\n")
print("\t\t\t\tWELCOME TO SALESMEN'S ANALYSIS TRACKER")
print("\t\t\t\t____________________________________________\n")
while True:
    print("\n\t\t\t\t\t        MENU")
    print("\t\t\t\t\t1...Insert Info")
    print("\t\t\t\t\t2...Display Details")
    print("\t\t\t\t\t3...Modify Info")
    print("\t\t\t\t\t4...Delete Record")
    print("\t\t\t\t\t5...Incentive Slab")
    print("\t\t\t\t\t0...Exit\n")
    ch=input("\t\t\t\t\tEnter your choice           :    ") 
    if ch=="1":
        insertrec()
        print("\n\t\t\t\t\tDATA INSERTED")
        c=input("\t\t\t\t\tEnter c to see the current data : ")
        if c=="c":
             readrec()
    elif ch=="2":
         while True:
               print("\n\t\t\t\t\tCHOOSE A MODE OF DISPLAY")
               print("\t\t\t\t\t1...Display Entire Record\n\t\t\t\t\t2...Display Specific Record\n\t\t\t\t\t3...Display Sales Reps In An Area\
\n\t\t\t\t\t4...Display Sales Reps of a Division\n\t\t\t\t\t5...Display Sales Reps of a Speciality\n\t\t\t\t\t6...Display Sales Reps \
who achieved Target\n\t\t\t\t\t7...Display Sales Reps who haven\'t achieved Target\n\t\t\t\t\t0...Return to Main Menu")
               t=input("\n\t\t\t\t\tEnter your choice       :  ")
               if t=="1":
                     readrec()
               elif t=="2":
                      r=input("\n\t\t\t\t\tEnter salesman id to be searched : ")
                      searchrec(r) 
               elif t=="3":
                      a=input("\t\t\t\t\tEnter area                   :   ")
                      repsarea(a)
               elif t=="4":
                     c=input("\t\t\t\t\tEnter Division             : ")
                     repscomp(c)
               elif t=="5":
                     d=input("\t\t\t\t\tEnter Speciality           :")
                     displaydiv(d)
               elif t=="6":
                     tac()
               elif t=="7":
                     tnc()
               elif t=="0":
                   break
               else:
                   print("\t\t\t\t\tINVALID OPTION")
    elif ch=="3":
      while True:
         print("\n\t\t\t\t\tCHOOSE A MODE OF ALTERATION\n\t\t\t\t\t1...Modify Area\n\t\t\t\t\t2...Modify Salary\n\t\t\t\t\t\
3...ModifySpeciality\n\t\t\t\t\t0...Return to Main Menu")
         h=input("\n\t\t\t\t\tEnter your choice                  :  ")
         if h=="1":
                r=input("\t\t\t\t\tEnter Salesman Id to modify  :  ")
                updatearea(r)
                print("\n\t\t\t\t\tDATA SUCCESSFULLY UPDATED!!!\n")
                c=input("\t\t\t\t\tEnter c to see the current data : ")
                if c=="c":
                    readrec()
         elif h=="2":
               r=input("\n\t\t\t\t\tEnter a salesman id to modify : ")
               updatesalary(r)
               c=input("\t\t\t\t\tEnter c to see the current data : ")
               if c=="c":
                  readrec()
         elif h=="3":
               r=input("\n\t\t\t\t\tEnter a salesman id to modify : ")
               updatesp(r)
               c=input("\t\t\t\t\tEnter c to see the current data : ")
               if c=="c":
                  readrec()
         elif h=="0":
              break
         else:
              print("\t\t\t\t\tINVALID OPTION")
    elif ch=="4":
        r=input("\n\t\t\t\t\tEnter salesman id for deletion : ")
        deleterec(r)
        c=input("\t\t\t\t\tEnter c to see the current data : ")
        if c=="c":
             readrec()
    elif ch=="5":
         slab()
    elif ch=="0":
         break
    else:
        print("\t\t\t\t\tINVALID OPTION")
print("\n\n","="*42,"THANKS!!!","="*60)


