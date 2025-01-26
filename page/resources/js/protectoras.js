


async function loadJSON(ruta) {
    try {
        const response = await fetch(ruta);
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return await response.json();
        // You can now use the JSON data
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

let protectoras = await loadJSON("resources\\js\\protectoras.json");
let comunidades = Object.keys(protectoras)

//creacion de componente comunidad
for (let comunidad of comunidades) {
    let comunidadAutonoma = document.createElement("div")
    comunidadAutonoma.className = "comunidad"


    let titulo = document.createElement("h2")
    titulo.innerHTML = comunidad
    comunidadAutonoma.appendChild(titulo)

    
    let protectorasCaja = document.createElement("div")
    protectorasCaja.className = "protectoras"

    for (let protectora of protectoras[comunidad]) {
        let protectoraButton = document.createElement("button")
        protectoraButton.className = "protectora"
        protectoraButton.setAttribute("popovertarget", "protectora"+ protectora.number)
        
        let popover = document.createElement("popover")
        popover.className = "popover"
        popover.innerHTML = `<img src="${protectora.logo}">` +"<br> numero: "+protectora.phone + "<br> email: " + protectora.mailto + "<br> web: " + protectora.web
        popover.setAttribute("popover", "true")
        popover.id = "protectora"+ protectora.number
        protectorasCaja.appendChild(popover)
        

        let name = document.createElement("h3")
        name.innerHTML = protectora.name
        protectoraButton.appendChild(name)

        protectorasCaja.appendChild(protectoraButton)

    }
    
    comunidadAutonoma.appendChild(protectorasCaja)
    document.querySelector("#CAs").appendChild(comunidadAutonoma)
    //break
}