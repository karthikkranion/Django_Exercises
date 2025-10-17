from django.shortcuts import render

# Create your views here.
def home(request):
    foods = [
        {
            'name': 'Spicy Chicken Biryani',
            'text': 'Aromatic basmati rice layered with tender chicken and bold spices, slow-cooked to perfection.',
            'price': 12.99,
            'image': 'https://pipingpotcurry.com/wp-content/uploads/2024/04/Chicken-Biryani-Piping-Pot-Curry.jpg'
        },
        {
            'name': 'Crispy Masala Dosa',
            'text': 'Golden crispy dosa filled with spiced potato mash, served with chutneys and hot sambar.',
            'price': 30.80,
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPRKGeMstIZbp32iyiVk8FtraGv4UhEoJ1fg&s'
        },
        {
            'name': 'Butter Chicken',
            'text': 'Tender chicken pieces simmered in a rich and creamy tomato-based sauce with butter and spices.',
            'price': 40.99,
            'image': 'https://i.pinimg.com/originals/b1/6e/0a/b16e0a64fb1c4c6feba0d4c93477042c.jpg'
        }
      
    ]
    return render(request, 'core/home.html', {'foods': foods})

def menu(request):
    menu_items = [
        {   'name': 'Spicy Chicken Biryani', 'description': 'Aromatic basmati rice layered with tender chicken and bold spices, slow-cooked to perfection.', 'price': 12.99, 'image': 'https://pipingpotcurry.com/wp-content/uploads/2024/04/Chicken-Biryani-Piping-Pot-Curry.jpg'},
        {   'name': 'Crispy Masala Dosa', 'description': 'Golden crispy dosa filled with spiced potato mash, served with chutneys and hot sambar.', 'price': 30.80, 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPRKGeMstIZbp32iyiVk8FtraGv4UhEoJ1fg&s'},
        {   'name': 'Butter Chicken', 'description': 'Tender chicken pieces simmered in a rich and creamy tomato-based sauce with butter and spices.', 'price': 40.99, 'image': 'https://i.pinimg.com/originals/b1/6e/0a/b16e0a64fb1c4c6feba0d4c93477042c.jpg'},
        {   'name': 'Paneer Tikka', 'description': 'Chunks of paneer marinated in yogurt and spices, grilled to perfection.', 'price': 25.50, 'image': 'https://tse2.mm.bing.net/th/id/OIP.DH0KMPXHqWYW28hEc7OXLQHaE8?pid=Api&P=0&h=220'},
        {   'name': 'Lamb Rogan Josh', 'description': 'Succulent lamb pieces cooked in a rich and aromatic curry sauce.', 'price': 45.00, 'image': 'https://img.freepik.com/premium-photo/lamb-rogan-josh-indian-food_198067-360919.jpg'},
        {   'name': 'Vegetable Biryani', 'description': 'Fragrant   basmati rice cooked with mixed vegetables and spices.', 'price': 20.00, 'image': 'https://www.madhuseverydayindian.com/wp-content/uploads/2022/11/easy-vegetable-biryani.jpg'},
        {   'name': 'Chicken Tikka Masala', 'description': 'Grilled chicken pieces in a creamy tomato sauce.', 'price': 35.00, 'image': 'https://149433378.v2.pressablecdn.com/wp-content/uploads/2020/08/Chicken-Tikka-Masala-scaled.jpg'},
        {   'name': 'Aloo Gobi', 'description': 'A dry curry  made with potatoes and cauliflower.', 'price': 18.00, 'image': 'https://www.cookwithmanali.com/wp-content/uploads/2014/09/Aloo-Gobi-.jpg'},
        {   'name': 'Naan Bread', 'description': 'Soft and fluffy Indian bread.', 'price': 5.00, 'image': 'https://tse2.mm.bing.net/th/id/OIP.-3ASxu90N4jqHVb6tUcvSAHaHI?pid=Api&P=0&h=220'},]
    return render(request, 'core/menu.html',{'menu_items': menu_items }) # type: ignore

def tracking(request):
    return render(request, 'core/tracking.html')    

def reservation(request):       
    return render(request, 'core/reservation.html')

def contact(request):   
    return render(request, 'core/contact.html') 

def cart_view(request):
    cart_items = [
        {
            'name': 'Paneer Tikka',
            'price': 25.50,
            'image': 'https://tse2.mm.bing.net/th/id/OIP.DH0KMPXHqWYW28hEc7OXLQHaE8?pid=Api&P=0&h=220'
        },
        {
            'name': 'Butter Chicken',
            'price': 40.99,
            'image': 'https://i.pinimg.com/originals/b1/6e/0a/b16e0a64fb1c4c6feba0d4c93477042c.jpg'
        }
    ]
    return render(request, 'core/cart.html', {'cart_items': cart_items})