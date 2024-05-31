from db import cur, conn

def login():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        select_one_user = """SELECT * FROM users WHERE username = %s;"""
        cur.execute(select_one_user, (username,))
        user_data = cur.fetchone()

        if user_data:
            # TODO: Implement password verification
            print("Login successful!")
            return
        else:
            attempts += 1
            print(f"Incorrect username or password. {max_attempts - attempts} attempts remaining.")

    print("Maximum number of login attempts reached. Your account has been blocked.")

login()