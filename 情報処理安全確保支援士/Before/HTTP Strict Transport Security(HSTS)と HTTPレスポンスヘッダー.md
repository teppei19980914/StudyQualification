# HTTP Strict Transport Security(HSTS)と HTTPレスポンスヘッダー

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士令和4年春期 午前Ⅱ 問14](https://www.sc-siken.com/kakomon/04_haru/am2_14.html)  
[情報処理安全確保支援士令和6年春期 午前Ⅱ 問20](https://www.sc-siken.com/kakomon/06_haru/am2_20.html)  

## HTTP Strict Transport Security(HSTS)とは

### 定義(RFC 6797)

**HSTS(HTTP Strict Transport Security)** とは、Webサーバが HTTPレスポンスヘッダーを通じてブラウザに対し、「このサイトには **今後、必ず HTTPS でのみ接続せよ**」と指示するセキュリティ機構です。  

- 標準：**RFC 6797**
- 目的：  
    - 平文HTTP通信の防止  
    - SSL Stripping 攻撃の防止  
    - HTTPS強制による通信の完全性/機密性確保  

## HSTS の仕組み(動作原理)

### 基本フロー

1. ユーザが **HTTPS** でサイトにアクセス
2. サーバが HTTPS 応答時に **Strict-Transport-Security ヘッダー** を返却
3. ブラウザがその内容を **ローカルに記憶**
4. 指定期間中、**HTTPアクセスを自動的に HTTPS に置き換え**

重要点：  
- **HTTP通信そのものを行わずに HTTPS に変換**する  
- サーバに届く前に、**ブラウザ内部で処理される**

## Strict-Transport-Security ヘッダーの構造

### 基本構文(RFC 6797)

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

### 各ディレクティブの意味

| ディレクティブ | 意味 |
|----------------|------|
| max-age | HSTSを有効とする秒数(例：31536000秒＝1年) |
| includeSubDomains | サブドメインにもHSTSを適用 |
| preload | ブラウザのHSTSプリロードリスト登録を許可 |

## HSTS と HTTPSリダイレクトの違い

| 観点 | HTTPSリダイレクト | HSTS |
|------|------------------|------|
| 処理主体 | サーバ | **ブラウザ** |
| 初回HTTP通信 | 発生する | **発生しない(記憶後)** |
| SSL Stripping耐性 | 弱い | **強い** |
| 依存要素 | HTTPレスポンス | HTTPSレスポンス＋記憶 |

→ **HSTSは「リダイレクトの上位互換」ではなく、「攻撃耐性を補強する仕組み」**

## SSL Stripping 攻撃と HSTS

### SSL Stripping 攻撃とは

- 攻撃者が **HTTP→HTTPS のリダイレクトを改ざん**
- ユーザを **平文HTTP通信のまま** 偽装サイトへ誘導
- 認証情報を盗聴/改ざん

### HSTS の防御効果

- ブラウザが **最初からHTTPSしか使わない**
- 攻撃者が HTTP通信を成立させられない
- よって **SSL Stripping が成立しない**

## HSTS の注意点/運用リスク

### 設定ミスの影響

- HTTPSが利用不能になると **サイトに一切アクセスできなくなる**
- 証明書失効/期限切れ時の影響が大きい

### 初回アクセス問題

- 初回が HTTP の場合、HSTS がまだ効かない
- **HSTS Preload** により対策

## HSTS Preload

### 概要

- Chrome/Firefox/Edge 等が持つ **事前登録リスト**
- 初回アクセス前から HTTPS を強制

### 利用条件(代表例)

- max-age ≥ 31536000
- includeSubDomains 指定
- HTTPS完全対応

## HTTPレスポンスヘッダーの位置づけ

### HTTPレスポンスヘッダーとは

サーバがクライアントに返す **制御情報** を含むヘッダー群のことです。  

例：  
- Cache-Control
- Expires
- Set-Cookie
- Content-Type
- Strict-Transport-Security

### セキュリティヘッダーの役割

- **アプリ改修不要でブラウザ挙動を制御**
- Web攻撃(XSS/Clickjacking/MITM)の防止

## Cache-Control ヘッダーとは

### 定義(RFC 9111/RFC 7234)

**Cache-Control** は、HTTP通信において「レスポンスをキャッシュしてよいか、どの程度保持してよいか」を指定するための **キャッシュ制御用HTTPヘッダー** です。  

- 標準：**RFC 9111(旧 RFC 7234)**
- 対象：  
  - ブラウザキャッシュ  
  - プロキシキャッシュ  
  - CDN

### Cache-Control の基本構文

```
Cache-Control: <directive>, <directive>, ...
```

複数のディレクティブをカンマ区切りで指定します。  

例：  
```
Cache-Control: no-store, no-cache, must-revalidate
```

### 代表的な Cache-Control ディレクティブ

#### キャッシュ禁止系

##### no-store

- **一切キャッシュしてはならない**
- ディスク/メモリ保存も禁止

用途：
- 認証情報
- 個人情報
- 金融取引画面

##### no-cache

- キャッシュ保存は可能
- **再利用時に必ずサーバへ再検証**

#### 有効期限系

##### max-age

- キャッシュの有効期間(秒)

意味：  
- 1時間は再問い合わせ不要

##### s-maxage

- **共有キャッシュ(プロキシ/CDN)専用**
- max-age より優先される

#### 再検証系

##### must-revalidate

- 有効期限切れ後は **必ず再検証**
- 独自判断での再利用を禁止

#### キャッシュ範囲指定

##### public

- 誰でもキャッシュ可能
- 認証不要な静的コンテンツ向け

##### private

- **共有キャッシュは禁止**
- ブラウザ個人キャッシュのみ許可

## なぜキャッシュ制御が重要か

キャッシュが原因で以下のリスクが生じます。

- ログアウト後も履歴から閲覧可能
- 他人の端末で個人情報が残留
- プロキシに機密情報が保存される

## 安全な設定例(認証画面)

**「no-store」が最重要**  

```
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
```

## Expires/Pragma との関係

| ヘッダー | 特徴 |
|--------|------|
| Cache-Control | 現行標準、詳細制御可能 |
| Expires | 絶対時刻指定、古い仕様 |
| Pragma | HTTP/1.0互換用 |

### Expires の例

```
Expires: Thu, 01 Jan 1970 00:00:00 GMT
```

## HTTPリクエスト側の Cache-Control

クライアントも Cache-Control を指定可能です。  

意味：
- キャッシュを使わず再取得要求

## 周辺知識

### 関連セキュリティヘッダー

| ヘッダー | 防御対象 |
|---------|----------|
| CSP | XSS |
| X-Frame-Options | Clickjacking |
| X-Content-Type-Options | MIMEスニッフィング |
| Referrer-Policy | 情報漏えい |

### TLSとの関係

- HSTSは **TLSそのものを提供しない**
- あくまで **HTTPS利用を強制する制御策**

### キャッシュと Cookie
- Set-Cookie があるレスポンスは private 扱いされやすい
- 認証情報 × キャッシュは要注意

### CDN と Cache-Control
- s-maxage が CDN 制御で重要
- private 指定で CDN キャッシュ回避
