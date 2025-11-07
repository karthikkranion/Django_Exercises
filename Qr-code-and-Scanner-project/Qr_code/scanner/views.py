from django.shortcuts import render
from pathlib import Path
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Qrcode
import qrcode #type:ignore
from io import BytesIO
from django.core.files.base import ContentFile
from pyzbar.pyzbar import decode  #type:ignore
from PIL import Image  #type:ignore
import os
# Create your views here.
def generate_qr(request):
    if request.method == 'POST':
        data_name = request.POST.get('qr_data')
        mobile_number = request.POST.get('mobile_number')
        upi_id = request.POST.get('upi_id')

        # validation can be added here
        if not mobile_number.isdigit() or len(mobile_number) < 10:
            return render(request, 'scanner/generate.html')
        
        amount = 0.00  # default amount
        note = f"Payment from {data_name}, Mobile: {mobile_number}"

        # upi link
        data = f"upi://pay?pa={upi_id}&pn=GS Petrol Pump&tn={note}&am={amount}&cu=INR"
        
         # generate qr code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        buffer = BytesIO()
        img.save(buffer)
        filename = f"qr_{mobile_number}.png"
        filebuffer = ContentFile(buffer.getvalue())

       
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # save inside media/
        file_path = fs.save(f'qr_codes/{filename}', filebuffer)  # Django creates qr_codes folder automatically


        Qrcode.objects.create(data=data, mobile_number=mobile_number,upi_id=upi_id)

        return render(request, 'scanner/generate.html', {'file_path': fs.url(file_path),'mobile_number':mobile_number})
    return render(request,'scanner/generate.html')


def scan_qr(request):
    if request.method == 'POST':
        # Handle uploaded QR image
        if request.FILES.get('qr_image'):
            qr_image = request.FILES['qr_image']

            # Save uploaded image temporarily
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save(f'scanned_qr/{qr_image.name}', qr_image)
            file_path = fs.path(filename)

            # Decode the QR image
            decoded_data = decode(Image.open(file_path))
            if decoded_data:
                qr_text = decoded_data[0].data.decode('utf-8')

                try:
                    # Try to find the QR in DB
                    matching_qr = Qrcode.objects.get(data=qr_text)

                    # Delete QR file from media/qr_codes/
                    file_to_delete = os.path.join(settings.MEDIA_ROOT, 'qr_codes', f'qr_{matching_qr.mobile_number}.png')
                    if os.path.exists(file_to_delete):
                        os.remove(file_to_delete)

                    # Delete the DB record
                    matching_qr.delete()

                    message = f"QR code matched and deleted successfully for mobile: {matching_qr.mobile_number}"

                except Qrcode.DoesNotExist:
                    message = "QR code scanned successfully, but not found in database."

                return render(request, 'scanner/scanner.html', {
                    'qr_data': qr_text,
                    'message': message,
                    'qr_list': Qrcode.objects.all()
                })
            else:
                return render(request, 'scanner/scanner.html', {
                    'error': 'No QR code found in the image.'
                })

    # GET request or no file uploaded: show scanner page with all QR codes
    return render(request, 'scanner/scanner.html')
    