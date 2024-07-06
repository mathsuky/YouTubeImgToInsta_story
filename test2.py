from PIL import ImageFont
import os

# フォントディレクトリ
font_dirs = [
    "/Library/Fonts",
    "/System/Library/Fonts",
    os.path.expanduser("~/Library/Fonts")
]

# 日本語フォントを含む可能性があるファイル拡張子
font_extensions = [".ttf", ".otf", ".ttc"]

# 日本語フォントをリストアップ
japanese_fonts = []

for font_dir in font_dirs:
    for root, _, files in os.walk(font_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in font_extensions):
                font_path = os.path.join(root, file)
                try:
                    font = ImageFont.truetype(font_path)
                    # 日本語フォントかどうかを判定するために一部の日本語文字が描画できるかを確認
                    test_string = "日本語"
                    font.getsize(test_string)
                    japanese_fonts.append(font_path)
                except Exception:
                    continue

# 日本語フォントのパスを表示
for font in japanese_fonts:
    print(font)
