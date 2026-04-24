# ## Circle K History Exporter

### Công cụ Python giúp sao lưu toàn bộ lịch sử giao dịch từ app Circle K Việt Nam ra file Excel.

#### Chạy thử:

![](C:\Users\nghia\AppData\Roaming\marktext\images\2026-04-24-23-29-51-2026-04-24-23-24-51-image.png)

#### Kết quả:

<img src="file:///C:/Users/nghia/AppData/Roaming/marktext/images/2026-04-24-23-31-35-image.png" title="" alt="" width="533">

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

<img src="file:///C:/Users/nghia/AppData/Roaming/marktext/images/2026-04-24-20-38-49-image.png" title="" alt="" width="376">

#### 4. Mở app Circle K - giao dịch

![](C:\Users\nghia\AppData\Roaming\marktext\images\2026-04-24-20-39-43-image.png)

#### 5. Mở Http Toolkit - bật Android Device via ADB

![](C:\Users\nghia\AppData\Roaming\marktext\images\2026-04-24-20-41-53-image.png)

#### 6. Lấy API transaction

![](C:\Users\nghia\AppData\Roaming\marktext\images\2026-04-24-20-42-52-image.png)

#### 7. Lấy token (Đã login trong app Circle K và bật app)

![](C:\Users\nghia\AppData\Roaming\marktext\images\2026-04-24-21-27-57-Untitled.png)

#### 8. Coppy và dán token

![](C:\Users\nghia\AppData\Roaming\marktext\images\2026-04-24-21-28-50-image.png)

#### 9. Chạy python ở powershell

```powershell
python main.py
```
