import sqlite3

def get_user_data(username):
    # KẾT NỐI DATABASE GIẢ LẬP
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # LỖI BẢO MẬT NGHIÊM TRỌNG: SQL INJECTION
    # Nối chuỗi trực tiếp mà không kiểm tra đầu vào
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    print(f"Executing query: {query}")
    cursor.execute(query) 
    data = cursor.fetchall()
    conn.close()
    return data

# Giả lập người dùng nhập dữ liệu
user_input = "admin' OR '1'='1" 
get_user_data(user_input)
