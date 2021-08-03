from model import *
    
class MainApp():
    material=[]

    def __init__(self):
        i=Material()
        i.set_items(['milk','water','sugar','coffee','tea'])
        i.set_itmcapacity([10000,15000,8000,2000,2000])
        i.set_price([15,10,10,5])
        MainApp.material.append(i)

    def appstart(self):
        self.total=[0,0,0,0]
        while True:
            ch=self.appoption()
            
            if ch==1:
                self.coffee()
                

            elif ch==2:
                self.tea()
                
                
            elif ch==3:
                self.black_coffee()
                
                
            elif ch==4:
                self.black_tea()
                
                
            elif ch==5:
                self.refill()

   
            elif ch==6:
                self.totle()

                
            elif ch==7:
                self.contstatus()

               
            elif ch==8:
                self.rest()

  
            elif ch==9:
                break
                
        
    def appoption(self):
        print("********************************")
        print("1 For Make Coffee              *")
        print("2 For Make Tea                 *")
        print("3 For Make Black Coffee        *")
        print("4 For Make black Tea           *")
        print("5 For Refill Containe          *")
        print("6 For Check Totle Sale         *")
        print("7 For Container Status         *")
        print("8 For Reset container          *")
        print("9 For Exit TCVM                *")
        print("********************************")
        choice=int(input("Enter Your Choice"))
        print("********************************")
        return choice



    def coffee(self):
        cup=int(input("How much coffee you want:- "))
        m=[80,20,15,4,0]
        x=[]   
        for i in MainApp.material:
            if i.get_itmcapacity() > m:
                print("price",i.get_price()[0]*cup)
                for j in range(len(i.get_itmcapacity())):
                    m[j]=m[j]*cup
                    v=i.get_itmcapacity()[j]-m[j]
                    x.append(v)
                i.set_itmcapacity(x)
                self.total[0]+=cup
                cho=input("y/n")
                if cho=='y':
                    ch=self.appstart()
                print("price",i.get_price()[0]*cup)

                    
            else:
                print("********************************")
                print("not enough item to make coffee")
                

        
    def tea(self):
        cup=int(input("How much Tea you want:- "))
        m =[40,60,15,0,5]
        x=[]
        for i in MainApp.material:
            if i.get_itmcapacity() > m:
                print("price",i.get_price()[1]*cup)
                for j in range(len(i.get_itmcapacity())):
                    m[j]=m[j]*cup
                    v=i.get_itmcapacity()[j]-m[j]
                    x.append(v)
                i.set_itmcapacity(x)
                self.total[1]+=cup
                    
            else:
                print("********************************")
                print("not enough item to make tea")
                
                
        
    def black_coffee(self):
        cup=int(input("How much Black coffee you want:- "))
        m =[0,100,15,3,0]
        x=[]
        for i in MainApp.material:
            if i.get_itmcapacity() > m: 
                print("price",i.get_price()[2]*cup)
                for j in range(len(i.get_itmcapacity())):
                    m[j]=m[j]*cup
                    v=i.get_itmcapacity()[j]-m[j]
                    x.append(v)
                i.set_itmcapacity(x)
                self.total[2]+=cup
            else:
                print("*********************************")
                print('not enough item to make black tea')
                
        
        
    def black_tea(self):
        cup=int(input("How much Black Tea you want:- "))
        m =[0,100,15,0,3]
        x=[]
        for i in MainApp.material:
            if i.get_itmcapacity() > m: 
                print("price",i.get_price()[3]*cup)
                for j in range(len(i.get_itmcapacity())):
                    m[j]=m[j]*cup
                    v=i.get_itmcapacity()[j]-m[j]
                    x.append(v)
                i.set_itmcapacity(x)
                self.total[3]+=cup
            else:
                print("********************************")
                print("not enough item to make black tea")
                


        
    def refill(self):
        
        m=int(input("enter for milk"))
        w=int(input("enter for water"))
        s=int(input("enter for sugar"))
        c=int(input("enter for coffee"))
        t=int(input("enter for tea"))
        x=[m,w,s,c,t]
        
        for i in MainApp.material:
            i.set_itmcapacity(x)

            
            
    def totle(self):
        print("---items---item sale---total")
        tot=0
        itm=['coffee      ','tea         ','black coffee','black tea   ']
        for i in MainApp.material:
            for j in range(len(i.get_price())):
                print(itm[j],'  ',self.total[j],"     ",i.get_price()[j]*self.total[j])
                tot+=i.get_price()[j]*self.total[j]
        print('********************************')
        print("total sale is:-",tot)


        
    def contstatus(self):
        rem=[]
        total=[10000,15000,8000,2000,2000]
        for i in MainApp.material:
            for j in range(len(i.get_itmcapacity())):
                rem.append(i.get_itmcapacity()[j])
        for i in MainApp.material:
            for k in range(len(rem)):
                print(i.get_items()[k],'=>',rem[k]*100/total[k],'% left')
                    

            
    def rest(self):
        re=[10000,15000,8000,2000,2000]
        for i in MainApp.material:
            i.set_itmcapacity(re)
        print('********************************')
        print("container reset")

        

m=MainApp()
m.appstart()

