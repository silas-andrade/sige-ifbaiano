$(document).ready(function () {
    $("#openreader-btn").qrCodeReader({
        target: "#target-input",
        audioFeedback: true,
        multiple: false,
        skipDuplicates: false,
        callback: function (codes) {
            console.log(codes);
        }
    });
});