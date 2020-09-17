def solution(phone_number):
    return '*' * len(phone_number[:-4]) + phone_number[-4:]
    
if __name__=="__main__":

    phone_number = "01033334444"
    print(f'#: {phone_number} | sol: {solution(phone_number)} | ans: *******4444')
    
    phone_number = "027778888"
    print(f'#: {phone_number} | sol: {solution(phone_number)} | ans: *****8888')
