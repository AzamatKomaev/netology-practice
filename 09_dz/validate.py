import re


REGEX_PATTERN = r'/(([АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{1,2})(\d{2,3})|(\d{4}[АВЕКМНОРСТУХ]{2})(\d{2})|(\d{3}C?D{1,2}\d{3})(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]\d{4})(\d{2})|(\d{3}[АВЕКМНОРСТУХ])(\d{2})|(\d{4}[АВЕКМНОРСТУХ])(\d{2}))/i'

def validate_rus_auto_number(car_id: str):
    is_valid = re.match(REGEX_PATTERN, car_id)
    print(is_valid)
    
    

def main():
    validate_rus_auto_number("А222ВС")


if __name__ == '__main__':
    main()
