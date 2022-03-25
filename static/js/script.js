$(document).ready(function () {
  $('.sidenav').sidenav({ edge: "right" });
});

$(document).ready(function () {
  $('input#username, input#password, input#phone_number').characterCounter();
});

$(document).ready(function () {
  $('.fixed-action-btn').floatingActionButton();
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
          console.log("Record type:  " + record.recordType);
          console.log("MIME type:    " + record.mediaType);
          console.log("Record id:    " + record.id);
          if (record.recordType == "text") {

            const textDecoder = new TextDecoder(record.encoding);
            let code = textDecoder.decode(record.data);
            console.log(code);

          }
        }
      };

    }).catch(error => {
      /// Something wrong with hardware
    });
  }

}