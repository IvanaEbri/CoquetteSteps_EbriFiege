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
    // Get all product price elements with class "product-price"
    var priceElements = document.getElementsByClassName("product-price");

    // Loop through each price element
    for (var i = 0; i < priceElements.length; i++) {
    var priceElement = priceElements[i];

      // Extract the price text content
      var price = priceElement.textContent.trim(); // Remove leading/trailing whitespace

      // Format the price using the formatPrice function
    var formattedPrice = formatPrice(price);

      // Update the price element's text content with the formatted price
    priceElement.textContent = formattedPrice;
    }
});

function formatPrice(price) {
    // Convert price to a string and split on decimal point
    price = price.toString().split(".");

    // Extract integer and decimal parts (handling missing decimal)
    var integerPart = price[0];
    var decimalPart = (price.length > 1) ? price[1] : "";

    // Format the integer part with thousands separators
    integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, ".");

    // Ensure at least two decimal places (add leading zeros if needed)
    // if (decimalPart=="") {
    //    decimalPart= decimalPart.padStart(2, "0")
    // };
    

    // Combine formatted parts with comma and dollar sign
    return `${integerPart}${decimalPart}`;
}

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
            console.log(`Agregando producto con tamaño ${selectedSize} al carrito`);
            
            // Aquí iría tu lógica para agregar el producto al carrito, por ejemplo, enviar una solicitud al servidor
            // Simularemos una alerta por ahora
            alert(`Producto con tamaño ${selectedSize} agregado al carrito`);
        } else {
            alert('Por favor, selecciona un tamaño antes de agregar al carrito');
        }
    });
});
    