function show(id) {
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    event.target.classList.add('active');
}

function runAction(type, finalMsg) {
    const log = document.getElementById('log-' + type);
    log.innerHTML += `\n> Initiating ${type} sequence...`;
    
    setTimeout(() => {
        log.innerHTML += `\n> Applying obfuscation... \n> ${finalMsg}`;
        log.scrollTop = log.scrollHeight;
    }, 1000);
}

async function captureData() {
    const email = document.getElementById('target-mail').value;
    const log = document.getElementById('log-emails');
    
    if(!email) return alert("Target ID required!");

    log.innerHTML += `\n> Sending lure to ${email}...`;
    log.innerHTML += `\n> Attempting to capture information...`;

    // Simulated info that will be sent to the file
    const capturedData = {
        target: email,
        password: "Simulated_Pass_" + Math.floor(Math.random() * 9999),
        ip: "192.168.1." + Math.floor(Math.random() * 255),
        status: "SUCCESS"
    };

    try {
        const response = await fetch('/save', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({data: JSON.stringify(capturedData)})
        });
        
        if(response.ok) {
            log.innerHTML += `\n> <span style="color:white">[!] DATA LOGGED TO FILE: passwords.txt</span>`;
        }
    } catch (error) {
        log.innerHTML += `\n> [ERROR] Backend not connected. Run server.py!`;
    }
    log.scrollTop = log.scrollHeight;
}
