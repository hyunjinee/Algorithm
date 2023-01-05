# 595. Big Countries

![595](https://user-images.githubusercontent.com/63354527/107177068-44238200-6a14-11eb-99ad-51d9f04211ef.PNG)

문제 해석: 3백만보다 크거나 2500백만 보다 인구가 많으면 큰 도시이다. sql문을 써서 그 도시들을 나타내라.

## 풀이 1

```sql
SELECT name, population, area FROM World WHERE population > 25000000 OR area > 3000000
```

## 풀이 2

```sql
#Union
SELECT name, population, area
FROM World
WHERE area > 3000000

UNION

SELECT name, population, area
FROM World
WHERE population > 25000000
```

Why Union is faster than OR?

Strictly speaking, Using UNION is faster when it comes to cases like scan two different column like this.

(Of course using UNION ALL is much faster than UNION since we don't need to sort the result. But it violates the requirements)

Suppose we are searching population and area, Given that MySQL usually uses one one index per table in a given query, so when it uses the 1st index rather than 2nd index, it would still have to do a table-scan to find rows that fit the 2nd index.

When using UNION, each sub-query can use the index of its search, then combine the sub-query by UNION.
