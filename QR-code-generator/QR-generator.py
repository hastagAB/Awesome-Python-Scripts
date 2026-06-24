import qrcode as QR

def create(content, filename):
    img = QR.make(content)
    img.save(filename)
    return f"here is you file saved at {filename}"
   
result = create("Pass any info here", "company.png")#info, filename
print(result)

