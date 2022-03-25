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
if ('NDEFReader' in window) { 
ndef.scan().then(() => {
    console.log("Scan started successfully.");
    ndef.onreadingerror = () => {
        console.log("Cannot read data from the NFC tag. Try another one?");
    };
    ndef.onreading = event => {
        console.log("NDEF message read. ");
        alert(`ndef`)
    };
}).catch(error => {
    console.log(`Error! Scan failed to start: ${error}.`);
});
}