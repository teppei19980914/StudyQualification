# クリックジャッキング攻撃(Clickjacking)

## はじめに

2025年10月のプロジェクトマネージャ試験受験を終え、2026年春の情報処理安全確保支援士に向けて勉強中です。  
本記事を含めた各知識のインデックスや学習の道のりについては、「[情報処理安全確保支援士への道のり(随時更新中)](https://qiita.com/teppei19980914/items/6411cb70f2937cbefdcc)」をご参照ください。  
**本記事は学習した内容を記載しています。**  

## 該当問題

[情報処理安全確保支援士令和4年秋期 午前Ⅱ 問11](https://www.sc-siken.com/kakomon/04_aki/am2_11.html)  

## 1. クリックジャッキング攻撃とは  

クリックジャッキングとは、**ユーザが意図しない UI 操作をさせられる攻撃** であり、特に iframe を悪用した **UI Redressing(UI の見かけを偽装する攻撃)** の代表例です。  

攻撃者は次の手法を使います。  

- 正規サイトを透明(opacity:0)または半透明の iframe で表示  
- ボタン/画像を重ね、ユーザのクリックを乗っ取る  
- 表面的には無害に見えるが、実際には「設定変更」「購入」「許諾」ボタンを押してしまう  

## 2. 攻撃の典型パターン

### 2.1 iframe による透明化/重ね合わせ攻撃

```html
<iframe src="https://victim.example.com" style="opacity:0; z-index:1000; position:absolute;"></iframe>
<button style="z-index:999;">クリック！</button>
```

ユーザは上のボタンを押したつもりが、透明 iframe 内のボタンを押します。  

### 2.2 SNS で多発：Likejacking

透明化した Facebook/Twitter の「Like」ボタンを押させます。  

### 2.3 権限許可の誤操作誘導(Permission Clickjacking)

スマートフォンやブラウザの許可画面を透明化し、下記などの「許可」ボタンを誤クリックさせます。  

- カメラ  
- マイク  
- 位置情報  
- 通知  

## 3. クリックジャッキングが危険な理由

クリックジャッキングでは、**攻撃者はユーザの認証済みセッションを悪用するだけでよく、Cookie を盗む必要はないです。**  
そのため、下記などの利用者本人の操作として扱われてしまいます。  

- アカウント設定変更  
- OAuth の不正承認  
- EC サイトでの商品購入  
- 管理画面の設定操作  

## 4. 防御策(X-Frame-Options/CSP)

### 4.1 X-Frame-Options(旧来方式だが依然有効)  

| 値 | 意味 |
|----|------|
| DENY | iframe での埋め込み禁止 |
| SAMEORIGIN | 同一オリジンのみ iframe を許可 |
| ALLOW-FROM URL | 指定 URL のみ許可(互換性は低い) |

例：  

```
X-Frame-Options: SAMEORIGIN
```

### 4.2 CSP(Content-Security-Policy)frame-ancestors(現在の推奨)  

**X-Frame-Options の後継的役割**を担い、柔軟かつブラウザ対応が広いです。  

```
Content-Security-Policy: frame-ancestors 'self' https://trusted.example.com;
```

## 5. アプリ側の追加対策

### 5.1 Frame Busting スクリプト(補助的)

ただし CSP 導入後は補助的な扱いです。  

```javascript
if (top !== self) {
    top.location = self.location;
}
```
### 5.2 重要操作の再認証

ユーザ操作 1 回で危険な処理を行えないようにします。  

- 2FA(多要素認証)  
- パスワード再入力  
- 二段階確認ダイアログ  

## 6. 関連攻撃(支援士的に押さえるべき)

| 攻撃名称 | 概要 |
|----------|------|
| **Likejacking** | SNS の「Like」を透明 iframe で押させる |
| **Cursorjacking** | カーソル位置を偽装して誤クリック誘導 |
| **Tabnabbing** | 放置されたタブを書き換えてフィッシング |
| **UI Deception** | UI の見た目を操作して錯誤誘発 |
| **CSRF** | クリックジャッキングと併用で強力に |
