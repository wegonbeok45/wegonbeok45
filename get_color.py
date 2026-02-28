import sys
from PIL import Image
import collections

try:
    img = Image.open('C:/Users/ta/Desktop/Profile/d8f3815be820ec3a5fb8f8b902fcabc3 (1).gif')
    img = img.convert('RGB')
    
    # Get colors from the edges of the first frame (likely the background)
    width, height = img.size
    edges = []
    for x in range(width):
        edges.append(img.getpixel((x, 0)))
        edges.append(img.getpixel((x, height - 1)))
    for y in range(height):
        edges.append(img.getpixel((0, y)))
        edges.append(img.getpixel((width - 1, y)))
        
    counts = collections.Counter(edges)
    dominant_color = counts.most_common(1)[0][0]
    
    hex_color = "{:02x}{:02x}{:02x}".format(*dominant_color)
    print("DOMINANT_HEX:", hex_color)
except Exception as e:
    print("ERROR:", str(e))
