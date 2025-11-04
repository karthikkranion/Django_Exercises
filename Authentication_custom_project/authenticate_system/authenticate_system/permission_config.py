from product.models import Product

PERMISSION_CONFIG ={
    'customer':{
        Product:['view'],
    },
    'seller':{
        Product:['view','change','add'],
    }
}