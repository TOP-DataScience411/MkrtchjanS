class ChessKing:
    # Словари
    files = {chr(97 + i): i + 1 for i in range(8)}
    ranks = {str(i): i for i in range(1, 9)}
    
    def __init__(self, color: str = 'white', square: str = None):
        """Инициализация короля с указанием цвета и начальной позиции.
        Если square не задан, используется стандартная начальная позиция:'e1' для белого короля, 'e8' для черного."""
        self.color = color.lower()
        if square:
            self.square = square.lower()
        else:
            self.square = 'e1' if self.color == 'white' else 'e8'
    
    def __repr__(self) -> str:
        """Машиночитаемое представление."""
        return f"{self.color[0].upper()}K: {self.square}"
    
    def __str__(self) -> str:
        """Человекочитаемое представление."""
        return self.__repr__()
    
    def is_turn_valid(self, new_square: str) -> bool:
        """Проверка валидности хода."""
        if len(new_square) != 2:
            return False
        new_square = new_square.lower()
        
        file_diff = abs(self.files[new_square[0]] - self.files[self.square[0]])
        rank_diff = abs(self.ranks[new_square[1]] - self.ranks[self.square[1]])
        
        return (file_diff <= 1 and rank_diff <= 1) and (file_diff + rank_diff != 0)
    
    def turn(self, new_square: str) -> None:
        """Выполняет ход, если он валиден иначе ValueError."""
        if not self.is_turn_valid(new_square):
            raise ValueError("Invalid move for Chess King.")
        self.square = new_square.lower()

#wk = ChessKing()
#wk.color: white
#wk.square_initial: e1
#wk.turn_e2: WK: e2,
#wk_after_turn: WK: e1
#wk_invalid_turn: ValueError
#bk.color: black
#bk.square: e8

