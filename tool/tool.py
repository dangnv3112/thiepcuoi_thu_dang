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
    input_file_path = "D:/thiep2/thiepcuoilangman/thiep_3.txt"  # Tệp văn bản gốc
    output_file_path = "D:/thiep2/thiepcuoilangman/thiep_4.txt"  # Tệp sau khi thay thế

    # Danh sách thay thế: {từ_cũ: từ_mới}
    replacements_dict = {f">04<":">15<",
f">02<":">Minh Thư<",
f">03<":">11H30<",
f">7<":">1<",
f"Lưu ý : Hiện tại đang có nhiều đơn vị giả mạo , quý khách vui lòng liên hệ trực tiếp qua số hotline 0353.602.165 MS LINH để đảm bảo quyền lợi":"",
f"Bản quyền 08-2022 thuộc về Thiệp cưới điện tử®":""}

    # Gọi hàm để thay thế
    replace_words_in_file(input_file_path, output_file_path, replacements_dict)
