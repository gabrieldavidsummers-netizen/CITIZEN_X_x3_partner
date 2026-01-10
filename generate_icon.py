from PIL import Image
# Create a 512x512 black square (The Calculator "Cloak")
img = Image.new('RGB', (512, 512), color = (0, 0, 0))
img.save('calc_icon.png')
print("--- ICON MANIFESTED ---")
