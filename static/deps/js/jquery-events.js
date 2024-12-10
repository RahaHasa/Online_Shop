$(document).ready(function() {
    $('.add-to-cart-button').on('click', function() {
        const productId = $(this).data('productId');  // Получаем ID товара из data-атрибута
        
        // Отправляем AJAX запрос
        $.ajax({
            url: '/cart/cart_add/', // Путь к представлению для добавления в корзину
            method: 'POST',
            data: {
                product_id: productId,
                csrfmiddlewaretoken: getCookie('csrftoken')  // Отправляем CSRF токен
            },
            success: function(data) {
                console.log(data);
                // Обновляем корзину на странице
                $('.cart-items').html(data.cart_items_html);
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });
});

// Функция для получения CSRF токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$(document).ready(function() {
    $('.add-to-cart-button').on('click', function() {
        const productId = $(this).data('productId');  // Получаем ID товара
        addToCart(productId);  // Вызовем функцию из jquery-ajax.js
    });
});
