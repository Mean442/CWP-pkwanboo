#!/usr/bin/env python3
import sys

# 1. ดึง Parameter ทั้งหมดโดยข้ามชื่อไฟล์ (sys.argv[0])
params = sys.argv[1:]

# 2. เช็กว่าถ้าจำนวน Parameter ไม่เท่ากับ 1 ให้พิมพ์ none
if len(params) != 1:
    print("none")
else:
    # ดึงค่า Parameter ออกมาด้วย for loop เต็ม
    target_param = ""
    for p in params:
        target_param = p

    # 3. ถามคำตอบจากผู้ใช้ผ่าน input()
    user_input = input("What was the parameter? ")

    # 4. เปรียบเทียบค่า
    if user_input == target_param:
        print("Good job!")
    else:
        print("Nope, sorry...")