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
    var parts = price.split(".");
    var integerPart = parts[0];
    var decimalPart = parts.length > 1 ? parts[1] : "";
  
    // Formatear la parte entera con separadores de miles
    integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  
    // Agregar la coma como separador de decimales y el signo de dólar
    return integerPart + "," + decimalPart;
};

// Obtener todos los botones
const botones = document.querySelectorAll('button');

// Función para manejar el click en un botón
function handleClick(event) {
    // Remover la clase 'selected' de todos los botones
    botones.forEach(boton => {
        boton.classList.remove('selected');
    });

    // Agregar la clase 'selected' solo al botón clickeado
    event.target.classList.add('selected');
    const selectedSize = sizeElement.getAttribute('data-talle');
    console.log('Talle seleccionado:', selectedSize);

}

// Asignar el evento 'click' a cada botón
botones.forEach(boton => {
  boton.addEventListener('click', handleClick);
});