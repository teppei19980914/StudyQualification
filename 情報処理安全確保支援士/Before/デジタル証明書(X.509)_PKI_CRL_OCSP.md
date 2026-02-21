# デジタル証明書(X.509)/PKI/CRL/OCSP

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報セキュリティスペシャリスト平成25年春期 午前Ⅱ 問3](https://www.sc-siken.com/kakomon/25_haru/am2_3.html)  
[情報セキュリティスペシャリスト平成26年秋期 午前Ⅱ 問4](https://www.sc-siken.com/kakomon/26_aki/am2_4.html)  
[情報処理安全確保支援士令和3年秋期 午前Ⅱ 問8](https://www.sc-siken.com/kakomon/03_aki/am2_8.html)  
[情報処理安全確保支援士令和5年秋期 午前Ⅱ 問3](https://www.sc-siken.com/kakomon/05_aki/am2_3.html)  
[情報処理安全確保支援士令和5年春期 午前Ⅱ 問6](https://www.sc-siken.com/kakomon/05_haru/am2_6.html)  

## なぜ PKI が必要なのか？

ユーザが「https://example.com」にアクセスするとき、次の疑問が必ず発生します。  

- このサーバは本当に“example.com”なのか？  
- 公開鍵は本物なのか？誰かが偽サイトを作っていないか？  

**これを保証する技術が PKI(公開鍵基盤)です。**  
PKI の目的は、**公開鍵を安全に信用できる状態にすること**です。  

## PKI の構成要素

### CA(Certification Authority：認証局)

- 利用者へ**X.509公開鍵証明書**を発行する主体  
- インターネット世界における「信頼の根」  
- EV証明書などは**CA/B Forum**により審査基準が標準化されている  

### RA(Registration Authority：登録局)

- 証明書申請者の本人確認を実施  
- 証明書発行は行わず、CAの前段階処理を担う  

### VA(Validation Authority：証明書有効性検証局)

- クライアントからのリアルタイムの問合せにはOCSP(Online Certificate Status Protocol)やSCVPが用いられ、VAにはレスポンダ(サーバ)の機能が実装されます。  
- 以下の方法で公開鍵証明書の有効性を検証し、クライアントからの証明書の有効性に関する問い合わせに応答  
    * CAの公開鍵で署名を検証  
    * 証明書の有効期限を確認  
    * CRLの集中管理  
    * CRLを確認  

### AA(Attribute Authority：属性認証局)

- CAに代わり属性証明書を発行  

### ● Repository

証明書/CRL を公開するサーバです。  

### ● Subscriber

証明書を利用する主体です。  

### 利用者(Subscriber)
- 証明書を利用して認証/署名/暗号化を行う  

## X.509 デジタル証明書とは(RFC 5280)

証明書は **公開鍵の身分証明書**です。  

### 主な構造

証明書は「CA が署名した公開鍵の名刺」です。  

- Subject(誰の証明書か)  
- Issuer(どの CA が保証したか)  
- Public Key  
- Validity(有効期間)  
- Extensions(用途制限など)  
- CA Signature(CA の電子署名)  

## 重要拡張領域

### Key Usage

暗号化、署名など利用用途を制限します。  

### EKU(Extended Key Usage)

serverAuth/clientAuth など詳細用途を表します。  

### SAN(Subject Alternative Name)

複数 FQDN を 1 枚にまとめます。  
※ブラウザは CNではなく **SAN をチェック**します。  

### CRL Distribution Points/AIA

失効確認用 URL(CRL/OCSP)を格納します。  

## PKI の信頼チェーン

```
Root CA
  ↓
Intermediate CA
  ↓
End Entity(Web サーバ等)
```

ブラウザは下記を行い、安全性を判断します。  

1. 署名検証  
2. チェーンの正しさ  
3. 有効期間  
4. SAN の一致  
5. 失効状態の確認  

## 証明書失効(Revocation)

証明書が有効期間中でも無効化される場合を表します。  

代表例：
- 秘密鍵漏洩
- 組織変更
- サーバ廃止
- 誤発行

## CRL(Certificate Revocation List：失効証明書リスト)

有効期限内であるにもかかわらず、秘密鍵の漏えい、紛失、証明書の被発行者の規則違反などの理由により安全性が担保されなくなったために、失効となったデジタル証明書の一覧表です。  


## CRLの構造(ASN.1)

```
CertificateList ::= SEQUENCE {
  tbsCertList          TBSCertList,
  signatureAlgorithm   AlgorithmIdentifier,
  signatureValue       BIT STRING
}

TBSCertList ::= SEQUENCE {
  version                Version OPTIONAL,
  signature              AlgorithmIdentifier,
  issuer                 Name,
  thisUpdate             Time,
  nextUpdate             Time OPTIONAL,
  revokedCertificates    SEQUENCE OF RevokedCertificate OPTIONAL,
  crlExtensions          Extensions OPTIONAL
}
```

### RevokedCertificate の要素

- **serialNumber**  
- **revocationDate**  
- **extensions(失効理由、invalidityDate など)**  

## 重要項目

### thisUpdate

CRLが発行された日時です。  

### nextUpdate

次回CRLが更新されるべき日時です。  
この時刻を過ぎているCRLは信頼できません。  

### CRLの運用上の課題

#### CRLファイルの巨大化

発行数が増えるほどCRLが大きくなり、クライアントのダウンロード負担が増えます。  

#### リアルタイム性が低い

CRLは「定期更新」であり、即時の失効反映はできません。  

#### 大規模PKIでは非効率

証明書数が数百万枚を超えるとCRLだけでは運用困難になります。  

#### 問題点

- ファイルが巨大化  
- 更新のタイムラグ(リアルタイム性の欠如)  

### Delta CRL(差分CRL)

RFC 5280準拠の仕組みで、**CRLの差分のみ配布して効率を改善する方式**。

#### 利点

- ネットワーク負荷を削減
- 大規模環境で有効

#### 注意点(午後問題向け)

- Delta CRL単体では不可  
- **Base CRL と併せて検証する必要がある**

## OCSP(Online Certificate Status Protocol)

証明書の失効状態をリアルタイムに問い合わせます。  

### 応答

- good(有効)  
- revoked(失効)  
- unknown(不明)  

### 利点

- CRL より最新性が高い  
- 必要な証明書だけ確認するため効率的  

### CRL検証手順

1. **CRL署名検証**  
2. thisUpdate/nextUpdate の妥当性確認  
3. 対象証明書の serialNumber が revokedCertificates に含まれているか確認  
4. 必要に応じて reasonCode の内容を参照  
5. Base CRL + Delta CRL を併用する場合は整合性確認  

## OCSP Stapling(RFC 6066)

Web サーバが事前に OCSP 応答を取得し、TLS ハンドシェイク時にクライアントへ提供する方式です。  

### メリット

- 高速化  
- プライバシー保護  
- OCSP サーバ負荷軽減  

## 証明書の種類

| 種類 | 用途 |
|------|------|
| サーバ証明書 | HTTPS、TLS通信 |
| クライアント証明書 | 利用者認証 |
| コード署名証明書 | ソフトウェア署名 |
| S/MIME 証明書 | メール署名/暗号化 |

## CA/B Forum Baseline Requirements

商用 CA が従う国際標準です。  

- サーバ証明書の有効期間は **398日以内**  
- ドメイン所有確認の標準化  
- 失効対応の統一  

## 周辺知識

### HSM(Hardware Security Module)

CA の秘密鍵を厳重に保護する装置です。  

### KDF(PBKDF2/HKDF/Argon2)

パスワードから安全な鍵を導出します。  

### PFS(Perfect Forward Secrecy)

ECDHE などにより、秘密鍵漏洩でも過去通信を守ります。  

### ACME(Let's Encrypt)

証明書自動発行プロトコルです。  
