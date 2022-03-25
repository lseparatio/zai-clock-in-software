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

  function startScanning(){
      const ndef = new NDEFReader();

      ndef.scan().then(() => {

        ndef.onreadingerror = () => {
           // Could not scan a tag, try another
        };

        ndef.onreading = event => {
          //Scanned a tag successfully
        };

      }).catch(error => {
        /// Something wrong with hardware
      });
  }

}