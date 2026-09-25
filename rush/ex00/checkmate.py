def checkmate(board):
    # ดักถ้าไม่ใช่ str บอก error
    if type(board) != str:
        print("Error")
        return

    # แยกกระดานเป็นแต่ละแถว
    rows = board.splitlines()
    size = len(rows)

    # null board
    if size == 0:
        print("Error")
        return

    # ต้องเป็นสี่หลี่ยมจตุรัส
    for row in rows:
        if len(row) != size:
            print("Error")
            return

    # หา king และนับ king
    king_count = 0
    king_row = 0
    king_col = 0
    # loop ว่า king อยู่ไหน
    for r in range(size):
        for c in range(size):
            if rows[r][c] == "K":
                king_count += 1
                king_row = r
                king_col = c

    # ดัก king ถ้ามีเกิน 1 บอก error
    if king_count != 1:
        print("Error")
        return

    #flag
    in_check = False

    # ---------- เบี้ย Pawn เดินได้ขึ้นลง แต่กินได้ซ้ายขวา----------
    # เบี้ยกินเฉียงขึ้น เบี้ยต้องอยู่แถวล่างของ King ถึงจะกินได้
    if king_row + 1 < size:
        # เช็คแถวเฉียงซ้าย เฉียงขวา ถ้ามีเบี้ยก้โดนกิน
        # เฉียงซ้าย
        if king_col - 1 >= 0 and rows[king_row + 1][king_col - 1] == "P":
            in_check = True
        #เฉียงขวา
        if king_col + 1 < size and rows[king_row + 1][king_col + 1] == "P":
            in_check = True

    # ---------- เช็คเรือกับควีน สองตัวนี้เดินเป็นเส้นตรง ได้ทุกทิศ ----------
    # เดินบน มองไปข้างบน
    for r in range(king_row - 1, -1, -1):
        piece = rows[r][king_col]
        if piece in "PBRQ":
            if piece == "R" or piece == "Q":
                in_check = True
            break

    # มองลงข้างล่าง
    for r in range(king_row + 1, size):
        piece = rows[r][king_col]
        if piece in "PBRQ":
            if piece == "R" or piece == "Q":
                in_check = True
            break

    # มองไปทางซ้าย
    for c in range(king_col - 1, -1, -1):
        piece = rows[king_row][c]
        if piece in "PBRQ":
            if piece == "R" or piece == "Q":
                in_check = True
            break

    # มองไปทางขวา
    for c in range(king_col + 1, size):
        piece = rows[king_row][c]
        if piece in "PBRQ":
            if piece == "R" or piece == "Q":
                in_check = True
            break

    # ---------- เช็คเฉียง (Bishop, Queen) ----------
    # i คือระยะห่างจาก King (1 ช่อง, 2 ช่อง, ...)

    # เฉียงซ้ายบน
    for i in range(1, size):
        r = king_row - i
        c = king_col - i
        if r < 0 or c < 0:
            break
        piece = rows[r][c]
        if piece in "PBRQ":
            if piece == "B" or piece == "Q":
                in_check = True
            break

    # เฉียงขวาบน
    for i in range(1, size):
        r = king_row - i
        c = king_col + i
        if r < 0 or c >= size:
            break
        piece = rows[r][c]
        if piece in "PBRQ":
            if piece == "B" or piece == "Q":
                in_check = True
            break

    # เฉียงซ้ายล่าง
    for i in range(1, size):
        r = king_row + i
        c = king_col - i
        if r >= size or c < 0:
            break
        piece = rows[r][c]
        if piece in "PBRQ":
            if piece == "B" or piece == "Q":
                in_check = True
            break

    # เฉียงขวาล่าง
    for i in range(1, size):
        r = king_row + i
        c = king_col + i
        if r >= size or c >= size:
            break
        piece = rows[r][c]
        if piece in "PBRQ":
            if piece == "B" or piece == "Q":
                in_check = True
            break

    # ---------- แสดงผล ----------
    if in_check:
        print("Success")
    else:
        print("Fail")