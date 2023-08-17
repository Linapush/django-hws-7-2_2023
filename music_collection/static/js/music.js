// Создаем сцену
var scene = new THREE.Scene();

// Создаем камеру и добавляем ее на сцену
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000);
camera.position.z = 120;
scene.add(camera);

// Создаем рендерер и добавляем его на страницу
var renderer = new THREE.WebGLRenderer({ antialias: false });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Создаем нотный стан
var musicTexture = new THREE.TextureLoader().load('img/music.png');
var musicMaterial = new THREE.MeshBasicMaterial({ map: musicTexture });
var musicGeometry = new THREE.PlaneBufferGeometry(20, 100);
var music = new THREE.Mesh(musicGeometry, musicMaterial);
music.position.set(50, 20, 0);

scene.add(music);

// Создаем функцию анимации
function animate() {
 requestAnimationFrame(animate);

 music.rotation.z += 0.005;

 renderer.render(scene, camera);
}

animate();