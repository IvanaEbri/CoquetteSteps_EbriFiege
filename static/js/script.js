/*----- ANDA ------ */
document.addEventListener("DOMContentLoaded", function () {
    const sizeButtons = document.querySelectorAll('.size-button');
    const addToCartButton = document.getElementById('add-to-cart');
    const removeFromCartButtons = document.querySelectorAll('.remove-from-cart');
    let selectedSize = null;

    sizeButtons.forEach(button => {
        button.addEventListener('click', function () {
            sizeButtons.forEach(btn => btn.classList.remove('selected'));
            button.classList.add('selected');
            selectedSize = button.getAttribute('data-talle');
        });
    });

    if (addToCartButton) {
        addToCartButton.addEventListener('click', function () {
            if (selectedSize) {
                const productId = addToCartButton.getAttribute('data-product-id');

                fetch('/Cart/agregar/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
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
                        actualizarCarrito(data.cant_prduct, data.total_compra);
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
    }

    removeFromCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            const itemId = button.getAttribute('data-item-id');

            fetch('/Cart/eliminar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    item_id: itemId
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById(`cart-item-${itemId}`).remove();
                    actualizarCarrito(data.cant_prduct, data.total_compra);
                } else {
                    alert(`Error al eliminar el producto del carrito: ${data.error}`);
                }
            })
            .catch(error => {
                alert('Hubo un error al procesar la solicitud. Por favor, inténtalo nuevamente.');
            });
        });
    });

    function actualizarCarrito(cantidadProductos, totalCompra) {
        document.querySelector('.cart').textContent = `🛒 ${cantidadProductos}`;
        const totalElement = document.getElementById('total-compra');
        if (totalElement) {
            totalElement.textContent = `$ ${totalCompra}`;
        }
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; cookies.length > i; i++) {
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
