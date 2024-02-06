import pymysql as ps
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
data = 3

if data == 1:
    conn = ps.connect(host='localhost', user='root', password='1234', db='Project_mig', charset='utf8')
    curs = conn.cursor()

    curs.execute("""
select tk.`시점`, `대상별`,`15세이상인구 (천명)`,`15세 이상 인구 (천명)`, `경제활동인구 (천명)`,`- 경제활동인구 (천명)`, tk.`실업률 (%)`, tm.`실업률 (%)`
from total_korea as tk
inner join total_mig as tm
on tk.`시점` = tm.`시점`
where `대상별` = '이민자'""")

    rows = curs.fetchall()

    cols = ['시점', '대상별', '15세이상인구 (천명)', '15세 이상 인구 (천명)', '경제활동인구 (천명)', '- 경제활동인구 (천명)', '실업률 (%)', '실업률 (%)']
    df =  pd.DataFrame(rows, columns=cols)
    print(df)

    plt.figure(figsize=(12,3))
    plt.subplot(1,3,1)
    plt.plot(df['시점'], df['15세이상인구 (천명)'], label='국내 15세 이상 인구 (천명)', color='#4494FF')
    plt.title('국내 15세 이상 인구 (천명)')
    plt.xticks(df['시점'], df['시점'])

    plt.subplot(1,3,2)
    plt.plot(df['시점'], df['15세 이상 인구 (천명)'], label='이민자 15세 이상 인구 (천명)', color='red')
    plt.title('이민자 15세 이상 인구 (천명)')
    plt.xticks(df['시점'], df['시점'])

    plt.subplot(1,3,3)
    plt.bar(df['시점'], df['15세이상인구 (천명)'], label='15세이상인구 (천명)')
    plt.bar(df['시점'], df['15세 이상 인구 (천명)'], label='15세이상인구 (천명)')
    plt.title('15세 이상 인구 비교 (천명)')
    plt.xticks(df['시점'], df['시점'])

    plt.tight_layout()
    plt.show()

    conn.close()

if data == 2:
    conn = ps.connect(host='localhost', user='root', password='1234', db='Project_mig', charset='utf8')
    curs = conn.cursor()

    curs.execute("""
select tk.`시점`, `대상별`,`15세이상인구 (천명)`,`15세 이상 인구 (천명)`, `경제활동인구 (천명)`,`- 경제활동인구 (천명)`, tk.`실업률 (%)`, tm.`실업률 (%)`
from total_korea as tk
inner join total_mig as tm
on tk.`시점` = tm.`시점`
where `대상별` = '이민자'""")

    rows = curs.fetchall()

    cols = ['시점', '대상별', '15세이상인구 (천명)', '15세 이상 인구 (천명)', '경제활동인구 (천명)', '- 경제활동인구 (천명)', '실업률 (%)', '실업률 (%)']
    df = pd.DataFrame(rows, columns=cols)
    print(df)

    plt.figure(figsize=(12, 3))
    plt.subplot(1, 3, 1)
    plt.plot(df['시점'], df['경제활동인구 (천명)'], label='국내 15세 이상 인구 (천명)', color='#4494FF')
    plt.title('국내 경제활동 인구 (천명)')
    plt.xticks(df['시점'], df['시점'])

    plt.subplot(1, 3, 2)
    plt.plot(df['시점'], df['- 경제활동인구 (천명)'], label='이민자 15세 이상 인구 (천명)', color='red')
    plt.title('이민자 경제활동 인구 (천명)')
    plt.xticks(df['시점'], df['시점'])

    plt.subplot(1, 3, 3)
    plt.bar(df['시점'], df['경제활동인구 (천명)'], label='15세이상인구 (천명)')
    plt.bar(df['시점'], df['- 경제활동인구 (천명)'], label='15세이상인구 (천명)')
    plt.title('경제 활동 인구 (천명)')
    plt.xticks(df['시점'], df['시점'])

    plt.tight_layout()
    plt.show()

    conn.close()


# 경제 효과 계산
if data == 3:
    conn = ps.connect(host='localhost', user='root', password='1234', db='Project_mig', charset='utf8')
    curs = conn.cursor()

    curs.execute('''
    select `시점`, 
	`100만원 미만 (천명)`*50, 
	`100만원 이상 ~200만원 미만 (천명)`*150,
	`200만원 이상 ~300만원 미만 (천명)`*250,
	`300만원 이상 ~ (천명)`*350
from income_mig 
where `대상별(1)` = '외국인';
    ''')

    rows =  curs.fetchall()
    df = pd.DataFrame(rows, columns=['시점', '100만원 미만 (천명)', '100만원 이상 ~200만원 미만 (천명)', '200만원 이상 ~300만원 미만 (천명)', '300만원 이상 ~ (천명)'])
    print(df)