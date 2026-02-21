# Pass-the-Hash攻撃とWindows NTLM認証

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士令和5年春期 午前Ⅱ 問2](https://www.sc-siken.com/kakomon/05_haru/am2_2.html)  

## 1. Pass-the-Hash(PtH)攻撃とは  

Pass-the-Hash(PtH)攻撃とは、**Windowsが内部で保持する“パスワードハッシュ(NTLMハッシュ)”を盗み、そのまま認証に利用してログインする攻撃**です。  

### ❗重要ポイント  

- ハッシュ＝“パスワードの代わり”として機能する  
- パスワードの平文を知らなくても認証可能  
- 横移動(Lateral Movement)攻撃の中心的手法  
- 権限昇格/ドメイン制圧に直結する  

## 2. NTLM(New Technology LAN Manager)認証とは  

Windows が提供するチャレンジレスポンス方式の認証プロトコルです。  
現在の標準は **Kerberos** だが、互換性のため **NTLM も残存しています**。  

### 2.1 NTLM の種類

- **NTLMv1**：DES ベースのチャレンジレスポンス計算と LM Hash を使用する弱い方式 → **利用非推奨**  
- **NTLMv2**：HMAC-MD5 を利用した強化版(ただし PtH は防げない)  

### 2.2 NTLM 認証(チャレンジレスポンス方式)

パスワード本体が送られない利点があるが**盗んだハッシュ値を使えば本人になりすますことが可能**という致命的弱点があります。  

1. クライアントがログイン要求  
2. サーバがチャレンジ値を送信  
3. クライアントは **パスワード→NTLMハッシュ** を使い応答を生成  
4. サーバ側に登録されたハッシュで検証  

## 3. Pass-the-Hash攻撃の仕組みと手順

### 3.1 手順①：NTLMハッシュの取得  

Windows の **LSASS(Local Security Authority Subsystem Service)** から資格情報を抽出します。  

主なツール：  

- **Mimikatz(最も有名)**  
- Invoke-Mimikatz(PowerShell版)  
- Metasploit(hashdump モジュール)  

LSASS が保持しているもの：  

- NTLM ハッシュ  
- Kerberos TGT/TGS チケット    
- LSA Secrets(サービスアカウント情報など)  

### 3.2 手順②：ハッシュをそのまま認証に使用  

**平文パスワードが不要で認証可能です。**  

例：PsExec をハッシュで実行  
```
PsExec.exe \TARGET cmd.exe -u user -H <NTLMハッシュ>
```

### 3.3 手順③：横移動(Lateral Movement)  

取得した資格情報を使い、ネットワーク内の他端末へ侵入します。  
最終的には **ドメインコントローラ(DC)奪取** を狙うのが典型的攻撃シナリオです。  

横移動手法：  

- SMB(C$/ADMIN$)  
- WinRM  
- WMI  
- RDP  

## 4. NTLM が PtH に弱い理由(設計上の問題)

- NTLM は「パスワード」ではなく「パスワードハッシュ」を認証に使用  
- **ハッシュを知っている＝パスワードを知っているに等しい**  
- セッションキー生成にもハッシュを使用  
- Kerberos のような“チケット署名検証”の仕組みが弱い  

そのため、**1 回でも侵害されると横移動が容易になります**。  

## 5. PtH 攻撃の有効な対策(Microsoft 推奨)

### 5.1 Credential Guard(Windows 10+)

VBS(仮想化基盤)により LSASS を隔離して資格情報窃取を防止します。  
これは、**最も強力な防御策**です。  

### 5.2 LAPS(Local Administrator Password Solution)

- PCごとに異なるローカル管理者パスワードを自動で設定  
- 横移動耐性が大幅に向上  
- ドメイン管理のベストプラクティス  

### 5.3 管理者アカウントの分離

- 日常操作用アカウントと特権管理用アカウントを分ける  
- 特権アカウントでのログオンを最小化する  

### 5.4 NTLM の無効化(Kerberos の強制)

- グループポリシーで NTLM 認証を拒否  
- SMB サインを必須化  
- 既存システムの互換性要検討  

### 5.5 LSASS プロセス保護(RunAsPPL)

LSASS への不正読取を防止：  
```
HKLM\SYSTEM\CurrentControlSet\Control\Lsa
"RunAsPPL"=dword:00000001
```

### 5.6 SMBv1 の無効化

EternalBlue 系脆弱性の悪用防止にも有効です。  

## 6. Windows 認証の比較(NTLM vs Kerberos)

| 項目 | NTLM | Kerberos |
|------|------|----------|
| 認証方式 | チャレンジレスポンス | チケット(KDC)方式 |
| 弱点 | Pass-the-Hash | Pass-the-Ticket(TGT/TGS) |
| セキュリティ強度 | 中 | 高 |
| 推奨度 | 互換性目的 | **Windowsドメインの標準方式** |

## 7. MITRE ATT&CK との対応(エビデンス)

| 攻撃技術 | ID | 内容 |
|----------|------|---------|
| Credential Dumping | T1003 | LSASS から資格情報を抽出 |
| Pass-the-Hash | **T1550.002** | ハッシュを使った認証なりすまし |
| Pass-the-Ticket | T1550.003 | Kerberos チケット悪用 |

MITRE ATT&CK によって **実際の攻撃フレームワークとマッピング可能**です。  

## 8. 周辺知識(試験で一緒に問われる領域)

### 8.1 SAM(Security Accounts Manager)

ローカル資格情報の保存場所です。  
SAMデータベースも Mimikatz の標的になります。  

### 8.2 Kerberos のチケット盗難(Pass-the-Ticket)

PtH の兄弟攻撃です。  
TGT/TGS を盗んで成りすましを行います。  

### 8.3 Protected Users グループ  

- NTLM を禁止  
- 資格情報キャッシュ無効  
- 高セキュリティ運用向き  

### 8.4 SMB サイン(Message Signing)

中間者攻撃を防止します。  
NTLM 環境でも有効です。  
