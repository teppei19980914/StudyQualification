# JVN/脆弱性対策ポータル/CWE

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士令和5年秋期 午前Ⅱ 問12](https://www.sc-siken.com/kakomon/05_aki/am2_12.html)  
[情報処理安全確保支援士令和6年春期 午前Ⅱ 問9](https://www.sc-siken.com/kakomon/06_haru/am2_9.html)  

## JVN(Japan Vulnerability Notes)

**JVN(Japan Vulnerability Notes)** は、日本国内で利用されるソフトウェア等の脆弱性情報を提供するポータルサイトです。

#### 運営主体(公式エビデンス：IPA/JPCERT/CC)

JVN は以下の 2 社が共同運営しています。  

- IPA(独立行政法人 情報処理推進機構)
- JPCERT/CC(一般社団法人 JPCERT コーディネーションセンター)

#### JVN の役割

- 脆弱性情報の公開(国内ソフトウェア中心)
- 対応状況(パッチ／緩和策／回避策)の掲載
- 開発者と調整(調整済み情報を公開)
- CVE ID との対応づけ
- CWE、CVSS による評価の提示

#### 特徴

- **日本語で利用可能**  
- 国内ソフトウェア/IoT 機器など**日本で普及している製品に関する情報が充実**
- 漏えい事故を防ぐため、開発者との調整期間後に公開される

## 脆弱性対策ポータルサイト(JVN iPedia)

**JVN iPedia(脆弱性対策データベース)** は、JVN と密接に連携しつつ、国内外の脆弱性情報を幅広く集約するデータベースです。  

#### 運営主体

- IPA(独立行政法人 情報処理推進機構)

#### 情報源

JVN iPedia は以下から脆弱性情報を収集し、データベース化します。

- JVN
- NVD(National Vulnerability Database：米国)
- ベンダーのセキュリティ情報
- 海外 CERT の公表情報

#### 特徴

- **日本語で脆弱性情報を検索可能**
- 製品カテゴリ別の統計情報を提供  
- マルチベンダ製品の CVE 対応状況を確認できる  

#### CVSS 評価も提供

CVSS v3 に基づく脆弱性深刻度を提供することで、ユーザ/企業のリスク評価に役立てます。

## CWE(Common Weakness Enumeration)

**CWE(Common Weakness Enumeration)** は、MITRE 社が管理する **「ソフトウェアの脆弱性につながる根本原因(弱点)」を分類/体系化した標準リスト** です。

#### CWE が扱うもの

CWE は **脆弱性(CVE)そのものではありません**。  
扱うのは下記のような脆弱性です。  

- CWE-79: クロスサイトスクリプティング(XSS)
- CWE-89: SQL インジェクション
- CWE-22: ディレクトリトラバーサル
- CWE-352: CSRF
- CWE-787: Out-of-bounds Write

#### 目的

- 脆弱性の原因を体系的に理解
- セキュア開発/レビューの品質向上
- 開発者/研究者向けの共通語彙(共通フレームワーク)として利用

#### CWE と CVE の違い

| 項目 | CWE | CVE |
|------|------|------|
| 対象 | 脆弱性を生む「弱点」 | 実際に発見された脆弱性 |
| 例 | 「入力検証不足」 | 「Log4j の RCE 脆弱性」 |
| 管理 | MITRE | MITRE |
| 役割 | 原因の分類 | 個々の脆弱性識別子 |

## JVN/JVN iPedia/CVE/CWE の関係図

```
[脆弱性の原因] ——→ CWE(弱点分類)
       |
       ↓(実際の脆弱性として発見)
     CVE(固有ID)
       |
       ↓
 NVD/JVN/JVN iPedia で公開
```

## 周辺知識

### CVE(Common Vulnerabilities and Exposures)

- MITRE が管理する**脆弱性の識別子**
- 例：CVE-2021-44228(Log4Shell)

### CVSS(Common Vulnerability Scoring System)

- 脆弱性の深刻度を 0.0～10.0 でスコア化
- JVN および JVN iPedia で常に表示される

### SCAP(Security Content Automation Protocol)

ITシステムの脆弱性、設定状態、ソフトウェアの識別情報などを標準化された形式で表現・交換・評価するための仕様群です。  

#### SCAPが必要とされた背景

従来のセキュリティ運用には以下の課題がありました。  
これを解決するために、NISTが中心となって策定した共通言語群が SCAP です。  

* ベンダごとに脆弱性IDや表記が異なる  
* 手作業による脆弱性管理で属人化  
* 構成チェック結果がツール間で共有できない  

#### SCAPの目的

SCAPの目的は次の3点に集約できます。

1. 脆弱性・設定情報の標準化  
2. 自動評価・自動監査の実現  
3. ツール間の相互運用性確保  

#### SCAPの全体構造

SCAPは単一規格ではなく、複数の標準仕様の集合体であり、これを「SCAPの構成要素」と呼びます。  

##### CVE(Common Vulnerabilities and Exposures)

脆弱性を一意に識別するための共通ID体系です。  
JVN/NVD/IPAでも利用されています。  

##### CCE(Common Configuration Enumeration)

セキュリティ設定項目を一意に識別するID体系です。  
OS/ミドルウェアの設定監査で利用されます。  

##### CPE(Common Platform Enumeration)

ソフトウェアやOS、ハードウェアを識別するための命名規則です。  
「どの製品に該当するか」を機械判定するために必須です。  

##### CVSS(Common Vulnerability Scoring System)

脆弱性の深刻度を数値化する指標です。  
優先度付の根拠となり、SCAPでは「評価結果の共通尺度」として使用されます。  

##### OVAL(Open Vulnerability and Assessment Language)

システム状態を監査するための記述言語です。  
XCCDFが「何を」、OVALが「どう調べるか」という役割です。  

##### OCIL(Open Checklist Interactive Language)

自動化できない項目を人に質問するための言語です。  
人手確認を標準化しています。  

##### ARF(Asset Reporting Format)

評価結果を記録/交換するための形式です。  

##### Asset Identification(資産識別)

評価対象システムを識別する仕組みです。  

##### Vulnerability Data Feeds(脆弱性情報配信)

NVDなどから提供される脆弱性データです。  

##### Checklist Data Feeds(チェックリスト配信)

セキュリティ設定ベンチマークの配信です。  

##### SCAP Data Stream

上記要素を一つにまとめて配布する仕組みです。  

### CERT/CC

- 米国のコンピュータセキュリティインシデント対応機関
- 脆弱性調整プロセスの先駆者
