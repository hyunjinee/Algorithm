import sys
vowel = {'a','e','i','o','u'}
while (1):
	test = sys.stdin.readline().rstrip()
	if test == 'end':
		break
	pw = list(test)
	v_flag = 0 # 모음 존재하는지 확인
	v_cnt = 0  # 모음 3개 연속인지 확인
	c_cnt = 0  # 자음 3개 연속인지 확인
	err = 0  # 같은 문자 연속 2개 or 자음/모음 연속 3개인 경우 1
	for i in range(len(pw)):
		if i > 0:
			if pw[i] == pw[i-1]:
				if pw[i] != 'e' and pw[i] != 'o':
					err = 1
					break
		if pw[i] in vowel:
			v_flag = 1
			v_cnt += 1
			c_cnt = 0
			if v_cnt == 3:
				err = 1
				break
		else:
			v_cnt = 0
			c_cnt += 1
			if c_cnt == 3:
				err = 1
				break
	
	if (err != 1) and (v_flag == 1):
		print("<"+ test +"> is acceptable.")
	else:
		print("<" + test + "> is not acceptable.")