# AAAフレームワーク/RADIUS/DIAMETER  

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報セキュリティスペシャリスト平成28年秋期 午前Ⅱ 問1](https://www.sc-siken.com/kakomon/28_aki/am2_1.html)  

## 1. AAAフレームワーク  

AAAはネットワークアクセス管理の基本概念であり、以下の3要素からなります。  

1. Authentication(認証)  
2. Authorization(認可)  
3. Accounting(アカウンティング：利用記録)  

### ■ Authentication

利用者が **誰であるか** を確認するプロセスです。  

例：  
- パスワード  
- ワンタイムパスワード  
- デジタル証明書(X.509)  
- 多要素認証(MFA)  

### ■ Authorization

認証済みのユーザが **何をしてよいか** を制御する仕組みです。  

例：  
- VPN接続可否  
- ネットワークサービス利用権限  
- VLAN割当など  

### ■ Accounting

利用者の行動/接続情報を記録します。  

例：  
- 接続/切断時刻  
- 利用したサービス  
- 転送量ログ  

ログ管理に関する国際基準は ISO/IEC 27002 に基づきます。  

## 2. RADIUS(Remote Authentication Dial-In User Service)  

RADIUSはもっとも普及しているネットワーク認証プロトコルです。  
Wi-Fi、VPN、スイッチ、FW など幅広い機器が対応しています。  

### ■ 特徴

- **UDPベース**(ポート：1812/1813)  
- パスワード部分のみ暗号化(共有鍵方式)  
- クライアント → サーバの質問応答型  
- AAA機能の集中管理が可能  

### ■ 主な用途

- 802.1X 認証(企業LAN、Wi-Fi)  
- ISPにおけるユーザ認証  
- VPN接続管理  

### ■ 課題

- 全文暗号化ではない  
- UDPのため信頼性が低い  
- 拡張性に限界  

そのため、後継として DIAMETER が策定されています。

## 3. DIAMETER(RADIUS の後継プロトコル)  

**RADIUS(半径) → DIAMETER(直径)** → より強化されたAAAプロトコルであることから由来しています。  

### ■ 特徴

- **TCP または SCTP** を使用 → 高信頼  
- 全メッセージを暗号化可能(TLS/IPsec)  
- 高い拡張性(AVP：Attribute Value Pair)  
- 大規模ネットワーク向けに設計  

### ■ 主な用途

- LTE/5G モバイルネットワークの認証基盤  
- IMS(IP Multimedia Subsystem)  
- 通信事業者ネットワークの加入者管理  

企業LANで広く使われる RADIUS に対し、DIAMETER は通信キャリアの本格的な認証基盤として利用されています。

## 4. RADIUS と DIAMETER の比較(試験頻出)

| 観点 | RADIUS | DIAMETER |
|------|--------|----------|
| RFC | 2865/2866 | 6733 |
| プロトコル | **UDP** | **TCP/SCTP** |
| 暗号化 | パスワードのみ | TLS/IPsec で全体暗号化 |
| 拡張性 | 低い | 高い |
| 利用領域 | 企業LAN/ISP | LTE/5G/IMS(通信事業者) |
| 信頼性 | 再送頼り | TCPにより高い信頼性 |

## 5. 周辺知識(AAA関連)

### ■ IEEE 802.1X  

ネットワークアクセス制御(NAC)の標準規格です。

構成要素：  
- **Supplicant**(クライアント)  
- **Authenticator**(スイッチ/アクセスポイント)  
- **Authentication Server**(通常 RADIUS)  

### ■ EAP(Extensible Authentication Protocol)

802.1X で利用される認証方式の枠組みです。  
例：EAP-TLS、PEAP、EAP-TTLS など。  

### ■ TACACS+

Cisco中心に利用されるAAAプロトコルです。  

特徴：  
- **全通信が暗号化される**  
- 管理者操作に強い  
- きめ細かなコマンド権限付与が可能  

### ■ SSO(Single Sign-On)  

AAAの概念を広げ、複数サービスを一度の認証で利用可能にする技術です。  
SAML、OAuth2、OIDC などが主流です。  
