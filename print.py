RRTable = {}

Flag = True


while Flag:
    
    name = input('Enter the host or domain name (Exit to quit program): ' )

    if name == "exit":
        Flag = False
    else:
        DNSQuery = input('Enter the type of DNS query (0. A, 1. AAAA, 2. CNAME, 3. NS: ')
        

        if "name" in RRTable:
                print(name + " already exists. ")
        else:
            RRTable["Name"] =  name
            RRTable["Type"] =  DNSQuery
            print("Added: " + name)







