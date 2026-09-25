# main.py
from checkmate import checkmate


def main():
    # ตัวอย่างที่ 1 (ควรได้ Success)
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)


if __name__ == "__main__":
    main()