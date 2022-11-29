myFunction = (pokemon) => {
    fetch('/save_recent_pokemon',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(pokemon),
    })
    .then(response => response.json())
    .then(data => {
    console.log('Success:', data);
    })
    .catch((error) => {
     console.error('Error:', error)
    });

        document.getElementById("image_url").src = pokemon.image_url
        document.getElementById("name").innerHTML = pokemon.name;
        document.getElementById("hp").innerHTML = 'HP ' + pokemon.hp;
        document.getElementById("attack").innerHTML = 'ATTACK ' + pokemon.attack +'/ SpATK ' + pokemon.special_attack ;
        document.getElementById("defense").innerHTML = 'DEFENSE ' + pokemon.defense +'/ SpDEF ' + pokemon.special_defense ;
        document.getElementById("speed").innerHTML = 'SPEED ' + pokemon.speed;
        document.getElementById("weight").innerHTML = 'WEIGHT ' + pokemon.weight + 'g';
 };
