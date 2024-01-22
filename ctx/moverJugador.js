class Mover{
    constructor(x, y, speed, radius) {
        this.radius = radius;
        this.x = x;
        this.y = y;
        this.speed = speed;
        this.keys = {};
        window.addEventListener("keydown", (e) => {
          this.keys[e.key] = true;
        });
        window.addEventListener("keyup", (e) => {
          this.keys[e.key] = false;
        });
       
    }
    update() {
        if (this.keys["ArrowUp"] && this.y > 0) {
          this.y -= this.speed;
        }
        if (this.keys["ArrowDown"] && this.y + this.radius < innerHeight) {
          this.y += this.speed;
        }
        if (this.keys["ArrowLeft"] && this.x > 0) {
          this.x -= this.speed;
        }
        if (this.keys["ArrowRight"] && this.x + this.radius  < innerWidth) {
          this.x += this.speed;
        }
    }
}