print("Enter your location")
location=input()
if location=="wadakkanchery":
  print("Select Your Restaurants:")
  print('''
  1. Court View
  2. Cafe Hayatt
  3. Shawarma Corner 
  4. Arabian Cornish
  5. Planet Burger''')
  mycart=[]
  totalcost=[]
  sum=0
  x=int(input())
  r=''
  def menu_CV():
    print('''   
    welcome to Court View
    ***********************''')
    print('''
      Please select your category

          a. Main Courses
          b. Hot Beverages
          c. Shakes

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==1:
    r=menu_CV()
    if r=="a":
      print(''' 
         Main Courses    
       ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       bw1  Normal Chicken Shawarma            -     80
       bw2  Whole Meat Chicken shawarma        -     ₹100
       bw3  Kashmiri Barbeque                  -     ₹380
       bw4  Pepper Barbeque                    -     ₹400
       bw5  Al faham Mandi                     -     ₹650''')
      item=["Normal Chicken Shawarma","Whole Meat Chicken shawarma","Kashmiri Barbeque","Pepper Barbeque","Al faham Mandi"]
      price=[80,100,380,400,650]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
        Hot Beverage
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1        Tea                          -     ₹10
       cw2        Coffee                       -     ₹12
       cw3        Lime Tea                     -     ₹15
       cw4        Mint Tea                     -     ₹15
       cw5        Hot Badam                    -     ₹20
       cw6        Masala Tea                   -     ₹20''')
      item=["Tea","Coffee","Lime Tea","Mint Tea","Hot Badam","Masala Tea"]
      price=[10,12,15,15,20,20]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes
      ----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Sharja                         -     ₹60
       dw2      Pista                          -     ₹60
       dw3      Oreo                           -     ₹80
       dw4      Choco Chip Cookie              -     ₹100
       dw5      Dates Magic                    -     ₹100
       dw6      Neapolitan                     -     ₹100
       dw7      Hazelnut Chocolate             -     ₹100
       dw8      Triple Nut Caramel             -     ₹120''')
      item=["Sharja","Pista"," Oreo","Choco Chip Cookie","Dates Magi","Dates Magic","Neapolitan","Hazelnut Chocolate","Triple Nut Caramel"]
      price=[60,60,80,100,100,100,100,120]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
        Your Order has been Placed !!!!
        ----------------------------''')
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680623 or pincode==680624:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680623 or pincode==680624:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680623 or pincode==680624:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                            
  def menu_CH():
    print('''   
      welcome to Cafe Hayatt
     ************************''')
    print('''
      Please select your category

          a. Main courses
          b. Varities of Tea's & coffee
          c. Shakes & Falooda

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==2:
    r=menu_CH()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                              PRICE
      ******      *******                            ******* 
       bw1    Crispy Veg Burger                  -     ₹45
       bw2    Crispy Chicken Burger              -     ₹55
       bw3    Grill Chicken Burger               -     ₹85
       bw4    Normal Shawarma                    -     ₹80
       bw5    Normal Shawarma with cheese        -     ₹100
       bw6    Full Meat Shawarma                 -     ₹110
       bw7    Full Meat Shawarma with cheese     -     ₹130
       bw8    Shawarma Fries                     -     ₹140
       bw9    Al Faham full                      -     ₹370 ''')
      item=["Crispy Veg Burger","Crispy Chicken Burger","Grill Chicken Burger","Normal Shawarma","Normal Shawarma with cheese","Full Meat Shawarma","Full Meat Shawarma with cheese","Shawarma Fries","Al Faham full"]
      price=[45,55,85,80,100,110,130,140,370]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Varities of Tea's & coffee
        -----------------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE          ITEMS                               PRICE
      ******        *******                             ******* 
       cw1        Tea                               -     ₹20
       cw2        Coffee                            -     ₹20
       cw3        Lime Tea                          -     ₹25
       cw4        Espresso                          -     ₹40
       cw5        Cafe Latte                        -     ₹50
       cw6        Cold Brew coffee                  -     ₹65
       cw7        Irish Cold coffee                 -     ₹65
       cw8        Mocha coffee                      -     ₹70''')
      item=["Tea","Coffee","Lime Tea","Espresso","Cafe Latte","Cold Brew coffee","Irish Cold coffee","Mocha coffee"]
      price=[20,20,25,40,50,65,65,70]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes & Falooda
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Vanila                        -     ₹60
       dw2      Chocolate                      -     ₹60
       dw3      Golden Oreo                   -     ₹80
       dw4      Nutella                       -     ₹80
       dw5      ferrero                       -     ₹90
       dw6      Choco Caramel                 -     ₹100
       dw7      Dry Fruit Falooda             -     ₹110''')
      item=["Vanila","Chocolate","Golden Oreo","Nutella","ferrero","Choco Caramel","Dry Fruit Falooda"]
      price=[60,60,80,80,90,100,110]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680623 or pincode==680624:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680623 or pincode==680624:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680623 or pincode==680624:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")

  def menu_SC():
    print('''   
      welcome to Shawarma Corner
     ****************************''')
    print('''
      Please select your category

          a. Shawarma & Wraps
          b. Soft Drinks
          c. Hot Drinks

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==3:
    r=menu_SC()
    if r=="a":
      print(''' 
        Shawarma & Wraps    
      -------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       bw1  Regular Chicken Shawarma           -     ₹80
       bw2  Chicken Crispy Shawarma            -     ₹90
       bw3  Chicken Cheese Shawarma            -     ₹95
       bw4  Whole Meat Shawarma                -     ₹110
       bw5  New Mexican Shawarma               -     ₹130
       bw6  Lebanese Beef Shawarma             -     ₹130
       bw7  Chunky Chicken Wrap                -     ₹90
       bw8  Cheesey Grilled Chicken Wraps      -     ₹110  ''')
      item=["Regular Chicken Shawarma","Chicken Crispy Shawarma","Chicken Cheese Shawarma","Whole Meat Shawarma","New Mexican Shawarma","Lebanese Beef Shawarma","Chunky Chicken Wrap","Cheesey Grilled Chicken Wraps"]
      price=[90,90,95,110,130,130,90,110]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])        
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Soft Drinks
        --------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                  PRICE
      ******      *******                                ******* 
       cw1        Cola                               -     ₹20
       cw2        Sprite                             -     ₹20
       cw3        Mountain Dew                       -     ₹20
       cw4        Fanta                              -     ₹20
       cw5        7up                                -     ₹20
       cw6        Fresh Lemonade                     -     ₹25
       cw7        Sparkling Water                    -     ₹30''')
      item=["Cola","Sprite","Mountain","Fanta","7up","Fresh Lemonade","Sparkling Water"]
      price=[20,20,20,20,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
          Hot Drinks
         ------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Tea                           -     ₹12
       dw2      Coffee                        -     ₹12
       dw3      Lemon Tea                     -     ₹15
       dw4      Sulaimani                     -     ₹15
       dw5      Plain Milk                    -     ₹20
       dw6      Badam Milk Hot                -     ₹25
       dw7      Dry Fruits Honey Milk         -     ₹30''')
      item=["Tea","Coffee","Lemon Tea","Sulaimani","Plain Milk","Badam Milk Hot","Dry Fruits Honey Milk"]
      price=[12,12,15,15,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680623 or pincode==680624:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680623 or pincode==680624:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680623 or pincode==680624:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")

  def menu_AC():
    print('''   
      welcome to Arabian Cornish
     ****************************''')
    print('''
      Please select your category

          a. Main courses
          b. Indian Breads
          c. Sides & Curries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==4:
    r=menu_AC()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
   
       CODE        ITEMS                               PRICE
      ******      *******                             ******* 
       bw1      Veg Biryani                       -     ₹70
       bw2      Chicken Biryani                   -     ₹110
       bw3      Beef Biryani                      -     ₹130
       bw4      Mutton Biryani                    -     ₹160
       bw5      Veg Fried Rice                    -     ₹100
       bw6      Chicken Fried Rice                -     ₹130
       bw7      Grilled Chicken Kabsa             -     ₹230
       bw8      Al Faham Mandi                    -     ₹680
       bw9      Al Faham full                     -     ₹380 ''')
      item=["Veg Biryani","Chicken Biryani","Beef Biryani","Mutton Biryani","Veg Fried Rice","Chicken Fried Rice","Grilled Chicken Kabsa","Al Faham Mandi","Al Faham full"]
      price=[70,110,130,160,100,130,230,680,380]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Indian Breads
        ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                 PRICE
      ******      *******                               ******* 
       cw1        Appam                             -     ₹10
       cw2        Dosa                              -     ₹10
       cw3        Parotta                           -     ₹12
       cw4        Bhatoora                          -     ₹15
       cw5        Roti                              -     ₹15
       cw6        Poori                             -     ₹15
       cw7        Naan                              -     ₹15
       cw8        Cheese Naan                       -     ₹20''')
      item=["Appam","Dosa","Parotta","Bhatoora","Roti","Poori","Naan","Cheese Naan"]
      price=[10,10,12,15,15,15,15,20]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
         Sides & Curries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Veg Kurma                      -     ₹60
       dw2      Egg Curry                      -     ₹70
       dw3      Gopi Manchuri                  -     ₹75
       dw4      Butter Paneer Masala           -     ₹90
       dw5      Chicken Curry                  -     ₹90
       dw6      Beef Curry                     -     ₹100
       dw7      Duck Roast                     -     ₹130
       dw8      Mutton kurma                   -     ₹140
       dw9      Green Salad                    -     ₹45
       dw10     Yoghurt                        -     ₹30''')
      item=["Veg Kurma","Egg Curry","Gopi Manchuri","Butter Paneer Masala","Chicken Curry","Beef Curry","Duck Roast","Mutton kurma","Green Salad","Yoghurt"]
      price=[60,70,75,90,90,100,130,140,45,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6]) 
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="dw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])   
        elif foodorder=="dw10":
          mycart.append(item[9]) 
          totalcost.append(price[9])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680623 or pincode==680624:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680623 or pincode==680624:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680623 or pincode==680624:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")

  def menu_PB():  
    print('''   
      welcome to Planet Burger
     **************************''')
    print('''
      Please select your category

          a. Burgers & Wraps
          b. Beverages
          c. Sides & Fries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==5:
    r=menu_PB()
    if r=="a":
      print(''' 
         Burgers    
       -----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
    
       CODE        ITEMS                            PRICE 
      ******      *******                          ******* 
       bw1  Regular Veg Burger                -     ₹50   
       bw2  Regular Chicken Burger            -     ₹60
       bw3  Double Cheese Burger              -     ₹70
       bw4  Zinger Burger                     -     ₹70
       bw5  Grill Chicken Burger              -     ₹79
       bw6  Chicken Chilli Cheese Burger      -     ₹99
       bw7  Chicken Tandoori Grill Burger     -     ₹120
       bw8  Extra Long Mexican Burger         -     ₹129 ''')
      item=["Regular Veg Burger","Regular Chicken Burger","Double Cheese Burger","Zinger Burger","Grill Chicken Burger","Chicken Chilli Cheese Burger","Chicken Tandoori Grill Burger","Extra Long Mexican Burger"]
      price=[50,60,70,70,79,99,120,129]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Beverages
        -----------------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1       Cola                               -     ₹35
       cw2       Sprite                             -     ₹35
       cw3       Diet Coke                          -     ₹35
       cw4       Sweet Tea                          -     ₹30
       cw5       Strawberry Banana Smoothie         -     ₹80
       cw6       Mango Pineapple Smoothie           -     ₹80
       cw7       Hot Chocolate                      -     ₹90''')
      item=["Cola","Sprite","Diet Coke","Sweet Tea","Strawberry Banana Smoothie","Mango Pineapple Smoothie","Hot Chocolate"]
      price=[35,35,35,30,80,80,90]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Sides & Fries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE         ITEMS                            PRICE
      ******       *******                          ******* 
       dw1      Classic Fries                 -     ₹60
       dw2      Chunky Fries                  -     ₹68
       dw3      Sweet Potato Fries            -     ₹70
       dw4      Chicken Nuggets               -     ₹90
       dw5      Onion Rings                   -     ₹60
       dw6      Chicken Strips                -     ₹120
       dw7      Hash Brownies                 -     ₹40''')
      item=["Classic Fries","Chunky Fries","Sweet Potato Fries","Chicken Nuggets","Onion Rings","Chicken Strips","Hash Brownies"]
      price=[60,68,70,90,60,120,40]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680623 or pincode==680624:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680623 or pincode==680624:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680623 or pincode==680624:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                            
elif location=="shoranur":
  print("Select Your Restaurants:")
  print('''
  1. Arabia
  2. Smake cakes & Bakes
  3. Burger hub
  4. Aboos’s
  5. Cool n fresh''')
  mycart=[]
  totalcost=[]
  sum=0
  x=int(input())
  r=''
  def menu_AR ():
    print('''   
       welcome to Arabia
    ***********************''')
    print('''
      Please select your category

          a. Main Courses
          b. Hot Beverages
          c. Shakes

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==1:
    r=menu_AR()
    if r=="a":
      print(''' 
         Main Courses    
       ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       bw1  chicken Fried rice               -     ₹130
       bw2  Biriyani                         -     ₹100
       bw3  Al faham                         -     ₹380
       bw4  Shawarma                         -     ₹100
       bw5  Al faham Mandi                   -     ₹650''')
      item=["Chicken fried rice","Biriyani","Al faham","Shawarma","Al faham Mandi"]
      price=[130,100,380,100,650]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_AR()
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
        Hot Beverage
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1        Cappuccino                  -     ₹35
       cw2        Cold Coffee                 -     ₹20
       cw3        Fruit tea                   -     ₹15
       cw4        Green Tea                   -     ₹15
       cw5        Hot Badam                   -     ₹20
       cw6        Masala Tea                  -     ₹20''')
      item=["Cappuccino","Cold cofee","Fruit Tea","Green Tea","Hot Badam","Masala Tea"]
      price=[35,20,15,15,20,20]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_AR()
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes
      ----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Kit kat                       -     ₹50
       dw2      Pista                         -     ₹50
       dw3      Oreo                          -     ₹55
       dw4      Chocolate                     -     ₹45
       dw5      Sharja                        -     ₹45
       dw6      Butter sctoch                 -     ₹50
       dw7      Hazelnut Chocolate            -     ₹100
       dw8      Triple Nut Caramel            -     ₹120''')
      item=["Kit kat","Pista"," Oreo","Chocolate","Sharjai","Butter sctoch","Hazelnut Chocolate","Triple Nut Caramel"]
      price=[50,50,55,45,45,50,100,120]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_AR()
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
        Your Order has been Placed !!!!
        ----------------------------''')
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679122 or pincode==679122:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679122 or pincode==679121:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679122 or pincode==679121:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")

  def menu_SM():
    print('''   
      welcome to Smake cakes &bakes
     ********************************''')
    print('''
      Please select your category

          a. Main courses
          b. Varities of cakes
          c. Shakes & Falooda

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==2:
    r=menu_SM()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                              PRICE
      ******      *******                            ******* 
       bw1    Veg Burger                         -     ₹45
       bw2    Crispy Chicken Burger              -     ₹55
       bw3    Bucket chicken                     -     ₹250
       bw4    Normal Shawarma                    -     ₹80
       bw5    Normal Shawarma with cheese        -     ₹100
       bw6    Chinese chopsey                    -     ₹140
       bw7    Full Meat Shawarma with cheese     -     ₹130
       bw8    American chopsey                   -     ₹140
       bw9    Al Faham full                      -     ₹370 ''')
      item=["Veg Burger","Crispy Chicken Burger","Bucket chicken","Normal Shawarma","Normal Shawarma with cheese","chinese chopsey","Full Meat Shawarma with cheese","American chopsey","Al Faham full"]
      price=[45,55,250,80,100,140,130,140,370]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_SM()
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Varities of Cakes &bakes
        -----------------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE          ITEMS                               PRICE
      ******        *******                             ******* 
       cw1        Carrot cake                       -     ₹120
       cw2        Black forest  1kg                 -     ₹620
       cw3        Mango cake 1kg                    -     ₹600
       cw4        starwberry cake 1kg               -     ₹540
       cw5        Exotic black forest cake 1kg      -     ₹700
       cw6        Royal mix fruit cake 1kg          -     ₹765
       cw7        Irish Cofee cake 1kg              -     ₹650
       cw8        Choco chip cake 1kg               -     ₹680''')
      item=["carrot cake","black forest","mango cake","strawberry cake","exotic black forest cake","royal mix fruit cake","irish cofee cake", "choco chip cake"]
      price=[120,620,600,540,700,765,650,680]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_SM()
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes & Falooda
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Vanila                        -     ₹60
       dw2      Chocolate                     -     ₹60
       dw3      Golden Oreo                   -     ₹80
       dw4      Nutella                       -     ₹80
       dw5      ferrero                       -     ₹90
       dw6      Choco Caramel                 -     ₹100
       dw7      Dry Fruit Falooda             -     ₹110''')
      item=["Vanila","Chocolate","Golden Oreo","Nutella","ferrero","Choco Caramel","Dry Fruit Falooda"]
      price=[60,60,80,80,90,100,110]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder==0:
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_SM()
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
        Your Order has been Placed !!!!
        ----------------------------''')
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679122 or pincode==679121:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679122 or pincode==679121:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
            
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679122 or pincode==679121:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                        
  def menu_BH():
    print('''   
      welcome to Burger hub
     ****************************''')
    print('''
      Please select your category

          a. Varieties of burger 
          b. Soft Drinks
          c. Hot Drinks

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==3:
    r=menu_BH()
    if r=="a":
      print(''' 
        Varieties of burger    
      -------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       bw1  Chicken crispy burger              -     ₹120
       bw2  Beef burger                        -     ₹100
       bw3  Chicken Cheese burger              -     ₹155
       bw4  Whole Meat burger                  -     ₹150
       bw5  American cheese burger             -     ₹200
       bw6  Classic cheese smash burger        -     ₹230
       bw7  Burger patty with french fries     -     ₹290
       bw8  Cheesey Grilled Chicken burger     -     ₹210  ''')
      item=["Chicken crispy burger","Beef burger","chicken cheese burger","whole meet burger","american cheese burger","classic cheese smash burger","burger patty with french fries","cheesy grilled chicken burger" ]
      price=[120,100,155,150,200,230,290,210]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])        
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_BH()
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Soft Drinks
        --------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                  PRICE
      ******      *******                                ******* 
       cw1        mountain dew                       -     ₹20
       cw2        Sprite                             -     ₹20
       cw3        cola                               -     ₹20
       cw4        appy fizz                          -     ₹20
       cw5        7up                                -     ₹20
       cw6        lime                               -     ₹25
       cw7        fanta                              -     ₹30''')
      item=["mountain dew","sprite","cola","appy fizz","7up","lime","fanta"]
      price=[20,20,20,20,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_BH()
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
          Hot Drinks
         ------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Cappuccino                     -     ₹30
       dw2      Coffee                         -     ₹12
       dw3      Ginger tea                     -     ₹15
       dw4      cofee mint                     -     ₹25
       dw5      Plain Milk                     -     ₹20
       dw6      Badam Milk Hot                 -     ₹25
       dw7      Dry Fruits Honey Milk          -     ₹30''')
      item=["cappuccino","Coffee","ginger Tea","cofee mint","Plain Milk","Badam Milk Hot","Dry Fruits Honey Milk"]
      price=[30,12,15,25,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_BH()
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
        Your Order has been Placed !!!!
        ----------------------------''')
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679122 or pincode==679121:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')

                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679122 or pincode==679121:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679122 or pincode==679121:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                            
  def menu_AB():
    print('''   
      welcome to Aboos’s
     ********************''')
    print('''
      Please select your category

          a. Main courses
          b. Juices
          c. Sides & Curries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==4:
    r=menu_AB()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
   
       CODE        ITEMS                               PRICE
      ******      *******                             ******* 
       bw1      Porota                            -     ₹10
       bw2      pathiri                           -     ₹15
       bw3      veg biriyani                      -     ₹90
       bw4      Mutton Biryani                    -     ₹160
       bw5      mixed Fried Rice                  -     ₹130
       bw6      Chicken Fried Rice                -     ₹110
       bw7      Grilled Chicken Kabsa             -     ₹230
       bw8      chicken khabab                    -     ₹100
       bw9      Al Faham full                     -     ₹380 ''')
      item=["porota","pathiri", "veg Biryani","Mutton Biryani","mixed Fried Rice","Chicken Fried Rice","Grilled Chicken Kabsa","chicken khabab","Al Faham full"]
      price=[10,15,90,160,130,110,230,100,380]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_AB()
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          juices
        ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                 PRICE
      ******      *******                               ******* 
       cw1        lime                              -     ₹25
       cw2        blue lime                         -     ₹30
       cw3        apple                             -     ₹25
       cw4        anar                              -     ₹25
       cw5        avil milk                         -     ₹25
       cw6        mango                             -     ₹25
       cw7        carrot                            -     ₹30
       cw8        orange                            -     ₹20''')
      item=["lime","blue lime","apple","anar","avil milk","mango","carrot","orange"]
      price=[25,30,25,25,25,25,30,20]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_AB()
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
         Sides & Curries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Veg Kurma                      -     ₹60
       dw2      Chicken curry                  -     ₹120
       dw3      fish curry                     -     ₹120
       dw4      Butter Paneer Masala           -     ₹100
       dw5      Egg curry                      -     ₹90
       dw6      butter chicken                 -     ₹150
       dw7      Duck Roast                     -     ₹130
       dw8      vegetable stew                 -     ₹90
       dw9      beef curry                     -     ₹145
       dw10     gopi manchuri                  -     ₹95''')
      item=["Veg Kurma","chicken curry","fish curry","Butter Paneer Masala","egg curry","butter chicken","Duck Roast","vegetable stew","beef curry","gopi manchuri"]
      price=[60,120,120,100,90,150,130,90,145,95]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6]) 
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="dw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])   
        elif foodorder=="dw10":
          mycart.append(item[9]) 
          totalcost.append(price[9])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_AB()
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
        Your Order has been Placed !!!!
        ----------------------------''')
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679122 or pincode==679121:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679122 or pincode==679121:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679122 or pincode==679121:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                            
  def menu_CF():  
    print('''   
      welcome to Cool n fresh
     *************************''')
    print('''
      Please select your category

          a. Snacks
          b. Beverages
          c. Sides & Fries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==5:
    r=menu_CF()
    if r=="a":
      print(''' 
         Snacks    
       -----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
    
       CODE        ITEMS                            PRICE 
      ******      *******                          ******* 
       bw1  Veg cutlet                        -     ₹15   
       bw2  chicken cutlet                    -     ₹25
       bw3  veg roll                          -     ₹20
       bw4  chicken roll                      -     ₹25
       bw5  chicken sandwitch                 -     ₹35
       bw6  paripuvada                        -     ₹10
       bw7  egg puff                          -     ₹20
       bw8  samosa                            -     ₹15 ''')
      item=["veg cutlet","chicken cutlet","veg roll","chicken roll","chicken sandwitch","paripuvada", "egg puffs","samosa"]
      price=[15,25,20,25,35,10,20,15]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_CF()
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Beverages
        -------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1       Mint                          -     ₹25
       cw2       Sprite                        -     ₹35
       cw3       cold cofee                    -     ₹35
       cw4       tea                           -     ₹10
       cw5       Strawberry Banana Smoothie    -     ₹80
       cw6       dark chocolate                -     ₹80
       cw7       Hot Chocolate                 -     ₹90''')
      item=["mint","Sprite","cold cofee","Tea","Strawberry banana smoothie","dark chocolate","Hot Chocolate"]
      price=[25,35,35,10,80,80,90]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_CF()
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Sides & Fries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE         ITEMS                            PRICE
      ******       *******                          ******* 
       dw1      Hash brownies                 -     ₹40
       dw2      Chunky Fries                  -     ₹68
       dw3      Sweet Potato Fries            -     ₹70
       dw4      prinkles                      -     ₹50
       dw5      Onion Rings                   -     ₹60
       dw6      Chicken fry                   -     ₹120
       dw7      classic fries                 -     ₹60''')
      item=["hash brownies","Chunky Fries","Sweet Potato Fries","prinkles","Onion Rings","Chicken fry","classic fries"]
      price=[40,68,70,50,60,120,60]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
          r=menu_CF()
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
             Your Order has been Placed !!!!
                ----------------------------''')
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0    
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679122 or pincode==679121:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679122 or pincode==679121:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)                     
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679122 or pincode==679121:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!") 
                            
elif location=="ottapalam":
  print("Select Your Restaurants:")
  print('''
  1. Fresh
  2. Aramana
  3. Mr bakers 
  4. Nila
  5. Top notch''')
  mycart=[]
  totalcost=[]
  sum=0
  x=int(input())
  r=''
  def menu_FR():
    print('''   
    welcome to Fresh
    ***********************''')
    print('''
      Please select your category

          a. Main Courses
          b. Hot Beverages
          c. Shakes

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==1:
    r=menu_FR()
    if r=="a":
      print(''' 
         Main Courses    
       ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       bw1  Normal Chicken Shawarma            -     80
       bw2  Whole Meat Chicken shawarma        -     ₹100
       bw3  Kashmiri Barbeque                  -     ₹380
       bw4  Pepper Barbeque                    -     ₹400
       bw5  Al faham Mandi                     -     ₹650''')
      item=["Normal Chicken Shawarma","Whole Meat Chicken shawarma","Kashmiri Barbeque","Pepper Barbeque","Al faham Mandi"]
      price=[80,100,380,400,650]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
        Hot Beverage
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1        Tea                          -     ₹10
       cw2        Coffee                       -     ₹12
       cw3        Lime Tea                     -     ₹15
       cw4        Mint Tea                     -     ₹15
       cw5        Hot Badam                    -     ₹20
       cw6        Masala Tea                   -     ₹20''')
      item=["Tea","Coffee","Lime Tea","Mint Tea","Hot Badam","Masala Tea"]
      price=[10,12,15,15,20,20]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes
      ----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Sharja                         -     ₹60
       dw2      Pista                          -     ₹60
       dw3      Oreo                           -     ₹80
       dw4      Choco Chip Cookie              -     ₹100
       dw5      Dates Magic                    -     ₹100
       dw6      Neapolitan                     -     ₹100
       dw7      Hazelnut Chocolate             -     ₹100
       dw8      Triple Nut Caramel             -     ₹120''')
      item=["Sharja","Pista"," Oreo","Choco Chip Cookie","Dates Magi","Dates Magic","Neapolitan","Hazelnut Chocolate","Triple Nut Caramel"]
      price=[60,60,80,100,100,100,100,120]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
        Your Order has been Placed !!!!
        ----------------------------''')
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679102 or pincode==679101:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679102 or pincode==679101:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)

                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679102 or pincode==679101:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                            
  def menu_AR():
    print('''   
      welcome to Aramana
     ************************''')
    print('''
      Please select your category

          a. Main courses
          b. Varities of Tea's & coffee
          c. Shakes & Falooda

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==2:
    r=menu_AR()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...?  
          Here is our menu, take your time!

       CODE        ITEMS                              PRICE
      ******      *******                            ******* 
       bw1    Crispy Veg Burger                  -     ₹45
       bw2    Crispy Chicken Burger              -     ₹55
       bw3    Grill Chicken Burger               -     ₹85
       bw4    Normal Shawarma                    -     ₹80
       bw5    Normal Shawarma with cheese        -     ₹100
       bw6    Full Meat Shawarma                 -     ₹110
       bw7    Full Meat Shawarma with cheese     -     ₹130
       bw8    Shawarma Fries                     -     ₹140
       bw9    Al Faham full                      -     ₹370 ''')
      item=["Crispy Veg Burger","Crispy Chicken Burger","Grill Chicken Burger","Normal Shawarma","Normal Shawarma with cheese","Full Meat Shawarma","Full Meat Shawarma with cheese","Shawarma Fries","Al Faham full"]
      price=[45,55,85,80,100,110,130,140,370]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Varities of Tea's & coffee
        -----------------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE          ITEMS                               PRICE
      ******        *******                             ******* 
       cw1        Tea                               -     ₹20
       cw2        Coffee                            -     ₹20
       cw3        Lime Tea                          -     ₹25
       cw4        Espresso                          -     ₹40
       cw5        Cafe Latte                        -     ₹50
       cw6        Cold Brew coffee                  -     ₹65
       cw7        Irish Cold coffee                 -     ₹65
       cw8        Mocha coffee                      -     ₹70''')
      item=["Tea","Coffee","Lime Tea","Espresso","Cafe Latte","Cold Brew coffee","Irish Cold coffee","Mocha coffee"]
      price=[20,20,25,40,50,65,65,70]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes & Falooda
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Vanila                        -     ₹60
       dw2      Chocolate                      -     ₹60
       dw3      Golden Oreo                   -     ₹80
       dw4      Nutella                       -     ₹80
       dw5      ferrero                       -     ₹90
       dw6      Choco Caramel                 -     ₹100
       dw7      Dry Fruit Falooda             -     ₹110''')
      item=["Vanila","Chocolate","Golden Oreo","Nutella","ferrero","Choco Caramel","Dry Fruit Falooda"]
      price=[60,60,80,80,90,100,110]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679102 or pincode==679101:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679102 or pincode==679101:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679102 or pincode==679101:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                        
  def menu_MB():
    print('''   
      welcome to Mr bakers
     ****************************''')
    print('''
      Please select your category

          a. Shawarma & Wraps
          b. Soft Drinks
          c. Hot Drinks

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==3:
    r=menu_MB()
    if r=="a":
      print(''' 
        Shawarma & Wraps    
      -------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       bw1  Regular Chicken Shawarma           -     ₹80
       bw2  Chicken Crispy Shawarma            -     ₹90
       bw3  Chicken Cheese Shawarma            -     ₹95
       bw4  Whole Meat Shawarma                -     ₹110
       bw5  New Mexican Shawarma               -     ₹130
       bw6  Lebanese Beef Shawarma             -     ₹130
       bw7  Chunky Chicken Wrap                -     ₹90
       bw8  Cheesey Grilled Chicken Wraps      -     ₹110  ''')
      item=["Regular Chicken Shawarma","Chicken Crispy Shawarma","Chicken Cheese Shawarma","Whole Meat Shawarma","New Mexican Shawarma","Lebanese Beef Shawarma","Chunky Chicken Wrap","Cheesey Grilled Chicken Wraps"]
      price=[90,90,95,110,130,130,90,110]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])        
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Soft Drinks
        --------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                  PRICE
      ******      *******                                ******* 
       cw1        Cola                               -     ₹20
       cw2        Sprite                             -     ₹20
       cw3        Mountain Dew                       -     ₹20
       cw4        Fanta                              -     ₹20
       cw5        7up                                -     ₹20
       cw6        Fresh Lemonade                     -     ₹25
       cw7        Sparkling Water                    -     ₹30''')
      item=["Cola","Sprite","Mountain","Fanta","7up","Fresh Lemonade","Sparkling Water"]
      price=[20,20,20,20,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
          Hot Drinks
         ------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Tea                           -     ₹12
       dw2      Coffee                        -     ₹12
       dw3      Lemon Tea                     -     ₹15
       dw4      Sulaimani                     -     ₹15
       dw5      Plain Milk                    -     ₹20
       dw6      Badam Milk Hot                -     ₹25
       dw7      Dry Fruits Honey Milk         -     ₹30''')
      item=["Tea","Coffee","Lemon Tea","Sulaimani","Plain Milk","Badam Milk Hot","Dry Fruits Honey Milk"]
      price=[12,12,15,15,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679102 or pincode==679101:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679102 or pincode==679101:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679102 or pincode==679101:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                        
  def menu_MB():
    print('''   
      welcome to Nila
     ****************************''')
    print('''
      Please select your category

          a. Main courses
          b. Indian Breads
          c. Sides & Curries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==4:
    r=menu_MB()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
   
       CODE        ITEMS                               PRICE
      ******      *******                             ******* 
       bw1      Veg Biryani                       -     ₹70
       bw2      Chicken Biryani                   -     ₹110
       bw3      Beef Biryani                      -     ₹130
       bw4      Mutton Biryani                    -     ₹160
       bw5      Veg Fried Rice                    -     ₹100
       bw6      Chicken Fried Rice                -     ₹130
       bw7      Grilled Chicken Kabsa             -     ₹230
       bw8      Al Faham Mandi                    -     ₹680
       bw9      Al Faham full                     -     ₹380 ''')
      item=["Veg Biryani","Chicken Biryani","Beef Biryani","Mutton Biryani","Veg Fried Rice","Chicken Fried Rice","Grilled Chicken Kabsa","Al Faham Mandi","Al Faham full"]
      price=[70,110,130,160,100,130,230,680,380]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Indian Breads
        ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                 PRICE
      ******      *******                               ******* 
       cw1        Appam                             -     ₹10
       cw2        Dosa                              -     ₹10
       cw3        Parotta                           -     ₹12
       cw4        Bhatoora                          -     ₹15
       cw5        Roti                              -     ₹15
       cw6        Poori                             -     ₹15
       cw7        Naan                              -     ₹15
       cw8        Cheese Naan                       -     ₹20''')
      item=["Appam","Dosa","Parotta","Bhatoora","Roti","Poori","Naan","Cheese Naan"]
      price=[10,10,12,15,15,15,15,20]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
         Sides & Curries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Veg Kurma                      -     ₹60
       dw2      Egg Curry                      -     ₹70
       dw3      Gopi Manchuri                  -     ₹75
       dw4      Butter Paneer Masala           -     ₹90
       dw5      Chicken Curry                  -     ₹90
       dw6      Beef Curry                     -     ₹100
       dw7      Duck Roast                     -     ₹130
       dw8      Mutton kurma                   -     ₹140
       dw9      Green Salad                    -     ₹45
       dw10     Yoghurt                        -     ₹30''')
      item=["Veg Kurma","Egg Curry","Gopi Manchuri","Butter Paneer Masala","Chicken Curry","Beef Curry","Duck Roast","Mutton kurma","Green Salad","Yoghurt"]
      price=[60,70,75,90,90,100,130,140,45,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6]) 
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="dw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])   
        elif foodorder=="dw10":
          mycart.append(item[9]) 
          totalcost.append(price[9])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679102 or pincode==679101:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679102 or pincode==679101:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)

                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679102 or pincode==679101:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                            


  def menu_NL():  
    print('''   
      welcome to Top notch
     **************************''')
    print('''
      Please select your category

          a. Burgers & Wraps
          b. Beverages
          c. Sides & Fries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==5:
    r=menu_NL()
    if r=="a":
      print(''' 
         Burgers    
       -----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
    
       CODE        ITEMS                            PRICE 
      ******      *******                          ******* 
       bw1  Regular Veg Burger                -     ₹50   
       bw2  Regular Chicken Burger            -     ₹60
       bw3  Double Cheese Burger              -     ₹70
       bw4  Zinger Burger                     -     ₹70
       bw5  Grill Chicken Burger              -     ₹79
       bw6  Chicken Chilli Cheese Burger      -     ₹99
       bw7  Chicken Tandoori Grill Burger     -     ₹120
       bw8  Extra Long Mexican Burger         -     ₹129 ''')
      item=["Regular Veg Burger","Regular Chicken Burger","Double Cheese Burger","Zinger Burger","Grill Chicken Burger","Chicken Chilli Cheese Burger","Chicken Tandoori Grill Burger","Extra Long Mexican Burger"]
      price=[50,60,70,70,79,99,120,129]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Beverages
        -----------------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1       Cola                               -     ₹35
       cw2       Sprite                             -     ₹35
       cw3       Diet Coke                          -     ₹35
       cw4       Sweet Tea                          -     ₹30
       cw5       Strawberry Banana Smoothie         -     ₹80
       cw6       Mango Pineapple Smoothie           -     ₹80
       cw7       Hot Chocolate                      -     ₹90''')
      item=["Cola","Sprite","Diet Coke","Sweet Tea","Strawberry Banana Smoothie","Mango Pineapple Smoothie","Hot Chocolate"]
      price=[35,35,35,30,80,80,90]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Sides & Fries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE         ITEMS                            PRICE
      ******       *******                          ******* 
       dw1      Classic Fries                 -     ₹60
       dw2      Chunky Fries                  -     ₹68
       dw3      Sweet Potato Fries            -     ₹70
       dw4      Chicken Nuggets               -     ₹90
       dw5      Onion Rings                   -     ₹60
       dw6      Chicken Strips                -     ₹120
       dw7      Hash Brownies                 -     ₹40''')
      item=["Classic Fries","Chunky Fries","Sweet Potato Fries","Chicken Nuggets","Onion Rings","Chicken Strips","Hash Brownies"]
      price=[60,68,70,90,60,120,40]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="yes":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==679102 or pincode==679101:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==679102 or pincode==679101:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)

                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==679102 or pincode==679101:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")
                        
elif location=="valapad":
  print("Select Your Restaurants:")
  print('''
  1. Al Baik Fried Chicken
  2. Cafe Manakesh
  3. Shawarma Street 
  4. Black Pepper Restaurant
  5. WereBurger''')
  mycart=[]
  totalcost=[]
  sum=0
  x=int(input())
  r=''
  def menu_CV():
    print('''   
    welcome to Al Baik Fried Chicken
    *********************************''')
    print('''
      Please select your category

          a. Main Courses
          b. Beverages
          c. Shakes

        if you finished your order please enter 'y'!!
                                                   ''')
    y=input()
    return y
  while x==1:
    r=menu_CV()
    if r=="a":
           print(''' 
         Main Courses    
       ----------------''')
           print('''
              can I take your order...? 
          Here is our menu, take your time!
          

       CODE        ITEMS                               PRICE
      ******      *******                             ******* 
       bw1  Fried Chicken 1pc (Normal/Spicy)      -     ₹65
       bw2  Fried Chicken 5pcs                    -     ₹620
       bw4  Chicken popcorn                       -     ₹55
       bw5  Chicken Nuggets 4pcs                  -     ₹45 ''')
           item=["Fried Chicken 1pc (Normal/Spicy)","Fried Chicken 5pcs","Fried Chicken 10pcs","Chicken popcorn","Chicken Nuggets 4pcs"]
           price=[65,310,620,55,45]
           nextorder=True
           while nextorder==True:
             print("Enter the item code : ")
             print("If you finish your order please enter '0'")
             foodorder=input()
             if foodorder=="bw1":
                mycart.append(item[0]) 
                totalcost.append(price[0])
             elif foodorder=="bw2":
                mycart.append(item[1]) 
                totalcost.append(price[1])
             elif foodorder=="bw3":
                mycart.append(item[2]) 
                totalcost.append(price[2])
             elif foodorder=="bw4":
                mycart.append(item[3]) 
                totalcost.append(price[3])
             elif foodorder=="bw5":
                mycart.append(item[4]) 
                totalcost.append(price[4])
             elif foodorder=="0":
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                nextorder=False
             else:
                print("Not In The List.....!")
    if r=="b":
      print('''   
        Hot Beverage
      ----------------''')
      print('''   
            Beverage
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1        Pepsi                        -     ₹35
       cw2        Coca Cola                    -     ₹35
       cw3        Sprite                       -     ₹35
       cw4        Mineral Water                -     ₹15
       cw5        Mountain Dew                 -     ₹35
       cw6        7up                          -     ₹35''')
      item=["Pepsi","Coca Cola","Sprite","Mineral Water","Mountain Dew","7up"]
      price=[35,35,35,15,35,35]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes
      ----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Sharja                         -     ₹60
       dw2      Pista                          -     ₹60
       dw3      Oreo                           -     ₹80
       dw4      Choco Chip Cookie              -     ₹100
       dw5      Dates Magic                    -     ₹100
       dw6      Neapolitan                     -     ₹100
       dw7      Hazelnut Chocolate             -     ₹100
       dw8      Triple Nut Caramel             -     ₹120''')
      item=["Sharja","Pista"," Oreo","Choco Chip Cookie","Dates Magi","Dates Magic","Neapolitan","Hazelnut Chocolate","Triple Nut Caramel"]
      price=[60,60,80,100,100,100,100,120]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
        Your Order has been Placed !!!!
        ----------------------------''')
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680566 or pincode==680567:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680566 or pincode==680567:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680566 or pincode==680567:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")


  def menu_CH():
    print('''   
      welcome to Cafe Manakesh
     ************************''')
    print('''
      Please select your category

          a. Main courses
          b. Varities of Tea's & coffee
          c. Shakes & Falooda

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==2:
    r=menu_CH()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                              PRICE
      ******      *******                            ******* 
       bw1    Crispy Veg Burger                  -     ₹45
       bw2    Crispy Chicken Burger              -     ₹55
       bw3    Grill Chicken Burger               -     ₹85
       bw4    Normal Shawarma                    -     ₹80
       bw5    Normal Shawarma with cheese        -     ₹100
       bw6    Full Meat Shawarma                 -     ₹110
       bw7    Full Meat Shawarma with cheese     -     ₹130
       bw8    Shawarma Fries                     -     ₹140
       bw9    Al Faham full                      -     ₹370 ''')
      item=["Crispy Veg Burger","Crispy Chicken Burger","Grill Chicken Burger","Normal Shawarma","Normal Shawarma with cheese","Full Meat Shawarma","Full Meat Shawarma with cheese","Shawarma Fries","Al Faham full"]
      price=[45,55,85,80,100,110,130,140,370]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Varities of Tea's & coffee
        -----------------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE          ITEMS                               PRICE
      ******        *******                             ******* 
       cw1        Tea                               -     ₹20
       cw2        Coffee                            -     ₹20
       cw3        Lime Tea                          -     ₹25
       cw4        Espresso                          -     ₹40
       cw5        Cafe Latte                        -     ₹50
       cw6        Cold Brew coffee                  -     ₹65
       cw7        Irish Cold coffee                 -     ₹65
       cw8        Mocha coffee                      -     ₹70''')
      item=["Tea","Coffee","Lime Tea","Espresso","Cafe Latte","Cold Brew coffee","Irish Cold coffee","Mocha coffee"]
      price=[20,20,25,40,50,65,65,70]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes & Falooda
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Vanila                        -     ₹60
       dw2      Chocolate                     -     ₹60
       dw3      Golden Oreo                   -     ₹80
       dw4      Nutella                       -     ₹80
       dw5      ferrero                       -     ₹90
       dw6      Choco Caramel                 -     ₹100
       dw7      Dry Fruit Falooda             -     ₹110''')
      item=["Vanila","Chocolate","Golden Oreo","Nutella","ferrero","Choco Caramel","Dry Fruit Falooda"]
      price=[60,60,80,80,90,100,110]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680566 or pincode==680567:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680566 or pincode==680567:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680566 or pincode==680567:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")


  def menu_SC():
    print('''   
      welcome to Cafe Manakesh
     ****************************''')
    print('''
      Please select your category

          a. Shawarma & Wraps
          b. Soft Drinks
          c. Hot Drinks

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==3:
    r=menu_SC()
    if r=="a":
      print(''' 
        Shawarma & Wraps    
      -------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       bw1  Regular Chicken Shawarma           -     ₹80
       bw2  Chicken Crispy Shawarma            -     ₹90
       bw3  Chicken Cheese Shawarma            -     ₹95
       bw4  Whole Meat Shawarma                -     ₹110
       bw5  New Mexican Shawarma               -     ₹130
       bw6  Lebanese Beef Shawarma             -     ₹130
       bw7  Chunky Chicken Wrap                -     ₹90
       bw8  Cheesey Grilled Chicken Wraps      -     ₹110  ''')
      item=["Regular Chicken Shawarma","Chicken Crispy Shawarma","Chicken Cheese Shawarma","Whole Meat Shawarma","New Mexican Shawarma","Lebanese Beef Shawarma","Chunky Chicken Wrap","Cheesey Grilled Chicken Wraps"]
      price=[90,90,95,110,130,130,90,110]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])        
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Soft Drinks
        --------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                  PRICE
      ******      *******                                ******* 
       cw1        Cola                               -     ₹20
       cw2        Sprite                             -     ₹20
       cw3        Mountain Dew                       -     ₹20
       cw4        Fanta                              -     ₹20
       cw5        7up                                -     ₹20
       cw6        Fresh Lemonade                     -     ₹25
       cw7        Sparkling Water                    -     ₹30''')
      item=["Cola","Sprite","Mountain","Fanta","7up","Fresh Lemonade","Sparkling Water"]
      price=[20,20,20,20,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
          Hot Drinks
         ------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Tea                           -     ₹12
       dw2      Coffee                        -     ₹12
       dw3      Lemon Tea                     -     ₹15
       dw4      Sulaimani                     -     ₹15
       dw5      Plain Milk                    -     ₹20
       dw6      Badam Milk Hot                -     ₹25
       dw7      Dry Fruits Honey Milk         -     ₹30''')
      item=["Tea","Coffee","Lemon Tea","Sulaimani","Plain Milk","Badam Milk Hot","Dry Fruits Honey Milk"]
      price=[12,12,15,15,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680566 or pincode==680567:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680566 or pincode==680567:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680566 or pincode==680567:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")


  def menu_AC():
    print('''   
      welcome to Black Pepper Restaurant
     ****************************''')
    print('''
      Please select your category

          a. Main courses
          b. Indian Breads
          c. Sides & Curries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==4:
    r=menu_AC()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
   
       CODE        ITEMS                               PRICE
      ******      *******                             ******* 
       bw1      Veg Biryani                       -     ₹70
       bw2      Chicken Biryani                   -     ₹110
       bw3      Beef Biryani                      -     ₹130
       bw4      Mutton Biryani                    -     ₹160
       bw5      Veg Fried Rice                    -     ₹100
       bw6      Chicken Fried Rice                -     ₹130
       bw7      Grilled Chicken Kabsa             -     ₹230
       bw8      Al Faham Mandi                    -     ₹680
       bw9      Al Faham full                     -     ₹380 ''')
      item=["Veg Biryani","Chicken Biryani","Beef Biryani","Mutton Biryani","Veg Fried Rice","Chicken Fried Rice","Grilled Chicken Kabsa","Al Faham Mandi","Al Faham full"]
      price=[70,110,130,160,100,130,230,680,380]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Indian Breads
        ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                 PRICE
      ******      *******                               ******* 
       cw1        Appam                             -     ₹10
       cw2        Dosa                              -     ₹10
       cw3        Parotta                           -     ₹12
       cw4        Bhatoora                          -     ₹15
       cw5        Roti                              -     ₹15
       cw6        Poori                             -     ₹15
       cw7        Naan                              -     ₹15
       cw8        Cheese Naan                       -     ₹20''')
      item=["Appam","Dosa","Parotta","Bhatoora","Roti","Poori","Naan","Cheese Naan"]
      price=[10,10,12,15,15,15,15,20]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
         Sides & Curries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Veg Kurma                      -     ₹60
       dw2      Egg Curry                      -     ₹70
       dw3      Gopi Manchuri                  -     ₹75
       dw4      Butter Paneer Masala           -     ₹90
       dw5      Chicken Curry                  -     ₹90
       dw6      Beef Curry                     -     ₹100
       dw7      Duck Roast                     -     ₹130
       dw8      Mutton kurma                   -     ₹140
       dw9      Green Salad                    -     ₹45
       dw10     Yoghurt                        -     ₹30''')
      item=["Veg Kurma","Egg Curry","Gopi Manchuri","Butter Paneer Masala","Chicken Curry","Beef Curry","Duck Roast","Mutton kurma","Green Salad","Yoghurt"]
      price=[60,70,75,90,90,100,130,140,45,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6]) 
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="dw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])   
        elif foodorder=="dw10":
          mycart.append(item[9]) 
          totalcost.append(price[9])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680566 or pincode==680567:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680566 or pincode==680567:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680566 or pincode==680567:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")


  def menu_PB():  
    print('''   
      welcome to WereBurger
     **************************''')
    print('''
      Please select your category

          a. Burgers & Wraps
          b. Beverages
          c. Sides & Fries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==5:
    r=menu_PB()
    if r=="a":
      print(''' 
         Burgers    
       -----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
    
       CODE        ITEMS                            PRICE 
      ******      *******                          ******* 
       bw1  Regular Veg Burger                -     ₹50   
       bw2  Regular Chicken Burger            -     ₹60
       bw3  Double Cheese Burger              -     ₹70
       bw4  Zinger Burger                     -     ₹70
       bw5  Grill Chicken Burger              -     ₹79
       bw6  Chicken Chilli Cheese Burger      -     ₹99
       bw7  Chicken Tandoori Grill Burger     -     ₹120
       bw8  Extra Long Mexican Burger         -     ₹129 ''')
      item=["Regular Veg Burger","Regular Chicken Burger","Double Cheese Burger","Zinger Burger","Grill Chicken Burger","Chicken Chilli Cheese Burger","Chicken Tandoori Grill Burger","Extra Long Mexican Burger"]
      price=[50,60,70,70,79,99,120,129]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Beverages
        -----------------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1       Cola                               -     ₹35
       cw2       Sprite                             -     ₹35
       cw3       Diet Coke                          -     ₹35
       cw4       Sweet Tea                          -     ₹30
       cw5       Strawberry Banana Smoothie         -     ₹80
       cw6       Mango Pineapple Smoothie           -     ₹80
       cw7       Hot Chocolate                      -     ₹90''')
      item=["Cola","Sprite","Diet Coke","Sweet Tea","Strawberry Banana Smoothie","Mango Pineapple Smoothie","Hot Chocolate"]
      price=[35,35,35,30,80,80,90]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Sides & Fries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE         ITEMS                            PRICE
      ******       *******                          ******* 
       dw1      Classic Fries                 -     ₹60
       dw2      Chunky Fries                  -     ₹68
       dw3      Sweet Potato Fries            -     ₹70
       dw4      Chicken Nuggets               -     ₹90
       dw5      Onion Rings                   -     ₹60
       dw6      Chicken Strips                -     ₹120
       dw7      Hash Brownies                 -     ₹40''')
      item=["Classic Fries","Chunky Fries","Sweet Potato Fries","Chicken Nuggets","Onion Rings","Chicken Strips","Hash Brownies"]
      price=[60,68,70,90,60,120,40]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680566 or pincode==680567:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680566 or pincode==680567:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680566 or pincode==680567:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")

elif location=="vadanappally":
  print("Select Your Restaurants:")
  print('''
  1. Five Star Fried Chicken
  2. Cafe Victoria
  3. Shawarmashi 
  4. Maharah Restaurant
  5. Burger28''')
  mycart=[]
  totalcost=[]
  sum=0
  x=int(input())
  r=''
  def menu_CV():
    print('''   
    welcome to Five Star Fried Chicken
    *********************************''')
    print('''
      Please select your category

          a. Main Courses
          b. Beverages
          c. Shakes

        if you finished your order please enter 'y'!!
                                                   ''')
    y=input()
    return y
  while x==1:
    r=menu_CV()
    if r=="a":
           print(''' 
         Main Courses    
       ----------------''')
           print('''
              can I take your order...? 
          Here is our menu, take your time!
          

       CODE        ITEMS                               PRICE
      ******      *******                             ******* 
       bw1  Fried Chicken 1pc (Normal/Spicy)     -     ₹65
       bw2  Fried Chicken 5pcs                   -     ₹310
       bw3  Fried Chicken 10pcs                  -     ₹620
       bw4  Chicken popcorn                      -     ₹55
       bw5  Chicken Nuggets 4pcs                 -     ₹45 ''')
           item=["Fried Chicken 1pc (Normal/Spicy)","Fried Chicken 5pcs","Fried Chicken 10pcs","Chicken popcorn","Chicken Nuggets 4pcs"]
           price=[65,310,620,55,45]
           
           
           nextorder=True
           while nextorder==True:
             print("Enter the item code : ")
             print("If you finish your order please enter '0'")
             foodorder=input()
             if foodorder=="bw1":
                mycart.append(item[0]) 
                totalcost.append(price[0])
             elif foodorder=="bw2":
                mycart.append(item[1]) 
                totalcost.append(price[1])
             elif foodorder=="bw3":
                mycart.append(item[2]) 
                totalcost.append(price[2])
             elif foodorder=="bw4":
                mycart.append(item[3]) 
                totalcost.append(price[3])
             elif foodorder=="bw5":
                mycart.append(item[4]) 
                totalcost.append(price[4])
             elif foodorder=="0":
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                nextorder=False
             else:
                print("Not In The List.....!")
    if r=="b":
      print('''   
        Hot Beverage
      ----------------''')
      print('''   
            Beverage
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1        Pepsi                        -     ₹35
       cw2        Coca Cola                    -     ₹35
       cw3        Sprite                       -     ₹35
       cw4        Mineral Water                -     ₹15
       cw5        Mountain Dew                 -     ₹35
       cw6        7up                          -     ₹35''')
      item=["Pepsi","Coca Cola","Sprite","Mineral Water","Mountain Dew","7up"]
      price=[35,35,35,15,35,35]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes
      ----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Sharja                         -     ₹60
       dw2      Pista                          -     ₹60
       dw3      Oreo                           -     ₹80
       dw4      Choco Chip Cookie              -     ₹100
       dw5      Dates Magic                    -     ₹100
       dw6      Neapolitan                     -     ₹100
       dw7      Hazelnut Chocolate             -     ₹100
       dw8      Triple Nut Caramel             -     ₹120''')
      item=["Sharja","Pista"," Oreo","Choco Chip Cookie","Dates Magi","Dates Magic","Neapolitan","Hazelnut Chocolate","Triple Nut Caramel"]
      price=[60,60,80,100,100,100,100,120]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
        Your Order has been Placed !!!!
        ----------------------------''')
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680614 or pincode==680569:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680614 or pincode==680569:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!") 
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680614 or pincode==680569:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")


  def menu_CH():
    print('''   
      welcome to Cafe Victoria
     ************************''')
    print('''
      Please select your category

          a. Main courses
          b. Varities of Tea's & coffee
          c. Shakes & Falooda

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==2:
    r=menu_CH()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                              PRICE
      ******      *******                            ******* 
       bw1    Crispy Veg Burger                  -     ₹45
       bw2    Crispy Chicken Burger              -     ₹55
       bw3    Grill Chicken Burger               -     ₹85
       bw4    Normal Shawarma                    -     ₹80
       bw5    Normal Shawarma with cheese        -     ₹100
       bw6    Full Meat Shawarma                 -     ₹110
       bw7    Full Meat Shawarma with cheese     -     ₹130
       bw8    Shawarma Fries                     -     ₹140
       bw9    Al Faham full                      -     ₹370 ''')
      item=["Crispy Veg Burger","Crispy Chicken Burger","Grill Chicken Burger","Normal Shawarma","Normal Shawarma with cheese","Full Meat Shawarma","Full Meat Shawarma with cheese","Shawarma Fries","Al Faham full"]
      price=[45,55,85,80,100,110,130,140,370]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Varities of Tea's & coffee
        -----------------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE          ITEMS                               PRICE
      ******        *******                             ******* 
       cw1        Tea                               -     ₹20
       cw2        Coffee                            -     ₹20
       cw3        Lime Tea                          -     ₹25
       cw4        Espresso                          -     ₹40
       cw5        Cafe Latte                        -     ₹50
       cw6        Cold Brew coffee                  -     ₹65
       cw7        Irish Cold coffee                 -     ₹65
       cw8        Mocha coffee                      -     ₹70''')
      item=["Tea","Coffee","Lime Tea","Espresso","Cafe Latte","Cold Brew coffee","Irish Cold coffee","Mocha coffee"]
      price=[20,20,25,40,50,65,65,70]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Shakes & Falooda
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Vanila                        -     ₹60
       dw2      Chocolate                      -     ₹60
       dw3      Golden Oreo                   -     ₹80
       dw4      Nutella                       -     ₹80
       dw5      ferrero                       -     ₹90
       dw6      Choco Caramel                 -     ₹100
       dw7      Dry Fruit Falooda             -     ₹110''')
      item=["Vanila","Chocolate","Golden Oreo","Nutella","ferrero","Choco Caramel","Dry Fruit Falooda"]
      price=[60,60,80,80,90,100,110]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680614 or pincode==680569:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680614 or pincode==680569:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680614 or pincode==680569:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
                            else:
                                print("!!!Enter a valid Phone Number!!!")
                                
                          else:
                            ("Delivery is not available at this pincode !!!")


  def menu_SC():
    print('''   
      welcome to Shawarmashi
     ****************************''')
    print('''
      Please select your category

          a. Shawarma & Wraps
          b. Soft Drinks
          c. Hot Drinks

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==3:
    r=menu_SC()
    if r=="a":
      print(''' 
        Shawarma & Wraps    
      -------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       bw1  Regular Chicken Shawarma           -     ₹80
       bw2  Chicken Crispy Shawarma            -     ₹90
       bw3  Chicken Cheese Shawarma            -     ₹95
       bw4  Whole Meat Shawarma                -     ₹110
       bw5  New Mexican Shawarma               -     ₹130
       bw6  Lebanese Beef Shawarma             -     ₹130
       bw7  Chunky Chicken Wrap                -     ₹90
       bw8  Cheesey Grilled Chicken Wraps      -     ₹110  ''')
      item=["Regular Chicken Shawarma","Chicken Crispy Shawarma","Chicken Cheese Shawarma","Whole Meat Shawarma","New Mexican Shawarma","Lebanese Beef Shawarma","Chunky Chicken Wrap","Cheesey Grilled Chicken Wraps"]
      price=[90,90,95,110,130,130,90,110]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])        
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Soft Drinks
        --------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                  PRICE
      ******      *******                                ******* 
       cw1        Cola                               -     ₹20
       cw2        Sprite                             -     ₹20
       cw3        Mountain Dew                       -     ₹20
       cw4        Fanta                              -     ₹20
       cw5        7up                                -     ₹20
       cw6        Fresh Lemonade                     -     ₹25
       cw7        Sparkling Water                    -     ₹30''')
      item=["Cola","Sprite","Mountain","Fanta","7up","Fresh Lemonade","Sparkling Water"]
      price=[20,20,20,20,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
          Hot Drinks
         ------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Tea                           -     ₹12
       dw2      Coffee                        -     ₹12
       dw3      Lemon Tea                     -     ₹15
       dw4      Sulaimani                     -     ₹15
       dw5      Plain Milk                    -     ₹20
       dw6      Badam Milk Hot                -     ₹25
       dw7      Dry Fruits Honey Milk         -     ₹30''')
      item=["Tea","Coffee","Lemon Tea","Sulaimani","Plain Milk","Badam Milk Hot","Dry Fruits Honey Milk"]
      price=[12,12,15,15,20,25,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680614 or pincode==680569:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680614 or pincode==680569:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680614 or pincode==680569:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')


  def menu_AC():
    print('''   
      welcome to Maharah Restaurant
     ****************************''')
    print('''
      Please select your category

          a. Main courses
          b. Indian Breads
          c. Sides & Curries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==4:
    r=menu_AC()
    if r=="a":
      print(''' 
        Main Courses    
      ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
   
       CODE        ITEMS                               PRICE
      ******      *******                             ******* 
       bw1      Veg Biryani                       -     ₹70
       bw2      Chicken Biryani                   -     ₹110
       bw3      Beef Biryani                      -     ₹130
       bw4      Mutton Biryani                    -     ₹160
       bw5      Veg Fried Rice                    -     ₹100
       bw6      Chicken Fried Rice                -     ₹130
       bw7      Grilled Chicken Kabsa             -     ₹230
       bw8      Al Faham Mandi                    -     ₹680
       bw9      Al Faham full                     -     ₹380 ''')
      item=["Veg Biryani","Chicken Biryani","Beef Biryani","Mutton Biryani","Veg Fried Rice","Chicken Fried Rice","Grilled Chicken Kabsa","Al Faham Mandi","Al Faham full"]
      price=[70,110,130,160,100,130,230,680,380]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="bw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Indian Breads
        ----------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                                 PRICE
      ******      *******                               ******* 
       cw1        Appam                             -     ₹10
       cw2        Dosa                              -     ₹10
       cw3        Parotta                           -     ₹12
       cw4        Bhatoora                          -     ₹15
       cw5        Roti                              -     ₹15
       cw6        Poori                             -     ₹15
       cw7        Naan                              -     ₹15
       cw8        Cheese Naan                       -     ₹20''')
      item=["Appam","Dosa","Parotta","Bhatoora","Roti","Poori","Naan","Cheese Naan"]
      price=[10,10,12,15,15,15,15,20]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="cw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
         Sides & Curries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       dw1      Veg Kurma                      -     ₹60
       dw2      Egg Curry                      -     ₹70
       dw3      Gopi Manchuri                  -     ₹75
       dw4      Butter Paneer Masala           -     ₹90
       dw5      Chicken Curry                  -     ₹90
       dw6      Beef Curry                     -     ₹100
       dw7      Duck Roast                     -     ₹130
       dw8      Mutton kurma                   -     ₹140
       dw9      Green Salad                    -     ₹45
       dw10     Yoghurt                        -     ₹30''')
      item=["Veg Kurma","Egg Curry","Gopi Manchuri","Butter Paneer Masala","Chicken Curry","Beef Curry","Duck Roast","Mutton kurma","Green Salad","Yoghurt"]
      price=[60,70,75,90,90,100,130,140,45,30]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6]) 
        elif foodorder=="dw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])
        elif foodorder=="dw9":
          mycart.append(item[8]) 
          totalcost.append(price[8])   
        elif foodorder=="dw10":
          mycart.append(item[9]) 
          totalcost.append(price[9])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680614 or pincode==680569:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680614 or pincode==680569:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680614 or pincode==680569:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')

  def menu_PB():  
    print('''   
      welcome to Burger28
     **************************''')
    print('''
      Please select your category

          a. Burgers & Wraps
          b. Beverages
          c. Sides & Fries

        if you finished your order please enter 'y'!!
                                                    ''')
    y=input()
    return y
  while x==5:
    r=menu_PB()
    if r=="a":
      print(''' 
         Burgers    
       -----------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!
    
       CODE        ITEMS                            PRICE 
      ******      *******                          ******* 
       bw1  Regular Veg Burger                -     ₹50   
       bw2  Regular Chicken Burger            -     ₹60
       bw3  Double Cheese Burger              -     ₹70
       bw4  Zinger Burger                     -     ₹70
       bw5  Grill Chicken Burger              -     ₹79
       bw6  Chicken Chilli Cheese Burger      -     ₹99
       bw7  Chicken Tandoori Grill Burger     -     ₹120
       bw8  Extra Long Mexican Burger         -     ₹129 ''')
      item=["Regular Veg Burger","Regular Chicken Burger","Double Cheese Burger","Zinger Burger","Grill Chicken Burger","Chicken Chilli Cheese Burger","Chicken Tandoori Grill Burger","Extra Long Mexican Burger"]
      price=[50,60,70,70,79,99,120,129]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="bw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="bw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="bw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="bw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="bw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])
        elif foodorder=="bw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="bw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="bw8":
          mycart.append(item[7]) 
          totalcost.append(price[7])          
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="b":
      print('''   
          Beverages
        -----------------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE        ITEMS                            PRICE
      ******      *******                          ******* 
       cw1       Cola                               -     ₹35
       cw2       Sprite                             -     ₹35
       cw3       Diet Coke                          -     ₹35
       cw4       Sweet Tea                          -     ₹30
       cw5       Strawberry Banana Smoothie         -     ₹80
       cw6       Mango Pineapple Smoothie           -     ₹80
       cw7       Hot Chocolate                      -     ₹90''')
      item=["Cola","Sprite","Diet Coke","Sweet Tea","Strawberry Banana Smoothie","Mango Pineapple Smoothie","Hot Chocolate"]
      price=[35,35,35,30,80,80,90]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="cw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="cw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="cw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="cw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="cw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="cw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="cw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="c":
      print('''   
        Sides & Fries
       ------------------''')
      print('''
              can I take your order...? 
          Here is our menu, take your time!

       CODE         ITEMS                            PRICE
      ******       *******                          ******* 
       dw1      Classic Fries                 -     ₹60
       dw2      Chunky Fries                  -     ₹68
       dw3      Sweet Potato Fries            -     ₹70
       dw4      Chicken Nuggets               -     ₹90
       dw5      Onion Rings                   -     ₹60
       dw6      Chicken Strips                -     ₹120
       dw7      Hash Brownies                 -     ₹40''')
      item=["Classic Fries","Chunky Fries","Sweet Potato Fries","Chicken Nuggets","Onion Rings","Chicken Strips","Hash Brownies"]
      price=[60,68,70,90,60,120,40]
      nextorder=True
      while nextorder==True:
        print("Enter the item code : ")
        print("If you finish your order please enter '0'")
        foodorder=input()
        if foodorder=="dw1":
          mycart.append(item[0]) 
          totalcost.append(price[0])
        elif foodorder=="dw2":
          mycart.append(item[1]) 
          totalcost.append(price[1])
        elif foodorder=="dw3":
          mycart.append(item[2]) 
          totalcost.append(price[2])
        elif foodorder=="dw4":
          mycart.append(item[3]) 
          totalcost.append(price[3])
        elif foodorder=="dw5":
          mycart.append(item[4]) 
          totalcost.append(price[4])   
        elif foodorder=="dw6":
          mycart.append(item[5]) 
          totalcost.append(price[5])
        elif foodorder=="dw7":
          mycart.append(item[6]) 
          totalcost.append(price[6])      
        elif foodorder=="0":
          print("Items=",mycart)
          print("Total Cost=",totalcost)
          nextorder=False
        else:
          print("Not In The List.....!")
    if r=="y":
        nextorder=False
        print('''
                Your Items
              -------------''')
        for i in mycart:
          print(i)
        print('''
                 Total Payment
                ---------------''')
        for i in totalcost:
          sum=sum+i
        print("₹",sum)
        x=0
        remove=int(input("If you want remove any item from your order please enter '1' otherwise enter '0'"))
        nextremove=True
        while nextremove==True:
            if remove==0:
                nextremove=False
                pincode=int(input("Enter you delivery pincode: "))
                if pincode==680614 or pincode==680569:
                  name=input("Enter your Name ")
                  housename=input("Enter your House Name ")
                  phoneno=input("Enter your Phone Number ")
                  if len(phoneno)==10 or len(phoneno)==6:
                      print('''
                          Your Order has been delivered to,
                          ''')
                      print("Name       : ",name)
                      print("House Name : ",housename)
                      print("Phone NO   : ",phoneno)
                      print('''
                      "Delivery Person will call you when he reach there"                
                      ''')
                      print('''
                              Your Items
                            -------------''')
                      for i in mycart:
                        print(i)
                      print('''
                               Total Payment
                              ---------------''')
                      for i in totalcost:
                        sum=sum+i
                      print("₹",sum)

                  else:
                      print("!!!Enter a valid Phone Number!!!")
                      
                else:
                  ("Delivery is not available at this pincode !!!")
            elif remove==1:
                sum=0
                print("Items=",mycart)
                print("Total Cost=",totalcost)
                d=int(input("Enter the position of the item to be removed or enter '100'"))
                if d==100:
                    nextremove=False
                    orderconfirm=input('''
                            Please confirm your order(Please Enter '1')
                            
                            if you want to cancel the order please enter '0'
            
                    ''')
                    if orderconfirm=="1":
                      pincode=int(input("Enter you delivery pincode: "))
                      if pincode==680614 or pincode==680569:
                        name=input("Enter your Name ")
                        housename=input("Enter your House Name ")
                        phoneno=input("Enter your Phone Number ")
                        if len(phoneno)==10 or len(phoneno)==6:
                            print('''
                                Your Order has been delivered to,
                                ''')
                            print("Name       : ",name)
                            print("House Name : ",housename)
                            print("Phone NO   : ",phoneno)
                            print('''
                            "Delivery Person will call you when he reach there"
                            ''')
                            print('''
                                    Your Items
                                  -------------''')
                            for i in mycart:
                              print(i)
                            print('''
                                     Total Payment
                                    ---------------''')
                            for i in totalcost:
                              sum=sum+i
                            print("₹",sum)
                        else:
                            print("!!!Enter a valid Phone Number!!!")
                            
                      else:
                        ("Delivery is not available at this pincode !!!")
                else:
                    mycart.pop(d-1)
                    totalcost.pop(d-1)
                    if d==100:
                        nextremove=False
                        orderconfirm=input('''
                                Please confirm your order(Please Enter '1')
                                
                                if you want to cancel the order please enter '0'
                
                        ''')
                        if orderconfirm=="1":
                          pincode=int(input("Enter you delivery pincode: "))
                          if pincode==680614 or pincode==680569:
                            name=input("Enter your Name ")
                            housename=input("Enter your House Name ")
                            phoneno=input("Enter your Phone Number ")
                            if len(phoneno)==10 or len(phoneno)==6:
                                print('''
                                    Your Order has been delivered to,
                                    ''')
                                print("Name       : ",name)
                                print("House Name : ",housename)
                                print("Phone NO   : ",phoneno)
                                print('''
                                "Delivery Person will call you when he reach there"
                                ''')
        
    else:
        print("!! Plaease enter a valid Category !!")   
else:
    print('''
         service is not available in this locality
         -----------------------------------------
                     coming soon!
        ''')
