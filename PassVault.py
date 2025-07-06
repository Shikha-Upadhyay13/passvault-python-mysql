import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="1310", database="passvault")
cursor = conn.cursor()

#adding a new credentials
def add_credentials(site, username, password):
    cursor.execute("insert into credentials(site, username, password) values(%s,%s,%s)", (site,username,password))
    conn.commit()
    print("credential added succesfully")

#view all saved credentials
    
def view_credentials():
    cursor.execute("select* from credentials")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Site: {row[0]} | Username: {row[1]} | Password: {row[2]}")

        
#search credentials by site name
def search_site(site):
    cursor.execute("select username, password from credentials where site=%s",(site,))
    result= cursor.fetchone()
    if result:
        print(f"Username: {result[0]}, Password: {result[1]}")
    else:
        print("No credentials found for that site")
            
#delete a credential
def delete_site(site):
    cursor.execute("delete from credentials where site=%s",(site,))
    conn.commit()
    print("Credential deleted successully (if existed)")

def export_credentials_to_csv():
    cursor.execute("select site,username,password from credentiald")
    rows = cursor.fetchall()

#main menu
while True:
         print("\nPassvault Menu")
         choice = input("[1] Add credential\n" "[2] View All\n" "[3] Search site\n" "[4] Delete site\n" "[5] Exit\n").strip()
         if choice == '1':
            site = input("Site name: ")
            username= input("Username: ")
            password= input("Password:")
            add_credentials(site, username, password)
         elif choice == '2':
            view_credentials()
         elif choice == '3':
            site = input("Enter site to search: ")
            search_site(site)
         elif choice == '4':
            site = input("Enter site name to delete: ")
            delete_site(site)
         elif choice == '5':
             print("Exiting PassVault")
             break
         else :
             print("Invalid choice")


    
             
