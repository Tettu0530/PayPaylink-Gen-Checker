# PayPayLinkGenerator & Checker
本ソフトは決済サービス「PayPay」の非公式APIを用いられて作られたPayPay送金リンク生成ソフトです。
本ソフトを使用の上いかなる損害が生じても開発者(Tettu0530)は一切責任を負いません。

# 機能 | Function
- PayPayLink Generate
  - 最大18000Links/sで生成可能
  - 任意の数生成可能
  - threadingによる並列化でさらに高速化可能(お使いのCPUの性能に依存します)
- PayPayLink Checker
  - 最大100Links/sで確認可能
  - Proxy(HTTP, HTTPS)を通じてアクセスすることでより安全にチェックできます。
