function generateToken() {
    fetch("/refectory/aluno/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
            token: "ALMOCO2026"
        })
    })
        .then(res => res.json())
        .then(data => {
            if (data.erro) {
                showNotification(data.erro);
                return;
            }

            // Número da ficha
            elTokenNumber.innerText = data.ficha;
            elQueueNumber.innerText = data.ficha;
            elEstTime.innerText = Math.max(1, Math.floor(data.ficha / 10));

            // Gerar QR Code
            elQrImage.src =
                "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=" +
                encodeURIComponent(data.ficha);

            // UI
            elNoToken.classList.add("hidden");
            elHasToken.classList.remove("hidden");
            elStatusBadge.classList.remove("hidden");

            showNotification("Ficha gerada com sucesso!");
        })
        .catch(() => {
            showNotification("Erro ao gerar ficha");
        });
}

document.addEventListener("DOMContentLoaded", () => {

    const elNoToken = document.getElementById('state-no-token');
    const elHasToken = document.getElementById('state-has-token');
    const elTokenNumber = document.getElementById('token-number');
    const elQrImage = document.getElementById('qr-image');
    const elQueueNumber = document.getElementById('queue-number');
    const elEstTime = document.getElementById('est-time');
    const elStatusBadge = document.getElementById('status-badge');
    const elNotification = document.getElementById('notification');

    window.generateToken = function () {
        fetch("/refectory/aluno/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                token: "ALMOCO2026"
            })
        })
            .then(res => res.json())
            .then(data => {
                if (data.erro) {
                    showNotification(data.erro);
                    return;
                }

                elTokenNumber.innerText = data.ficha;
                elQueueNumber.innerText = data.ficha;
                elEstTime.innerText = Math.max(1, Math.floor(data.ficha / 10));

                elQrImage.src =
                    "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=" +
                    encodeURIComponent(data.ficha);

                elNoToken.classList.add("hidden");
                elHasToken.classList.remove("hidden");
                elStatusBadge.classList.remove("hidden");

                showNotification("Ficha gerada com sucesso!");
            })
            .catch(() => {
                showNotification("Erro ao gerar ficha");
            });
    };

    function showNotification(msg) {
        elNotification.textContent = msg;
        elNotification.classList.remove('hidden');
        setTimeout(() => {
            elNotification.classList.add('hidden');
        }, 3000);
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});


// Função CSRF (OBRIGATÓRIA)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
