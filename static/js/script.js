$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
});

$(document).ready(function () {
    $('input#username, input#password, input#phone_number').characterCounter();
});

$(document).ready(function () {
    $('.fixed-action-btn').floatingActionButton();
});


const ndef = new NDEFReader();

async function startScanning() {
  await ndef.scan();
  ndef.onreading = event => {
    /* handle NDEF messages */
  };
}

const nfcPermissionStatus = await navigator.permissions.query({ name: "nfc" });
if (nfcPermissionStatus.state === "granted") {
  // NFC access was previously granted, so we can start NFC scanning now.
  startScanning();
} else {
  // Show a "scan" button.
  document.querySelector("#scanButton").style.display = "block";
  document.querySelector("#scanButton").onclick = event => {
    // Prompt user to allow UA to send and receive info when they tap NFC devices.
    startScanning();
  };
}