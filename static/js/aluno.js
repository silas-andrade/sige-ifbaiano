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

                if (data.erro) {
                    r.innerText = data.erro;
                    r.className = "resultado erro";
                    return;
                }

                r.innerHTML = `
                <p>Sua ficha é: <b>${data.ficha}</b></p>
                <p>Apresente este QR Code ao guarda</p>
                <div id="qrcode"></div>
            `;

                new QRCode(document.getElementById("qrcode"), {
                    text: data.token,
                    width: 200,
                    height: 200
                });
            });
    }

    new Html5Qrcode("reader").start(
        { facingMode: "environment" },
        { fps: 10, qrbox: 250 },
        onScanSuccess
    );
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        for (let cookie of document.cookie.split(";")) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}