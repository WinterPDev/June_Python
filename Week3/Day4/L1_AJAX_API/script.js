console.log('Script Linked Successfully! 🎉')

const pokeAPI = 'https://pokeapi.co/api/v2/pokemon/';

// Getting the value that is inputed into the search form.
const pokeName = document.querySelector('#pokeName');

const pokeDisplay = document.querySelector('#pokeList');


function getPokeData(event) {
    event.preventDefault();

    fetch(pokeAPI + pokeName.value)
        .then(response => response.json())
        .then(pokeData => {
            console.log(pokeData);
            pokeDisplay.innerHTML += `
            <div class="pokeBox">
                <p> Name : ${pokeData.name} </p>
                <p> Normal Ver: <img src="${pokeData.sprites.front_default}" alt="${pokeData.name}"> </p>
                <p> Shiny Ver: <img src="${pokeData.sprites.front_shiny}" alt="${pokeData.name}"> </p>
            </div>
            `
        })
        .catch(err => console.log(err))

}


async function getPokeDataList() {
    let pokeList = ['ninetales', 'clodsire', 'celebi', 'arceus', 'gengar'];

    for (let i = 0; i < pokeList.length; i++) {
        let response = await fetch(pokeAPI + pokeList[i]);
        let pokeData = await response.json();

        pokeDisplay.innerHTML += `
        <div class="pokeBox">
        <p> Name : ${pokeData.name} </p>
        <p> Normal Ver: <img src="${pokeData.sprites.front_default}" alt="${pokeData.name}"> </p>
        <p> Shiny Ver: <img src="${pokeData.sprites.front_shiny}" alt="${pokeData.name}"> </p>
    </div>
        `

    }

}