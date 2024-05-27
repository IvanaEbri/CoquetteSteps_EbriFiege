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
  }