# program to help a user navigate throuhg  a menu
import os
def enterAccountNumber():
    print("24Central Uganda")
    print("Enter Account Number\n0.Back 00.Main Menu")
    choice = str(input("Reply: "))
def mainMenu():
    print("24Central Uganda")
    print("24Central Services")
    print("1. 24Central Money\n2. Voice Bundles\n3. Internet Bundles\n4. Beerako(Borrow)\n5. Hello Tunes\n6. SMS Bundles\n7. My Account\n8. Roaming\n9. Quit")
    choice = str(input("Reply: "))
    
    if choice == '1':
        os.system('cls')
        airtelMoney()
    elif choice == '2':
        os.system('cls')
        voiceBundles()  
    elif choice == '3':
        os.system('cls')
        internetServices()      
    elif choice == '4':
        os.system('cls')
        beerako()    
    elif choice == '5':
        os.system('cls')
        helloTunes()   
    elif choice == '6':
        os.system('cls')
        smsBundle()    
    elif choice == '7':
        os.system('cls')
        myAccount()    
    elif choice == '8':
        os.system('cls')
        roaming()
    elif choice == '9':
        exit()
        
    else:
        print("\n24Central Uganda")
        print("Invalid input\nPlease try again\n")
        mainMenu()
            

#a function to handle airtel money      
def airtelMoney():
    print("24Central Uganda")
    print("24Central Money")
    print("1. Send Money\n2. Airtime/Bundles\n3. Withdraw Cash\n4. Pay Bill\n5. Payment\6. School Fees\n7. Financial Services\n8. Wewole\n9. 24CentralMoney Pay\n10. Back")
    choice = str(input("Reply: "))
    
    if choice == '1':
        os.system('cls')
        sendMoney()  
    elif choice == '2':
        os.system('cls')
        airtimeBundle()
    elif choice == '3':
        os.system('cls')
        withdrawCash()
    elif choice == '4':
        os.system('cls')
        payBill()
    elif choice == '5':
        os.system('cls')
        payment()
    elif choice == '6':
        os.system('cls')
        schoolFees()
    elif choice == '7':
        os.system('cls')
        financialServices()
    elif choice == '8':
        os.system('cls')
        wewole()
    elif choice == '9':
        os.system('cls')
        airtelMoneyPay()
    elif choice == '10':
        os.system('cls')
        mainMenu()
    else:
        os.system('cls')
        print("\n24Central Uganda")
        print("Invalid input\nPlease try again")
        airtelMoney()

    
    #a function for handling how money is sent
    def sendMoney():
        print("24Central Uganda")
        print("Send Money")
        print("1. 24Central and other number\n. 0. Back 00. Main Menuh\n*. Back")
        choice = str(input("Reply: ")) 
        if choice == '1':
            os.system('cls')
            enterNumber()
        elif choice == '0':
            os.system('cls')
            airtelMoney()
        elif choice == '00':
            os.system('cls')
            mainMenu()
        else:
            os.system('cls')
            print("\n24Central Uganda")
            print("Invalid input\nPlease try again")
            sendMoney()
                 
        def enterNumber():
            print("24Central Uganda")
            print("Enter Number")
            print("0. Back 00. Main Menu")
            choice1 = input("Reply: ")
            if choice == '0':
                os.system('cls')
                sendMoney()
            elif choice == '00':
                os.system('cls')
                mainMenu()
            else:
                os.system('cls')
                print("\n24Central Uganda")
                print("Invalid input\nPlease try again")
                enterNumber()
            #this will need function that checks if the customer has enough money in his account
    
    #afunction for handling the buy of airtime                    
    def airtimeBundle():
        print("24Central Uganda")
        print("Airtime Bundle")
        print("1. Buy Airtime\n2. Buy Data Bundle(Offers inside)\n3. Buy Voice Bundles\n4. IControl\n5. OTT Servce Tax\n0. Back 00. Main Menu\n* Back")
        choice = str(input("Reply: "))
        if choice =='1':
            os.system('cls')
            buyAirtime()
        elif choice == '2':
            os.system('cls')
            buyData()
            
        else:
            os.system('cls')
            print("\n24Central Uganda")
            print("Invalid input\nPlease try again")
            airtimeBundle()
            
        def buyAirtime():
            print("24Central Uganda")
            print("Buy Airtime")
            print("1. For Myself\n2. For Another Number\n0. Back 00. Main Menu\n* Back")
            if choice == '1':
                os.system('cls')
                airtimeForMyself()
            elif choice == '2':
                os.syetem('cls')
                airtimeForAnother()
                
            else:
                os.system('cls')
                print("\n24Central Uganda")
                print("Invalid input\nPlease try again")
                buyAirtime()
                
            def airtimeForMyself():
                print("24Central Uganda")
                print("For Myself")
                print("Enter Amount")
                choice = str(input("Reply: "))
                #will come back here later
                
            def airtimeForAnother():
                print("24Central Uganda")
                print("For Another Number")
                print("Enter Number")
                choice = ("Reply: ")
                if len(choice) == 10:
                    if choice[0] == '0' and choice[1] == '7' and choice[2] == '5' or '0':#begin from here
                        print("begin")
                        
                elif:
                    print('24Central Uganda')
                    print('Digits must be 10')
                    airtimeForAnother()
                
        def buyData():
                print("24Central Uganda")
                print("Buy Data Bundles")
                print("1. Data For Myself")
                print("2. Data For Another Number")
                print("0. Back 00. Main Menu")
                choice = str(input("Reply: "))
                
                def dataForMyself():
                    print("24Central Uganda")
                    print("Data For Myself")
                    print("1. Daily Bundle\n2. Weekly Bundle\n3. Monthly Bundle\n4. Quaterly Bundle\n5. Data ONLY OTT Pack\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
                    def dailyBundle():
                        print("24Central Uganda")
                        print("Daily Bundle")
                        print("1. 250/- for 15MB\n2. 500/- for 40MB\n3. 100/- for 100MB\n4. 2000/- for 300MB\n5. 3000/- for 500MB\n6. 2000/- for Night Pack 1GB\n7. More\n0. Back 00. Main Menu")
                        choice = str(input("Reply: "))
                        
                        def dailyMore():
                            print("24Central Uganda")
                            print("More")
                            print("1. 5000/- for 1GB (3days\n2. 10000/- for 3GB (3 days)\n0. Back 00. Main Menu")
                            choice = str(input("Reply: "))
                                    
                    def weeklyBundle():
                        print("24Central Uganda")
                        print("Weekly Bundle")
                        print("1. 7000/- for 1.17GB\n2. 15000/- for 4GB\n3. 20000/- for 7GB\n4. More\n0. Back 00. Main Menu")
                        choice = str(input("Reply: "))
                        
                        def weeklyMore():
                            print("24Central Uganda")
                            print("More")
                            print("1. 2000/- for 150MB\n2. 3500/- for 400MB\n0. Back 00. Main Menu")
                            choice = str(input("Reply: "))
                                
                    def monthlyBundle():
                        print("24Central Uganda")
                        print("Monthly Bundle")
                        print("1. 30000/- for 9GB\n2. 50000/- for 20GB\n3. 90000/- for 25GB\n4. 150000/- for 65GB\n5. More\n0. Back 00. Main Menu")
                        choice = str(input("Reply: "))
                        
                        def monthlyMore():
                            print("24Central Uganda")
                            print("More")
                            print("1. 5000/- for 500MB\n2. 10000/- for 1.5GB\n0. Back 00. Main Menu")
                            choice = str(input("Reply: "))
                            
                    def quaterlyBundle():
                        print("24Central Uganda")
                        print("Quaterly Bundle")
                        print("1. 39000/- for 4GB\n2. 780000/- for 10GB\n3. 130000/- for 20GB\n4. 450000/- for 85GB\n0. Back 00. Main Menu")
                        choice = str(input("Reply: "))
                                
                    def ottBundle():
                        print("24Central Uganda")
                        print("Data ONLY OTT Pack")
                        print("1. Daily Data + OTT Pack\n2. Weekly Data + OTT Pack\n3. Monthly Data + OTT Pack\n0. Back 00. Main Menu")
                        choice = str(input("Reply: "))
                        
                        def ottDaily():
                            print("24Central Uganda")
                            print("Daily Data + OTT Pack")
                            print("1. 450/- for 15MB + OTT\n2. 700/-for 40MB + OTT\n3. 1200/- for 100MB + OTT\n4. 5600/- for 1GB (3 Days) + OTT\n0. Back 00. Main Menu")
                            choice = str(input("Reply: "))
                        
                        def ottWeekly(): 
                            print("24Central Uganda")
                            print("Weekly Data + OTT Pack")
                            print("1. 8400/- for 1GB + OTT\n2. 21400/-for 5GB + OTT\n3. terminate_581085\n0. Back 00. Main Menu")
                            choice = str(input("Reply: "))
                            
                        def ottMonthly():
                            print("24Central Uganda")
                            print("Monthly Data + OTT Pack")
                            print("1. 26000/- for 1.75GB + OTT\n2. 36000/-for 5GB + OTT\n3. 56000/- for 12GB + OTT\n0. Back 00. Main Menu")
                            choice = str(input("Reply: "))
                            
                def dataForAnother():
                    print("24Central Uganda")
                    print("Enter Mobile Number")
                    print("0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
        def voiceBundle():
                print("24Central Uganda")
                print("Buy Voice Bundles")
                print("1. Voice Bundles For Myself\n2. Voice Bundles For Another\n0. Back 00. Main Menu\n* Back")
                choice = str(input("Reply: "))
                
                def voiceForMyself():
                    print("24Central Uganda")
                    print("1. Kawa\n2. Pakalast\n3. Kyabise\n4. Mega Bonus\n5. Power\n6. Voice\n0. Back 00. Main Menu\n* Back")
                    choice = str(input("Reply: "))
                    
                    def voice():
                        print("24Central Uganda")
                        print("1. Kawa 500\n2. Kawa 600\n3. Kawa Weekly\n0. Back 00. Main Menu\n* Back")
                        choice = str(input("Reply: "))
                        
                    def pakalast():
                        print("24Central Uganda")
                        print("1. Kika/Pakalast\n2. Paka 1200\n3. Paka Night\n4. Paka Weekly\n0. Back 00. Main Menu\n* Back")
                        choice = str(input("Reply: "))
                            
                    def kyabise():
                        print("24Central Uganda")
                        print("1. Kyabise Combo10\n2. Kyabise Combo20\n3. Kyabise Combo75\n4. Kyabise Night\n5. Kyabise Weekly\n6. Kyabise Monthly\n7. Kyabise 50K\n0. Back 00. Main Menu\n* Back")
                        choice = str(input("Reply: "))
                        
                    def megaBonus():
                        print("24Central Uganda")
                        print("1. Mega Bonus 10K\n2. Mega Bonus25K\n3. Mega Bonus 30K\n4. Mega Bonus 50K\n5. Mega Bonus 100K\n6. Kyabise Monthly\n7. Kyabise 50K\n0. Back 00. Main Menu\n* Back")
                        choice = str(input("Reply: "))
                        
                    def power():
                        print("24Central Uganda")
                        print("1. POWER_TOOTI\n2. POWER_TOOTI2\n0. Back 00. Main Menu\n* Back")
                        choice = str(input("Reply: "))
                        
                    def voice():
                        print("24Central Uganda")
                        print("1. Voice_125min\n2. Voice_300min\n3. 100mins@2000\n4. 300min@5000-3days\n5. 45mins@2k_weekly\n0. Back 00. Main Menu\n* Back")
                        choice = str(input("Reply: "))
                        
                def voiceForAnother():
                    print("24Central Uganda")
                    print("Enter Mobile Number")
                    print("0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
        def icontrol():
            print("24Central Uganda")
            print("IControl")
            print("1. Subscribe\n2. Make Payment\n0. Back 00. Main Menu")
            choice = str(input("Reply: ")) 
            
            def subscribe():
                print("24Central Uganda")
                print("Subscribe")
                print("1. IControl 60K\n2. IControl 200K\n3. IControl 300K\n4. IControl 500K0. Back 00. Main Menu")
                choice = str(input("Reply: "))  
                
        def ottServiceTax():
            print("24Central Uganda")
            print("OTTService Tax")
            print("1. For Self\n2. For Others\n0. Back 00. Main Menu")
            choice = str(input("Reply: ")) 
            
            def forSelf():
                print("24Central Uganda")
                print("OTT Servcie Tax For Self")
                print("1. Daily Tax -200/-\n2. Weekly Tax -1,400\n3. Monthly Tax -6,000/-\nQuaterly Tax -18,000/-\n4. Annual Tax -73,000/-\n0. Back 00. Main Menu")
                choice = str(input("Reply: "))
                
            def forOthers():
                print("24Central Uganda")
                print("OTT Servcie Tax For Others")
                print("1. Daily Tax -200/-\n2. Weekly Tax -1,400\n3. Monthly Tax -6,000/-\nQuaterly Tax -18,000/-\n4. Annual Tax -73,000/-\n0. Back 00. Main Menu")
                choice = str(input("Reply: "))
                
                def enterNumber():
                    print("Enter Number to Pay For")
                    print("0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                
    #a function for handling withdrawal of cash                                                             
    def withdrawCash():
        print("24Central Uganda")
        print("Enter Amount\n0. Back 00. Main Menu\n* Back")
        choice = str(input("Reply: "))
        
        def enterPin():
            print("24Central Uganda")
            print("Withdrawal of /amount/ charge UGX /amount/. Comfirmwith your PIN\n0. Back 00. Main Menu\n* Back")
            #will continue with this later
    
    #a function manage payment of bills        
    def payBill():
        print("Pay Bill")
        print("1. UMEME TouchPay\n2. Water\n3. Pay TV\n4. Pay Solar\n5. UEDCL\6. KCCA\n7. URA\n8. 24Central Postpaid\n9. Others\n10. Next\n* Back")
        choice = str(input("Reply: "))
        
        #a funtion to handle umeme payment
        def payUmeme():
            print("24Central Uganda")
            print("1. Pay Bill\2. Pay YAKA\n3. check UMEME balance\n4. Token Enquiry\n0. Back 00. Main Menu")
            choice = str(input("Reply: "))
            
            def payBil():
                print("24Central Uganda")
                print("Enter UMEME A/C Number\n0. Back 00.Main Menu")
                choice = str(input("Reply: "))
                
            def yaka():
                print("24Central Uganda")
                print("Enter YAKA Number\n0. Back 00.Main Menu")
                choice = str(input("Reply: "))
                
            def checkUmemeBalance():
                print("24Central Uganda")
                print("Enter UMEME A/C Number\n0. Back 00.Main Menu")
                choice = str(input("Reply: "))
                
            def tokenEnquiry():
                print("24Central Uganda")
                print("Please Enter 24Central Money Transaction ID\n0. Back 00.Main Menu")
                choice = str(input("Reply: "))
            
            #a function handle water payment bill       
        def water():
            print("24Central Uganda")
            print("Water")
            print("1. Pay NWSC\n2. Check NWSC Balance\n0. Back 00.Main Menu")
            choice = str(input("Reply: "))
            
            def nwsc():
                print("24Central Uganda")
                print("0. Back 00. Main Menu")
                choice = str(input("Reply: "))
            
            def nwscBalance():
                print("24Central Uganda")
                print("0. Back 00. Main Menu")
                choice = str(input("Reply: "))
            
            #a function to handle pay tv subscriptions       
        def payTv():
            print("24Central Uganda")
            print("Pay TV")
            print("1. DSTV / GOTV\n2. STARTIMES TV\n3. AZAM TV\4. SIMBA TV\n5. KWESE TV\n0. Back 00. Main Menu")
            choice = str(input("Reply: "))
            
            #dstv and gotv subscription
            def dstvGotv():
                print("24Central Uganda")
                print("1. Pay DSTV\n2. Pay GOTV\n3. Bouquet Prices\n0. Back 00. Main Menu")
                choice = str(input("Reply: "))
                
                #dstv subscription
                def dstv():
                    print("24Central Uganda")
                    print("Enter your DSTV number\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                
                #gotv subscription    
                def gotv():
                    print("24Central Uganda")
                    print("Enter your GOTV number\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
                def bouquetPrices():
                    print("24Central Uganda")
                    print("Enter your PIN to confirm\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
            
            #startimes tv subscription        
            def startimes():
                print("24Central Uganda")
                print("1. Pay Startimes\n2. View Card Details\n3. Change Bouquet\n0. Back 00. Main Menu")
                choice = str(input("Reply: "))
                
                def payStartimes():
                    print("24Central Uganda")
                    print("Enter Startimes card number\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))

                def viewCardDetails():
                    print("24Central Uganda")
                    print("Enter STARTIMES card number\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
                def changeBouquet():
                    print("24Central Uganda")
                    print("Enter Startimes card number\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
            
            #azam tv subscription         
            def azam():
                print("24Central Uganda")
                print("1. AZAM TV\n2. Mobile TV\n0. Back 00. Main Menu")
                choice = str(input("Reply: "))
                
                def azamTv():
                    print("24Central Uganda")
                    print("Enter the Card Number\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
                def azamMobile():
                    print("24Central Uganda")
                    print("Please enter reference?Mobile Number of TV Subscriber\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                
                #simba TV subscription       
            
            #Simba tv subscription
            def simba():
                print("24Central Uganda")
                print("Enter Simba TV A/C number\n0. Back 00. Main Menu")
                choice = str(input("Reply: "))
            
            #kwese tv subscription    
            def kwese():
                print("24Central Uganda")
                print("KweseIflix Subscription payment")
                print("1. 1 DAy Pass+1GB( 5K UGX)\n2. 3 Day Pass+2GB( 10K UGX)\n3.7 Day Pass+3GB( 20KUGX)\n4. 30 Day Pass+20GB(55K UGX)\n0. Back 00. Main Menu")
                choice = str(input("Reply: "))
                
                def aday():
                    print("24Central Uganda")
                    print("Confirm your purchase of 1 DAY 5000 KweseIflix VIP Pass\n1. Confrim\n2. Cancel\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
                    def adayConfrim():
                        print("24Central Uganda")
                        print("Pay Kwese\nAmount : 5000\nCharge : UGX 0\nEnter PIN to confrim\n0. Back 00. Main Menu")
                        choice = str(input("Reply: "))
                        
                    #def adayCancel():
                        
                        
                def threeDay():
                    print("24Central Uganda")
                    print("Confirm your purchase of 3 DAY 10000 KweseIflix VIP Pass\n1. Confrim\n2. Cancel\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
                    def threeDayConfrim():
                        print("24Central Uganda")
                        print("Pay Kwese\nAmount : 10000\nCharge : UGX 0\nEnter PIN to confrim\n0. Back 00. Main Menu")
                        choice = str(input("Reply: "))
                        
                    #def threeDayCancel():
                    
                def sevenDay():
                    print("24Central Uganda")
                    print("Confirm your purchase of 7 DAY 20000 KweseIflix VIP Pass\n1. Confrim\n2. Cancel\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
                    def sevenDayConfrim():
                        print("24Central Uganda")
                        print("Pay Kwese\nAmount : 20000\nCharge : UGX 0\nEnter PIN to confrim\n0. Back 00. Main Menu")
                        choice = str(input("Reply: "))
                        
                    #def sevenDayCancel():
                    
                def thirtyDay():
                    print("24Central Uganda")
                    print("Confirm your purchase of 30 DAY 55000 KweseIflix VIP Pass\n1. Confrim\n2. Cancel\n0. Back 00. Main Menu")
                    choice = str(input("Reply: "))
                    
                    def thirtyDayConfirm():
                        print("24Central Uganda")
                        print("Pay Kwese\nAmount : 55000\nCharge : UGX 0\nEnter PIN to confrim\n0. Back 00. Main Menu")
                        choice = str(input("Reply: "))
                        
                    #def thirtyDayCancel():
                    
                #Begin from here next time
                    
            #a function to handle solar payment
        def paySolar():
                print("24Central Uganda")
                print("Pay Solar\n1. MKOPA Solar\n2. DLIGHT Solar\n3. Sun King\n4. SOLAR Now\n5.VILLAGE Power\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
                #This function will be called by all items in the menu
                def chooseOption():
                    print("24Central Uganda")
                    print("Enter Amount\n0.Back 00.Main Menu")
                    choice = str(input("Reply: "))
                    
        #a function to handle uedcl payment
        def uedcl():
            print("24Central Uganda")
            print("Enter Meter Number\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
        #a function to handle kcca payments
        def kcca():
            print("24Central Uganda")
            print("Enter Your Reference Number\n0.Back 00.Main Menu")
            choice = str(input("Reply: ")) 
            
        #a function handle ura payments
        def ura():
            print("24Central Uganda")
            print("URA\n1. Pay Registered\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
            def prnNumber():
                print("24Central Uganda")
                print("Enter the PRN/PTN Number you wish to pay for\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))    
            
        def airtelPostpaid():
            print("24Central Uganda")
            print("Enter postpaid Number\n0.Back 00.Main Menu")
            choice = str(input("Reply: ")) 
            
        def others():
            print("24Central Uganda")
            print("Enter Business Number\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
        def next():
            print("24Central Uganda")
            print("1. WENRECO\n2. Local Government Payments\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))  
            
            def wenreco():
                print("24Central Uganda")
                print("WENRECO\n1. Buy Units\n2. Check Wenreco service Fee\n0.Back 00.Main Menu")
                choice = str(input("Reply: ")) 
                
                def buyUnits():
                    print("24Central Uganda")
                    print("Enter WENRECO Meter Number\n0.Back 00.Main Menu")
                    choice = str(input("Reply: "))
                    
                def checkServiceFee():
                    print("24Central Uganda")
                    print("Enter WENRECO A/C Number\n0.Back 00.Main Menu")
                    choice = str(input("Reply: "))
                    
            def localGovernment():
                print("24Central Uganda")
                print("No trusted certificate found")
                
    #a function to handle payments
    def payment():
        print("24Central Uganda")
        print("Payments\n1. PayEasy\2. Multiplex\3. BETTING and GAMING\n4. Uganda Cranes\n5. Kabaka Run\n6. UNEB\n7. Mobipay\n0.Back 00.Main Menu")
        choice = str(input("Reply: ")) 
        
        def payEasy():
            print("24Central Uganda")
            print("Enter Business Number\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))  
            
        def multiplex():
            print("24Central Uganda")
            print("Multiplex\n1. Pay Multiplex\n2. View Multiplex Balance\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
            def payMultiplex():
                print("24Central Uganda")
                print("Enter your Vehicle Reg. No\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
            def viewMultiplexBalance():
                print("24Central Uganda")
                print("Enter your Vehicle Reg. No\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
        def bettingGaming():
            print("24Central Uganda")
            print("BETTING and GAMING\n1. Kagwirawo\n2. Betway\n3. BetPawa\n4. ElitBet\n5. BetLion\n6. WorldStar\n7. AbaBet\n8. Betin\n9. Grand Victoria\n10. Next\n11. Betcity\n12. MojaBet\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
            def kagwirawo():
                print("24Central Uganda")
                print("Kagwirawo\n1. Bet\n2. Deposit\n3. My receipts\n4. Check Balance\n5. Withdraw\n6. Register\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
                def bet():
                    #if u dont have an account
                    print("24Central Uganda")
                    print("You are not yet registered. Please register for a Kagwirawo account first.")#beging from here
                    
        def ugandCranes():
            print("24Central Uganda")
            print("Buy your ticket")
            print("1. Ordinary - 15,000\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
            def payOrdinary():
                print("24Central Uganda")
                print("Dial *185*5# to pay for your ordinary ticket")
                
        def kabakaRun():
            print("24Central Uganda")
            print("Enter Amount\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
        def uneb():
            print("24Central Uganda")
            print("Enter Invoice Number\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
        def mobipay():
            print("24Central Uganda")
            print("Enter Merchant Code\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
    #a function to handle payment of school fees
    def schoolFees():
        print("24Central Uganda")
        print("School Fees\1. Bridge Schools\n2. School Pay\n3. Flexipay\n0.Back 00.Main Menu")
        choice = str(input("Reply: "))
        
        def bridgeSchools():
            print("24Central Uganda")
            print("Enter pupil Id\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
        def schoolPay():
            print("24Central Uganda")
            print("School Pay\n1. Pay Fees\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
            def schoolCode():
                print("24Central Uganda")
                print("Enter School Code\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
    
    #a function to handle financial services            
    def financialServices():
        print("24Central Uganda")
        print("Financial Services\n1. Banks\n2. Group Collections\n3. M-SACCO\n4. ATM Withdrawal\n5. NSSF Savings\n0.Back 00.Main Menu")
        choice = str(input("Reply: "))  
        
        def banks(): 
            print("24Central Uganda")
            print("Banks\1. Equity\n2. Centenary\n3. Pride Microfinance\n4. Barclays Bank\n5. DFCU\n6. Bank Of Africa\n7. STANBIC\n8. NC Bank\n9. Standard Chartered\n10. Next\n0. Back 00Mani Menu")
            
            def equity():
                print("24Central Uganda")
                print("1. 24Central Money to Bank\n2. Bank to 24Central Money\n3. Account Balance\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
                def moneyToBank():
                    print("24Central Uganda")
                    print("1. On my account\n2. On another account\n0.Back 00.Main Menu")
                    choice = str(input("Reply: "))
                    
                def bankToMoney():
                    enterAccountNumber()
                    
            def centenary():
                enterAccountNumber()
                
            def prideMicrofinance():
                enterAccountNumber()
                
            def barclaysBank():
                enterAccountNumber()
                
            def dfcu():
                enterAccountNumber()
                
            def bankOfAfrica():
                enterAccountNumber()
                
            def stanbic():
                enterAccountNumber()
                
            def ncBank():
                enterAccountNumber()
                
            def standardChartered():
                enterAccountNumber()
                
            def next():
                print("24Central Uganda")
                print("NEXT\n1. Finance Trust Bank\n2. Housing Finance Bank\n3. KCB\n4. DTB\n5. Orient Bank\n6. GT Bank\n7. Opportunity\n8. Tropical\n9. Post Bank\n10. Eco Bank\n11. UGAFODE\n12. FINCA\n13. Top Finance Bank")
                choice = str(input("Reply: "))
                
                def financeTRustBank():
                    enterAccountNumber()
                    
                def housingFinanceBank():
                    enterAccountNumber()
                    
                def kcb():
                    enterAccountNumber()
                    
                def dtb():
                    enterAccountNumber()
                    
                def orientBank():
                    enterAccountNumber()
                    
                def gtBank():
                    enterAccountNumber()
                    
                def opportunity():
                    enterAccountNumber()
                    
                def tropical():
                    enterAccountNumber()
                    
                def postBank():
                    enterAccountNumber()
                    
                def ecoBank():
                    enterAccountNumber()
                    
                def ugafode():
                    enterAccountNumber()
                    
                def finca():
                    enterAccountNumber()
                    
                def topFinanceBank():
                    enterAccountNumber()
                    
        def groupCollections():
            print("24Central Uganda")
            print("Group Collections\n1. Review request for money\n0.Back 00.Main menu")
            choice = str(input("Reply: "))
            
            def reviewRequest():
                print("24Central Uganda")
                print("Enter Request ID\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
        def mSacco():
            print("24Central Uganda")
            print("1. Deposit\n2. Check Balance\n3. Mini statement\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
            def deposit():
                print("24Central Uganda")
                print("Enter SACCO ID\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
            def checkBalance():
                print("24Central Uganda")
                print("Enter SACCO ID\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
            def miniStatement():
                print("24Central Uganda")
                print("Enter SACCO ID\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
        def atmWithdrawal():
            print("24Central Uganda")
            print("Enter PIN to confirm\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
                
        def nssfSavings():
            print("24Central Uganda")
            print("NSSF Savings\n1. Individual\2. Employer\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
            def nssfNumber():
                print("24Central Uganda")
                print("Enter NSSF Number\n0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
            def employer():
                print("24Central Uganda")
                print("Enter Txn Ref Number\n0.Back 00.Main Menu")#crosscheck txn number
                choice = str(input("Reply: "))
                
    #a function to handle wewole services
    def wewole():
        print("Welcome to the Wewole loan service by JUMO")
        print("1. Get a loan\n2. Repay my alone\n3. Check my loan balance\n4. About Wewole\n5. View Key TandCs")
        choice = str(input("Reply: "))
        
        def getLoan():
            print("How much do you need?\nEnter an amount between UGX 1,500 and UGX 10,000\n0.Back")
            choice = str(input("Reply: "))
            
        def repayLoan():
            print("You do not have any loan right now\n1. Get a loan\n0. Back")
            choice = str(input("Reply: "))#option 1 calls function to get alone
            
        def checkStatus():
            print("Enter the PIN to confirm")
            choice = str(input("Reply: "))
            
        def aboutWewole():
            print("1. What is Wewole?\n2. How do I qualify\n3. Fees\n4. How do I pay?\n5. Getting bigger loans\n6. What happens if I pay late?\n0.Back")
            choice = str(input("Reply: "))
            
            def firstOption():
                print("24Central Uganda")
                print("Wewole offers loans to selected 24Central customers. No savings or paperwork neede and paid directly into your AM account.\n0.Back")
                choice = str(input("Reply: "))
                
            def secondOption():
                print("24Central Uganda")
                print("To qualify for Wewole you must frequently recharge with talktime and use your AM account\n0.Back")
                choice = str(input("Reply: "))
                
            def thirdOption():
                print("24Central Uganda")
                print("Fees vary according to your AM account usage and your loan payment history. All fees are shown during your loan applicating process.\n0.Back")
                choice = str(input("Reply: "))
                
            def fourthOption():
                print("24Central Uganda")
                print("You can repay your loan at any time\n1. Full payment\n2. Part payment\n0.Back")
                choice = str(input("Reply: "))
                
                def fullPayment():
                    print("24Central Uganda")
                    print("To pay your loan in full, make sure you have enough money in your AM account on the due date and select \"Repay my loan\" on the main menu\n0.Back")
                    choice = str(input("Reply: "))
                    
                def partPayment():
                    print("24Central Uganda")
                    print("To make a loan repayment at any time, select \"Repay my loan\" on the main menu. Make sure you pay your full loan balance by the due date.")
                    choice = str(input("Reply: "))
                
            def fifthOption():
                print("24Central Uganda")
                print("Pay your Wewole loan on time, everytime and keep using your AM account and you may qualify for bigger loans in future.\n0.Back")
                choice = str(input("Reply: "))
                
            def sixthOption():
                print("24Central Uganda")
                print("If you do not pay the loan balance by the due date, a late payment fee will be chraged as shown when you applied for the loan.\n0.Back")
                choice = str(input("Reply: "))
                
        def viewKey():
            print("24Central Uganda")
            print("1. Wewole Key TandCs\n2. Service Key TandCs\n0.Back")
            choice = str(input("Reply: "))
            
            def wewoleTand():
                print("24Central Uganda")
                print("When you accept the JUMO TandCs, you consent to receiving SMSs and 24Central sharing your personal information with JUMO tc.jumo.world/augl\n1.Next\n0.Back")
                choice = str(input("Reply: "))
                def next():
                    print("24Central Uganda")
                    print("All fees are shown during the loan application process. The loan amount fees and due date will be sent by SMS after your loan application\n1.Next\n0.Back")
                    choice = str(input("Reply: "))
                    
                    def next():
                        print("24Central Uganda")
                        print("Your loan repayment method is agreed when you apply. To make a loan repayment at anytime, select \"Repay my loan\".\n1.Next\n0.Back")
                        choice = input("Replay: ")
                        
                        def next():
                            print("24Central Uganda")
                            print("A late payment fee will be charged, and added to your loan balance if you do not pay your loan on the due date\n0.Back")
                            choice = str(input("Reply: "))
                            
            def wewoleServiceTand():
                print("24Central Uganda")
                print("When you accept the JUMO TandCs, you concent to receiving SMSs and 24Central sharing your personal information with JUMO.tc.jumo.world/aug\n1.Next\n0.Back")
                choice = str(input("Reply: "))
                
                def next():
                    print("24Central Uganda")
                    print("JUMO will share your personal informtion and usage with authorised parties (eg. Financial service providers) for regulatory and commercial purposes.\n1.Next\n0.Back")
                    choice = str(input("Reply: "))
                    
                    def next():
                        print("24Central Uganda")
                        print("If you apply for a mobile financial service product, you will have to accept the terms and conditions when applying for the product.\n0.Back")
                        choice = str(input("Reply: "))
            
    #a function handle airtel money pay services    
    def airtelMoneyPay():
        print("24Central Uganda")
        print("Enter Merchant ID\n0.Back 00.Main Menu")
        choice = str(input("Reply: "))
        
#a function to handle voice bundles
def voiceBundles():
    print("24Central Uganda")
    print("1. Daily\n2. Weekly\n3. Monthly\n4. Kyabise Combos\n5. International\n6. Gift\n7. Freaky Friday\n* Back")
    choice = str(input("Reply: "))
    
    def daily():
        print("24Central Uganda")
        print("1. My Pakalast\n2. Pakalast 30Mins@1000\n3. 100Mins@2000\n4. 300Mins@5000-3days\n5. Kawa 10Mins@500\n6. Power Tooti\n7. Night Bundle (10pm-6am)\n8. Zaweze Bundles\n* Back")
        choice = str(input("Reply: "))
        
        def myPakalast():
            print("24Central Uganda")
            print("MYPAKALAST\n1. 36Mins_36MBs_36SMS@1100\n2. 40Mins_40MBs_40SMS@1200\n3. 55Mins_55MBs_55SMS@1500\n* Back")
            choice = str(input("Reply: ")) #My pakalast credits from airteime directly
            
        def pakalast():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 1000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def mins():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 2000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def threeDays():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def kawa():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 500 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def powerTooti():
            print("24Central Uganda")
            print("1. Tooti 30Mins @ 800\n2. Tooti 25Mins @ 500\n* Back")
            choice = str(input("Reply: "))   
            
            def optionOne(): 
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
            
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 800 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                
            def optionTwo():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
            
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 500 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
        def nightBundle():
            print("24Central Uganda")
            print("1. Kyabise Night 15Mins_15MB_15SMS@500\n2. Paka Night 20Min@300\n* Back")#from airtime
            choice = str(input("Reply: "))
            
    def weekly():
        print("24Central Uganda")
        print("1. 45Mins@2000\n2. Kawa 90Mins@3500\n3. Pakalast 225Mins@6000\n* back")
        choice = str(input("Reply: "))
        
        def optionMins():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 2000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def optionKawa():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 3500 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def optionPaka():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 500 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
    def monthly():
        print("24Central Uganda")
        print("1. CMD 4500Mins @ 50,000\n2. CMD 2000Mins @ 30,000\n3. CMD 750Mins @ 10k 2Weeks\n4. 125Mins@5k\n5. 300Mins@10k\n6. CMD 3600Mins @ 75k\n* Back")
        choice = str(input("Reply: "))
        
        def firstOption():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 50000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def secondOption():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 30000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def thirdOption():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 10000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def fourthOption():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 10000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def fifthOption():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 10000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def sixthOption():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
            
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 75000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
    def kyabiseCombos():
        print("24Central Uganda")
        print("1. Daily\n2. Weekly\n3. Monthly\n* Back")
        choice = str(input("Reply: "))
        
        def kabiseDaily():
            print("24Central Uganda")
            print("1. 20MB+WTF_20Mins_20SMS@1500\n2. 75MB_75Mins_75SMS@2500\n3. 10MB_10Mins_10SMS@750\n* Back")
            choice = str(input("Reply: "))
            
            def OptionFirst():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
            
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 1500 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
            def optionSecond():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
            
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 2500 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
            def optionThird():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
            
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 750 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
        def kaybiseWeekly():
            print("24Central Uganda")
            print("1. 300MB_300Mins_300SMS@10,000\n* Back")
            choice = str(input("Reply: "))
            
            def option():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
            
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 10000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
        def kaybiseMonthly():
            print("24Central Uganda")
            print("1. 1.3GB_1300Mins_1300SMS@50,000\n2. 500MB_500Mins_500SMS@20000\n* Back")
            choice = str(input("Reply: "))
            
            def option1():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
            
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 50000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
            
            def option2():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
            
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 20000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))        
                                
    def international():
        print("24Central Uganda")
        print("1. East Africa Bundles\n2. Country Bundles\n3. US/Asia Bundle\n4. Europe/S.Asia Bundle\n5. Africa Bundle\n* Back")
        choice = str(input("Reply: "))
        
        def eastAfrica():
            print("24Central Uganda")
            print("1. Kenya\n2. Rwanda\n3. South Sudan\n* Back")
            choice = str(input("Reply: "))
            
            def currencyCharges():
                print("24Central Uganda")
                print("1. Daily - 10Mins(2800/=)\n2. Weekly - 60Mins(15000/=)\n* Back")
                choice = str(input("Reply: "))
                
                def chargeOne():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 2800 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
                def chargeTwo():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 15000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
            
            def kenya():
                currencyCharges()
                
            def rwanda():
                currencyCharges()
                
            def southSudan():
                currencyCharges()
                
        def countryBundles():
            print("24Central Uganda")
            print("1. USA\n2. India\n3. China\n4. Nigeria\n* Back")
            choice = int(input("Input: "))
            
            def usa():
                print("AIrtel Uganda")
                print("1. Weekly-60Mins(7,500/=)\n2. Monthly-200Mins@20k\n* Back")
                choice = str(input("Reply: "))
                
                def usa1():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 7500 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
                def usa2():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 20000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
            def india():
                print("24Central Uganda")
                print("1. Weekly - 100Mins@10,000/=\n2. Monthly - 200Mins@20,000/=\n* Back")
                choice = str(input("Reply: "))
                
                def india1():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 10000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
                def india2():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 20000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
            def china():
                print("24Central Uganda")
                print("1. Weekly - 60Mins@7,500/=\n2. Monthly - 200Mins@20,000/=\n* Back")
                choice = str(input("Reply: "))
                
                def china1():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 7500 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
                def china2():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 20000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
            def nigeria():
                print("24Central Uganda")
                print("1. Weekly - 11Mins@5,000/=\n* Back")
                choice = str(input("Reply: "))
                
                def nigeria1():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 10000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
        def usAsia():
            print("24Central Uganda")
            print("1. USA, India, China, Malaysia, Singapore, S.Korea, Hong Kong\n* Back")
            choice = str(input("Reply: "))
            
            def optionUs():
                print("AIrtel Uganda")
                print("1. Weekly-30Mins5,000/=\n2. Monthly-200Mins@20,000\n* Back")
                choice = str(input("Reply: "))
                
                def optionWeekly():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
                def optionMonthly():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 20000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
        def europAsia():
            print("24Central Uganda")
            print("1. UK, Germany, Pakistan, Thailand, Sweden, Denmark, Japan, Austria, New Zeland, Indies\n* Back")
            choice = str(input("Reply: "))
            
            def optionEurop():
                print("AIrtel Uganda")
                print("1. Weekly-30Mins5,000/=\n* Back")
                choice = str(input("Reply: "))
                
                def optionWeekly():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
                        
        def africaBundle():
            print("24Central Uganda")
            print("1. Nigeria, Namibia\n* Back")
            choice = str(input("Reply: "))
            
            def optionNigeria():
                print("AIrtel Uganda")
                print("1. Weekly-11Mins5,000/=\n* Back")
                choice = str(input("Reply: "))
                
                def optionWeekly():
                    print("24Central Uganda")
                    print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                    choice = str(input("Reply: "))
            
                    #airtime just deducts from your airtime
                    def airtelMoney():
                        print("24Central Uganda")
                        print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                        choice = str(input("Reply: "))
        
    def giftBundle():
        print("24Central Uganda")
        print("1. Daily 10Mins_10MB_10SMS@750\n2. Daily 20Mins_20SMS_20MB+50MBSTF @1500\n3. Daily 75Mins_75SMS_75MB @2500\n* Back")
        choice = str(input("Reply: "))
        
        def enterNumber():
            print("24Central Uganda")
            print("Please enter number (075xxx or 070xxx):\n#.to quit\n* Back")
            choice = str(input("Reply: "))
            
        def giftOption1():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 750 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def giftOption2():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 1500 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def giftOption3():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 2500 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))

    def freakyFriday():
        print("24Central Uganda")
        print("1. 30min, 2GB@3k_24hrs\n2. 100min, 3GB@5k_3days\n* Back")
        choice = str(input("Reply: "))
        
        def freakyOption1():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 3000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
            def freakyOption2():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
        
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))

#a function to handle internet service bundles      
def internetServices():
    print("24Central Uganda")
    print("Internet Services\n1. Daily\n2. Weekly\n3. Monthly\n4. Quarterly\n5. Data Share\n6. MyPakalast Data\n7. Volume Check\n8. Gift\n9. Settings\n10. Data Tooti\n11. More\n12. Hello Tunes\* Back")
    choice = str(input("Reply: "))
    
    def dailyData():
        print("24Central Uganda")
        print("1. 500/= for 40MB\n2. 1000/= for 100MB\n3. 2000/= for 300MB\n4. 3000/= for 500MB(3 Days)\n5. 5000/= for 1GB(3 Days)\n6. 10000/= for 3GB(3 Days)\n7. 250/= for 15MB\nn. Next\n* Back")
        choice = str(input("Reply: "))
        
        def terms():
            print("24Central Uganda")
            print("1. For Auto Renew\n2. For One Time bundle\n* Back")
            choice = str(input("Reply: "))
            
        def data1():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 500 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def data2():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 1000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def data3():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 2000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def data4():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 3000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def data5():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def data6():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 10000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def data7():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 250 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def nextOption():
            print("24Central Uganda")
            print("8. 2000/= for Night 1GB\n* Back")
            choice = str(input("Reply: "))
            
            def data8():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
        
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 2000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
    
    def weeklyData():
        print("24Central Uganda")
        print("1. 2000/= for 150MB\n2. 3500/= for 400MB\n3. 7000/= for 1.17GB\n4. 15000/= for 4GB\n5. 20000/= for 7GB\n* Back")
        choice = str(input("Reply: "))
        
        def weekTerm():
            print("24Central Uganda")
            print("1. For Auto Renew\n2. For One Time bundle\n* Back")
            choice = str(input("Reply: "))
        
        def week1():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 2000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def week2():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 3500 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def week3():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 7000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def week4():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 15000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def week5():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 20000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
    def monthlyData():
        print("24Central Uganda")
        print("1. 10000/= for 1.5GB\n2. 30000/= for 9GB\n3. 50000/= for 20GB\n4. 90000/= for 25GB\n5. 150000/= for 65GB\n6. 5000/= for 500MB\n* Back")
        choice = str(input("Reply: "))
        
        def monthTerm():
            print("24Central Uganda")
            print("1. For Auto Renew\n2. For One Time Bundle\n* Back")
            choice = str(input("Reply: "))
            
        def month1():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 10000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def month2():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 30000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def month3():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 50000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def month4():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 90000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def month5():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 150000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def month6():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
        
    def quarterlyData():
        print("24Central Uganda")
        print("1. 39000/= for 4GB\n2. 78000/= for 10GB\n3. 130000/= for 20GB\n4. 450000/= for 85GB\n* Back")
        choice = str(input("Reply: "))
        
        def quarterm():
            print("24Central Uganda")
            print("1. For Auto Renew\n2. For One Time bundle\n* Back")
            choice = str(input("Reply: "))
            
        def quart1():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 39000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def quart2():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 78000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def quat3():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 130000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def quart4():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 450000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
    
    def dataShare():
        print("24Central Uganda")
        print("1. Tugabane (share data)\n2. Data Me2U\n* Back")
        choice = str(input("Reply: "))
        
        def share1():
            print("24Central Uganda")
            print("1. Activate\n2. Deactivate\n3. Check Status\n* Back")
            choice = str(input("Reply: "))
            
            def activate():
                print("24Central Uganda")
                print("Enter Dependent Number")
                choice = str(input("Reply: "))
                
            def deactivate():
                print("24Central Uganda")
                print("Enter Dependent/Sponsor Number")
                choice = str(input("Reply: "))
                
            def checkStatus():
                print("24Central Uganda")
                print("Dear customer are currently not on any Tugabane")
                
        def dataMe():
            print("24Central Uganda")
            print("Please Enter Number")
            choice = str(input("Reply: "))

    def myPakalast():
        print("24Central Uganda")
        print("DATA MYPAKALAST\n------------------\n1. Daily _ 6.5GB@11000/=\n* Back")
        choice = str(input("Reply: "))
        
        def pakachoice():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 11000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
    def volumeCheck():
        print("24Central Uganda")
        #create a function that reads what is in the file containing the data bundle balance
            
    def gift():
        print("24Central Uganda")
        print("1. Daily\n2. Weekly\n3. Monthly\n* Back")
        choice = str(input("Reply: "))
        
        def dailyGift():
            dailyData()
            
        def weeklyGift():
            weeklyData()
            
        def weeklyGift():
            monthlyData()
            
    def settings():
        print("24Central Uganda")
        print("Dear Customer, tour request is being processed. Please wait for confirmation SMS")
        exit()
        
    def tootiBundle():
        print("24Central Uganda")
        print("1. Tooti 50MB: 1 hour @ 500\n2. Happy Hour 1GB: 1 hour @ 5000\n* Back")
        choice = str(input("Reply: "))
        
        def tooti1():
            print("24Central Uganda")
            print("1. For Auto Renew\n2. For One time bundle\n* Back")
            choice = str(input("Reply: "))
            
            def payTooti1():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
        
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 500 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
        def tooti2():
            print("24Central Uganda")
            print("1. For Auto Renew\n2. For One time bundle\n* Back")
            choice = str(input("Reply: "))
            
            def payTooti2():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
        
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
    def more():#This will done on a later date
        print("24Central Uganda")
        print("1. Monthly Free 20MB\n2. Games Club\n3. PayWay\n4. Auto-renew\n5. Roaming Data\n* Back")
        choice = str(input("Reply: "))
        
    def helloTunes():
        print("24Central Uganda")
        print("The session timed out")
        exit()

#a function to handle borrowing        
def beerako():
    print("24Central Uganda")
    print("1. Airtime Beerako\n2. Data/Voice Beerako\n* Back")
    choice = str(input("Reply: "))
    
    def airtimeBeerako():
        print("24Central Uganda")
        print("Welcome to 24Central Beerako. Please select\n1. Get 200\n2. About Beerako\n3. Balance check\n00 Language change\n* Back")
        choice = str(input("Reply: "))
        
        def get():
            print("24Central Uganda")
            print("Your account will be credited with 200/= at UGX 22/= service charge. Reply with:\n1. to confirm\n2. to go back\n* Back")
            choice = str(input("Reply: "))
            
        def about():
            print("Beerako is a service that allows you to borrow advance airtime within your qualified limit and pay back later at 11% service charge\nTo qualify for UGX 500 spend 60 days on the network and top up to atleast UGX 1,500\nThis will occur when you top up, receive Me2U or manually payback via *155*7#\nTo pay back my Beerak dial *155*7#\n* Back")
            choice = str(input("Reply: "))
            
        def balanceCheck():
            print("24Central Uganda")
            #should read from the file containing ur balance
            
        def languageChange():
            print("24Central Uganda")
            print("Reply with:\n1. for English\n2. for Luganda\n* Back")
            choice = str(input("Reply: "))
            #work on it later
    def dataBeerako():
        print("24Central Uganda")
        print("1. for auto advance\n2. Data Beerako\n3. Voice Beerako\n4. To Repay debt\n0. for debt info\n* Back")
        choice = str(input("Reply: "))
        
        def autoAdvance():
            print("24Central Uganda")
            #work on it later
            
        def data():
            print("24Central Uganda")
            print("Reply with:\n1. Data\n2. Voice\n* Back")
            choice = str(input("Reply: ")) #option one should give data bundle immediately and option two give u a voice of 500 that is kawa
            
        def voice():
            print("24Central Uganda")
            print("Reply with:\n1. Data\n2. Voice\n* Back")
            choice = str(input("Reply: ")) #option one should give data bundle immediately and option two give u a voice of 500 that is kawa
            
        def repayDebt():
            print("24Central Uganda")
            print("Reply with:\n1. Data\n2. Voice\n* Back")
            choice = str(input("Reply: ")) #choose which one u want ot pay
            
            
        def debtInfo():
            print("24Central Uganda")
            print("Reply with:\n1. Data\n2. Voice\n* Back")
            choice = str(input("Reply: ")) #both should give you your remaining balance
            
#a function for handling hello tunes services        
def helloTunes():    
    print("24Central Uganda")
    print("Welcome to Hello tunes\n1. Ugandan Top 10\n2. International Top 10\n3. E.Africa\n4. Oldies\n5. Gospel\n6. Islam\n7. Delete tune\8. Unsubscribe\n9. Library\n Search\n11. Luganda\n* Back")
    choice = str(input("Reply: "))
 
#a function to handle sms bundles   
def smsBundle():
    print("24Central Uganda")
    print("SMS Bundles\n1. 24Central\n2. All Local Networks\n3. Gift SMS\n4. Cancel Auto renewal\n* Back")#option 4 automatically cancels any auto renewal that u have
    choice = str(input("Reply: "))
    
    def airtel():
        print("24Central Uganda")
        print("1. 100 SMS @ 250 (Daily)\n2. Daily Plus @ 500\n3. 700 SMS @ 1000 (Weekly)\n4. 4000 SMS @ 5000 (Monthly)\n* Back")
        choice = str(input("Reply: "))

        def terms():
            print("24Central Uganda")
            print("1. For Auto Renew\n2. For One Time bundle\n* Back")
            choice = str(input("Reply: "))
            
        def sms1():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 250 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def sms2():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 500 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def sms3():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 1000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def sms4():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
    def allLocal():
        print("24Central Uganda")
        print("1. 10 SMS @ 500 (Monthly)\n2. 25 SMS @ 1000 (Monthly)\n3. 50 SMS @ 3000 (Monthly)\n4. 125 SMS @ 5000 (Monthly)\n* Back")
        choice = str(input("Reply: "))
        
        def all1():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 500 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def all2():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 2000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def all3():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 3000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def all4():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 5000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
    def gift():
        print("24Central Uganda")
        print("1. 24Central SMS\n2. All Local Networks\n* Back")
        choice = str(input("Reply: "))
        
        def gift24Central():
            airtel()
            
        def giftAll():
            allLocal()
               
#a function handle my account
def myAccount():
        print("24Central Uganda")
        print("My account\n1. Check Balance\n2. Change PIN\n3. Request Statement\n4. Last 4 Transactions\n5. Invite a Friend\n6. Messages\7. PIN Reset\n8. Transaction Status\n0.Back 00.Main Menu")
        
        def checkBalance():
            print("24Central Uganda")
            print("Enter your PIN to confirm\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
        def changePin():
            print("24Central Uganda")
            print("Please enter your current PIN\0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
            def newPin():
                print("24Central Uganda")
                print("Enter your new PIN to confirm\0.Back 00.Main Menu")
                choice = str(input("Reply: "))
                
        def requestStatement():
            print("24Central Uganda")
            print("Enter Your Email ID\0.Back 00.Main Menu")
            choice = str(input("Reply: "))
                
        def lastTransaction(): #Last 4 transactions
            print("24Central Uganda")
            print("Enter your PIN to confirm\0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
        def inviteFriend():
            print("24Central Uganda")
            print("Enter the Mobile Number you wish to invite to 24CentralMoney\n0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
        def messages():
            print("24Central Uganda")
            print("Messages\n1. Viral Secret Code\n2. Resend Recent message\0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
        #def pinReset():
            
        def transactionStatus():
            print("24Central Uganda")
            print("Enter transaction ID\0.Back 00.Main Menu")
            choice = str(input("Reply: "))
            
#a function to handle roaming bundles
def roaming():
    print("24Central Uganda")
    print("1. Data Bundles One network\n2. Roaming Combos One network\n3. New Roaming Data Bundles\n* Back")
    choice = str(input("Reply: ")) 
    
    def terms():
        print("24Central Uganda")
        print("1. For Auto Renew\n2. For One Time bundle\n* Back")
        choice = str(input("Reply: ")) 
  
    def roam1():
        print("24Central Uganda")
        print("1. Weekly 250MB @ 50,000\n2. Weekly 600MB @ 100,000\n* Back")
        choice = str(input("Reply: "))
        
        def weekly1():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 50000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
    
        def weekly2():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 100000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
    def roam2():
        print("24Central Uganda")
        print("1. 25,000 Bundle - 10mins, 100MB\n2. 65,000 Bundle - 25mins, 500MB\n* Back")
        choice = str(input("Reply: "))
        
        def bundle25():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 25000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
        def bundle65():
            print("24Central Uganda")
            print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
            choice = str(input("Reply: "))
    
            #airtime just deducts from your airtime
            def airtelMoney():
                print("24Central Uganda")
                print("24Central has initiated a debit of UGX 65000 from your AM account.\nEnter PIN\n* Back")
                choice = str(input("Reply: "))
                
    def roam3():
        print("24Central Uganda")
        print("1. One Network bundles\n* Back")
        choice = str(input("Reply: "))
        
        def oneRoam():
            print("24Central Uganda")
            print("1. 4000/= for 40MB\n2. 8000/= for 1GB\n3. 40,000/= for 3GB\n4. 55,000/= for 10GB\n* Back")
            choice = str(input("Reply: "))
            
            def one1():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
        
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 4000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
            def one2():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
        
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 8000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
            def one3():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
        
                #airtime  just deducts from your airtime amount
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 40000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                    
            def one4():
                print("24Central Uganda")
                print("Please select your billing option\n1. Airtime\n2. 24Central Money\n* Back")
                choice = str(input("Reply: "))
        
                #airtime just deducts from your airtime
                def airtelMoney():
                    print("24Central Uganda")
                    print("24Central has initiated a debit of UGX 55000 from your AM account.\nEnter PIN\n* Back")
                    choice = str(input("Reply: "))
                
        
mainMenu()
