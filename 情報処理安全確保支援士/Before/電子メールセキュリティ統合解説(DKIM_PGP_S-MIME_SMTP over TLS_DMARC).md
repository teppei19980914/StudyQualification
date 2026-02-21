# 電子メールセキュリティ統合解説(DKIM/PGP/S-MIME/SMTP over TLS)

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報セキュリティスペシャリスト平成27年春期 午前Ⅱ 問2](https://www.sc-siken.com/kakomon/27_haru/am2_2.html)  
[情報処理安全確保支援士令和元年秋期 午前Ⅱ 問12](https://www.sc-siken.com/kakomon/01_aki/am2_12.html)  
[情報処理安全確保支援士令和6年秋期 午前Ⅱ 問10](https://www.sc-siken.com/kakomon/06_aki/am2_10.html)  

## 1. 電子メールの脅威と背景(RFC 5322 など)

電子メールはもともと「平文通信」が前提で設計されたため、以下の脅威が存在します。

#### ● 電子メールの主要脅威

- 通信経路での盗聴(Sniffing)
- 改ざん(Header/Body tampering)
- From 偽装(Sender Spoofing)
- 中間者攻撃(MITM)
- マルウェア添付、フィッシング
- スパムメールによる詐欺/感染拡大

これらを防ぐため、メールセキュリティは **多層構造** で強化される必要があります。

## 2. DKIM(DomainKeys Identified Mail)  

DKIM は、**電子メールに暗号学的署名を付与し、送信ドメインの正当性と改ざん検知を提供する技術**です。

### 2.1 DKIM が提供するセキュリティ
- **送信ドメイン認証(Sender Authentication)**
- **メッセージ改ざん検知(Integrity)**

### 2.2 DKIM の処理概要

1. 送信者がメール本文/ヘッダを正規化(Canonicalization)
2. ハッシュ化した値を秘密鍵で署名
3. 署名を「DKIM-Signature」ヘッダとして付与
4. 受信側は DNS から公開鍵を取得し、署名検証を実施

### 2.3 DKIM-Signature フィールド例

```
DKIM-Signature: v=1; a=rsa-sha256; d=example.jp; s=selector1;
 h=From:To:Subject:Date;
 bh=Q2sY9uE...(body-hash);
 b=F7g3sA...(signature)
```

#### 主なタグ一覧

| タグ | 意味 |
|------|-------|
| v | バージョン |
| a | 署名アルゴリズム |
| d | 署名ドメイン |
| s | セレクタ(鍵識別子) |
| h | 署名対象ヘッダ |
| bh | 本文ハッシュ |
| b | 署名値 |

### 2.4 DNS に公開される DKIM 鍵(TXT レコード)

```
selector1._domainkey.example.jp IN TXT (
 "v=DKIM1; k=rsa; p=MIIBIjANBgkqh..."
)
```

### 2.5 DKIM の弱点(RFC 6376/RFC 7489)

- **From 表示名との一致保証は弱い → DMARC が補完**
- **メーリングリストによる書き換えで署名が壊れやすい → ARC が補完**

## 3. PGP(Pretty Good Privacy)／OpenPGP(RFC 4880)

PGP はユーザが公開鍵を交換し合い、**メール本文にエンドツーエンド暗号化と電子署名を付与する方式**です。

### 3.1 PGP の主要特徴

| 機能 | 説明 |
|------|------|
| 暗号化 | 受信者の公開鍵を使用 |
| 電子署名 | 送信者の秘密鍵を使用 |
| 鍵管理方式 | Web of Trust(分散型) |

#### Web of Trust とは

- 中央 CA を持たず、ユーザ同士が鍵に署名して信頼を構築
- 利点：分散型で柔軟  
- 欠点：企業での運用負荷が高い

## 4. S/MIME(Secure/Multipurpose Internet Mail Extensions)  

S/MIME は **企業向け PKI メールセキュリティ** 技術です。

### 4.1 S/MIME の特徴

| 機能 | 説明 |
|--------|---------|
| 暗号化 | CMS(Cryptographic Message Syntax)利用 |
| 電子署名 | X.509 証明書で署名 |
| 鍵管理 | PKI(CA による証明書管理) |
| 互換性 | 多くのクライアントが標準対応 |

### 4.2 PGP との比較

| 観点 | PGP/OpenPGP | S/MIME |
|------|----------------|---------|
| 鍵管理 | Web of Trust | PKI(CAが発行) |
| ユーザ対象 | 個人利用 | 組織利用 |
| 運用性 | ユーザ管理 | 組織的な証明書管理 |
| 国際標準 | RFC 4880 | RFC 5751 |

## 5. SMTP over TLS(RFC 3207)

SMTP を TLS で暗号化し、通信経路上での盗聴/改ざんを防ぐ仕組みです。  

### 5.1 STARTTLS の流れ

1. SMTP で平文接続  
2. クライアントが `STARTTLS` を送信  
3. TLS ハンドシェイク開始  
4. 暗号化チャネル確立後、SMTP を継続  

### 5.2 SMTP over TLS が提供するセキュリティ

| 項目 | 説明 |
|-------|------|
| 暗号化 | 経路の盗聴防止 |
| 改ざん検知 | TLS の MAC により検知 |
| サーバ認証 | TLS 証明書で正当性を保証 |

※注意：メール本文は転送の途中で復号されるため、**エンドツーエンド暗号化ではありません**。  

## 6. メール認証技術(SPF/DKIM/DMARC/ARC)

### 6.1 SPF(Sender Policy Framework)RFC 7208

DNS に「正当な送信元 IP アドレス」を登録し、**サーバなりすましを検出**する技術です。  

### DMARC 深掘り解説(RFC 7489 準拠)

DMARC(Domain-based Message Authentication, Reporting, and Conformance)は、SPF および DKIM の検証結果と **From ドメインの整合性(Alignment)** を基準とした受信側ポリシーを定義するメール認証技術です。  

#### DMARC の目的

1. **なりすまし(From 偽装)を検知/防止**
2. **メール改ざんの発見**
3. **SPF/DKIM の運用強化**
4. **レポートによる可視化(RUA/RUF)**

#### DMARC の適用条件

DMARC は From ヘッダのドメイン(Header-From)を基準として SPF/DKIM の結果を参照します。  

- **SPF Alignment** → Envelope-From と Header-From が同一組織(Organizational Domain)
- **DKIM Alignment** → DKIM 署名の d= ドメイン と Header-From が同一組織

#### DMARC ポリシー(p=)の詳細

DMARC のポリシーには以下の 3 種類です(RFC 7489 Section 6.3)。

| ポリシー | 意味 | 効果 |
|---------|------|-------|
| `p=none` | 監視モード(何もしない) | 認証結果はログ化されるが配送は通常どおり |
| `p=quarantine` | 隔離 | 迷惑メールフォルダへ移動などの弱い拒否 |
| `p=reject` | 拒否 | 認証失敗メールを SMTP レベルで拒否 |

##### none(監視モード)

- SPF/DKIM の整合性を可視化する「導入初期」に利用
- RUA レポートで送信元の状況を把握し、誤検知がないかを確認する

##### quarantine(隔離)

- 一部の失敗メールを迷惑メールへ
- 正当なメールが誤検知される場合に備えて「段階的導入」で利用する

##### reject(拒否)

- 最も強力な保護
- 認証失敗メールを配送前に拒否するため、なりすまし防止に極めて有効
- 正当な送信がすべて SPF/DKIM と整合する状態になってから適用

#### Alignment(整合性)とは？

DMARC は SPF/DKIM が成功しても「From ドメインと一致していなければ成功扱いになりません」。  

例：  

- SPF の検証は mail.example.net が成功  
- Header-From は example.jp  
→ **Alignment 不一致 → DMARC 失敗**  

これは「From 偽装」の本質的対策です。  

#### DMARC レポート(RUA/RUF)

DMARC はレポート送信先を DNS で指定できます。  

```
rua=mailto:dmarc-report@example.jp
ruf=mailto:dmarc-forensic@example.jp
```

- **RUA(Aggregate Report)** → 集計レポート  
- **RUF(Forensic Report)** → 失敗時のエビデンス(原文含む場合あり)

運用者はレポート分析によって、以下を把握できます。  

- 自社ドメインを悪用する送信元
- SPF/DKIM の誤設定
- メーリングリストや転送経路での破損

#### メール転送と DMARC の課題

メール転送(Forward)では以下の問題が発生します。  

1. **SPF が失敗する(送信元 IP が変わるため)**
2. **DKIM が破損する(書き換えによる)**

これに対応する技術：  

- **ARC(Authenticated Received Chain)RFC 8617**
- 転送元が「署名連鎖(Chain)」を付与し、受信者が整合性を判断できる

#### DMARC と SPF/DKIM の役割関係

| 技術 | 目的 | 限界 |
|------|------|------|
| SPF | メールを送ったサーバ IP が正当か | 転送で失敗しやすい |
| DKIM | 電子署名で改ざん防止 | メール加工で署名破損 |
| DMARC | From と SPF/DKIM の整合性を検証し受信側ポリシーを決定 | SPF/DKIM が前提 |

DMARC は **SPF/DKIM を統合し、メール正当性を判断する最終ゲート**です。  

### 6.4 ARC(Authenticated Received Chain)RFC 8617

メーリングリスト転送などで DKIM が壊れても、**署名チェーンを保証する仕組み**です。  

## 7. メールの暗号化技術の比較(体系まとめ)

| 技術 | 暗号化範囲 | 認証方式 | 主用途 |
|------|-------------|-----------|-----------|
| PGP | エンドツーエンド | Web of Trust | 個人利用 |
| S/MIME | エンドツーエンド | PKI | 企業利用 |
| SMTP over TLS | 経路(Hop-by-hop) | TLS 証明書 | 通信経路暗号化 |

## 8. 周辺知識

### 8.1 MIME(Multipurpose Internet Mail Extensions)

- 画像、PDF、添付の送信を可能にする仕組み
- S/MIME も MIME形式で表現される

### 8.2 Base64

バイナリデータを ASCII 化する方式です。  
メールで暗号化データや添付が扱えるようになります。  

### 8.3 POP3S/IMAPS(TLS 受信)

| プロトコル | ポート | 概要 |
|------------|--------|--------|
| POP3S | 995 | TLS による暗号化受信 |
| IMAPS | 993 | TLS による暗号化受信 |

### 8.4 PKI と証明書失効

S/MIME や TLS では、証明書失効確認として、下記が利用されます。  

- **CRL(Certificate Revocation List)**
- **OCSP(Online Certificate Status Protocol)**
