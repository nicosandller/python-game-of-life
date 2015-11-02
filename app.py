from board import Board
import time


Sistema = Board(10)
Sistema.insert_blinker()
Sistema.insert_toad()


while True:
        Sistema.show()
        Sistema.next()
        time.sleep(1)
