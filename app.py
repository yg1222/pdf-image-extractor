import fitz  # PyMuPDF
import io
from PIL import Image

# Open the PDF file
pdf_document = "Scan 3.pdf"
doc = fitz.open(pdf_document)

# Iterate through each page
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    images = page.get_images(full=True)

    # Iterate through the images in each page
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]

        # Convert to PIL Image
        image = Image.open(io.BytesIO(image_bytes))
        image_filename = f"scan3_p{page_num + 1}_image_{img_index + 1}.png"
        
        # Save the image
        image.save(image_filename)
        print(f"Saved {image_filename}")
