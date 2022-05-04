# Bigbang_Fan

專案使用Flask架構，呈現Bigbang粉絲部落格網站  
===========================
基礎功能:  
使用者帳號註冊、登入、登出與修改密碼功能  
使用者個人資料新增刪除修改  
使用者部落格文章與封面照片新增、呈現、編輯修改  
使用者角色權限管理  

===========================  

使用者帳號註冊、運用flask-loging實現login、logout與修改密碼功能  
sql連動紀錄user帳號密碼與blog內容   
粉絲團頁面展示bootstrap    
blog展示網誌類別、網誌內文編輯更新、圖片上傳更改、更新時間   
===========================  

###########環境依賴  
  Flask  
###########部署步驟  
1. pip install flask  //安裝flask執行環境  

2. python manager.py  //啟動  
   


###########目錄結構描述  
├── Readme.md                       // help  
├── manager                         // 應用  
├── app_blog                        // 配置  
│   ├── artist                      // 使用者  
│           ├── __init__.py       
│           ├── form.py            //表單格式  
│           ├── model.py           //使用者資料設定  
│           └── view.py            //網頁呈現  
│   ├── blog                       // 部落格內文  
│           ├── __init__.py  
│           ├── form.py  
│           ├── model.py  
│           └── view.py  
│   ├── main                       // 部落格分類  
│           ├── __init__.py  
│           ├── errorhandler.py  
│           ├── form.py  
│           ├── model.py  
│           └── view.py
│   ├──  static                    // web靜態資源載入  
│         └── css  
│            └── styles.css         
│         └── data  
│            └── data_register.db // 資料庫  
│         └── image_folder  
│            └── [pictures]   
│   ├── templates                 // 網頁檔  
│   ├── __init__.py                  
│   └── decorator_permission.py   //   
└── config                        // 配置  



###########V1.0.0 版本內容更新 
1. 新功能     aaaaaaaaa
2. 新功能     bbbbbbbbb
3. 新功能     ccccccccc
4. 新功能     ddddddddd
