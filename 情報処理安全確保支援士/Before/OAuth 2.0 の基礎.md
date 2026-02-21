# OAuth 2.0 の基礎

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士平成29年春期 午前Ⅱ 問14](https://www.sc-siken.com/kakomon/29_haru/am2_14.html)  
[情報処理安全確保支援士令和5年秋期 午前Ⅱ 問14](https://www.sc-siken.com/kakomon/05_aki/am2_14.html)  

## OAuth 2.0 とは(エビデンス：RFC 6749)

OAuth 2.0 は **リソース所有者(ユーザ)の認証情報を第三者アプリに渡さず、安全に API 利用権限(アクセストークン)を委譲する仕組み** です。  

### 主な登場人物(RFC 6749 Section 1.1)

|名称|説明|
|----|----|
|**Resource Owner(ユーザ)**|リソースサーバ内の保護された情報へのアクセスを許可するエンドユーザーであり、クライアントの利用者|
|**Client(クライアントアプリ)**|リソースオーナーの認可を得てリソースサーバにアクセスするサードパーティアプリケーション|
|**Authorization Server(認可サーバ)**|ユーザ認証を行い、トークンを発行|
|**Resource Server(API サーバ)**|保護された情報を保持し、アクセストークンの検証を行い、リソースを提供|

OAuth2.0 は **認証ではなく認可のプロトコル** である点が重要です。  

## OAuth2.0 のトークン種別(RFC 6749/RFC 6750)

### アクセストークン(Access Token)

- API へのアクセス権限を持つトークン  
- **Bearer Token(RFC 6750)** が最も一般的  
- Bearer は「提示するだけで権限を与える」ため、**漏洩すると即悪用される**  

### リフレッシュトークン(Refresh Token)

- アクセストークン再発行のために使用  
- 長期間有効であることが多く、厳重に管理される必要がある  
- パブリッククライアントでは利用制限されることがある  

## OAuth2.0 の代表的なフロー(RFC 6749)

### Authorization Code Grant(推奨)

最も安全とされる方式です。  
サーバ側でトークン授受を行い、秘密保持が可能です。  

#### PKCE(RFC 7636)  

スマホアプリなどのパブリッククライアント向けに安全性を強化します。  
code_verifier と code_challenge によるチャレンジレスポンスで攻撃を防ぎます。  

主な防御対象：  

- 認可コードの窃取攻撃  
- 中間者攻撃  

### Implicit Grant

アクセストークンが URL フラグメントで直接返却される方式です。  
**トークン漏洩リスクが高く、現在は使用非推奨となっています**。  

### Client Credentials Grant

サーバ間通信で利用します。  
ユーザは登場しません。  

### Resource Owner Password Credentials(ROPC)

ユーザ ID/パスワードをアプリが直接受け取る方式です。  
**セキュリティ上の問題から廃止方向です**。

## OAuth2.0 の脅威と対策(RFC 6819)

### 主な攻撃例

|攻撃|説明|
|----|----|
|認可コード窃取攻撃|攻撃者が認可コードを奪い取りトークンを取得|
|リダイレクトURI差し替え|攻撃者が悪意のコールバックURLを登録させる|
|アクセストークン漏洩|Bearer Token が盗まれ、API が不正利用される|
|CSRF攻撃|ログイン/認可画面への強制遷移|

### 重要な対策(RFC 6819)

- Redirect URI の厳格一致  
- PKCE の導入  
- 状態トークン state による CSRF 防止  
- HTTPS の必須利用  
- トークンの短命化  
- Refresh Token へのローテーション導入(Token Binding)  

試験では **state パラメータの役割(CSRF 対策)** が頻出です。  

## OpenID Connect(認証)との違い

OAuth2.0 ：**認可(Authorization)**  
OpenID Connect(OIDC)： **認証(Authentication)**  

OIDC は OAuth2.0 を拡張し、ID トークン(JWT)を使用してユーザ認証を実現します。  

OIDC の主な仕様：  

- ID Token(JWT)  
- UserInfo エンドポイント  
- Discovery(.well-known/openid-configuration)  

## セキュリティトークンの仕様(知識補強)

|トークン|仕様|特徴|
|--------|------|------|
|JWT|RFC 7519|署名付き JSON。ID Token などに利用|
|Bearer Token|RFC 6750|所持者に権限付与|
|SAML Assertion|OASIS SAML|企業の SSO で利用|
