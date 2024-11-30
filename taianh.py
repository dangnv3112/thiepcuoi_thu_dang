import os
import requests

def download_images(url_list, save_folder):
    # Tạo thư mục lưu ảnh nếu chưa tồn tại
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        print(f"Đã tạo thư mục: {save_folder}")

    for idx, url in enumerate(url_list, start=1):
        try:
            # Gửi yêu cầu GET đến URL
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Kiểm tra lỗi HTTP

            # Xác định tên tệp từ URL hoặc tạo tên tùy ý
            filename = os.path.basename(url)
            if not filename:
                filename = f"image_{idx}.jpg"
            filepath = os.path.join(save_folder, filename)

            # Lưu ảnh vào thư mục
            with open(filepath, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Tải xuống thành công: {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi tải xuống {url}: {e}")

if __name__ == "__main__":
    # Danh sách các URL ảnh cần tải
    urls = [
"https://content.pancake.vn/1/s751x536/fwebp/cf/cf/28/5f/f9ca08165577556ed2df053b0962a0e8e670490844d7ad5e84fa48b2.png",
"https://content.pancake.vn/1/s751x536/cf/cf/28/5f/f9ca08165577556ed2df053b0962a0e8e670490844d7ad5e84fa48b2.png",

"https://statics.pancake.vn/web-media/35/7a/ab/a5/2bcc8b3414fa20782f68d8d552b13313f2a24e5b267a97b3cf3a5ec3.ttf"]

    # Thư mục lưu ảnh
    save_directory = "C:/Thuchon/thumoi_files"

    # Gọi hàm tải ảnh
    download_images(urls, save_directory)
