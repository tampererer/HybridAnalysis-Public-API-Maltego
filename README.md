# [Hybrid Analysis Public API] Maltego Local Transforms
Maltego Local Transform to use Hybrid Analysis Public API - https://www.hybrid-analysis.com/apikeys/info

# Prerequisites
- Hybrid Analysis Public API access
- Python 2.7.x + requests, json module
- Python 3.6.x will probably work.

# 必要なもの
- Hybrid Analysis Public APIのアクセス権
- Python 2.7.x + requests, json モジュール
- Python 3.6.x でもたぶん動作します。

# Setup
- Edit HA.py and set "apikey" and "secret" variable with your API key and Secret. If you have multiple API keys and Secrets, you can set them to increase quota.
- Put all python files into your working directory. (e.g. C:\Maltego\Transforms\HybridAnalysis)
- Open HA.mtz to import Maltego configuration.
- The current configuration uses the following directories, so you may have to change them according to your environment. (Maltego -> Transforms -> Transform Manager)  

  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\HybridAnalysis

# セットアップ
- HA.py の中で、apikey と secret という変数に、自分の API key と Secret を記載してください。複数の API key と Secret を持っている場合は、クォータを増やすために複数記載することもできます。
- 全てのPythonファイルを、このTransform用に作ったディレクトリに置いてください。（例： C:\Maltego\Transforms\HybridAnalysis）
- HA.mtz を開いて、Maltegoの設定をインポートしてください。
- mtzファイルに含まれる設定では、下記のディレクトリが指定されていますが、自分の環境に合わせて変更してください。（Maltego -> Transforms -> Transform Manager）

  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\HybridAnalysis

# Transforms
- [HA] hash_to_all  
Input: Hash  
Output: Domain, IP address, Filename, Malware name, Threat score, File type, Tag  
<img src="https://user-images.githubusercontent.com/16297449/42555973-0af5b38a-8525-11e8-8a7a-88c8657414e3.png" width="600">

- [HA] hash_to_c2host  
Input: Hash  
Output: Domain  
<img src="https://user-images.githubusercontent.com/16297449/42556053-4b5ba2a4-8525-11e8-896e-5b196ae26119.png" width="300">

- [HA] hash_to_c2ip  
Input: Hash  
Output: IP address  
<img src="https://user-images.githubusercontent.com/16297449/42556117-80963c72-8525-11e8-904c-9ddf2bcb45b2.png" width="300">

- [HA] hash_to_filename  
Input: Hash  
Output: Filename  
<img src="https://user-images.githubusercontent.com/16297449/42556165-acce01da-8525-11e8-87e5-9a58a9889388.png" width="300">

- [HA] hash_to_filetype  
Input: Hash  
Output: File type  
<img src="https://user-images.githubusercontent.com/16297449/42556314-283a02ba-8526-11e8-84ee-2a9118306411.png" width="900">

- [HA] hash_to_label  
Input:   
Output:   

- [HA] hash_to_md5  
Input:   
Output:   

- [HA] hash_to_sha256  
Input:   
Output:   

- [HA] hash_to_similar  
Input:   
Output:   

- [HA] hash_to_tag  
Input:   
Output:   

- [HA] hash_to_threatscore  
Input:   
Output:   

- [HA] c2host_to_hash  
Input:   
Output:   

- [HA] c2ip_to_hash  
Input:   
Output:   

- [HA] label_to_hash  
Input:   
Output:   

- [HA] authentihash_to_hash  
Input:   
Output:   

- [HA] tag_to_hash  
Input:   
Output:   
