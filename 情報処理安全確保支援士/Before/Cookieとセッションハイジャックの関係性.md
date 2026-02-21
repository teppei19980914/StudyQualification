# Cookieとセッションハイジャックの関係性

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士平成29年春期 午前Ⅱ 問5](https://www.sc-siken.com/kakomon/29_haru/am2_5.html)  
[情報処理安全確保支援士平成30年春期 午前Ⅱ 問11](https://www.sc-siken.com/kakomon/30_haru/am2_11.html)  

## 1. セッションIDとCookieの基本(基礎整理)
HTTPはステートレスであるため、**ユーザ識別/ログイン状態保持**のために Web アプリケーションはセッションID(Session ID)を利用します。  

典型例：  

```
Set-Cookie: SESSIONID=abc123; Secure; HttpOnly; SameSite=Lax
```

### Cookieの主な属性

|属性|意味|
|---|---|
|Secure|HTTPSでのみ送信|
|HttpOnly|JavaScript 未参照化(XSS対策)|
|SameSite|CSRF対策(Lax/Strict/None)|
|Domain|送信先ドメイン制御|
|Path|送信先URLパス制御|
|Expires/Max-Age|有効期限|

---

## 2. セッションハイジャック攻撃の種類

|攻撃名|概要|
|---|---|
|**セッションID盗聴**|HTTPSでないと平文盗聴される|
|**XSSによるCookie奪取**|document.cookie が盗まれる|
|**CSRF**|Cookieを悪用して本人として操作|
|**Session Fixation(セッション固定化)**|攻撃者が「特定のセッションID」を被害者に使わせる|

## 3. Session Fixation(セッション固定化)攻撃とは

**攻撃者があらかじめ用意したセッションIDを、被害者に使わせてログインさせる攻撃** のことです。  

#### ■ 攻撃の流れ(RFC 6265/OWASP ASVS)

1. 攻撃者が Web サイトにアクセスし「未ログイン状態のセッションID」を取得  
2. そのセッションIDを被害者に強制的に使わせる  
   - URL パラメータ：`https://site/login?sessionid=AAA`  
   - Set-Cookie ヘッダを偽装  
   - 脆弱なサイトで攻撃者が Cookie を指定できるケース  
3. 被害者がそのセッションIDでログインしてしまう  
4. 攻撃者は同じセッションIDでログイン状態を再現できる(成り代わり成功)  

#### ■ 固定化攻撃が成立する条件

- **ログイン前後でセッションIDが変わらないこと**  
- Cookie による正しい制御がされていないこと  
- SameSite/HttpOnly/Secure が適切でない場合が多い  

## 4. Session Fixation 攻撃に有効な対策(必須)

### ✦ 1. ログイン時にセッションIDを再生成する(最重要)

OWASP ASVS/OWASP Session Management チートシートでは、**ログイン成功時に必ず新しいセッションIDへ再発行**が推奨されています。  

```
login_success:
    regenerate_session_id()
```

これにより、攻撃者が用意した ID を使わせてもログイン時には無効化されます。

### ✦ 2. セッションIDを URL に含めない(URL-based Session)

URL パラメータにセッションIDがあると下記などに情報が残ってしまい、漏洩リスクが極めて高いため厳禁です。  

- ブラウザ履歴  
- リファラ  
- ブックマーク  
- Webサーバログ  

### ✦ 3. Cookie の属性設定(Secure/HttpOnly/SameSite)

|属性|効果|
|---|---|
|Secure|HTTPSのみ送信 → 盗聴防止|
|HttpOnly|JSから参照不可 → XSSで盗まれない|
|SameSite=Lax/Strict|外部サイトから Cookie を送信させない|

Session Fixation 自体は Cookie 属性だけで完全には防げませんが、**攻撃者が Cookie を強制送信する可能性を下げる** 効果があります。  

### ✦ 4. セッション有効期限の短縮

短いほど攻撃成功確率が下がります。  

### ✦ 5. User-Agent/IP アドレスなどでセッション紐付け

100%ではないが、攻撃成功を大幅に困難にします。  

## 5. セッションID生成の要件(OWASP)

- **128bit以上の暗号学的乱数**  
- **CSPRNG(暗号学的擬似乱数生成器)で生成**  
- predictable(予測可能)でないこと  

セッション固定化攻撃では「予測」ではなく「強要」が問題なので、**乱数の強度だけでは不十分** である点に注意が必要です。  

## 6. Cookie と Session Fixation の関係整理

|対策|Session Fixationに対する効果|補足|
|---|---|---|
|セッションID再生成|◎ 完全対策|必須|
|Secure|△|Cookie強制送信の難度が上がる|
|HttpOnly|×|Session Fixation は Cookie 読み取り不要|
|SameSite|○|外部からの強制送信を一部防ぐ|
|短期有効期限|△|攻撃成功ウィンドウが縮む|

**Session Fixation を根本的に封じられるのは「セッションID再生成」だけ**です。  

## 7. 周辺知識(支援士/高度試験頻出)

### ● CSRFとの違い

|項目|Session Fixation|CSRF|
|---|---|---|
|目的|攻撃者が用意したセッションIDを使わせる|ユーザのCookieを悪用して不正操作|
|前提|固定化した ID でログインさせる|正規のセッションIDを保持している|
|関連属性|SameSite が間接的効果|SameSite が主対策|

### ● XSSとの関係

* XSSは「セッションIDを盗む」  
* Session Fixationは「セッションIDを押し付ける」  

両者は**攻撃ベクトルが逆方向**なのです。  

### ● OAuth2.0 のセッション固定化

OAuthの redirect_uri に State を含めない場合、「セッション固定化(State固定化)」が発生します。  
