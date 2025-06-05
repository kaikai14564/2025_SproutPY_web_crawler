# Report

Q1: 如何擷取 Wikipedia 的 internal links？用了什麼過濾條件？
1.找出所有 <a> 標籤並提取 href 屬性
2.以 /wiki/ 開頭（表示為內部文章頁面）
3.不包含冒號 :（排除分類、檔案、使用者頁等特殊頁面）
4.使用 urljoin() 將相對連結轉成完整網址

Q2: 如何判斷一個連結是否應該被拜訪？
1.該連結尚未被訪問過
2.網域必須為 en.wikipedia.org
3.路徑需以 /wiki/ 開頭
4.路徑中不能包含 :

Q3: 各元件的角色說明（fetcher, parser, filter, 等）
fetcher.py: 發送 HTTP 請求並取得網頁內容
parser.py: 從網頁中擷取標題與連結資訊
filter.py: 過濾不合條件的連結
crawler.py: 控制爬蟲流程
storage.py: 寫入最終結果到 results.csv

Q4: 若要擴展到爬 10,000 頁，你會改進什麼？
1.增加暫存機制
2.使用資料庫儲存，而不是 CSV

Q5: 此系統的潛在應用場景有哪些？
1.建立搜尋引擎索引
2.內容推薦系統