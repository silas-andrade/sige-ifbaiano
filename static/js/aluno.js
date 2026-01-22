function onScanSuccess(decodedText) {
    fetch("/refectory/aluno/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
            token: decodedText
        })
    })
        .then(res => res.json())
        .then(data => {
            const r = document.getElementById("resultado");

            if (!data.erro) {
                r.innerHTML = `
                    <p>Sua ficha é: <b>${data.ficha}</b></p>
                    <div id="qrcode"></div>
                `;

                new QRCode(document.getElementById("qrcode"), {
                    text: data.token,
                    width: 200,
                    height: 200
                });
            }
        });
}

document.addEventListener("DOMContentLoaded", () => {
    new Html5Qrcode("reader").start(
        { facingMode: "environment" },
        { fps: 10, qrbox: 250 },
        onScanSuccess
    );
});

/* CSRF padrão Django */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}