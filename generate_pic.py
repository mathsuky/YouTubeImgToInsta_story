from PIL import Image, ImageDraw, ImageFont
import textwrap


def wrap_text(text, font, max_width):
    lines = []
    words = text.split()
    while words:
        line = ""
        while words and font.getbbox(line + words[0])[2] <= max_width:
            line += (words.pop(0) + ' ')
        lines.append(line)
    return lines


def generate_pic(thumbnail_path, title, channel_name):
    width = 500
    height = 888

    base_img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(base_img)

    thumbnail_img = Image.open(thumbnail_path)
    thumbnail_width, thumbnail_height = thumbnail_img.size

    x = (width - thumbnail_width) // 2
    y = (height - thumbnail_height) // 2 - 150
    font = ImageFont.truetype('ヒラギノ丸ゴ ProN W4.ttc', 24)

    black_back = Image.new('RGB', (480, 500), color='black')

    base_img.paste(black_back, (x, y))
    base_img.paste(thumbnail_img, (x, y))
    y_offset = 0
    wrapped_title = wrap_text(title, font, 460)
    for line in wrapped_title:
        draw.text((x + 10, y + 150 + 200 + y_offset),
                  line, font=font, fill='white')
        y_offset += font.getbbox(line)[3] + 5
    draw.text((x + 10, y + 150 + 200 + 35 + y_offset),
              channel_name, font=font, fill='white')

    file_name = 'insta_story.png'
    base_img.save(file_name)
