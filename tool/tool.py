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
    input_file_path = "D:/thiep2/thiepcuoilangman/index.txt"  # Tệp văn bản gốc
    output_file_path = "D:/thiep2/thiepcuoilangman/index1.txt"  # Tệp sau khi thay thế

    # Danh sách thay thế: {từ_cũ: từ_mới}
    replacements_dict = {f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/2B90752A-19C2-4BC8-A33D-0CCCC6FA32E0-e1705040892710-1024x683.jpeg":"thiep\H2H02500.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/E1688A8E-C5E3-49B3-A5B4-2AF6EB7F6BAF.jpeg":"thiep\H2H02567.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/BEEFADED-A61C-4802-A47C-65450136B451.jpeg":"thiep\H2H02726.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/A91CA144-C1FF-474D-B4D6-F3DAC89B3DB1.jpeg":"thiep\H2H02748.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/680E95E0-8069-44F3-A286-4F8D81C2D425.jpeg":"thiep\H2H02764.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/D6231ABF-3CCB-4FD4-B252-D0505AC48803.jpeg":"thiep\H2H02772.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/0F3691F5-4ACA-48B8-810A-C4D0A766B998-e1705072255839.jpeg":"thiep\H2H02796.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/67369EDA-AB9B-42BA-BB2C-8C1147C31E71.jpeg":"thiep\H2H02881.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/D705C86D-1D18-430C-8ACD-C05F512F302F-e1705073822731.jpeg":"thiep\H2H02922.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/AE583BCD-DFD5-4E52-901D-3A711D5DAA12.jpeg":"thiep\H2H02956.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/FF508208-8C60-4E2D-862A-1E81D79CE9C7-e1705073693356.jpeg":"thiep\H2H02959.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/E6BDD24D-609C-4722-BA61-B7F5213391D8.jpeg":"thiep\H2H03021.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/2B90752A-19C2-4BC8-A33D-0CCCC6FA32E0-e1705040892710.jpeg":"thiep\H2H03048.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/F38950F8-62A2-4FC3-B2FD-5C8B5438114E-e1705040910718.jpeg":"thiep\H2H03062.jpg",
f"https://thiepdientu.com.vn/wp-content/uploads/2024/01/E3F7CC09-A2B0-4F8C-852F-B27DF96A6A9B-e1705040930946.jpeg":"thiep\H2H03074.jpg"}

    # Gọi hàm để thay thế
    replace_words_in_file(input_file_path, output_file_path, replacements_dict)
