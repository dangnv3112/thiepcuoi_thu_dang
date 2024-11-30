def replace_words_in_file(input_file, output_file, replacements):
    """
    Đọc tệp văn bản, thay thế các từ dựa trên danh sách thay thế và lưu kết quả vào tệp mới.

    :param input_file: Đường dẫn đến tệp đầu vào (TXT)
    :param output_file: Đường dẫn đến tệp đầu ra (TXT)
    :param replacements: Từ điển {từ_cũ: từ_mới} để thay thế
    """
    try:
        # Đọc nội dung từ tệp đầu vào
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Thay thế các từ dựa trên từ điển replacements
        for old_word, new_word in replacements.items():
            content = content.replace(old_word, new_word)

        # Ghi nội dung đã chỉnh sửa vào tệp đầu ra
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Đã thay thế và lưu kết quả vào: {output_file}")
    except FileNotFoundError:
        print(f"Không tìm thấy tệp: {input_file}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Sử dụng chương trình
if __name__ == "__main__":
    # Đường dẫn tệp đầu vào và đầu ra
    input_file_path = "C:/Thuchon/thumoi.txt"  # Tệp văn bản gốc
    output_file_path = "C:/Thuchon/thumoi_2.txt"  # Tệp sau khi thay thế

    # Danh sách thay thế: {từ_cũ: từ_mới}
    replacements_dict = {f"https://content.pancake.vn/1/s1200x650/fwebp0/e2/56/53/ea/083ac71c09fa5d17a99c036569a096557ac175e3bda2b3257164ab2a.jpg":"thumoi_files/filecuoi/H2H02500.jpg",
f"https://content.pancake.vn/1/s50x50/fwebp/e2/56/53/ea/083ac71c09fa5d17a99c036569a096557ac175e3bda2b3257164ab2a.jpg":"thumoi_files/filecuoi/H2H02500.jpg",
f"https://content.pancake.vn/1/e1/a4/05/bc/e69c5e06a07fd2c7e376992932daca40092236b6edb70082b3f8f707.jpg":"thumoi_files/filecuoi/H2H03258-min.jpg",
f"https://content.pancake.vn/1/bb/cc/63/8c/860fe535b6a6fb3f070ea73fbd1950ae9604352efe58664543e28947.jfif":"thumoi_files/filecuoi/H2H02881.jpg",
f"https://content.pancake.vn/1/39/f0/59/fc/a5ad00bec633af1d30efce36ba7400cce8ac23a0c40a9633b64f94ee.jpg":"thumoi_files/filecuoi/H2H02959.jpg",
f"https://content.pancake.vn/1/s523x584/fwebp/1a/9a/3c/0e/af5cd91e5dfda0749417473da9b042221f89c058732ca4bc6ce5e5c0.jpg":"thumoi_files/filecuoi/H2H03062-min.jpg",
f"https://content.pancake.vn/1/s523x584/fpng/1a/9a/3c/0e/af5cd91e5dfda0749417473da9b042221f89c058732ca4bc6ce5e5c0.jpg":"thumoi_files/filecuoi/H2H03062-min.jpg",
f"https://content.pancake.vn/1/s577x641/fwebp/e1/a4/05/bc/e69c5e06a07fd2c7e376992932daca40092236b6edb70082b3f8f707.jpg":"thumoi_files/filecuoi/H2H03258-min.jpg",
f"https://content.pancake.vn/1/s577x641/fpng/e1/a4/05/bc/e69c5e06a07fd2c7e376992932daca40092236b6edb70082b3f8f707.jpg":"thumoi_files/filecuoi/H2H03258-min.jpg",
f"https://content.pancake.vn/1/s523x584/fwebp/a8/69/4d/25/1bc60326fe7c70a08c922e74d2a5c1347959c7ad9d3f6f987afa6e8c.jpg":"thumoi_files/filecuoi/H2H02726.jpg",
f"https://content.pancake.vn/1/s523x584/fpng/a8/69/4d/25/1bc60326fe7c70a08c922e74d2a5c1347959c7ad9d3f6f987afa6e8c.jpg":"thumoi_files/filecuoi/H2H02726.jpg",
f"https://content.pancake.vn/1/e9/80/6a/05/fcf14d0545da0e656237816d3712c50d2792afda074a96abfd9bcec5.jpg":"thumoi_files/filecuoi/H2H03370-min.jpg",
f"https://content.pancake.vn/1/09/00/8a/b4/692735fdc0775ae1530963a767ce4264df77078f659771a3cde9c5ac.jpg":"thumoi_files/filecuoi/H2H02814.jpg",
f"https://content.pancake.vn/1/s587x681/fwebp/ad/c0/11/16/06080e040619cef49e87d7e06a574eb61310d3dc4bdc9f0fec3638c9.jpg":"thumoi_files/filecuoi/H2H02470.jpg",
f"https://content.pancake.vn/1/s587x681/fpng/ad/c0/11/16/06080e040619cef49e87d7e06a574eb61310d3dc4bdc9f0fec3638c9.jpg":"thumoi_files/filecuoi/H2H02470.jpg",
f"https://content.pancake.vn/1/84/b3/f5/cd/cc7957b9f0e497f01a17d05f9e73406b7650b249c169b424c7ee1767.jpg":"thumoi_files/filecuoi/H2H03119-min.jpg",
f"https://content.pancake.vn/1/s588x526/fwebp/60/b1/5e/e9/89fd2d2d6cd9a62db6e70776243eb9ed8603fc1fb415bdc95da92104.jpg":"thumoi_files/filecuoi/H2H02922.jpg",
f"https://content.pancake.vn/1/s588x526/fpng/60/b1/5e/e9/89fd2d2d6cd9a62db6e70776243eb9ed8603fc1fb415bdc95da92104.jpg":"thumoi_files/filecuoi/H2H02922.jpg",
f"https://content.pancake.vn/1/s648x590/fwebp/7a/e8/d6/f6/da197a5a3542dfe09e7faa9e118999103385582808a2e2014fc72986.jpg":"thumoi_files/filecuoi/H2H03193-min.jpg",
f"https://content.pancake.vn/1/s648x590/fpng/7a/e8/d6/f6/da197a5a3542dfe09e7faa9e118999103385582808a2e2014fc72986.jpg":"thumoi_files/filecuoi/H2H03193-min.jpg",
f"https://content.pancake.vn/1/s587x681/fwebp/9d/60/03/fe/ecbd36b01369b3064a01426c59166451161e648939a52fd952564e21.jpg":"thumoi_files/filecuoi/H2H03281-min.jpg",
f"https://content.pancake.vn/1/s587x681/fpng/9d/60/03/fe/ecbd36b01369b3064a01426c59166451161e648939a52fd952564e21.jpg":"thumoi_files/filecuoi/H2H03281-min.jpg",
f"https://content.pancake.vn/1/s587x681/fwebp/cb/87/1f/67/25cdb38375c4ffc82ea938461257c5fbb49f3407e402f3e6ff903387.jpg":"thumoi_files/filecuoi/H2H02772.jpg",
f"https://content.pancake.vn/1/s587x681/fpng/cb/87/1f/67/25cdb38375c4ffc82ea938461257c5fbb49f3407e402f3e6ff903387.jpg":"thumoi_files/filecuoi/H2H02772.jpg",
f"https://content.pancake.vn/1/s587x681/fwebp/43/f6/88/e6/33fad2e85f20c3cab3d076535139371b0378fccc049b1083efffb1c5.jpg":"thumoi_files/filecuoi/H2H02796.jpg",
f"https://content.pancake.vn/1/s587x681/fpng/43/f6/88/e6/33fad2e85f20c3cab3d076535139371b0378fccc049b1083efffb1c5.jpg":"thumoi_files/filecuoi/H2H02796.jpg",
f"https://content.pancake.vn/1/ad/c0/11/16/06080e040619cef49e87d7e06a574eb61310d3dc4bdc9f0fec3638c9.jpg":"thumoi_files/filecuoi/H2H02470.jpg",
f"https://statics.pancake.vn/web-media/e1/a4/05/bc/e69c5e06a07fd2c7e376992932daca40092236b6edb70082b3f8f707.jpg":"thumoi_files/filecuoi/H2H03258-min.jpg",
f"https://statics.pancake.vn/web-media/bb/cc/63/8c/860fe535b6a6fb3f070ea73fbd1950ae9604352efe58664543e28947.jfif":"thumoi_files/filecuoi/H2H02881.jpg",
f"https://statics.pancake.vn/web-media/39/f0/59/fc/a5ad00bec633af1d30efce36ba7400cce8ac23a0c40a9633b64f94ee.jpg":"thumoi_files/filecuoi/H2H02959.jpg",
f"https://statics.pancake.vn/web-media/1a/9a/3c/0e/af5cd91e5dfda0749417473da9b042221f89c058732ca4bc6ce5e5c0.jpg":"thumoi_files/filecuoi/H2H03062-min.jpg",
f"https://statics.pancake.vn/web-media/a8/69/4d/25/1bc60326fe7c70a08c922e74d2a5c1347959c7ad9d3f6f987afa6e8c.jpg":"thumoi_files/filecuoi/H2H02726.jpg",
f"https://statics.pancake.vn/web-media/e9/80/6a/05/fcf14d0545da0e656237816d3712c50d2792afda074a96abfd9bcec5.jpg":"thumoi_files/filecuoi/H2H03370-min.jpg",
f"https://statics.pancake.vn/web-media/09/00/8a/b4/692735fdc0775ae1530963a767ce4264df77078f659771a3cde9c5ac.jpg":"thumoi_files/filecuoi/H2H02814.jpg",
f"https://statics.pancake.vn/web-media/ad/c0/11/16/06080e040619cef49e87d7e06a574eb61310d3dc4bdc9f0fec3638c9.jpg":"thumoi_files/filecuoi/H2H02470.jpg",
f"https://statics.pancake.vn/web-media/84/b3/f5/cd/cc7957b9f0e497f01a17d05f9e73406b7650b249c169b424c7ee1767.jpg":"thumoi_files/filecuoi/H2H03119-min.jpg",
f"https://statics.pancake.vn/web-media/60/b1/5e/e9/89fd2d2d6cd9a62db6e70776243eb9ed8603fc1fb415bdc95da92104.jpg":"thumoi_files/filecuoi/H2H02922.jpg",
f"https://statics.pancake.vn/web-media/7a/e8/d6/f6/da197a5a3542dfe09e7faa9e118999103385582808a2e2014fc72986.jpg":"thumoi_files/filecuoi/H2H03193-min.jpg",
f"https://statics.pancake.vn/web-media/9d/60/03/fe/ecbd36b01369b3064a01426c59166451161e648939a52fd952564e21.jpg":"thumoi_files/filecuoi/H2H03281-min.jpg",
f"https://statics.pancake.vn/web-media/cb/87/1f/67/25cdb38375c4ffc82ea938461257c5fbb49f3407e402f3e6ff903387.jpg":"thumoi_files/filecuoi/H2H02772.jpg",
f"https://statics.pancake.vn/web-media/43/f6/88/e6/33fad2e85f20c3cab3d076535139371b0378fccc049b1083efffb1c5.jpg":"thumoi_files/filecuoi/H2H02796.jpg"}

    # Gọi hàm để thay thế
    replace_words_in_file(input_file_path, output_file_path, replacements_dict)
