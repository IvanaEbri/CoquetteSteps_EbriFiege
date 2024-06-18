/*----- ULTIMO UPDATE ------ */

/*document.addEventListener("DOMContentLoaded", function() {
    var priceElements = document.getElementsByClassName("product-price");
    for (var i = 0; i < priceElements.length; i++) {
    var priceElement = priceElements[i];
    var price = priceElement.textContent;
    var formattedPrice = formatPrice(price);
    priceElement.textContent = formattedPrice;
    }
});

function formatPrice(price) {
    // Remover el signo de dólar y separar los decimales
    price = price.toString();
    var parts = price.split(".");
    var integerPart = parts[0];
    var decimalPart = parts.length > 1 ? parts[1] : "";

    // Formatear la parte entera con separadores de miles
    integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    
    // Agregar la coma como separador de decimales y el signo de dólar
    return integerPart + "," + decimalPart;
};

// Obtener todos los botones
const botones_talle = document.querySelectorAll('.size-button');

// Función para manejar el click en un botón
function handleClick(event) {
    // Remover la clase 'selected' de todos los botones
    botones_talle.forEach(boton => {
        boton.classList.remove('selected');
    });

    // Agregar la clase 'selected' solo al botón clickeado
    event.target.classList.add('selected');
}

// Asignar el evento 'click' a cada botón
botones_talle.forEach(boton => {
boton.addEventListener('click', handleClick);
});

const addToCartButton = document.getElementById('add-to-cart');

addToCartButton.addEventListener('click', function () {
    const selectedButton = document.querySelector('.size-button.selected');
    if (!selectedButton) {
        alert('Por favor selecciona el talle.');
        return;
    }
    const selectedSize = selectedButton.getAttribute('data-talle');
    addToCart(selectedSize);
});

const selectedButton = document.querySelector('.size-button.selected');

function addToCart(talle) {
    fetch('/agregar_al_carro/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ size: talle })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al añadir al carro');
        }
        return response.json();
    })
    .then(data => {
        console.log('Producto añadido al carro:', data);
        alert('Producto añadido al carro.');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al añadir al carro.' + selectedButton);
    });
}; 
*/

/*----- UPDATE VIEJO ------ */
document.addEventListener("DOMContentLoaded", function () {
    const sizeButtons = document.querySelectorAll('.size-button');
    const addToCartButton = document.getElementById('add-to-cart');
    let selectedSize = null;

    // Manejar clic en botones de tamaño
    sizeButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Remover la clase 'selected' de todos los botones
            sizeButtons.forEach(btn => btn.classList.remove('selected'));
            
            // Agregar la clase 'selected' al botón clickeado
            button.classList.add('selected');
            
            // Obtener el tamaño seleccionado
            selectedSize = button.getAttribute('data-talle');
        });
    });

    // Manejar clic en el botón 'Añadir al carrito'
    addToCartButton.addEventListener('click', function () {
        if (selectedSize) {
            const productId = addToCartButton.getAttribute('data-product-id');

            fetch('/Carrito/agregar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken') // Agregar token CSRF para seguridad
                },
                body: JSON.stringify({
                    product_id: productId,
                    talle: selectedSize
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(`Producto con tamaño ${selectedSize} agregado al carrito`);
                } else {
                    alert(`Error al agregar el producto al carrito: ${data.error}`);
                }
            })
            .catch(error => {
                alert('Hubo un error al procesar la solicitud. Por favor, inténtalo nuevamente.');
            });
        } else {
            alert('Por favor, selecciona un tamaño antes de agregar al carrito');
        }
    });

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
});
