# XMLデジタル署名

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士令和5年秋期 午前Ⅱ 問4](https://www.sc-siken.com/kakomon/05_aki/am2_4.html)  
[情報セキュリティスペシャリスト平成26年春期 午前Ⅱ 問2](https://www.sc-siken.com/kakomon/26_haru/am2_2.html)  

## XMLデジタル署名とは（W3C 勧告に基づく解説）

XMLデジタル署名（XML Signature）は、**XML文書に電子署名を適用するための国際標準仕様**であり、  
W3C と IETF が共同策定した **W3C勧告「XML Signature Syntax and Processing」** に基づいています。

電子署名として必要な以下の性質を XML 文書上で実現します。

- **完全性（改ざん検知）**  
- **認証（署名者の識別）**  
- **否認防止**

特に XML は構造に自由度があり、空白や属性順序の違いで別文書と解釈されるため、  
**署名前処理（Transform）や正規化（Canonicalization）が不可欠**です。

## XML署名の基本構造（W3C 正式仕様）

```xml
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">

    <SignedInfo>
        <!-- 署名対象のURI、Transform、正規化、ハッシュ方式など -->
    </SignedInfo>

    <SignatureValue>
        <!-- SignedInfo を署名者の秘密鍵で署名した値 -->
    </SignatureValue>

    <KeyInfo>
        <!-- 公開鍵・X.509証明書など（任意） -->
    </KeyInfo>

</Signature>
```

#### ● SignedInfo  
署名対象データ、Transform、ハッシュアルゴリズムを定義するブロック。  
XML署名では **文書そのものではなく、この SignedInfo 部分に対して署名を施す**ことが特徴です。  
「署名対象のURI」は「\<Reference URI="署名対象のURI"\>」のように「Reference属性」に記述します。  

#### ● SignatureValue  
SignedInfo を秘密鍵で署名した値。  
検証時には公開鍵で SignatureValue を確認します。

#### ● KeyInfo（任意）  
公開鍵情報や証明書を含められます。  
セキュリティ方針により外部鍵管理とする場合は省略されます。

## 署名形式（Detached / Enveloped / Enveloping）

XML署名では、**署名が文書中のどこに配置されるか**によって形式が分かれます。

### 1. Detached Signature（デタッチ署名）

- 署名と署名対象が物理的に分離されている  
- `<Reference URI="http://example.com/data.xml">` のように外部リソースを指定  
- 既存文書を改変できない場合に適する  
- バイナリデータにも利用可能  

### 2. Enveloped Signature（エンベロープ署名）

署名対象 XML 文書の内部に `<Signature>` が埋め込まれる形式。

```xml
<Document>
    <Data> ... </Data>
    <Signature> ... </Signature>
</Document>
```

- 文書全体をまとめて扱いやすい  
- 署名自身を署名対象に含めないため、Transform に **Enveloped Signature Transform** が必要  

### 3. Enveloping Signature（エンベローピング署名）

署名文書がデータを内包する形式。

```xml
<Signature>
    <Object>・・・署名対象データ・・・</Object>
</Signature>
```

- 署名とデータを “1つの XML として配布したい” 場合に便利  
- XML署名が“容器”となり、複数の `<Object>` を含めることも可能  

## 正規化（Canonicalization：C14N）

XML は以下の違いだけで別文書として扱われます。

- 空白・改行  
- 属性の順序  
- XML 宣言の有無  
- 名前空間の扱い  

署名時の入力文書と検証時の文書が少しでも異なると検証に失敗するため、  
**正規化（C14N：Canonical XML）によって XML を唯一の形に統一** します。

例：  
- `xmlns` の統一  
- 属性順序の並べ替え  
- 無駄な空白の除去

W3C は **Canonical XML 1.0 / 1.1**, **Exclusive Canonical XML** を勧告しています。

## Transform（署名前処理）

XML署名では署名対象データに対する前処理を **Transform 要素**で定義します。

代表例：

- **Canonicalization（正規化）**
- **XPath Transform（署名範囲の絞り込み）**
- **Enveloped Signature Transform**  
  → エンベロープ署名で `<Signature>` を署名対象から除く目的

Transform は **XMLの柔軟性による“改ざんではない差異”を吸収する**ためのしくみです。

## XML（Extensible Markup Language）

XML は W3C が策定した **構造化データを表現するためのマークアップ言語**です。

- HTML が「見た目」を記述するのに対し、XML は「データ構造」を表現する  
- 階層構造で意味を表すため、電子署名の対象として扱いやすい  
- SOAP、SAML、電子政府システムなど多くの分野で利用  

## W3C（World Wide Web Consortium）

W3C はティム・バーナーズ＝リーらが主導する **Web 技術の標準化団体**です。

- HTML / CSS / XML / SVG  
- WebCrypto API  
- XML Signature / XML Encryption  

など、Web の基盤となる技術仕様を策定しています。

## XML署名の周辺知識（支援士でよく出る領域）

### ● XML Encryption（XML暗号）
XML署名が「完全性」を担保するのに対し、  
**XML Encryption は「機密性」を XML レベルで実現する**ための標準仕様。  
署名と併用することが多い。

### ● XAdES（XML Advanced Electronic Signatures）
EU の電子署名法に基づく **高度電子署名規格**で、XML署名を拡張したもの。  
タイムスタンプや長期検証情報の付加が可能。

### ● SAML（Security Assertion Markup Language）
シングルサインオン（SSO）で利用される認証情報を XML でやりとりする枠組み。  
SAML のアサーションには XML署名が利用される。

### ● SOAP・WS-Security
Webサービスの世界では、SOAP メッセージに対して XML署名や暗号化を適用できる。
