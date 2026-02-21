# MPLS/PPP/PPPoE/PPTP/IPsec

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士平成31年春期 午前Ⅱ 問19](https://www.sc-siken.com/kakomon/31_haru/am2_19.html)  

## MPLS(Multiprotocol Label Switching)

パケットにラベルを付与し、そのラベルに基づいて高速に転送する仕組みです。  

### 特徴

* ラベルスイッチングにより高速転送  
* L2とL3の中間的な技術(Layer 2.5と呼ばれる)  
* ISPのVPNサービス(IP-VPN)で利用  
* QoS(DiffServ)やトラフィックエンジニアリングに強い  

### MPLSの構成要素

|名称|意味|
|:----|:----|
|LSR（Label Switch Router）|MPLS ラベルを見て転送するルータ|
|LER（Label Edge Router）|MPLSネットワークの入口・出口でラベル付加・削除|
|FEC（Forwarding Equivalence Class）|ルーティンググループ|
|LSP（Label Switched Path）|MPLS 上の経路|

## PPP(Point-to-Point Protoco)

2転換の通信リンクでデータを送受信するためのデータリンク層プロトコルです。  

### 特徴

* 認証機能(PAP/CHAP)あり  
* エラー検出  
* LCP(リンク制御)とNCP(ネットワーク制御)で構成  
* ダイヤルアップ接続(アナログ回線/ISDN)で使用されてきた  

### PPPの構成プロトコル

|プロトコル|役割|
|:----|:----|
|LCP（Link Control Protocol）|リンクの確立・維持・切断|
|NCP（Network Control Protocol）|IP, IPX などネットワーク層の設定|
|PAP（Password Authentication Protocol）|平文認証|
|CHAP（Challenge Handshake Authentication Protocol）|挑戦応答方式の安全な認証|

## PPPoE(PPP over Ethernet)

イーサネット上でPPPをカプセル化する方式です。  

### 特徴

* 主に家庭のインターネット接続(ADSL/FTTH)で使用  
* ISPの認証をPPPのPAP/CHAPによって実施  
* Ethernetフレーム内にPPPフレームを格納(カプセル化)  

## PPTP(Point-to-Point Tunneling Protocol)

PPPフレームをIPネットワーク上でトンネル化し、仮想専用線(VPN)を実現する技術です。  

### 特徴

* PPPをGREトンネルでカプセル化  
* Microsoftが主導して普及  
* 古いVPN技術で、現在はセキュリティ上非推奨  

## 周辺知識

### L2TP(Layer 2 Tunneling Protocol)

* PPTPとL2Fを統合した後継技術  
* 暗号化機能はないためIPsecとセットで利用(L2TP/IPsec)  

### IPsec

* VPNの標準  
* 暗号化(ESP)  
* 認証(AH)  
* IKE(鍵交換)  
* 企業VPNのデファクト

### GRE(Generic Routing Encapsulation)

* 任意のL3パケットをカプセル化  
* PPTPの内部でも使用されている  

### L3VPNとL2VPN(MPLS)

|種別|仕組み|
|:----|:----|
|MPLS L3 VPN|MP-BGP で経路交換（IP-VPN）|
|MPLS L2 VPN|VPLS, VPWS|

### NGN(Next Generation Network)

* MPLSをベースとしたキャリア網  
* QoSと制御が強力  

### 認証方式

|認証方式|特徴|
|:----|:----|
|PAP|平文パスワード → 非推奨|
|CHAP|Challenge-Response 方式、盗聴に強い|
|MS-CHAPv2|PPTPで使用 → 重大な脆弱性|
