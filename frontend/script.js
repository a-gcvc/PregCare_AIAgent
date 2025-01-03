document.getElementById('predict-button').addEventListener('click', () => {
    const data = getFormData();
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = `${data.prediction}`;
        })
        .catch(error => console.error('Greška prilikom predikcije:', error));
});

document.getElementById('add-data-button').addEventListener('click', () => {
    const data = getFormData();
    fetch('http://127.0.0.1:5000/add-data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => console.error('Greška prilikom dodavanja podataka:', error));
});

function getFormData() {
    return {
        Godine: parseInt(document.getElementById('godine').value),
        GornjiKrvniiPritisak: parseInt(document.getElementById('gornjiPritisak').value),
        DonjiKrvniPritisak: parseInt(document.getElementById('donjiPritisak').value),
        KoncentracijaGlukoze: parseFloat(document.getElementById('glukoza').value),
        TempTijela: parseFloat(document.getElementById('tempTijela').value),
        OtkucajiSrca: parseInt(document.getElementById('otkucajiSrca').value),
    };
}

function ocistiFormu(){
    document.getElementById('godine').value="";
    document.getElementById('gornjiPritisak').value="";
    document.getElementById('donjiPritisak').value="";
    document.getElementById('glukoza').value="";
    document.getElementById('tempTijela').value="";
    document.getElementById('otkucajiSrca').value="";
    document.getElementById('result').innerHTML="";
}


