import tkinter as tk
from tkinter import messagebox
#tạo kích thước cho một ô vuông trên bàn cờ (pixel)
CELL_SIZE = 8

class RookBoard:
    def __init__(self, root, n, rooks):
         # Cửa sổ chính
        self.root = root
# Kích thước bàn cờ n x n
        self.n = n
 # Danh sách quân xe (row, col)
        self.rooks = rooks
 # Quân xe đang được chọn
        self.selected_rook = None
# Tạo vùng vẽ
        self.canvas = tk.Canvas(
            root,
            width=n * CELL_SIZE,
            height=n * CELL_SIZE
        )
        self.canvas.pack()
# Vẽ bàn cờ và quân xe ban đầu
        self.draw_board()
        self.draw_rooks()
#Điều khiển sự kiện bằng click chuột
        self.canvas.bind("<Button-1>", self.on_click)
    #SAFE / UNSAFE
    def is_unsafe(self, row, col):
#r,c toạ độ quân xe
        for r, c in self.rooks:
            if r == row or c == col:
                return True
        return False

    # vẽ bàn cờ
    def draw_board(self):
    #xóa ô cờ cũ
        self.canvas.delete("cell")
        for i in range(self.n):
            for j in range(self.n):

                # Ô không an toàn → màu đỏ
                if self.is_unsafe(i, j):
                    color = "#FF6B6B"
                else:
                       # Màu bàn cờ vua
                    color = "#000000" if (i + j) % 2 == 0 else "#FFFFFF"

                self.canvas.create_rectangle(
                    j * CELL_SIZE,
                    i * CELL_SIZE,
                    (j + 1) * CELL_SIZE,
                    (i + 1) * CELL_SIZE,
                    fill=color,
                    tags="cell"
                )

    #vẽ quân xe
    def draw_rooks(self):
#xóa quân xe cũ
        self.canvas.delete("rook")
        for r, c in self.rooks:
            x = c * CELL_SIZE + CELL_SIZE // 2
            y = r * CELL_SIZE + CELL_SIZE // 2
            self.canvas.create_text(
                x, y,
                text="♜",
                font=("", 28),
                tags="rook"
            )

# kiểm tra luật
    def is_valid_rook_move(self, start, end):
        sr, sc = start
        er, ec = end
#tạo điều kiện cho quân xe chỉ được đi cùng hàng hoặc cùng cột
        if sr != er and sc != ec:
            return False
#không được đi trùng 
        if end in self.rooks and end != start:
            return False
# Không được đi xuyên quân khác  
        for r, c in self.rooks:
            if (r, c) == start:
                continue
             # Cùng hàng
            if sr == er and r == sr:
                if min(sc, ec) < c < max(sc, ec):
                    return False
                #cùng cột
            if sc == ec and c == sc:
                if min(sr, er) < r < max(sr, er):
                    return False
        return True


# Di Chuyển
    def move_rook(self, start, end):
        self.rooks.remove(start)
        self.rooks.append(end)
        self.draw_board()
        self.draw_rooks()
    # xử lí click chuột
    def on_click(self, event):
  # Chuyển tọa độ pixel → tọa độ ô
        row = event.y // CELL_SIZE #mỗi 8 pixel = 1 ô ngang
        
        col = event.x // CELL_SIZE #mỗi 8 pixel = 1 ô 
 # Kiểm tra click có nằm trong bàn cờ không
        if not (0 <= row < self.n and 0 <= col < self.n):
            return
 # Nếu chưa chọn quân xe
        if self.selected_rook is None:
            if (row, col) in self.rooks:
                self.selected_rook = (row, col)
                # Nếu đã chọn quân xe → chọn ô đích
        else:
            if self.is_valid_rook_move(self.selected_rook, (row, col)):
                self.move_rook(self.selected_rook, (row, col))
            else:
                messagebox.showwarning(
                    "Sai luật",
                    "Quân xe chỉ được đi ngang hoặc dọc!"
                )
            self.selected_rook = None
# MAIN 
if __name__ == "__main__":
    n = int(input("Nhập kích thước bàn cờ n: "))
    num = int(input("Nhập số quân xe: "))

    rooks = []
    for i in range(num):
        r = int(input(f"Xe {i+1} - hàng: "))
        c = int(input(f"Xe {i+1} - cột: "))
        rooks.append((r, c))

    root = tk.Tk()
    root.title("Bàn cờ quân Xe (Rook)")
    app = RookBoard(root, n, rooks)
    root.mainloop()
