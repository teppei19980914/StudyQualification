# ソフトウェアパターンと GoF デザインパターン

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士令和6年秋期 午前Ⅱ 問22](https://www.sc-siken.com/kakomon/06_aki/am2_22.html)  

## ソフトウェアパターンとは

### 定義(エビデンス)

- Christopher Alexander  
- Gamma et al., *Design Patterns: Elements of Reusable Object-Oriented Software*  
- POSA(Pattern-Oriented Software Architecture)

**ソフトウェアパターンとは、繰り返し発生する設計上の問題に対して、実績のある解決策を再利用可能な形でまとめた知識体系です。**

重要なのは「**コード断片**」ではなく、下記をセットで表現する点です。  

- 問題(Context)
- 解決すべき課題(Problem)
- 解決方法(Solution)
- 効果/トレードオフ(Consequences)

## ソフトウェアパターンの階層分類(試験重要)

ソフトウェアパターンは、適用レベルにより次のように分類されます。

### アーキテクチャパターン

#### 特徴

- システム全体構造を規定
- 高レベル設計

#### 代表例

- MVC(Model–View–Controller)
- レイヤードアーキテクチャ
- クライアント／サーバ
- マイクロサービス

→ **「システムの骨格」を決めます**

### デザインパターン(GoF)

#### 特徴

- クラス/オブジェクト間の設計指針
- オブジェクト指向設計の再利用知識

### イディオム(実装パターン)

#### 特徴

- 特定言語に依存
- コーディングレベル

#### 例

- Java の try-with-resources
- C++ の RAII

## GoF(Gang of Four)とは

### GoF の位置付け(エビデンス)

- Erich Gamma  
- Richard Helm  
- Ralph Johnson  
- John Vlissides  

1994年に以下の名著を出版し、この書籍で **23個のデザインパターン** が体系化されました。  
***Design Patterns: Elements of Reusable Object-Oriented Software***  

## GoF デザインパターンの全体構成

GoF のデザインパターンは、目的別に **3分類** されます。  

```
GoF デザインパターン(全23)
├─ 生成(Creational) : 5
├─ 構造(Structural) : 7
└─ 振る舞い(Behavioral) : 11
```

## 生成パターン(Creational Patterns)

### 目的

- **オブジェクト生成方法を抽象化**
- new の乱用を防止

### 代表例

| パターン | 概要 |
|---|---|
| Singleton | インスタンスを1つに制限 |
| Factory Method | 生成処理をサブクラスに委譲 |
| Abstract Factory | 関連オブジェクト群を生成 |
| Builder | 構築手順と表現を分離 |
| Prototype | 複製による生成 |

## 構造パターン(Structural Patterns)

### 目的

- **クラスやオブジェクトの構造を柔軟に構成**
- 変更に強い設計

### 代表例

| パターン | 概要 |
|---|---|
| Adapter | インタフェース変換 |
| Decorator | 機能を動的に追加 |
| Composite | 木構造を一様に扱う |
| Facade | 窓口を単純化 |
| Proxy | 代理制御 |

## 振る舞いパターン(Behavioral Patterns)

### 目的

- **オブジェクト間の責務分担と通信制御**

### 代表例

| パターン | 概要 |
|---|---|
| Observer | 状態変化の通知 |
| Strategy | アルゴリズム切替 |
| Command | 処理をオブジェクト化 |
| Template Method | 処理骨格を定義 |
| State | 状態に応じて振る舞い変更 |

## ソフトウェアパターンとフレームワークの違い

| 項目 | パターン | フレームワーク |
|---|---|---|
| 形態 | 抽象的知識 | 具体的コード |
| 再利用 | 思想/設計 | 実装 |
| 例 | MVC, GoF | Spring, Struts |

## 周辺知識①：アーキテクチャパターンとの関係

- MVC は **アーキテクチャパターン**
- MVC 内部実装で GoF が使われる

例：  
- Observer(View更新)
- Strategy(入力処理切替)

## 12. 周辺知識②：アンチパターン

### 定義

- 一見よさそうだが、実際には問題を悪化させる設計

### 例

- God Object
- Spaghetti Code
- Golden Hammer
