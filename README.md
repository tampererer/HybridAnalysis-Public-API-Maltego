# [HybridAnalysis] Maltego Local Transforms
Maltego Local Transform to use Hybrid Analysis Public API - https://www.hybrid-analysis.com/apikeys/info

# Prerequisites
- Hybrid Analysis Public API access
- Python 2.7.x + requests, json module

# 必要なもの
- Hybrid Analysis Public APIのアクセス権
- Python 2.7.x + requests, json モジュール

# Setup
- Edit HA.py and set "apikey" and "secret" variable with your API key and Secret. If you have multiple API keys and Secrets, you can set them to increase quota.
- Put HA.py and MaltegoTransform.py into your working directory. (e.g. C:\Maltego\Transforms\HybridAnalysis)
- Open HA.mtz to import Maltego configuration.
- The current configuration uses the following directories, so you may have to change them according to your environment. (Maltego -> Transforms -> Transform Manager)  

  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\HybridAnalysis

# セットアップ
- HA.py の中で、apikey と secret という変数に、自分の API key と Secret を記載してください。複数の API key と Secret を持っている場合は、Quotaを増やすために複数記載することもできます。
- HA.py と MaltegoTransform.py を、このTransform用に作ったディレクトリに置いてください。（例： C:\Maltego\Transforms\HybridAnalysis）
- HA.mtz を開いて、Maltegoの設定をインポートしてください。
- mtzファイルに含まれる設定では、下記のディレクトリが指定されていますが、自分の環境に合わせて変更してください。（Maltego -> Transforms -> Transform Manager）

  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\HybridAnalysis

# Transforms
- hash_to_all
- hash_to_c2host
- hash_to_c2ip
- hash_to_filename
- hash_to_filetype
- hash_to_label
- hash_to_md5
- hash_to_sha256
- hash_to_similar
- hash_to_tag
- hash_to_threatscore
- c2host_to_hash
- c2ip_to_hash
- label_to_hash
- authentihash_to_hash
- tag_to_hash
