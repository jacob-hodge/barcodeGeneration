from PIL import Image, ImageDraw


def words_to_rgb(word1, word2, word3):
    word1 = word1.ljust(10)
    word2 = word2.ljust(10)
    word3 = word3.ljust(10)

    ascii1 = [ord(char) for char in word1]
    ascii2 = [ord(char) for char in word2]
    ascii3 = [ord(char) for char in word3]

    rgb_colors = []
    for i in range(10):
        rgb = (ascii1[i], ascii2[i], ascii3[i])
        rgb_colors.append(rgb)

    return rgb_colors



def draw_concentric_circles(rgb_colors, image_size=800, gap=2, filename="concentric_circles.png"):
    img = Image.new("RGB", (image_size, image_size), "white")
    draw = ImageDraw.Draw(img)

    max_radius = image_size // 2
    radius_step = (max_radius - gap * 10) // 10 

    for i, color in enumerate(rgb_colors):
        outer_radius = max_radius - i * (radius_step + gap)
        inner_radius = outer_radius - gap
        
        top_left_white = (image_size // 2 - outer_radius, image_size // 2 - outer_radius)
        bottom_right_white = (image_size // 2 + outer_radius, image_size // 2 + outer_radius)
        
        draw.ellipse([top_left_white, bottom_right_white], fill="white")

        top_left_color = (image_size // 2 - inner_radius, image_size // 2 - inner_radius)
        bottom_right_color = (image_size // 2 + inner_radius, image_size // 2 + inner_radius)
        
        draw.ellipse([top_left_color, bottom_right_color], fill=color)

    img.save(filename, "PNG")


rgb_colors = words_to_rgb("£1399.00","world6789","testtestte")
draw_concentric_circles(rgb_colors)