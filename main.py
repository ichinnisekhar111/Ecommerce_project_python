class User:
    def __init__(self,id,username,password,role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def user_info(self):
        return f'{self.id},{self.username},{self.password},{self.role}\n'



class Authentication:
    def register(self):
        id = int(input("Enter user ID : "))
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        role = input("Enter your role : ")

        with open('users.txt','r') as f:
            data = f.readlines()

        for line in data:
            details = line.strip().split(',')
            if details[1] == username:
                print("User name already exist")
                return

        user= User(id,username,password,role)
        user_data = user.user_info()
        with open('users.txt','a') as f:
            f.write(user_data)
            print("Registration successful")

    def login(self):
        username = input("Enter your username : ")
        password = input("Enter your password : ")

        with open('users.txt','r') as f:
            data = f.readlines()

        is_found = False
        for line in data:
            details = line.strip().split(',')
            db_username = details[1]
            db_password = details[2]
            if db_username == username and db_password == password:
                is_found = True
                print("Login Successful")
                
        if not is_found:
            print("Invalid Credentials")



class Product:
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def product_info(self):
        return f"{self.id},{self.name},{self.price},{self.quantity}\n"



class Admin:
    def add_product(self):

        id = int(input("Enter product ID : "))
        name = input("Enter product name : ")
        price = int(input("Enter product price : "))
        quantity = int(input("Enter product quantity : "))
        product = Product(id,name,price,quantity)

        with open('products.txt','r') as f:
            data= f.readlines()

        is_found= False
        with open('products.txt','w') as f:
            for line in data:
                details = line.strip().split(',')
                db_product_name = details[1]
                if db_product_name == name:
                    is_found = True
                    new_quantity = quantity + int(details[3])
                    f.write(f"{details[0]},{details[1]},{details[2]},{new_quantity}\n")
                else:
                    f.write(line)
        if not is_found:
            with open('products.txt','a') as f:
                product_data = product.product_info()
                f.write(product_data)
                print("Product Added successfully")


    def delete_product(self):
        id = int(input("Enter product ID : "))
        with open('products.txt','r') as f:
            data= f.readlines()

        if len(data) == 0:
            print('No Products Available!')
            return

        is_found =False
        with open('products.txt','w') as f:
            for line in data:
                details = line.strip().split(',')
                db_product_id = int(details[0])
                if db_product_id == id:
                    is_found= True
                else:
                    f.write(line)
        if is_found:
            print("Product deleted successfully")
        else:
            print("Product not found")


    def update_product(self):
        with open('products.txt','r') as f:
            data= f.readlines()

        if len(data) == 0:
            print('No Products Available!')
            return

        is_found = False
        id = int(input("Enter product ID : "))

        with open("products.txt",'w') as f:
            for line in data:
                details = line.strip().split(',')
                db_product_id = int(details[0])
                if db_product_id ==id:
                    is_found = True
                    print("what you want to update")
                    choice = int(input("1.Name \n2.Price \n3.Quantity \n4.All details \n"))
                    match choice:
                        case 1:
                            new_name = input("Enter new name: ")
                            f.write(f"{details[0]},{new_name},{details[2]},{details[3]}\n")
                            print("Product Name updated successfully")
                        case 2:
                            new_price = input("Enter new price: ")
                            f.write(f"{details[0]},{details[1]},{new_price},{details[3]}\n")
                            print("Product updated successfully")
                        case 3:
                            new_quantity = input("Enter new quantity: ")
                            f.write(f"{details[0]},{details[1]},{details[2]},{new_quantity}\n")
                            print("Product quantity updated successfully")
                        case 4:
                            new_name = input("Enter new name: ")
                            new_price = input("Enter new price: ")
                            new_quantity = input("Enter new quantity: ")
                            f.write(f"{details[0]},{new_name},{new_price},{new_quantity}\n")
                            print("All details updated successfully")
                        case _:
                            print("Invalid choice")
                            f.write(line)
                else:
                    f.write(line)
                    
        if not is_found:
            print("Product Not Found")    

        
    def search_product(self):
        with open('products.txt','r') as f:
            data= f.readlines()

        if len(data) == 0:
            print('No Products Available!')
            return

        id = int(input("Enter product ID : "))
        for line in data:
            details = line.strip().split(',')
            db_product_id = int(details[0])
            if db_product_id == id:
                print('-------------------------------------')
                print('|ID   |NAME      |PRICE  |QUANTITY  |')
                print('-------------------------------------')
                print(f'|{details[0]+' '*(5-len(details[0]))}|{details[1]+' '*(10-len(details[1]))}|{details[2]+' '*(7-len(details[2]))}|{details[3]+' '*(10-len(details[3]))}|')
                print('-------------------------------------')
                return
        print("Product not found")


    def view_all_products(self):
        with open('products.txt','r') as f:
            data= f.readlines()

        if len(data) == 0:
            print('No Products Available!')
            return

        print('-------------------------------------')
        print('|ID   |NAME      |PRICE  |QUANTITY  |')
        print('-------------------------------------')
        for line in data:
            details = line.strip().split(',')      
            print(f'|{details[0]+' '*(5-len(details[0]))}|{details[1]+' '*(10-len(details[1]))}|{details[2]+' '*(7-len(details[2]))}|{details[3]+' '*(10-len(details[3]))}|')
        print('-------------------------------------')
        

        


        

auth = Authentication()
# auth.login()
admin = Admin()
# admin.add_product()
# admin.delete_product()
# admin.search_product()
# admin.update_product()
# admin.view_all_products()

