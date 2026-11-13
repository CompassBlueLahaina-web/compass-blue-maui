import sys
from PIL import Image, ImageOps
U="/mnt/user-data/uploads/"; OUT=sys.argv[1]+"/assets/img/"
# name: (file, crop box as fractions l,t,r,b or None)
S={"bed-mountains":("45e0fe96-image.jpg",None),
   "room-lanai":("e57b703d-image.jpg",None),
   "bed-lanai":("32604684-image.jpg",None),
   "room-orchid":("a41af7de-image.jpg",(0,0.02,1,0.68)),   # crop out the binder (unit number + QR code)
   "lanai-mountains":("9e3cc410-image.jpg",(0.06,0.05,0.97,0.9)),
   "lobby-ocean":("84d7465b-image.jpg",None),
   "kitchen":("ec39ae98-image.jpg",None),
   "kitchen-counter":("effc6a98-image.jpg",(0,0,0.86,1)),   # crop out fridge edge with WiFi sign
   "bath-doorknob":("7004da5e-image.jpg",None),
   "shower":("6937f39e-image.jpg",None)}
for n,(f,c) in S.items():
    im=ImageOps.exif_transpose(Image.open(U+f)).convert("RGB")
    if c: w,h=im.size; im=im.crop((int(c[0]*w),int(c[1]*h),int(c[2]*w),int(c[3]*h)))
    for W in (640,1280):
        r=im if im.width<=W else im.resize((W,round(im.height*W/im.width)),Image.LANCZOS)
        r.save(f"{OUT}{n}-{W}.webp","WEBP",quality=76,method=6)
        if W==1280: r.save(f"{OUT}{n}.jpg","JPEG",quality=80,optimize=True,progressive=True); print(n,r.size)
im=ImageOps.exif_transpose(Image.open(U+"45e0fe96-image.jpg")).convert("RGB")
ImageOps.fit(im,(1200,630),Image.LANCZOS,centering=(0.5,0.35)).save(OUT+"share.jpg","JPEG",quality=82,optimize=True)
