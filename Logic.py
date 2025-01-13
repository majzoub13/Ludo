from Piece import Piece
import random as rand


class Logic:
    def __init__(self):
        self.protected_places = [13, 39]
        self.color_protected_places = {
            "y":0
            "r":26
        }
        return

    def roll_dice(self):
        return rand.randint(1, 6)

    def add_piece(self, board, player):
            base_piece = Player.get_base_piece
            board[self.color_protected_places[player.team]].pieces.append(base_piece)
            base_piece.position = self.color_protected_places[player.team]

    def move_piece(self, board, curr_pos, number):
        piece = board[curr_pos].pieces.pop()
        next_pos = curr_pos + number
        piece.counter += number
        board[next_pos].pieces.append(piece)
        return next_pos

    def move(self, board, player, depth=0):
            number = self.roll_dice()
            if depth = 4:
                return
            # we have all pieces in base(starting case)
            if player.all_pieces_in_base() and number == 6:
                self.add_piece(board, player)
                    move(board,player,depth+=1)
            else:
                return        
            # if we have pieces in base not placed
            if not player.is_base_empty():
                if number == 6:
                    while(validation == False):
                        choice = input("Choose 0 to add a new piece or 1 to move piece")
                        match choice:
                            case 0:
                                validation = True
                                self.add_piece(board, player)
                                move(board,player,depth+=1)
                                return
                            case 1:
                                validation = True
                                # we have move case outside for both states when base is empty and when there is in base but we want to move
                               break
                            case _:
                               print("invalid input")

            # if the player base is empty and we need to move only or for move
            pieces = player.get_movable_pieces()
            print("choose piece to move")
            for index,piece in pieces:
                print(f"{index}- piece at {piece.position}")
            while(validation==False)        
                user_choice = int(input("Enter the index of the piece you want to select : "))
                if(0<= user_choice < len(pieces)):
                    validation  = True
                else:
                    print("invalid input")
            #user input right
            piece = pieces[user_choice]                   
            if number == 6 :
                check_and_move(board,player,piece,number)
                move(board,player,depth+=1)
            else:
                check_and_move(board,player,piece,number)
                return
                       
                       
        
    def check_and_move(self,board,player,piece,number):
        current_position = piece.position
        potential_position = current_position + number
        # checking if the potential index has pieces
        # if it doesn't we check for wall
        if len(board[potential_position].pieces) == 0:
            for i in range(current_position + 1, potential_position + 1):
                # checked that two pieces of the same team excluding None are neighbors and different from the moved piece team
                 if board[i].pieces[0].team == board[i+1].pieces[0].team and board[i].pieces[0] != piece.team and board[i].pieces[0] != None:
                     return False
                 # here the path is clear so we move
                 else    
                    new_position = self.move_piece(board, piece, number)
                    piece.position = new_position    
        # if it does we try to kill/remove the piece 
        else:
            for p in board[potential_position].pieces:
                if p.team != piece.team:
                    kill(board,p)    
                    return True
    def kill(self,board,piece):
        board[piece.position].pieces.remove(piece)
        piece.position = None
        return
        
            
