# シングルサインオン(SSO)と SAML 認証

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士令和5年春期 午前Ⅱ 問3](https://www.sc-siken.com/kakomon/05_haru/am2_3.html)  

## 2. シングルサインオン(SSO)とは  

### ■ 定義

シングルサインオン(SSO)とは、**一度の認証で複数のサービスにログインできる仕組み** です。  

NIST SP 800-63 では、認証(Authentication)と認可(Authorization)を区別しID 連携が行われる形態を「Federation(フェデレーション)」と定義しています。  

### ■ SSO が必要とされる理由  

- 利用者の利便性向上  
- パスワード管理の負荷軽減  
- パスワード再利用リスクの低減  
- アクセス統制の一元管理(IDP側で統制が可能)  
- ログ管理の統合  

## 3. フェデレーション(ID 連携)の構成  

SSO は一般に **ID プロバイダ(IdP)** と **サービスプロバイダ(SP)** の2者間連携によって成立します。  

|役割|説明|
|----|----|
|**IdP(Identity Provider)**|ユーザ認証を実施し、認証情報をトークンとして発行|
|**SP(Service Provider)**|IdP からの認証トークンを検証し、サービスへのアクセスを許可|

SAML/OIDC といったプロトコルにより、この認証情報の受け渡しが標準化されています。  

## 4. SAML 認証とは(エビデンス：OASIS SAML 2.0)  

SAML(Security Assertion Markup Language)は**XML ベースのフェデレーション認証プロトコル**です。  

代表的に利用されるのは **SAML 2.0(OASIS 標準)**です。  

### ■ SAML の特徴  

- XML + デジタル署名(XML-Signature)による高い信頼性  
- Webブラウザによる SSO に適する(SAML Web Browser SSO Profile)  
- メッセージを SP ↔ IdP 間で交換して認証連携  
- エンタープライズ SSO の定番プロトコル(企業/大学/行政で広く採用)  

## 5. SAML の構成要素  

### ● Assertion  

IdP が SP に渡す「ユーザ情報 + 認証結果」の XML 署名付きデータです。  

含まれる情報：  

- 認証方法(Password/MFA 等)  
- 認証時刻  
- ユーザ属性(メールアドレスなど)  
- 有効期限条件(NotBefore/NotOnOrAfter)  

### ● Binding  

SAML メッセージを HTTP 上でどう運ぶかを規定するものです。主に下記があります。  

- HTTP-Redirect  
- HTTP-POST(最も一般的)  

### ● Profile  

具体的なユースケースでの振る舞いを定義しています。  
- **Web Browser SSO Profile**(試験で最重要)

## 6. SAML 認証フロー(Web Browser SSO Profile)

1. **ユーザが SP へアクセス**  
2. SP は認証が必要と判断し、**IdP にリダイレクト**  
3. **IdP がユーザを認証**(例：ID/パスワード + MFA)  
4. IdP は **署名付き SAML Assertion を生成**  
5. SP に Assertion を POST(HTTP-POST バインディング)  
6. SP は署名検証し、ユーザをログイン状態にする    

このフローにより、「パスワードを SP に渡さない」＝**セキュアなフェデレーション認証**が実現されます。  

## 7. SAML のセキュリティ対策(OASIS 標準)

### ■ XML 署名(XML Digital Signature)の検証  

- Assertion の改ざん防止  
- IdP 公開鍵による署名検証が必須  

### ■ リプレイ防止  

- NotBefore/NotOnOrAfter による期限管理  
- 一度使った Assertion ID を再使用不可にする  

### ■ HTTPS の利用  

- 機密性確保(RFC 8446/TLS1.3)  

### ■ SP と IdP の相互メタデータ交換  

- 証明書  
- エンドポイント URL  
- 署名要求のポリシー  

## 8. SAML と他の SSO 技術の比較  

|技術|用途/特徴|基盤技術|
|----|--------------|------------|
|**SAML 2.0**|企業/学術機関向け、SSO の代表|XML + 署名|
|**OpenID Connect(OIDC)**|Web/モバイルサービス向け認証(OAuth2.0 拡張)|JSON + JWT|
|**OAuth 2.0**|認可プロトコル(認証ではない)|Bearer Token|

試験では、**SAML＝認証連携、OAuth＝認可、OIDC＝認証**  の区別を問う問題が頻出です。  

## 9. 周辺知識(試験対策)

### ● IdP/SP の役割  

特に **SP が Assertion の署名を検証して認証を完了させる**という点が重要です。  

### ● フェデレーションメタデータ  

XML 形式で、SP と IdP の設定情報(証明書/エンドポイント)を交換します。  

### ● シングルログアウト(SLO)  

1 回のログアウトで複数システムのセッション破棄を行う仕組みです。  

### ● JWT(JSON Web Token)  

OIDC では SAML の Assertion の代わりに JWT を利用します。  
