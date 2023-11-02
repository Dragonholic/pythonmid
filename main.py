# 병원 대기실 존재 대기실 들어온 순으로 앉는 자료형 구성
# 병원에는 13개의 부서 존재
# 각환자 데이터는 다음과 같은 형식 가짐
# 성별(1) + 나이(2) + 질병코드(3) + 접수유무(1)


def Judgement_code(code): #주어진 코드 판단 함수

    if code[0] == 'm':
        man =  1
        woman = 0
    else:
        woman = 1
        man = 0

    old = code[1]+code[2]

    sickcode = code[3]+code[4]+code[5]

    if code[6] == 'Y':
        receipt = 1
    else:
        receipt = 0

    process_code = [man, woman, old, sickcode,  receipt]

    return process_code


def Judgement_department(code):  #담당부서 판단 함수

    if code[6] == 'N':
        return '접수처'
    elif int(code[1]+code[2]) <20 :
        return  '소아청소년과'
    elif code[3] == 'O' or code[3] == 'P' or code[3] == 'Q' or code[0]== 'F':
        return  '산부인과'

    elif code[3] == 'A' or code[3] == 'B' or code[3] == 'C' or code[3] == 'D' :
        return '감염외과'
    elif code[3] == 'E' or code[3] == 'K':
        return '내과'
    elif code[3] == 'F' :
        return  '정신의학과'
    elif code[3] == 'G' :
        return  '신경외과'
    elif code[3] == 'H':
        if int(code[4]+code[5])<=59  :
            return "안과"
        elif int(code[4]+code[5])>59  :
            return "이비인후과"
    elif code[3] == 'L' :
        return  '피부과'
    elif code[3] == 'M' :
        return  '정형외과'
    elif code[3] == 'N' :
        return  '비뇨기과'

    elif code[3] == 'R' or code[3] == 'S' or code[3] == 'V' :
        return  '응급외과'

    else :
        return '접수처'


def Judgement_department_num(code):  #담당부서 번호 판단 함수
    if code[6] == 'N':
        return '접수처'
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

def Judgement_department_worker(code):
    deparment = code[0]+code[1]

    return deparment





def Judement_workercode(code):
    workdepartment_code = code[0]+code[1]
    holyday = code[2]
    bill = code[3]+code[4]+code[5]+code[6]
    salary = code[7]+code[8]+code[9]+code[10]
    worker = [workdepartment_code,holyday,bill,salary]
    return worker








def Print_parient(num, wname, man, woman): #출력함수
    print(num )
    print(wname )
    print(man)
    print(woman)
    return





# 실행 부분



waiting_room = []  #환자 대기
worker_room = []    #직원 대기


#부서별


jupsu = ["00","접수처",0,0,0] #부서번호 부서명 부서진료수익 부서별기여도 부서인원
gam = ["01","감염외과",0,0,0]
ne = ["02","내과", 0,0,0]
psy = ["03","정신의학과",0,0,0]
sin = ["04","신경외과",0,0,0]
an = ["05","안과",0,0,0]
ee = ["06","이비인후과",0,0,0]
pe = ["07","피부과",0,0,0]
jung = ["08", "정형외과",0,0,0]
be = ["09", "비뇨기과",0,0,0]
san = ["10", "산부인과",0,0,0]
im = ["11", "응급외과",0,0,0]
so = ["12", "소아청소년과",0,0,0]
department_set = [jupsu, gam, ne, psy, sin, an, ee, pe, jung, be, san, im, so]
department_numset = ["00","01","02","03","04","05","06","07","08","09","10","11","12"]


working_people = []





w_n = input()   #직원 수 입력
w_n = int(w_n)  #직원 수
for i in range(w_n):

    worker_room.append(input()) #각 직원 직원번호 부여

for j in range(w_n):
    worker_code = waiting_room[j] # 각 직원 배속 부서확인

    workplace_code = worker_code[0]+worker_code[1]

    if workplace_code == '01': # 부서에 인원 추가
        gam[4] += 1
    elif workplace_code == '02':
        ne[4] += 1
    elif workplace_code == '03':
        psy[4] += 1
    elif workplace_code == '04':
        sin[4] += 1
    elif workplace_code == '05':
        an[4] += 1
    elif workplace_code == '06':
        ee[4] += 1
    elif workplace_code == '07':
        pe[4] += 1
    elif workplace_code == '08':
        jung[4] += 1
    elif workplace_code == '09':
        be[4] += 1
    elif workplace_code == '10':
        san[4] += 1
    elif workplace_code == '11':
        im[4] += 1
    elif workplace_code == '12':
        so[4] += 1
    elif workplace_code == '00':
        jupsu[4] += 1


for i in range(12):
    if department_set[i] > 2:
        exit(-1)             #직원이 3명 이상인 경우 오류 처리










p_n = input()   #환자 수 입력
p_n = int(p_n)  #환자 수
for i in range(p_n):

    waiting_room.append(input())






total_revenue = 0    #총 수익
total_expenditure = 0   #총 지출
today = 0
patient_count = 0
lose_patient = 0
patient_count_not = 0 #휴일 판단 카운트


for i in range(p_n):
    patient_code = waiting_room.pop(0) # 첫순서 뽑기
    department = Judgement_department(patient_code) #부서이름 저장
    process_code = Judgement_code(patient_code) #판단한 코드 배열
    department_num = Judgement_department_num(patient_code) #부서번호 저장

    for j in range(13):                                     #어느 부서세요
        if department_numset[j] == department_num :         #
            if department_set[j][4] == 0 :  #부서에 인원이 없으면 돌려보냄
                lose_patient += 1           #놓친 인원 추가

            else:
                for k in range (w_n):       #부서에 사람 찾기
                    if department_num == Judgement_department_num(worker_room[k]) :

                        if Judement_workercode(worker_room[k])[2] != (today % 7) :        #휴일 아니면 진료

                            department_set[j][2] += Judement_workercode(worker_room[k])[3]  # 부서 집합에 진료비 합산
                            total_revenue += Judement_workercode(worker_room[k])[3] #총 수익에 진료비 합산
                            #######################일한 사람 진료수익 계산해야함
                            working_people.append(k)  #일한 사람 기록

                            patient_count += 1                  # 진료한 환자 +1
                            patient_count_not = 0               # 후배 대신 진료
                            if patient_count % 10 == 0:         # 10명 진료하면 날자 지남
                                today += 1

                        else :
                            patient_count_not += 1

                if patient_count_not !=  0:  # 환자가 휴일로 진료 못받았으면 놓친 인원 추가
                    lose_patient += 1
                    patient_count_not = 0






    if today % 28 == 0 :                # 4주차 일요일날월급 제공
        for j in range(w_n):
            total_expenditure += int(Judement_workercode(worker_room[j])[3])




















#출력단

print("-------------------------------\n")
print("운영일수 총수입 총지출 실수입 처리환자 놓친환자\n")
print("-------------------------------\n")
#병원통계 출력
print("-------------------------------\n")
print("직원번호 소속부서 총진료수익 기여도\n")
print("-------------------------------\n")
#직원 성과 출력


print("-------------------------------\n")
print("총 ",non,"명 \n")
print("-------------------------------\n")
print("부서번호 부서명 남자수 여자수\n")
print("-------------------------------\n")
#부서통계 출력
print("-------------------------------\n")
print("총 ",non,"명 \n")





