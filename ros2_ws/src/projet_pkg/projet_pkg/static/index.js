var socket = io();

socket.on('etat_data', function(data) {
    document.getElementById('temperature').innerText = data.temperature + "°C";
    document.getElementById('luminosite').innerText = data.luminosite + " lux";
    document.getElementById('presence_exterieur').innerText = data.presence_exterieur ? "Oui" : "Non";
    document.getElementById('presence_interieur').innerText = data.presence_interieur ? "Oui" : "Non";
    document.getElementById('time').innerText = data.time || "00:00";
    document.getElementById('volet').innerText = data.volet;
    document.getElementById('chauffage').innerText = data.chauffage;
    document.getElementById('lumiere').innerText = data.lumiere;
    document.getElementById('buzzer').innerText = data.buzzer;
});

socket.on('update_alarme', function(data) {
    let alarme_Texte = document.getElementById('alarme');
    let alarme_Bouton = document.getElementById('alarme_Bouton');

    if (data.alarme === "ON") {
        alarme_Texte.innerText = "ON";
        alarme_Texte.classList.remove("off");
        alarme_Texte.classList.add("on");
        alarme_Bouton.classList.remove("alarme-off");
        alarme_Bouton.classList.add("alarme-on");
        alarme_Bouton.innerText = "Click pour désactiver l'alarme";
    } else {
        alarme_Texte.innerText = "OFF";
        alarme_Texte.classList.remove("on");
        alarme_Texte.classList.add("off");
        alarme_Bouton.classList.remove("alarme-on");
        alarme_Bouton.classList.add("alarme-off");
        alarme_Bouton.innerText = "Click pour activer l'alarme";
    }
});

function Etat_Alarme() {
    let etat = document.getElementById('alarme').innerText;
    let new_etat = etat === "OFF" ? "ON" : "OFF";
    socket.emit('etat_alarme', { alarme: new_etat });
}
