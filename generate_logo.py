from PIL import Image, ImageDraw

def generate_logo():
    # Create a 512x512 image with transparency
    size = (512, 512)
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Minimalist Trident/Photography Hybrid
    # Central Spike (Vertical Rectangle)
    draw.rectangle([240, 80, 272, 432], fill="white")
    
    # Curved U-shape base
    draw.arc([100, 140, 412, 380], start=0, end=180, fill="white", width=25)
    
    # Left and Right Spikes
    draw.rectangle([100, 100, 125, 260], fill="white")
    draw.rectangle([387, 100, 412, 260], fill="white")
    
    # Camera Lens Circle (Center)
    draw.ellipse([180, 180, 332, 332], outline="white", width=8)
    draw.ellipse([215, 215, 297, 297], outline="white", width=4)
    
    # Small Dot for Flash/Shutter
    draw.ellipse([280, 120, 295, 135], fill="white")

    # Ensure directories exist
    import os
    os.makedirs("portfolio/static/portfolio/images", exist_ok=True)

    # Save versions
    image.save("portfolio/static/portfolio/images/logo.png")
    image.resize((64, 64), Image.Resampling.LANCZOS).save("portfolio/static/portfolio/images/favicon.png")

if __name__ == "__main__":
    generate_logo()
    print("Logo and Favicon files have been written to portfolio/static/portfolio/images/")
