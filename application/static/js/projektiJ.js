function dergoMesazhin() {
    var emri = document.getElementById("emri").value;
    var mbiemer = document.getElementById("mbiemer").value;
    var email = document.getElementById("email").value;
    var numer = document.getElementById("numer").value;
    var mesazhi = document.getElementById("mesazhi").value;
    var msg = document.getElementById("msg");
    if (emri.length > 0 && mbiemer.length > 0 && email.length > 0 && numer.length > 0 && mesazhi.length > 0) {
        msg.innerHTML = "Mesazhi u dergua me suksese"
        msg.style.background="green";
    }
    else {
        msg.innerHTML = "Ju lutem plotesoni fushat!"
        msg.style.background="red";
    }
}

