document.addEventListener("DOMContentLoaded", function () {
    /*
    This function is only to show date and time on front page
    */
    currentTime();


    let keypad = document.getElementsByClassName("click-nr");

    for (let key of keypad) {
        key.addEventListener("click", function () {
            let clockNumber = key.innerText;
            let clockNumberDiv = document.getElementById("clock-number");
            if (clockNumberDiv.value.length <= 3) {
                clockNumberDiv.value += clockNumber;
            }
        });
    }

    function currentTime() {
        /*
         This is only to show time and
         date on index page.
        */
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
        document.getElementById("time").innerHTML = `Time: ${time} Date: ${currentDate}`;
    }


    if ('NDEFReader' in window) {
        /*
        This function is checking if NDEF is on
        because at this time NFC in browser is 
        suported by Chrome on Android and webview
        only. If is on then we scan for NFC tags
        and decode and send the information in clock
        number input field.
        */
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
            /* 
            Change placeholder to 
            confirm NFC is ready and working.
            */
            document.getElementById("clock-number").placeholder = "NFC READY";
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

    function autoSend() {
        /*
        This function is auto sending the form
        when are 4 caracters in form.
        */
        let text = document.getElementById("clock-number").value;
        if (text.length != 4) {
            console.log(text);
        } else {
            document.getElementById("clock-in-form").submit();
        }
        setTimeout(function () { autoSend(); }, 1000);
    }
    autoSend();
});