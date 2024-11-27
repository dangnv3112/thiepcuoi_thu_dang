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
"http-equiv=",
"https://www.ewedinvite.site/MAU6",
"https://content.pancake.vn/1/s1200x650/fwebp0/a6/39/08/bc/35712a53574988edf5fca8aa7529729e5ab64d9ee712afc33acccca3.jpg",
"https://content.pancake.vn/1/s50x50/fwebp/a6/39/08/bc/35712a53574988edf5fca8aa7529729e5ab64d9ee712afc33acccca3.jpg",
"https://statics.pancake.vn/",
"https://content.pancake.vn/",
"https://www.youtube.com/",
"https://a.pancake.vn/",
"https://fonts.gstatic.com/",
"https://fonts.googleapis.com/",
"https://analytics.tiktok.com/i18n/pixel",
"https://analytics.tiktok.com/api/v2/pixel",
"https://content.pancake.vn/1.1/30/5a/c2/93/9ec72c8ce8898050035dddbb989c950bc1faabdc1fdcc11175dea467.svg",
"https://content.pancake.vn/1/s751x536/fwebp/cf/cf/28/5f/f9ca08165577556ed2df053b0962a0e8e670490844d7ad5e84fa48b2.png",
"https://content.pancake.vn/1/s840x1600/fwebp/65/3c/aa/be/35e135afc2c6420bc52abd8fb3768c346420d9efa7b879cd959ee353.png",
"https://maps.app.goo.gl/FpsRtbAQ3wuRroTm7",
":{",
"https://content.pancake.vn/1.1/30/5a/c2/93/9ec72c8ce8898050035dddbb989c950bc1faabdc1fdcc11175dea467.svg",
"https://content.pancake.vn/1/26/8c/55/23/de09d48410d6f6f2cc07965e1a293a7ca313c080e6ee4ce88ebc760e.jfif",
"https://content.pancake.vn/1/s840x1600/fwebp/59/c7/94/c5/6ff8a40c1cd9da9f4a1fcff2c4e3b0cd69532ec524e163ade46635bd.png",
"https://content.pancake.vn/1/s840x1600/59/c7/94/c5/6ff8a40c1cd9da9f4a1fcff2c4e3b0cd69532ec524e163ade46635bd.png",
"https://content.pancake.vn/1/s614x780/41/c3/9d/8e/aefaab9d606661c0e01d89fd8435e35a176148b3f965ae93ffba5a6b.jfif",
"https://content.pancake.vn/1/s613x722/0e/84/4c/53/9e6cdb71870eddfacc95058f441828e10413e6bb63c84cfdb4815abe.jfif",
"https://content.pancake.vn/1/s765x473/fwebp0/f0/f0/71/0f/57b9229829e5627838e139a18bc1eb03f448aa1f1e23cb0533f4f940.png",
"https://content.pancake.vn/1/s765x473/f0/f0/71/0f/57b9229829e5627838e139a18bc1eb03f448aa1f1e23cb0533f4f940.png",
"https://content.pancake.vn/1/s545x593/fwebp/21/54/83/cb/163b4872b6600196d0ac068b1f046c5dd5f9d20c3ddad5e7c0abea9b.jfif",
"https://content.pancake.vn/1/s545x593/21/54/83/cb/163b4872b6600196d0ac068b1f046c5dd5f9d20c3ddad5e7c0abea9b.jfif",
"https://content.pancake.vn/1/s589x652/fwebp/7e/af/79/6c/77ae75d44fc77c376aef27a7dc67f249917e3045d30ca6f8f7cbd59e.jfif",
"https://content.pancake.vn/1/s589x652/7e/af/79/6c/77ae75d44fc77c376aef27a7dc67f249917e3045d30ca6f8f7cbd59e.jfif",
"https://content.pancake.vn/1/s543x590/fwebp/a6/98/f7/28/025c625e8b2f2f7b9a825661cbd04e6a394ea4851b61288679daae4a.jfif",
"https://content.pancake.vn/1/s543x590/a6/98/f7/28/025c625e8b2f2f7b9a825661cbd04e6a394ea4851b61288679daae4a.jfif",
"https://content.pancake.vn/1/s751x441/fwebp/9e/15/98/a2/3bb0491db823fcff403c522e0cec401b55262eba10b022861fe5f666.png",
"https://content.pancake.vn/1/s751x441/9e/15/98/a2/3bb0491db823fcff403c522e0cec401b55262eba10b022861fe5f666.png",
"https://content.pancake.vn/1/s841x1601/fwebp/c2/09/96/ab/ba31a7a6826987143735240f66694cfbcfe8e3126fbe65302171ccee.png",
"https://content.pancake.vn/1/s841x1601/c2/09/96/ab/ba31a7a6826987143735240f66694cfbcfe8e3126fbe65302171ccee.png",
"https://content.pancake.vn/1/s799x1521/fwebp/67/95/92/10/934a1bd7382d5bc78753f7e3e2731c0e18af93e6b523305962612921.png",
"https://content.pancake.vn/1/s799x1521/67/95/92/10/934a1bd7382d5bc78753f7e3e2731c0e18af93e6b523305962612921.png",
"https://content.pancake.vn/1/s482x482/fwebp/75/f1/20/e0/16292656646d6defe01bbe7ad882b99ca1cacabcb8eb31e581e8ac33.webp",
"https://content.pancake.vn/1/s482x482/fpng/75/f1/20/e0/16292656646d6defe01bbe7ad882b99ca1cacabcb8eb31e581e8ac33.webp",
"https://content.pancake.vn/1/s986x116/fwebp/36/24/be/d8/f903790cf58b5fdd4e2e4337bf68628618b6921c7e68d8514654896a.png",
"https://content.pancake.vn/1/s986x116/36/24/be/d8/f903790cf58b5fdd4e2e4337bf68628618b6921c7e68d8514654896a.png",
"https://content.pancake.vn/1/a8/9b/6c/0c/a9f3ee5224c4a1bdffb7910ece5b41c4b1342789387a87c769bf8ad1.jfif",
"https://content.pancake.vn/1/e2/8c/c5/37/905dccbcd5bc1c1b602c10c95acb9986765f735e075bff1097e7f457.jfif",
"https://content.pancake.vn/1/s611x680/fwebp/f9/72/5a/88/fe8e5d85b0fd5c6775e6523462143e2e73a27455844895a07e2b0f55.jfif",
"https://content.pancake.vn/1/s611x680/f9/72/5a/88/fe8e5d85b0fd5c6775e6523462143e2e73a27455844895a07e2b0f55.jfif",
"https://content.pancake.vn/1/s588x650/fwebp/eb/5b/c4/50/98fec609d98e091e56d5f5c44bbb921a8bdcc671f0315c18a84312e7.jfif",
"https://content.pancake.vn/1/s588x650/eb/5b/c4/50/98fec609d98e091e56d5f5c44bbb921a8bdcc671f0315c18a84312e7.jfif",
"https://content.pancake.vn/1/s588x650/fwebp/7d/3b/45/ec/77144bdb3c342f00f15e32408dcd10d6866d82475da0f905885040ef.jfif",
"https://content.pancake.vn/1/s588x650/7d/3b/45/ec/77144bdb3c342f00f15e32408dcd10d6866d82475da0f905885040ef.jfif",
"https://content.pancake.vn/1/s624x698/fwebp/a6/98/f7/28/025c625e8b2f2f7b9a825661cbd04e6a394ea4851b61288679daae4a.jfif",
"https://content.pancake.vn/1/s624x698/a6/98/f7/28/025c625e8b2f2f7b9a825661cbd04e6a394ea4851b61288679daae4a.jfif",
"https://content.pancake.vn/1/s601x702/fwebp/26/8c/55/23/de09d48410d6f6f2cc07965e1a293a7ca313c080e6ee4ce88ebc760e.jfif",
"https://content.pancake.vn/1/s601x702/26/8c/55/23/de09d48410d6f6f2cc07965e1a293a7ca313c080e6ee4ce88ebc760e.jfif",
"https://content.pancake.vn/1/s622x695/fwebp/e2/8c/c5/37/905dccbcd5bc1c1b602c10c95acb9986765f735e075bff1097e7f457.jfif",
"https://content.pancake.vn/1/s622x695/e2/8c/c5/37/905dccbcd5bc1c1b602c10c95acb9986765f735e075bff1097e7f457.jfif",
"https://content.pancake.vn/1/a6/98/f7/28/025c625e8b2f2f7b9a825661cbd04e6a394ea4851b61288679daae4a.jfif",
"https://content.pancake.vn/1/s782x548/fwebp/cf/cf/28/5f/f9ca08165577556ed2df053b0962a0e8e670490844d7ad5e84fa48b2.png",
"https://content.pancake.vn/1/s782x548/cf/cf/28/5f/f9ca08165577556ed2df053b0962a0e8e670490844d7ad5e84fa48b2.png",
"https://statics.pancake.vn/web-media/45/76/a0/59/89970ab18480eeed952d05128f6abc65fe7c0cac3c8d09c86725daf6.jpg)",
"https://content.pancake.vn/1/s751x536/cf/cf/28/5f/f9ca08165577556ed2df053b0962a0e8e670490844d7ad5e84fa48b2.png",
"https://statics.pancake.vn/web-media/f5/f1/41/aa/b6a0dd0c2a8cc07c0be70e066410a2cb9506e4ae9a3d88a8e238b53c.otf",
"https://statics.pancake.vn/web-media/65/48/68/4f/ca5a0c732f276b6fef504eddf0e2d6cdf65cf198b0440dde6d90c5a8.ttf",
"https://statics.pancake.vn/web-media/35/7a/ab/a5/2bcc8b3414fa20782f68d8d552b13313f2a24e5b267a97b3cf3a5ec3.ttf",
"https://statics.pancake.vn/web-media/04/eb/01/7a/e19221a44fabb6fd54c6339fd43b1c25ebbe20e97f6633beed4cbc79.ttf",
"https://content.pancake.vn/1/4b/52/7f/e7/666682ecfee619a3451cf2566aba653946dc13bfe52f47456f186874.png",
"https://statics.pancake.vn/web-media/41/c3/9d/8e/aefaab9d606661c0e01d89fd8435e35a176148b3f965ae93ffba5a6b.jfif",
"https://statics.pancake.vn/web-media/9e/15/98/a2/3bb0491db823fcff403c522e0cec401b55262eba10b022861fe5f666.png",
"https://statics.pancake.vn/web-media/67/95/92/10/934a1bd7382d5bc78753f7e3e2731c0e18af93e6b523305962612921.png",
"https://content.pancake.vn/1/d8/88/b5/1f/ce7bea1db3f2c535a89a2c99988aeba8d3a361b2c72c9d08950d10e7.svg",
"https://statics.pancake.vn/web-media/26/8c/55/23/de09d48410d6f6f2cc07965e1a293a7ca313c080e6ee4ce88ebc760e.jfif",
"https://statics.pancake.vn/web-media/59/c7/94/c5/6ff8a40c1cd9da9f4a1fcff2c4e3b0cd69532ec524e163ade46635bd.png",
"https://statics.pancake.vn/web-media/0e/84/4c/53/9e6cdb71870eddfacc95058f441828e10413e6bb63c84cfdb4815abe.jfif",
"https://statics.pancake.vn/web-media/f0/f0/71/0f/57b9229829e5627838e139a18bc1eb03f448aa1f1e23cb0533f4f940.png",
"https://statics.pancake.vn/web-media/21/54/83/cb/163b4872b6600196d0ac068b1f046c5dd5f9d20c3ddad5e7c0abea9b.jfif",
"https://statics.pancake.vn/web-media/7e/af/79/6c/77ae75d44fc77c376aef27a7dc67f249917e3045d30ca6f8f7cbd59e.jfif",
"https://statics.pancake.vn/web-media/a6/98/f7/28/025c625e8b2f2f7b9a825661cbd04e6a394ea4851b61288679daae4a.jfif",
"https://statics.pancake.vn/web-media/c2/09/96/ab/ba31a7a6826987143735240f66694cfbcfe8e3126fbe65302171ccee.png",
"https://statics.pancake.vn/web-media/75/f1/20/e0/16292656646d6defe01bbe7ad882b99ca1cacabcb8eb31e581e8ac33.webp",
"https://maps.app.goo.gl/jYkYBLCdjSPP6mtu8",
"https://statics.pancake.vn/web-media/36/24/be/d8/f903790cf58b5fdd4e2e4337bf68628618b6921c7e68d8514654896a.png",
"https://statics.pancake.vn/web-media/a8/9b/6c/0c/a9f3ee5224c4a1bdffb7910ece5b41c4b1342789387a87c769bf8ad1.jfif",
"https://statics.pancake.vn/web-media/e2/8c/c5/37/905dccbcd5bc1c1b602c10c95acb9986765f735e075bff1097e7f457.jfif",
"https://statics.pancake.vn/web-media/f9/72/5a/88/fe8e5d85b0fd5c6775e6523462143e2e73a27455844895a07e2b0f55.jfif",
"https://statics.pancake.vn/web-media/eb/5b/c4/50/98fec609d98e091e56d5f5c44bbb921a8bdcc671f0315c18a84312e7.jfif",
"https://statics.pancake.vn/web-media/7d/3b/45/ec/77144bdb3c342f00f15e32408dcd10d6866d82475da0f905885040ef.jfif",
"https://statics.pancake.vn/web-media/cf/cf/28/5f/f9ca08165577556ed2df053b0962a0e8e670490844d7ad5e84fa48b2.png",
"https://statics.pancake.vn/web-media/45/76/a0/59/89970ab18480eeed952d05128f6abc65fe7c0cac3c8d09c86725daf6.jpg"
    ]

    # Thư mục lưu ảnh
    save_directory = "C:/thiepcuoi_new_2/thiepmoi_files"

    # Gọi hàm tải ảnh
    download_images(urls, save_directory)
