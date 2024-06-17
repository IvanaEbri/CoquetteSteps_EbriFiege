document.addEventListener("DOMContentLoaded", function() {
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
