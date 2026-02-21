# サイバー攻撃手法を分類したナレッジベースと MITRE ATT&CK

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[令和6年秋期試験問題　午前Ⅱ 問3 ](https://www.sc-siken.com/kakomon/06_haru/am2_22.html)  

## サイバー攻撃手法を分類したナレッジベースとは

### 定義

**サイバー攻撃手法を分類したナレッジベース**とは、過去に観測/分析された攻撃者の行動や手法を共通の観点/構造で整理し、共有可能にした知識体系のことです。  

### なぜナレッジベースが必要か

従来のセキュリティ対策には次の課題がありました。  

- マルウェア名や脆弱性IDごとの **点の対策**
- 攻撃の「手段」だけを見て「目的/流れ」が見えない
- 組織間での知見共有が困難

→ **攻撃者の行動(TTPs)を軸に整理する必要性** が高まりました。  

## MITRE ATT&CK とは

### 定義(エビデンス)

**MITRE ATT&CK** とは、実際のサイバー攻撃事例に基づき、攻撃者の戦術(Tactics)/技術(Techniques)/手順(Procedures)を体系的に整理したナレッジベースです。  

#### 公式根拠

- MITRE Corporation  
- https://attack.mitre.org/

### MITRE ATT&CK の位置づけ

| 観点 | 内容 |
|---|---|
| 主体 | MITRE(非営利研究機関) |
| 対象 | 実在する攻撃者行動 |
| 目的 | 検知/分析/対策の共通言語化 |
| 利用者 | SOC/CSIRT/ベンダ |

→ **脆弱性(CVE)ではなく「攻撃行動」を分類する点が本質**です。  

## ATT&CK の基本構造(試験最重要)

### TTPs に基づく整理

ATT&CK は以下の概念に基づきます。  

| 要素 | 内容 |
|---|---|
| Tactics | 攻撃の目的(なぜ) |
| Techniques | 攻撃手法(どうやって) |
| Procedures | 実際の実装/ツール |

### 戦術(Tactics)

戦術は **攻撃ライフサイクル上の目的** を表します。  
代表例(Enterprise ATT&CK)：  

- Initial Access(初期侵入)
- Execution(実行)
- Persistence(永続化)
- Privilege Escalation(権限昇格)
- Defense Evasion(防御回避)
- Credential Access(認証情報窃取)
- Lateral Movement(横展開)
- Command and Control(C2)
- Exfiltration(情報窃取)
- Impact(影響)

→ **試験では「Initial Access」などの名称を理解しているかが問われます。**

### 技術(Techniques)

各戦術の下に **具体的な攻撃手法** が定義されています。  

例：  

- Phishing(T1566)
- Valid Accounts(T1078)
- PowerShell(T1059.001)
- Pass the Hash(T1550.002)

## ATT&CK の3つのマトリクス

MITRE ATT&CK には複数の適用領域があります。  

| マトリクス | 対象 |
|---|---|
| Enterprise | 企業IT(Windows/Linux/Cloud) |
| Mobile | モバイル端末 |
| ICS | 制御システム |

## サイバー攻撃ナレッジベースとしての価値

### 従来型対策との違い

| 従来 | ATT&CK |
|---|---|
| シグネチャ依存 | 行動分析 |
| マルウェア名中心 | 攻撃工程中心 |
| 受動的 | 能動的分析 |

### 利用例(実務)

- SIEM の検知ルールを ATT&CK 技術にマッピング
- EDR アラートの攻撃フェーズ可視化
- レッドチーム演習の設計
- CSIRT 報告書の共通語彙

## 周辺知識(試験で差がつく)

### CVE/CWE/ATT&CK の違い

| 分類 | 何を扱うか |
|---|---|
| CVE | 脆弱性の識別子 |
| CWE | 脆弱性の設計上の弱点 |
| ATT&CK | 攻撃者の行動 |

### Kill Chain との関係

- Cyber Kill Chain：攻撃の段階モデル
- ATT&CK：段階ごとの具体的行動

→ **ATT&CK は Kill Chain を詳細化したものと理解可能**

### DEFEND/D3FEND

- MITRE D3FEND：防御側の対抗手段を整理
- ATT&CK と対になる概念
