# 175번 Combine Two Tables

[문제 보러가기](https://leetcode.com/problems/combine-two-tables/)

## 🅰 설계

테이블 두개가있다!!! personid가 겹치므로 조인을 해보자.

## ✅ 후기

```mysql
SELECT Person.FirstName, Person.LastName, Address.City, Address.State from Person LEFT JOIN Address on Person.PersonId = Address.PersonId;
```

// 새롭게 알게되거나 공유해서 알게된 점
조인조인조인~

// 고생한 점
