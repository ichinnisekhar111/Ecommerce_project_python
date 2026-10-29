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



auth = Authentication()
# auth.login()
admin = Admin()
admin.add_product()
        
