document.addEventListener("DOMContentLoaded", function() {
    currentTime()
    let buttons = document.getElementsByClassName("click_nr");

    for (let button of buttons) {
        button.addEventListener("click", function() {
            if (this.getAttribute("data-type") === "delete") {
                document.location.reload(true)
            } else {
                let clockNumber = this.getAttribute("data-type");
                let clockNumberDiv =  document.getElementById("clock_number");
                clockNumberDiv.innerText += clockNumber              
            }
        });
    }

function currentTime() {
    let date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();
    let dd = date.getDay();
    let ll = date.getMonth();
    let yy = date.getFullYear();


    hh = (hh < 10) ? "0" + hh : hh;
    mm = (mm < 10) ? "0" + mm : mm;
    ss = (ss < 10) ? "0" + ss : ss;
    dd = (dd < 10) ? "0" + dd : dd;
    ll = (ll < 10) ? "0" + ll : ll;

    let currentDate = dd + ":" + ll + ":" + yy;
    let time = hh + ":" + mm + ":" + ss;

    document.getElementById("time").innerHTML = `Date: ${currentDate} Time: ${time}`;
    var t = setTimeout(function () { currentTime() }, 1000);

}
})