# ## Circle K History Exporter

### Công cụ Python giúp sao lưu toàn bộ lịch sử giao dịch từ app Circle K Việt Nam ra file Excel.

#### Chạy thử:

![](./img/1.png)

#### Kết quả:

<img title="" src="./img/2.png" alt="" width="533">

### ## Hướng dẫn nhanh

#### 1. Chuẩn bị môi trường

Đảm bảo bạn đã cài đặt Python 3.10+. Mở Terminal (hoặc CMD/PowerShell) tại thư mục project và thực hiện các bước sau:

```powershell
# Tạo môi trường ảo
python -m venv .venv

# Kích hoạt (Windows)
.\.venv\Scripts\activate 

# Cài đặt thư viện
pip install -r requirements.txt
```

#### 2. Download Http Toolkit: [Download HTTP Toolkit for Windows Installer](https://httptoolkit.com/download/win-exe/)

#### 3. Gỡ lỗi USB, bật Chế độ nhà phát triển trên ĐT, connect với điện thoại

<img title="" src="./img/3.png" alt="" width="376">

#### 4. Mở app Circle K - giao dịch

![](./img/4.png)

#### 5. Mở Http Toolkit - bật Android Device via ADB

![](./img/6.png)

#### 6. Lấy API transaction

![](./img/7.png)

#### 7. Lấy token (Đã login trong app Circle K và bật app)

![](./img/8.png)

#### 8. Coppy và dán token

![](./img/9.png)

#### 9. Chạy python ở powershell

```powershell
python main.py
```
