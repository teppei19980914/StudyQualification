# Dos攻撃/Smurf攻撃/DDos攻撃/増幅型DDoS攻撃/マルチベクトル型DDoS攻撃

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報セキュリティスペシャリスト平成23年秋期 午前Ⅱ 問9](https://www.sc-siken.com/kakomon/23_aki/am2_9.html)  
[情報セキュリティスペシャリスト平成25年秋期 午前Ⅱ 問14](https://www.sc-siken.com/kakomon/25_aki/am2_14.html)  
[情報セキュリティスペシャリスト平成27年春期 午前Ⅱ 問10](https://www.sc-siken.com/kakomon/27_haru/am2_10.html)  
[情報処理安全確保支援士平成30年秋期 午前Ⅱ 問4](https://www.sc-siken.com/kakomon/30_aki/am2_4.html)  

## Dos(Denial Of Service)攻撃

DoS攻撃とは、**正規ユーザがサービスを利用できない状態を作り出す攻撃**です。  

目的：  

- サービス停止  
- 遅延発生(可用性低下)  
- 帯域や計算資源の枯渇  

### DoS攻撃の分類

#### ● 資源枯渇型

CPU/メモリ/スレッド/帯域などの資源を大量消費させる攻撃です。  

代表例：  

- SYN Flood(RFC 4987)  
- UDP Flood  
- ICMP Flood(Ping Flood)  

#### ● 脆弱性悪用型

実装バグを悪用してプロセスをクラッシュさせます。  

例：  

- Ping of Death  
- Teardrop攻撃(IPフラグメント再構成のバグ)  

#### ● DDos(Distributed Dos)攻撃

多数の踏み台(Bot)から攻撃を行います。  
近年の攻撃の主流で、Miraiボットネットなどが有名です。  

## Smurf攻撃(増幅型DoS)

Smurf攻撃とは、**ICMP Echo(Ping)とブロードキャストアドレスを悪用した増幅攻撃**です。  

参考：  
https://www.cert.org/historical/advisories/CA-1998-01.cfm

### 仕組み

Smurf攻撃は次のように行われます。  

1. 攻撃者が **送信元IPを被害者に偽装**した ICMP Echo Request を「ブロードキャストアドレス」宛に送信  
2. 同一ネットワーク上のすべてのホストが、被害者IPに対して **ICMP Echo Reply** を返却
3. 被害者には大量の ICMP 応答が集中し、帯域やCPUが枯渇  

### 図で理解する Smurf攻撃

```
攻撃者
  |
  |(送信元IPを被害者に偽装したPing)
  v
[ネットワークのブロードキャストアドレス]
  |—— 全ホストが応答 ————|
  v                                 v
Host A ———→                      (被害者IPへ集中)
Host B ———→
Host C ———→
```

1 つの送信パケット → 100台以上のホストが返信する可能性があるため、**大規模な増幅効果**が得られます。  

### Smurf攻撃が成立する条件

| 条件 | 詳細 |
|------|------|
| IPスプーフィングが可能 | 送信元IPを被害者に偽装する必要がある |
| ホストがBroadcast Pingに応答する設定 | OS側のICMP設定が脆弱 |
| ルータが directed broadcast を許可 | RFC2644以前の古い設定の場合は危険 |

RFC 2644 では **directed broadcast を禁止する**ことが強く推奨されています。  

## Smurf攻撃の対策(RFC 2644/CERT推奨)

### ルータ側の対策(最重要)

```
no ip directed-broadcast
```

Ciscoルータ推奨設定です。  
外部からブロードキャストアドレス宛の ICMP を遮断できます。  

### ホスト側の対策

- Broadcast Ping の応答禁止  
- 不要な ICMP メッセージをファイアウォールで制限  

### ネットワーク管理側の対策

- ブロードキャスト通信の最小化  
- 帯域監視による異常トラフィック検知  
- IDS/IPS による ICMP 異常パターン検出  

## 増幅型DDoS攻撃(Amplification DDoS Attack)とは  

増幅型DDoS攻撃とは、**小さな要求パケットを送信するだけで、攻撃対象に大量の応答パケットを送り付けられるような仕組みやプロトコルを悪用する攻撃方式** のことです。  

特徴：  

- 攻撃者 → 反射サーバ(DNS/NTP/SSDPなど)へ小さなリクエストを送信  
- 送信元IPを標的IPに偽装(IPスプーフィング)  
- 反射サーバ → 標的へ **巨大なレスポンス** を送信  
- 結果として **大量トラフィックが標的へ集中 → サービス不能(DoS)**  

増幅率(Amplification Factor)＝  **応答サイズ ÷ リクエストサイズ**

## 他の代表的な増幅型DDoS攻撃

### ■ DNS Amplification  

- リクエスト：小さなDNS問い合わせ  
- 応答：大きなDNS応答(特にANYクエリ)  
- 増幅率：最大 50倍超  

### ■ SSDP Amplification(UPnP)  

- リクエスト：数十B  
- 応答：数百B～数KB  
- 増幅率：約30倍  

### ■ CLDAP Amplification  

攻撃強度が高く、近年増加しています。  

増幅率：最大 70倍以上  
応答サイズが大きく、DDoS攻撃として強力です。  

### ■ Memcached Amplification  

増幅率：**最大51,000倍(歴史上最大級)**  

## 増幅型DDoS攻撃の共通対策

### ■ 不要サービスの停止

- NTP(monlist含む)  
- DNSオープンリゾルバ  
- SSDP/UPnP  
- CLDAP  

### ■ Rate Limiting/DoS防御装置

- レート制限  
- IPS/クラウドWAF  
- CDNによる吸収  

### ■ 監視とインシデントレスポンス(NIST SP 800-61)

- トラフィック監視  
- 異常検知  
- ISPとの連携  
- フォレンジックログ収集  

## マルチベクトル型DDoS攻撃（Multi‑Vector DDoS Attack）

### ● 定義  

マルチベクトル型DDoS攻撃とは、**複数の攻撃手法を同時に組み合わせて実施される大規模DDoS攻撃**の総称です。  
攻撃ベクトルが複数であるため、防御側のリソースを枯渇させ、単一の防御策では対処困難になります。

### ● 代表的な攻撃ベクトル  

- Volumetric Attack（UDP Flood、DNS Amplification）  
- Protocol Attack（TCP SYN Flood、Fragmentation攻撃）  
- Application Layer Attack（HTTP GET/POST Flood）

## DRDoS（Distributed Reflection DoS：反射型DoS攻撃）

### ● 定義  

送信元IPを標的IPに偽装し、第三者サーバ（DNS/NTPなど）の応答を大量に標的へ送らせる攻撃です。

### ● 危険性  

- IPスプーフィングのため攻撃元特定が困難  
- 少量トラフィックで大量攻撃（増幅率が高い）  
- 公開サーバが踏み台化する

## 代表的な増幅攻撃（Amplification Attack）

| 種類 | 説明 | 増幅倍率 |
|------|------|-----------|
| DNS Amplification | 小さな問い合わせ → 大きな応答 | 30〜70倍 |
| NTP Amplification | monlist 悪用 | 数百倍 |
| SSDP/UPnP | IoTデバイス悪用 | 数十〜数百倍 |
| Memcached Amplification | 最強クラスの増幅 | 最大50,000倍 |

## NTP Amplification Attack(NTP増幅攻撃)  

NTP(Network Time Protocol)は、ネットワーク機器/サーバの時刻同期に使われるプロトコル(UDP/123)です。  
問題となるのは、NTPの古い実装に存在した  **"monlist" コマンドによる増幅攻撃です。**  

### ■ monlist とは

`monlist` は「NTPサーバに最近アクセスした最大600台のクライアントリストを返す」管理者向けコマンドです。  

- 要求パケット：数十バイト  
- 応答パケット：数百～数千倍  

これにより、攻撃者は非常に高い増幅率を得られました。  

### ■ 攻撃の流れ(NTP Amplification)

1. 攻撃者 → NTPサーバへ `monlist` リクエスト(送信元IPを標的に偽装)  
2. NTPサーバ → 標的へ大量の応答パケット送信  
3. 標的サーバはトラフィック集中でダウン  

### ■ 対策(RFC 5905/NTP.org)

- **monlist 機能の無効化**(`disable monitor`)  
- `ntpq -c "rv 0"` で monitor 状態の確認  
- NTP のアップデート(Mode 6/7 の制限)  
- ファイアウォールで UDP/123 のインターネット公開を禁止  
- アクセス制御(`restrict` ルール)  

## DRDoS 防御（RFC 2827/BCP38）

- ISPによる送信元アドレスフィルタリング（IPスプーフィング防止）  
- DNSやNTPの公開制限  
- Recursive DNS 外部公開禁止  
- CDN/Anycast による負荷分散  
- Rate Limit による応答数制御  

## マルチベクトル型DDoSとの関係  
DRDoSは **マルチベクトルDDoSの一構成要素**としてよく利用されます。  
例：DNS増幅＋HTTP Flood、NTP増幅＋SYN Flood など。

## 周辺知識(午後問題でも問われるポイント)

### ■ DoS/DDoS の違い

- DoS：単一の攻撃元  
- DDoS：多数の攻撃元(Botnet)    

### IPスプーフィング(IP Spoofing)

Smurf攻撃に欠かせない技術です。  
攻撃者が送信元IPを被害者のIPに偽装します。  

#### 対策  

- **Ingress Filtering(RFC 2827/BCP 38)**  
    → 外部から来たパケットの送信元IPを検証し、不正なものを破棄します。  
- **Egress Filtering**  
    → 自ネットワークから出る不正な送信元IPを遮断します。  

### Amplification Attack(増幅型攻撃)

Smurf のほか、以下の攻撃も同様の構造をもちます。  

| 攻撃名 | 仕組み |
|--------|--------|
| DNS Amp | 小さなDNSリクエスト → 大量の応答パケット |
| NTP Amp | monlist要求による増幅 |
| SSDP Amp | UPnPを悪用した反射攻撃 |
| Chargen Amp | Chargenプロトコルの悪用 |

近年の DDoS は「反射/増幅攻撃」が主流です。  

### SYN Flood(RFC 4987)

TCP接続の「SYNキュー」を枯渇させる古典的攻撃です。  

#### 対策

- SYN Cookie の有効化  
- Firewall/Load Balancer での connection limit  

### Ping of Death

65535バイト超の異常パケットを送り、古いOSをクラッシュさせる攻撃です。

### ■ Botnet(ボットネット)

攻撃者に遠隔操作される多数のマルウェア感染端末の集合のことです。  
DDoSの主要な踏み台となります。  

### ■ CDN による DDoS 軽減

Cloudflare/Akamai などが提供します。  
**分散トラフィック吸収サービスです。**  

### DNS amp

脆弱性のある公開DNSキャッシュサーバを踏み台として悪用することで行われる分散型DDos攻撃の一種です。  

#### 攻撃手順

1. 攻撃者は、脆弱性のある複数の公開DNSキャッシュサーバに対して、送信元を攻撃対象としたDNSクエリをボットを介して発行する(このとき応答パケットのサイズができるだけ多くなるようにする)  
2. クエリを受け取ったDNSキャッシュサーバは、クエリの送信元に設定されている攻撃対象に対して応答パケットを一斉に送信する  
3. 大量の応答パケットを受け取った攻撃対象やそれが属するネットワークは過負荷状態となり正常なサービスの提供ができなくなる  

#### 踏み台にならないために

利用可能なホストのIPアドレスの範囲を設定するなど、DNSキャッシュサーバが不要なクエリを拒否するようにアクセス制限を施す必要があります。  
