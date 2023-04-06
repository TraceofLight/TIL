# TIL (SQL 복기)

### SELECT 문

테이블에 있는 데이터를 조회하는 명령문

```sql
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(date_of_birth, "%Y-%m-%d") as DATE_OF_BIRTH
FROM MEMBER_PROFILE
```

이와 같이 FROM 절과 함께 사용하여 테이블과 대상을 지정할 수 있다.

### WHERE 문

특정한 조건에 부합하는 데이터를 조회할 수 있도록 하는 조건 명령문

```sql
WHEWE TLNO IS NOT NULL AND GENDER = 'W' AND MONTH(DATE_OF_BIRTH) = 3
```

### ORDER BY 문

출력되는 결과물을 정렬하는 명령문

```sql
ORDER BY MEMBER_ID ASC (DESC)
```

정렬 대상인 열과 함께 사용하며 오름차순과 내림차순을 취사 선택할 수 있다.