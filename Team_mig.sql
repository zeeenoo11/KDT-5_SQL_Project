use Project_mig;


desc total_korea ;


ALTER TABLE total_korea
ADD foreign key (`시점`) 
references total_mig(`시점`);


ALTER TABLE total_mig
ADD PRIMARY KEY (`시점`, `대상별`);

ALTER TABLE total_mig
ADD PRIMARY KEY (`시점`, `대상별`);


select * from total_korea ;

select `시점`, `15세이상인구 (천명)`, `경제활동인구 (천명)`, `실업률 (%)`
from total_korea;

select * from total_mig ;

select `시점`, `15세 이상 인구 (천명)`, `- 경제활동인구 (천명)`, `실업률 (%)`
from total_mig as tm;

# inner join 활용해 추출
select tk.`시점`, `대상별`,`15세이상인구 (천명)`,`15세 이상 인구 (천명)`, `경제활동인구 (천명)`,`- 경제활동인구 (천명)`, tk.`실업률 (%)`, tm.`실업률 (%)`
from total_korea as tk
inner join total_mig as tm
on tk.`시점` = tm.`시점`
where `대상별` = '이민자';

select tk.`시점`, `대상별`,`15세이상인구 (천명)`,`15세 이상 인구 (천명)`, `경제활동인구 (천명)`,`- 경제활동인구 (천명)`, tk.`실업률 (%)`, tm.`실업률 (%)`
from total_korea as tk
inner join total_mig as tm
on tk.`시점` = tm.`시점`
where `대상별` = '이민자';

select tk.`시점`, `대상별`,`15세이상인구 (천명)`,`15세 이상 인구 (천명)`, `경제활동인구 (천명)`,`- 경제활동인구 (천명)`, tk.`실업률 (%)`, tm.`실업률 (%)`
from total_korea as tk
inner join total_mig as tm
on tk.`시점` = tm.`시점`
where `대상별` = '이민자';


# ------------ 경제 효과 계산
# 소득 총합
select * from income_mig ;

select `시점`, 
	`100만원 미만 (천명)`*50 as '<100', 
	`100만원 이상 ~200만원 미만 (천명)`*150 as '100 <= x < 200',
	`200만원 이상 ~300만원 미만 (천명)`*250 as '200 <= x < 300',
	`300만원 이상 ~ (천명)`*350 as '300 <= x'
from income_mig 
where `대상별(1)` = '외국인';
# 2017 191,100
# 

select * from gdp ;

create database immigrant_project;

use immigrant_project;

desc city_population ;

# 다중 PK 설정 (city_population)
alter table city_population 
add primary key (소재지, 시점);

# 다중 PK 참조
desc crime_by_region ;

alter table crime_by_region 
add foreign key(발생지역별, 시점) references city_population (소재지, 시점);


# 10만명당 범죄건수 지역별, 년도별 쿼리 (2015 ~ 2022)
select cbr.범죄별1, cbr.시점, cbr.발생지역별, cbr.데이터
from crime_by_region cbr 
	inner join city_population cp 
		on (cp.소재지, cp.시점) = (cbr.발생지역별, cbr.시점)
where (cbr.범죄별1 = 'A/Bⅹ100,000 (건/10만명)') & (cbr.시점 > 2014) ;

# 다중 PK 참조
desc foreign_distribution ;

alter table foreign_distribution 
add foreign key(행정구역별, 시점) references city_population (소재지, 시점);


# 지역별, 년도별 귀화자 비율 쿼리 (2015 ~ 2022)
select fd.행정구역별, fd.시점, fd.거주외국인별1, fd.합계, cp.전체인구,
		fd.합계 / cp.전체인구 as 귀화자비율
from city_population cp 
	inner join foreign_distribution fd 
		on (cp.소재지, cp.시점) = (fd.행정구역별, fd.시점)
where (fd.거주외국인별1 = '한국국적을 취득한 자 (명)') & (fd.거주외국인별2 = '소계');

# 국내 거주 외국인의 전반적인 삶의 만족도 (2022)
select * from life_satisfaction
where 특성별2 = '계';

# 영주권자, 귀화자의 한국사회 구성원이 되는데 문제가 되는 정도 (2022)
select * from society_member
where 특성별2 = '계';

