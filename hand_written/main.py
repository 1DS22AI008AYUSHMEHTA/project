from PIL import Image, ImageDraw, ImageFont

# Load handwriting font (make sure the font file is in your project folder)
font_path = "handwriting.ttf"  # Replace with your actual font filename
font_size = 24

# Prepare the text
text = """Python is a high-level, interpreted programming language known for its simplicity and readability.
It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
Python is widely used in web development, data science, AI, automation, and more.
It has a large standard library and a strong community that contributes to many third-party packages.
Being open-source and cross-platform, Python is accessible and popular among beginners and professionals alike."""

# Create a blank image
img = Image.new('RGB', (1000, 600), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Draw text (wrap manually)
x, y = 50, 50
for line in text.split('\n'):
    draw.text((x, y), line, font=font, fill=(255, 0, 0))
    y += font_size + 10

# Save the image
img.save("demo.png")
print("Text Converted to Handwriting Style Image")
