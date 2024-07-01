wel=("WELCOME to BOOK my CINE")
print(wel.center(80))
##logg=[]
##pas=[]


##a=str(input(1.0))
##print(a)
##


##
##class X:
##    def wel(self):
##        wel=("WELCOME to BOOK my CINE")
##        print(wel.center(80))



# a=int(input("Enter"))
# for i in range(a):
#    print("#",end=" ")


# a=input("user name")
# b=input("password")
# c='your password'
# for i in b:
#    print('*',end="")
    




class A():
    def log(self):
        logg=[]
        pas=[]
        log_in=(input("User name : "))
        log_pass=(input("Password : "))
        again_log=(input("re-user name : "))
        again_pass=(input("re-paseword : "))
        if log_in==again_log and log_pass==again_pass:
            print("Correct User name")
        else:
            print("enter the correct username and pass word")
            obj.log()

            
class B(A):
    def hi(self):
        
        
        b="Choose your option\n1.Ticket booking\n2.Ticket price\n3.Exit"
        d="Choose your Theatre\n1.Kg theatre\n2.miraj theatre\n3.central theatre"
        g={"Bolcony":500,"Platinum":300,"Gold":200,"Silver":100}
        
        
        print(b)
        c=[]
        a=int(input("enter option"))
        print(a)
        c.append(a)
        
        
        
        
        
        
        if c[0]==1:
            print(d)
            
            
        
        elif c[0]==2:
            print("---TICKET PRICE---".center(50))
            print(g)
            obj.hi()

            
        elif c[0]==3:
            print("Thank for using the book my cine")
            print(wel.center(80))
            obj.hi()
            
        else:
            print("incorrect value")
            obj.hi()
    
        
        

        
        
            
class C(B):
    def hello(self):
        d="\nChoose your Theatre\n1.Kg theatre\n2.miraj theatre\n3.central theatre"
        e=[]
        f=int(input((1,2,3)))
        
        e.append(f)
        
        if e[0]==1:
            k={1:"The Family Star",2:"Goat",3:"The First Oman",4:"premalu"}
            print(k)
        elif e[0]==2:
            k={1:"The Family Star",2:"Goat",3:"The First Oman",4:"premalu"}
            print(k)
        elif e[0]==3:
            k={1:"The Family Star",2:"Goat",3:"The First Oman",4:"premalu"}
            print(k)
        
        else:
            print("---Please choose correct option---",d)
            obj.hello()




class D(C):
    def tic(self):
        for r in range(1,11):
            for s in range(1,11):
                print("*",end=" ")
            print()
        q=int(input("Choose your row"))
        r=int(input("Choose your coloumn"))

        for o in range(1,11):
            for p in range(1,11):
                if q>0 and q<11 and o>0 and o<11:
                    if q==o and p==r :
                        print("#",end=" ")
                        
                    else:
                        print("*",end=" ") 
                else:
                  print("Please enter correct row and coloumn")
                    
            print()
         
            
class E(D):
    def mon(self):
        print("#","YOU SELECTED YOUR SEAT")
        
        import random
        a=(random.randint(1,10000))
        print("OTP",a)
        otp=int(input("Enter OTP"))
        if a==otp:
            print("Thank you for enter the otp")
            print("Received money")
            print("Ticket Booked\nENJOY THE MOVIE")
        else:
            print("incorrect otp")
            print("Please enter the correct otp")
            obj.mon()


class F(E):
    def mov(self):
        k={1:"The Family Star",2:"Goat",3:"The First Oman",4:"premalu"}
        j=[]
        l=k.keys()
        m=int(input(l))
        j.append(m)
        if j[0]==1:
            print("---Are you Choosed Movie---\n".center(50),k.get(1))
            obj.welcome()
            obj.tic()
            obj.mon()
                
        elif j[0]==2:
            print("---Are you Choosed Movie---\n".center(50),k.get(2))
            obj.welcome()
            obj.tic()
            obj.mon()
            
        elif j[0]==3:
            print("---Are you Choosed Movie---\n".center(50),k.get(3))
        
            obj.welcome()
            obj.tic()
            obj.mon()

        elif j[0]==4:
            print("---Are you Choosed Movie---\n".center(50),k.get(3))
            obj.welcome()
            obj.tic()
            obj.mon()

        else:
            print('***please correctly choose movie***\n',k)
            obj.mov()
        
    
class G(F):
    def welcome(self):
            
            g={"Bolcony":500,"Platinum":300,"Gold":200,"Silver":100}
            print(g)
            w=[]
            v=g.values()
            x=int(input(v))
            w.append(x)
            if w[0]==500:
                print("YOU PAYING AMOUNT=",w)
##                obj.tic()
##                obj.mon()
                
                
            elif w[0]==300:
                print("YOU PAYING AMOUNT=",w)
##                obj.tic()
##                obj.mon()
                
                    
                
            elif w[0]==200:
                print("YOU PAYING AMOUNT=",w)
##                obj.tic()
##                obj.mon()
                
        

            elif w[0]==100:
                print("YOU PAYING AMOUNT=",w)
##                obj.tic()
##                obj.mon()
                
            else :
                print("please enter correct amount")
                obj.welcome()
      

    


##class G(F):
##    def csk(self):
##        import random
##        a=(random.randint(1,10000))
##        print("OTP",a)
##        otp=int(input("Enter OTP"))
##        if a==otp:
##            print("Thank you for enter the otp")
##            print("Send your money")
##            
##            
##        else:
##            print("incorrect otp")
##            print("Please enter the correct otp")
##            obj.csk()
    

        
obj=G()

obj.log()
obj.hi()
obj.hello()
obj.mov()
##obj.tic()
##obj.welcome()
##obj.mon()







##
##a=int(input("Enter"))
##for i in range(a):
##    print("*")














