const canvas = document.querySelector("canvas");
const c = canvas.getContext("2d");

canvas.width = innerWidth;
canvas.height = innerHeight;

class Jugador {
  constructor(x, y, radius, color) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
  }
  draw() {
    c.beginPath();
    c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
    c.fillStyle = this.color;
    c.fill();
  }
}
class Projectile extends Jugador{
    constructor(x, y, radius, color, velocity) {
        super(x, y, radius, color);
        this.velocity = velocity;
    }
    update() {
        this.draw()
        this.x = this.x + this.velocity.x;
        this.y = this.y + this.velocity.y;
    }
}

let x = canvas.width / 2;
let y = canvas.height / 2;
const radius = 30;
const projectiles = [];
const player = new Jugador(x, y, radius, "blue");

function animate() {
    movimiento.update();
    requestAnimationFrame(animate);
    c.clearRect(0,0,canvas.width, canvas.height);
    x = movimiento.x;
    y = movimiento.y;
    player.x = x;
    player.y = y;
    player.draw()
    
    projectiles.forEach((projectile) => {
        projectile.update()
    })
}
const VEL = 3.75
const movimiento = new Mover(x,y,VEL, radius);
addEventListener('click', function(event) {
    const angle = Math.atan2(event.clientY - y, event.clientX - x);
    const projectile = new Projectile(x, y, 5, 'red', {
        x: Math.cos(angle) * VEL,
        y: Math.sin(angle) * VEL
    });
    projectiles.push(projectile);
});








animate();