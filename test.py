def Judgement_department_num(code):  #담당부서 번호 판단 함수
    if code[6] == 'N':
        return '00'
    elif int(code[1] + code[2]) < 20:
        return '12'
    elif code[3] == 'O' or code[3] == 'P' or code[3] == 'Q' or code[0]== 'F':
        return  '10'

    elif code[3] == 'A' or code[3] == 'B' or code[3] == 'C' or code[3] == 'D' :
        return '01'
    elif code[3] == 'E' or code[3] == 'K':
        return '02'
    elif code[3] == 'F' :
        return  '03'
    elif code[3] == 'G' :
        return  '04'
    elif code[3] == 'H':
        if int(code[4]+code[5])<=59  :
            return "05"
        elif int(code[4]+code[5])>59  :
            return "06"
    elif code[3] == 'L' :
        return  '07'
    elif code[3] == 'M' :
        return  '08'
    elif code[3] == 'N' :
        return  '09'

    elif code[3] == 'R' or code[3] == 'S' or code[3] == 'V' :
        return  '11'
    else :
        return '00'

k = "F46D03Y"
print(Judgement_department_num(k))