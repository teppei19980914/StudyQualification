# SQLとデータベース制約や関係演算等

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報セキュリティスペシャリスト平成22年秋期 午前Ⅱ 問21](https://www.sc-siken.com/kakomon/22_aki/am2_21.html)  
[情報セキュリティスペシャリスト平成24年春期 午前Ⅱ 問21](https://www.sc-siken.com/kakomon/24_haru/am2_21.html)  
[情報処理安全確保支援士令和3年秋期 午前Ⅱ 問21](https://www.sc-siken.com/kakomon/03_aki/am2_21.html)  

## SQL における制約(Constraint)とは  

制約とは **データの正確性/一貫性/整合性を保証するためのルール** であり、ACID特性のうち「一貫性(Consistency)」を担保する重要な仕組みです。  

## NOT NULL 制約

### 意味  

列に **NULL が入ることを禁止**します。  

### 例

```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name    VARCHAR(50) NOT NULL
);
```

### 特徴  

- INSERT/UPDATE で NULL を入れるとエラー  
- 空文字列 ("") と NULL は別扱い  

## CHECK 制約

### 意味  

列の値が **指定した条件を満たす場合のみ許可** します。  

### 例

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    age    INT CHECK(age BETWEEN 0 AND 150),
    grade  CHAR(1) CHECK(grade IN ('A','B','C'))
);
```

### 特徴  

- 条件違反時はエラー  
- RDBMS によりサポート差あり(MySQL 8.0 未満は無視)  

## UNIQUE 制約(重複禁止)

### 意味  

列、または列の組が **重複してはいけません**。  

### 例

```sql
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    email      VARCHAR(255) UNIQUE
);
```

複数列のユニークも可能：  

```sql
UNIQUE (room_id, reserved_day)
```

### 特徴  

- NULL は複数許可(SQL標準)  
- 多くのDBで自動的にインデックス作成  

## PRIMARY KEY 制約(主キー)

### 意味  

行を一意に識別するキーです。  

#### 主キーの性質  

- NOT NULL  
- UNIQUE  
- 1表に1つだけ定義可能  

### 例

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name       VARCHAR(50)
);
```

複合主キー：  

```sql
PRIMARY KEY(student_id, subject_id)
```

## FOREIGN KEY 制約(参照整合性制約)

### 意味  

他表の **主キーまたは UNIQUE 列** を参照し、整合性を保証します。  

### 例

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY
);

CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);
```

## 外部キーの参照アクション(ON DELETE/ON UPDATE)

| アクション | 動作 |
|-----------|------|
| NO ACTION | 不整合があれば拒否 |
| RESTRICT  | 参照されていれば削除/更新不可 |
| CASCADE   | 親の削除/更新を子へ伝播 |
| SET NULL  | 親削除時に子を NULL |
| SET DEFAULT | 既定値を設定 |

例：  

```sql
FOREIGN KEY(customer_id)
  REFERENCES customers(customer_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
```

## ALTER TABLE による制約追加/削除

### 追加

```sql
ALTER TABLE users
  ADD CONSTRAINT email_unique UNIQUE(email);
```

### 削除

```sql
ALTER TABLE users
  DROP CONSTRAINT email_unique;
```

## 周辺知識

### トランザクション(ACID)

- **A**tomicity(原子性)  
- **C**onsistency(一貫性)← 制約が担当  
- **I**solation(独立性)  
- **D**urability(永続性)  

### ER 図と外部キー

- 1対多は外部キーで表現  
- 多対多は中間テーブル(交差テーブル)を用いる  

### 正規化

外部キーは正規化の結果として自然に登場する。

## 関係演算(Relational Algebra)の体系整理

関係演算は **関係データベースの理論的基盤**であり、SQL の構文の多くは関係演算を基に設計されています。  

### 基本演算(5つ)

#### 選択(Selection：σ)

行を条件で絞り込む演算です。  
SQL の **WHERE** に対応しています。  

例(年齢>=20 の社員)：  

```
σ age >= 20 (Employees)
```

#### 射影(Projection：π)

列を抽出する演算です。  
SQL の **SELECT 列名** に対応します。  

例：  

```
π name, age (Employees)
```

#### 直積(Cartesian Product：×)

2つの関係をすべての組み合わせで結合します。  
SQL の **CROSS JOIN** に対応しています。  

#### 和(Union：∪)

2つの関係の和集合(重複削除)です。  
SQL の **UNION** に対応。  

#### 差(Difference：−)

片方にしか存在しない行を取得します。  
SQL の **EXCEPT/MINUS** に対応。  

### 派生演算(応用演算)

#### 共通(Intersection：∩)

共通する行を抽出します。  
SQL の **INTERSECT** に対応。  

#### 結合(Join)

SQL JOIN の原型です。  
自然結合/等値結合などが含まれます。  

例：  

```
Employees ⋈ Employees.dept_id = Departments.dept_id Departments
```

#### 商(Division：÷)

「すべての条件を満たす行」を求める演算です。  
SQL に直接の構文はなく、NOT EXISTS や HAVING COUNT で表現します。  

## SQL の4大命令(DML)

### SELECT(検索)

```sql
SELECT name, age FROM employees WHERE age >= 20;
```

### INSERT(追加)

```sql
INSERT INTO employees (id, name, age) VALUES (1, 'Taro', 30);
```

### UPDATE(更新)

```sql
UPDATE employees SET age = age + 1 WHERE id = 1;
```

### DELETE(削除)

```sql
DELETE FROM employees WHERE id = 1;
```

## SQL の周辺知識

### JOIN の種類

- INNER JOIN  
- LEFT/RIGHT OUTER JOIN  
- FULL OUTER JOIN  

### GROUP BY と HAVING

集約後の条件は HAVING。  

### ビュー(VIEW)

複雑なクエリを仮想表として再利用。  

### インデックス

検索性能改善(B+tree/Hash)。  

### GRANT文

#### 何を付与するか（Privilege）

表・ビュー等のDBオブジェクトに対する権限（例：SELECT/INSERT/UPDATE/DELETE等）を主体（ユーザ・ロール等）に付与します。  

#### 誰に付与するか（User / Role / PUBLIC）

多くのDBでは「ユーザ」「ロール（役割）」「PUBLIC（全員に相当する集合）」に付与できます。  
ただし、**PUBLICは“全権付与”ではありません**。単に「対象集合が広い」だけです（付与される権限の種類・範囲はGRANT句で明示したものに限定されます）。  

#### WITH GRANT OPTION（付与権）の意味

##### 何が起きるか

`WITH GRANT OPTION` を付けると、**受領者は「その権限をさらに他者へGRANTできる」**ようになります。  
逆に言えば、これが無い場合は「自分は使えるが、他人へ配れない」です。  

##### リスク

付与権は“権限の拡散”を招きやすいので、運用上は最小権限の観点から慎重に扱います。  

#####  REVOKEとの関係（CASCADEが絡む典型論点）

付与権で連鎖的に権限が配られた後に取り消すと、**連鎖（依存関係）**が発生します。  
例えばSQL Serverの説明では、GRANT OPTIONで与えられた権限を取り消す際にCASCADEを付けないと失敗し得る旨が示されています。  
製品差はありますが、「付与権は撤回が難しくなり得る」という実務的ポイントは共通理解として重要です。

### ビューと権限

- ビューは「表のように見せる論理オブジェクト」であり、参照権限（SELECT）の付与対象になり得る  
- ただし、ビューの定義や実装によっては、基表権限や所有者権限（definer/invokerの扱い）など追加論点が出る  
