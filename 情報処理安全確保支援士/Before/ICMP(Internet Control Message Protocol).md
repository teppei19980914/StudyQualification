# ICMP(Internet Control Message Protocol)

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士令和6年秋期 午前Ⅱ 問19](https://www.sc-siken.com/kakomon/06_aki/am2_19.html)  

## 1. ICMPとは何か(RFC 792)

ICMP(Internet Control Message Protocol)は、**IP通信の制御/エラー通知/経路診断を行うプロトコル**です。  
RFC 792 で正式に定義されており、“IPレイヤの補助プロトコルであり、エラー報告のために使用する” と記述されています。  

### 1.1 ICMPの役割  

- **エラーメッセージ通知**  
  - 宛先到達不能  
  - タイムエクシード  
  - パラメータ異常  
- **経路診断**  
  - ping(Echo Request/Reply)  
  - traceroute(Time Exceededを利用)  
- **ネットワーク制御**  
  - リダイレクト(経路変更指示)  
  - ソースクエンチ(現在は非推奨)  

## 2. ICMPメッセージ分類(RFC 792)

ICMP メッセージは **Type と Code** によって分類されます。  

### 2.1 代表的な ICMP Type

| 種類 | Type | 内容 |
|------|------|------|
| Echo Request | 8 | ping 送信 |
| Echo Reply | 0 | ping 応答 |
| Destination Unreachable | 3 | 宛先到達不能 |
| Time Exceeded | 11 | TTL 超過(tracerouteで利用) |
| Redirect | 5 | 経路変更指示 |
| Parameter Problem | 12 | パケット構造の異常 |

## 3. 宛先到達不能(Destination Unreachable)

Type 3 の代表的コード：

| Code | 意味 |
|------|------|
| 0 | Network Unreachable |
| 1 | Host Unreachable |
| 3 | Port Unreachable(UDP応答でよく使われる) |
| 4 | Fragmentation Needed(DF=1時) |

UDP(未接続型)では、宛先ポート未使用時に **ICMP Port Unreachable** が通知されるため、**UDPスキャンの検知**にも使われます。  

## 4. Time Exceeded(TTL超過)

TTLが0になるとルータが送信する ICMP Type 11のことです。  
traceroute は次の仕組みで動作しています。  

1. TTL=1 のパケット送信  
2. 1番目のルータで TTL=0 → ICMP Time Exceeded  
3. TTL=2 のパケット送信  
4. 2番目のルータで TTL=0 → ICMP Time Exceeded  
…これを繰り返すことで経路を特定  

## 5. ICMP Redirect(経路変更指示)

ルータがホストに対して「より適切なルータがあるので、そちらへ送信せよ」と通知します。  
しかし、攻撃者が悪用すると **MITM攻撃(中間者攻撃)** を可能にするため、現在では **管理ネットワーク以外では禁止が推奨**されています。  

## 6. ICMP攻撃(セキュリティ観点)

### 6.1 Smurf攻撃  

ブロードキャスト宛てに送信元IPを偽装した Echo Request を送信し、大量の Echo Reply を被害者に集中させる攻撃です。  
→ directed broadcast を禁止することで、Smurf攻撃を防止します。  

### 6.2 ICMP Flood(DoS攻撃)

大量の Echo Request を送り、CPU負荷や帯域枯渇を狙います。  
→ ICMPレート制限することでDos攻撃を防止できます。  

### 6.3 ICMP Tunneling  

ICMPペイロード内に任意データを埋めて通信する手法です。  
ファイアウォール回避に悪用されます。  
→ 組織では ICMP を必要最小限に制限することが推奨されます。  

## 7. ICMPv6(RFC 4443)

IPv6 では **ICMPv6 が必須プロトコル**であり、IPv6 ネットワーク制御の中核となります。  

### 7.1 ICMPv6が必須となる理由  

IPv4 よりも ICMP の重要性が高いからです。  

- **近隣探索(NDP：Neighbor Discovery Protocol)**  
    ARP を置き換える仕組み  
- **RA(Router Advertisement)**  
    IPv6アドレス自動生成  
- **MLD(Multicast Listener Discovery)**  
    マルチキャスト管理  

## 8. 周辺知識(試験で問われやすい)

### 8.1 ARPとの違い  

| プロトコル | 役割 |
|------------|------|
| ARP | L2アドレス解決(IPv4) |
| ICMP | IPエラー通知/診断 |
| ICMPv6(NDP) | IPv6版ARP |

### 8.2 UDPとの関係  

UDPは未接続型のため、未使用ポートへのアクセスでは**ICMP Port Unreachable(Type3 Code3)** が返されます。  
→ ポートスキャンの検知に活用されます。  

### 8.3 TCPとの関係  

TCPはコネクション型です。  
3ウェイハンドシェイクの段階では ICMP ではなく **RST** を返します。  

### 8.4 ファイアウォールでのICMP制御  

- ping応答を禁止  
- Redirectを禁止  
- Time Exceeded(traceroute)を制限  
- Fragmentation Needed(PMTUDに必須)は許可すべき  
