import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # --- SECURE CODING APPLIED ---
    # Thay vi noi chuoi (String Concatenation), ta dung Parameterized Query (?)
    # Day la cach chong SQL Injection hieu qua nhat.
    query = "SELECT * FROM users WHERE username = ?"
    
    print(f"Executing query safely...")
    
    # Tham so duoc truyen rieng biet, hacker khong the chen lenh vao duoc
    cursor.execute(query, (username,)) 
    
    data = cursor.fetchall()
    conn.close()
    return data

# Test thu du lieu
user_input = "admin" 
get_user_data(user_input)
