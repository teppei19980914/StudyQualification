# TCP23番ポート(Telnet)とウェルノウンポートの基礎知識

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報セキュリティスペシャリスト平成27年春期 午前Ⅱ 問18 ](https://www.sc-siken.com/kakomon/27_haru/am2_18.html)  
[情報処理安全確保支援士令和元年秋期 午前Ⅱ 問20](https://www.sc-siken.com/kakomon/01_aki/am2_20.html)  
[情報処理安全確保支援士令和3年秋期 午前Ⅱ 問11](https://www.sc-siken.com/kakomon/03_aki/am2_11.html)  

## TCP(Transmission Control Protocol)とは  

**RFC 793/RFC 1122/RFC 5681** で定義される、信頼性の高いコネクション指向型のトランスポート層プロトコルです。  

主な特徴：  

- コネクション型(3-way ハンドシェイク)  
- 信頼性(再送制御、順序制御、誤り検出)  
- フロー制御(ウィンドウ制御)  
- 輻輳制御(スロースタート、輻輳回避、ファストリトランスミット)  
- 全二重通信(Full-duplex)  

## TCPヘッダー各フィールドの詳細

TCPヘッダーには下記フィールドが用意されています。  

* Source Port
* Destination Port
* Sequence Number
* Acknowledgment Number
* Data Offset
* Control Flags
* Window Size
* Checksum
* Urgent Pointer
* Options

### 送信元ポート番号（Source Port）

- 通信元アプリケーションを識別
- クライアント側はエフェメラルポートを使用

**攻撃・運用との関係**
- セッション識別（5タプル）
- ポートスキャンの対象

### 宛先ポート番号（Destination Port）

- 通信先アプリケーションを識別
- HTTP(80), HTTPS(443) など

### シーケンス番号（Sequence Number）

- **送信データの先頭バイト番号**
- データの順序制御・再送制御に使用

**重要ポイント**
- 初期値（ISN）はランダム
- 推測されると **TCPセッションハイジャック** の危険

### 確認応答番号（Acknowledgment Number）

- 次に受信したいバイト番号を通知
- ACKフラグと組み合わせて使用

### データオフセット（Data Offset）

- TCPヘッダー長を示す
- 単位は32bitワード

**意義**
- オプションフィールドの有無を判定

### フラグ（Control Flags）

TCPの状態管理の中核を担います。  

| フラグ | 意味 |
|---|---|
| SYN | 接続要求 |
| ACK | 確認応答有効 |
| FIN | 正常終了 |
| RST | 異常終了 |
| PSH | 即時配送 |
| URG | 緊急データ有効 |

**試験頻出ポイント**
- SYN/ACK/FIN/RST の意味と役割
- 不正な組合せは攻撃検知に利用

### ウィンドウサイズ（Window Size）

- 受信側が受信可能なデータ量
- フロー制御の要

**関連攻撃**
- Window サイズ枯渇攻撃

### チェックサム（Checksum）

- TCPヘッダー＋データの誤り検出
- IP疑似ヘッダーも含む

### 緊急ポインタ（Urgent Pointer）

- URGフラグが立っている場合のみ有効
- 現在ではほぼ使用されない

### オプション（Options）

代表例：

- MSS（Maximum Segment Size）
- Window Scale
- SACK（Selective Acknowledgment）

**役割**
- 通信効率・信頼性向上

## TCP 3-way ハンドシェイク(接続確立)

TCP の接続確立は以下の手続きで行われます。  

```
Client → Server : SYN
Server → Client : SYN/ACK
Client → Server : ACK
```

目的：  

- 初期シーケンス番号(ISN)の同期  
- 双方向通信の準備完了  

## TCP の接続終了(4-way ハンドシェイク)

```
FIN →
         ← ACK
         ← FIN
ACK →
```

理由：  

- TCP は全二重通信のため、双方が独立して FIN を送る必要があります。

## 再送制御(Reliable Transmission)

TCP は誤り制御として「再送」を行います。  

### タイムアウト再送(RTO)

- ACK が返らなければ **Retransmission Timeout(RTO)** により再送  
- RTO は RTT の変動で動的に計算される(RFC 6298)  

### 重複ACKによる高速再送(Fast Retransmit)

3つ以上連続した Duplicate ACK を受信すると、**タイムアウトを待たずに高速再送** を行います。  

## フロー制御(Flow Control：受信側保護)

受信側がパンクしないための **ウィンドウ制御(Window Size)** を使用します。  

- 受信側は「受信可能バッファサイズ」をウィンドウサイズとして通知  
- 送信側はその範囲内でのみ送信可能  

## 輻輳制御(Congestion Control：ネットワーク保護)

RFC 5681 による代表的アルゴリズムです。  

### スロースタート(Slow Start)

最初は送信量(cwnd)を指数的に増加します。  
また、ネットワークの混雑を探りながら増やします。  

### 輻輳回避(Congestion Avoidance)

しきい値(ssthresh)を超えると増加ペースを線形に変更します。  

### 高速再送(Fast Retransmit)

Duplicate ACK を基に即座に再送します。  

### 高速回復(Fast Recovery)

混雑発生後も cwnd をゼロに戻さず制御し、スループット低下を軽減します。  

## MSS/MTU/フラグメンテーション

### MTU(Maximum Transmission Unit)

リンク層の最大フレームサイズ(Ethernet: 1500 byte)です。  

### MSS(Maximum Segment Size)

TCP セグメントが運べる最大データ量です。  
**MSS ≒ MTU - IPヘッダ - TCPヘッダ**  

### パス MTU ディスカバリ(PMTUD)

ICMP Fragmentation Needed を利用し、最適 MSS を発見する仕組みです。  

## ポート番号(IANA Port Registry)  

既存ファイル内容に準拠しています。  

- Well-Known Ports：0–1023  
- Registered Ports：1024–49151  
- Dynamic Ports：49152–65535  

TCP 23 ＝ Telnet(RFC 854)  
TCP 22 ＝ SSH(RFC 4251)  
TCP 80 ＝ HTTP(RFC 9110)  
TCP 443 ＝ HTTPS(RFC 9110)  

## TCP のセキュリティリスクと対策

### ● SYN Flood(DoS攻撃)

- 大量の SYN を送り、半開状態(SYN-RECV)を保持させる攻撃  
- 対策：SYN Cookies、ファイアウォール、SYN Backlog 拡張  

### ● セッションハイジャック

- シーケンス番号推測 → セッション乗っ取り  
- 現代のランダム ISN(RFC 6528)で困難に  

→ **SYNフラグ・シーケンス番号管理**が重要です。  

### ● Reset 攻撃(RST Spoofing)

RST を偽造して通信を強制切断します。  

## TCP と UDP の比較(試験頻出)

|項目|TCP|UDP|
|---|---|---|
|信頼性|あり|なし|
|コネクション|あり|なし|
|再送制御|あり|なし|
|速度|遅い|速い|
|用途|Web, メール|DNS, VoIP, ゲーム|
| ヘッダー | 複雑 | 簡素 |
| 攻撃面 | 状態管理が狙われる | 反射攻撃に利用 |

## Telnet の仕様(エビデンス：RFC 854)

Telnet は歴史の古い **仮想端末接続プロトコル**で、**RFC 854 “TELNET PROTOCOL SPECIFICATION”** によって規定されています。

RFC：https://datatracker.ietf.org/doc/html/rfc854  

### Telnet の特徴

- TCP23番ポートを使用  
- 通信内容は **平文(暗号化なし)**  
- パスワードや入力内容もそのままネットワーク上に流れる  
- 双方向のテキストベース通信  

## Telnet のセキュリティリスク

Telnet が今日利用されない最大の理由は「暗号化がないこと」です。

### ● 主なリスク

1. **盗聴(Sniffing)によるパスワード漏洩**  
2. **MITM(中間者攻撃)に弱い**  
3. **セッション乗っ取りが可能**  
4. **ブルートフォース攻撃の標的になりやすい**  
5. **古い OS/ネットワーク機器の脆弱性悪用に使われる**  

### ● 推奨される代替手段(エビデンス：RFC 4251)

Telnet の代わりに、暗号化通信が可能な **SSH(Secure Shell, TCP22)** の利用が標準となっています。  

## ウェルノウンポート(Well-Known Ports)

IANA により **0〜1023番がウェルノウンポート** と定義されています。  
これらは OS が管理し、サーバ用途で利用されるポートです。  

### 主なウェルノウンポート(IANA/RFC 準拠)

| ポート番号 | プロトコル | 用途 | 標準(RFC) |
|------------|------------|------|--------------|
| 20/21 | FTP | ファイル転送 | RFC 959 |
| 22 | SSH | セキュアリモートログイン | RFC 4251 |
| 23 | Telnet | 非暗号化リモートログイン | RFC 854 |
| 25 | SMTP | メール送信 | RFC 5321 |
| 53 | DNS | 名前解決 | RFC 1035 |
| 67/68 | DHCP | IP割当(UDP) | RFC 2131 |
| 69 | TFTP | 簡易ファイル転送 | RFC 1350 |
| 80 | HTTP | Web通信 | RFC 9110 |
| 110 | POP3 | メール受信 | RFC 1939 |
| 143 | IMAP | メール受信 | RFC 3501 |
| 443 | HTTPS | 暗号化Web通信 | RFC 9110 |

## 周辺知識

### ● ステルススキャン

- FIN / Xmas / Null スキャン
- フラグ挙動を悪用

### ● Nagle アルゴリズム

小さい TCP セグメントをまとめて送信することで遅延が発生します。  
→ SSH/Telnetではオフにすることがあります。  

### ● Delayed ACK

Nagle と組み合わせると遅延が大きくなる“相互作用問題”があります。  

### ● KeepAlive(TCP Keepalive)

長時間通信が無い場合、接続生存確認を行います。  

### ● TIME_WAIT

接続終了時に残る状態(2MSL保持)です。  

### ● ポート番号の分類

IANA ではポート番号を以下のように分類しています。  

| 区分 | 範囲 | 説明 |
|------|--------|--------|
| **Well-Known Ports** | 0–1023 | 代表プロトコル用(HTTP, SSH, Telnet等) |
| **Registered Ports** | 1024–49151 | 各アプリケーションが登録して利用 |
| **Dynamic/Private Ports** | 49152–65535 | クライアント側の動的ポート |

TCP23番ポートは **Well-Known Ports に属する** ため、スキャン対象として狙われやすい特徴があります。  

###  ファイアウォール/脆弱性管理での注意点

####  Telnet(TCP23)は外部公開しない  

FW では以下の設定が必須です。  

```text
外部 → 内部：TCP23 すべて拒否
内部 → 外部：必要な場合のみ許可(基本は不要)
```

#### SSH(22番)に移行する

暗号化されている SSH を利用するのが標準的対策です。  

#### ポートスキャン対策

攻撃者は以下の技術で23番をスキャンします。  

* SYNスキャン  
* TCP Connect スキャン  
* 全ポートスキャン

FW/IPS で検知/遮断することが推奨されます。  
