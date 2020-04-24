class Luhn:
    
    cardnum = ""
    
    def __init__(self, card_num):
        self.cardnum = card_num

    def valid(self):
        card_number = "".join(self.cardnum.split())
        if (card_number.isdigit() and len(card_number) > 1):
            temp = self.convert_Luhn(card_number)
            if temp%10 == 0:
                return True
            else:
                return False
        else:
            return False
        
    def convert_Luhn(self, input_string):
        card_val_int = int(input_string)
        Luhn_val = 0
        even_digit = False
        while (card_val_int > 0):
            current_val = card_val_int%10
            if (even_digit == True):
                current_val *= 2
                if (current_val > 9):
                    current_val -= 9
                even_digit = False  
            else:
                even_digit = True
            Luhn_val += current_val
            card_val_int = int(card_val_int/10)
        return Luhn_val
        
    