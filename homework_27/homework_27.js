
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

rand = getRandomInt(0, 999)

let friends = rand;
document.getElementById('friends').innerHTML = friends;



function hello(){
  document.getElementById('friends').innerHTML = friends + 1;
  document.getElementById('but_1').innerHTML = 'Очікується підтвердження';
  document.getElementById('but_1').setAttribute('disabled', true);
}

