document.addEventListener("DOMContentLoaded", function () {
    currentTime();
    let buttons = document.getElementsByClassName("click-nr");

    for (let button of buttons) {
        button.addEventListener("click", function () {
            if (this.getAttribute("data-type") === "delete") {
                document.location.reload(true);
            } else {
                let clockNumber = this.getAttribute("data-type");
                let clockNumberDiv = document.getElementById("clock-number");
                clockNumberDiv.value += clockNumber;
            }
        });
    }

    function currentTime() {
        let date = new Date();
        let hh = date.getHours();
        let mm = date.getMinutes();
        let ss = date.getSeconds();
        let dd = date.getDate();
        const month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        let ll = month[date.getMonth()];
        let yy = date.getFullYear();


        hh = (hh < 10) ? "0" + hh : hh;
        mm = (mm < 10) ? "0" + mm : mm;
        ss = (ss < 10) ? "0" + ss : ss;
        dd = (dd < 10) ? "0" + dd : dd;

        let currentDate = dd + " " + ll + " " + yy;
        let time = hh + ":" + mm + ":" + ss;
        setTimeout(function () { currentTime(); }, 1000);
        document.getElementById("time").innerHTML = `Date: ${currentDate} Time: ${time}`;
    }
});

if ('NDEFReader' in window) {
    navigator.permissions.query({ name: "nfc" }).then((nfcStatus) => {
        if (nfcStatus.state === "granted") {
            startScanning();
        } else {
            document.querySelector("#scan").onclick = event => {
                startScanning();
            };
        }
    });

    function startScanning() {
        const ndef = new NDEFReader();
        ndef.scan().then(() => {
            ndef.onreadingerror = () => {
            };
            ndef.onreading = event => {
                const message = event.message;
                for (const record of message.records) {
                    if (record.recordType == "text") {
                        const textDecoder = new TextDecoder(record.encoding);
                        document.getElementById("clock-number").value = textDecoder.decode(record.data);
                    }
                }
            };
        }).catch(error => {
            console.log(`Error! Scan failed to start: ${error}.`);
        });
    }
}