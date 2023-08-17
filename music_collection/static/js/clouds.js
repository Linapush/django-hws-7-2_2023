// Создаем сцену
var scene = new THREE.Scene();

// Создаем камеру и добавляем ее на сцену
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000);
camera.position.z = 300;
scene.add(camera);

// Создаем рендерер и добавляем его на страницу
var renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Создаем облако
var cloudsGeometry = new THREE.SphereGeometry(100, 32, 32);
var cloudsMaterial = new THREE.MeshBasicMaterial({
 color: 0xffffff,
    alphaMap: new THREE.TextureLoader().load('https://threejsfundamentals.org/threejs/resources/images/cloud.png'),
    transparent: true,
    opacity: 0.5,
 side: THREE.DoubleSide,
});
var cloudField = new THREE.Mesh(cloudsGeometry, cloudsMaterial);
scene.add(cloudField);

// Создаем функцию анимации
function animate() {
 requestAnimationFrame(animate);

 cloudField.rotation.y += 0.002;

 renderer.render(scene, camera);
}

animate(); 

// Задаем цвет фона
renderer.setClearColor(0x000000, 0); 

// Управление камерой
var controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.25;
controls.rotateSpeed = 0.35;
controls.autoRotate = true;
controls.autoRotateSpeed = 0.5;
controls.enableZoom = false;
controls.enablePan = false; 

// Обновление размеров окна
window.addEventListener( 'resize', onWindowResize, false );

function onWindowResize(){
 camera.aspect = window.innerWidth / window.innerHeight;
 camera.updateProjectionMatrix();
 renderer.setSize( window.innerWidth, window.innerHeight );
}
